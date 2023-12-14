import threading
import time
from io import BytesIO
import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from datetime import datetime
from PIL import Image
from models.model import *
import requests
import numpy as np
from models.control import *
from controls.image import *
from controls.text_palm import *
from controls.speech import *

# def image_generator(texts, request_id):
#     # AI: text to image
#     for index, text_part in enumerate(texts):
#         print("image generator:", index)
#         text_to_image(text_part, request_id)
   

def run_threads(prompt):
    ### future tasks: automation on this part
    text_splits = 3
    ###
    
    # get request_id and response from GPT
    ### future task: should be processed at the same time
    request_id = request_to_database(prompt)
    text_from_gpt = prompt_to_text(prompt)
    
    # split GPT's response and save it into database
    texts = split_text_into_prompts(text_from_gpt, text_splits)
    generative_text_to_database(texts, request_id)
    
    # save a list as dict of image links (no need to go to S3)
    image_urls_dict = {}
    
    # Create thread objects
    thread1 = threading.Thread(target=text_to_speech, args=(text_from_gpt, request_id))
    # thread2 = threading.Thread(target=image_generator, args=(texts, request_id))
    thread2 = threading.Thread(target=text_to_image, args=(texts[0], 0, image_urls_dict, request_id))
    thread3 = threading.Thread(target=text_to_image, args=(texts[1], 1, image_urls_dict, request_id))
    thread4 = threading.Thread(target=text_to_image, args=(texts[2], 2, image_urls_dict, request_id))
    
    # Start all threads
    thread2.start()
    thread3.start()
    thread4.start()
    
    thread1.start()

    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    # Continue with the main program after both threads are done
    print("Audio and images are fetched. Continue with the main program.")
    
    ### audio to be uploaded to S3
    # Define file paths
    # image_folder = r'C:\phase3\aivideo\trial\image\\'
    mp3_file = f'static/audio/{request_id}.mp3'
    ###
    
    # Load the audio
    audio = AudioFileClip(mp3_file)
    audio_duration = audio.duration
    
    dict_to_array = []
    # for index in range(len(image_urls_dict.keys())):
    for key in image_urls_dict.keys():
        dict_to_array.append(image_urls_dict[key])
    
    image_urls = dict_to_array
    # image_urls = grab_image(request_id)
    # print(image_urls)
    # data_image_urls_example = [
    #     'https://processed-model-result.s3.us-east-2.amazonaws.com/4af78ff7-6c86-4cc5-ac51-6933e2a93cb0_0.png', 
    #     'https://processed-model-result.s3.us-east-2.amazonaws.com/51a9995b-fc27-4757-b235-aff1b5bc74fc_0.png', 
    #     'https://processed-model-result.s3.us-east-2.amazonaws.com/d810e1f4-75b6-46ef-b1b6-19e10e8ab9fc_0.png'
    #     ]
    
    images_counter = len(image_urls)
    duration_image = audio_duration / images_counter

    # image_clips = [ImageClip(img, duration=duration_image) for img in image_files]  # Each image is displayed for 7 seconds
    image_clips = []

    for i, img_url in enumerate(image_urls):
        response = requests.get(img_url)
        img_stream = BytesIO(response.content)
        img = Image.open(img_stream)
        img_array = np.array(img)  # Convert to NumPy array
        img_clip = ImageClip(img_array, duration=duration_image)
        image_clips.append(img_clip)

    # Concatenate the ImageClips
    final_clip = concatenate_videoclips(image_clips, method="compose")

    # Set the audio of the clip
    final_clip = final_clip.set_audio(audio)

    # Set duration of the clip to match the audio duration
    final_clip = final_clip.set_duration(audio.duration)

    # Set the fps for the final_clip
    final_clip.fps = 1  # Adjust the value if needed

    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    video_filename = f'video_{timestamp}.mp4'

    # Output file path
    output_file_path = f'static/videos/{video_filename}'

    save_video_filename_database(video_filename, request_id)

    # Write the video to a file
    final_clip.write_videofile(output_file_path, codec='libx264')
    
    return output_file_path, video_filename, request_id

if __name__ == "__main__":
    run_threads()
