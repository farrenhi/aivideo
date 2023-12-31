# image url saved to MySQL database
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

def make_video(prompt):
    
    
    print("modified_prompt:", prompt)
    
    ### future tasks: automation on this part
    text_splits = 3
    ###

    # save the topic_prompt
    request_id = request_to_database(prompt)
    text_from_gpt = prompt_to_text(prompt)
    
#     text_from_gpt = """
# Snow White, a princess with ebony hair and skin as fair as snow, was adored by all but her jealous stepmother. 
# Enraged by Snow White's beauty, the queen ordered her death. 
# But the kind-hearted huntsman couldn't do it. 
# Snow White fled into the forest and found refuge with seven dwarfs. 
# The queen's wickedness was ultimately thwarted, and Snow White lived happily ever after.
# """

    texts = split_text_into_prompts(text_from_gpt, text_splits)

    generative_text_to_database(texts, request_id)


    ### break point
    user_input2 = input("Please check the prompt: ")
    print("You entered:", user_input2)


    # ### break point
    # user_input2 = input("Please check the prompt: ")
    # print("You entered:", user_input2)

    # AI: text to image
    # for text_part in texts:
    #     text_to_image(text_part, request_id)

    request_id = 76

    ### make narrative audio
    # text_to_speech(text_from_gpt, request_id)

    ### audio to be loaded from S3
    # Define file paths
    # image_folder = r'C:\phase3\aivideo\trial\image\\'
    mp3_file = f'static/audio/{request_id}.mp3'
    ###

    # Load the audio
    audio = AudioFileClip(mp3_file)
    audio_duration = audio.duration

    # Create ImageClips for each image
    # image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(".jpg")]

    image_urls = grab_image(request_id)
    print(image_urls)
    images_counter = len(image_urls)
    duration_image = audio_duration / images_counter

    ### break point
    user_input2 = input("Please check the prompt: ")
    print("You entered:", user_input2)


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
