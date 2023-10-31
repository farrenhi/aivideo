# image file are not saved to local storage
from io import BytesIO
import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from datetime import datetime
from PIL import Image
from model import *
import requests
import numpy as np
from control import *

### Provided text
request_id = 1
text = """Abraham Lincoln, the 16th President of the United States, stands as an enduring symbol of leadership, integrity, and emancipation. Born in a log cabin in Kentucky, Lincoln rose from humble beginnings to become a towering figure in American history. His steadfast resolve during the Civil War preserved the Union and led to the abolition of slavery with the Emancipation Proclamation. Lincoln's eloquence, exemplified in the Gettysburg Address, resonates through the ages, emphasizing the ideals of equality and democracy. His compassionate nature and ability to bridge divides endeared him to the nation. Lincoln's tragic assassination in 1865 only cemented his legacy, leaving an indelible mark on the American psyche. He remains an inspiration for leaders worldwide, a testament to the power of moral conviction in times of great challenge. Lincoln's enduring influence continues to shape the course of the United States, reminding us that even in adversity, noble principles can prevail.
"""

texts = split_text_into_prompts(text, 3)
for index, text in enumerate(texts):
    generative_text_to_database(text, request_id)

### audio to be loaded from S3
# Define file paths
# image_folder = r'C:\phase3\aivideo\trial\image\\'
mp3_file = r'C:\phase3\aivideo\trial\audio\classical.mp3'
# Load the audio
audio = AudioFileClip(mp3_file)

# Create ImageClips for each image
# image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(".jpg")]

### to be changed on request_id
request_id = 1

image_urls = grab_image(request_id)

audio_duration = audio.duration
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

# Resize the video to 720p
# final_clip = final_clip.resize(height=720)
# final_clip = final_clip.resize(height=480)  # Adjust height as needed

# Generate a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Output file path
output_file = f'output_video_{timestamp}.mp4'

# Write the video to a file
final_clip.write_videofile(output_file, codec='libx264')
