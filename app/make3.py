# image file are not saved to local storage
# app3 test for EV2. Use local images
from io import BytesIO
import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from datetime import datetime
from PIL import Image
# from model import *
import requests
import numpy as np
# from control import *
# from image import *

### Provided text
topic_prompt = "snowwhite story in 150 words"
request_id = 4
text_splits = 3
text = """
Snow White, a princess with ebony hair and skin as fair as snow, lived in a castle with her wicked stepmother, the Queen. Jealous of Snow White's beauty, the Queen ordered her death. However, the kind-hearted huntsman spared her and she found shelter with seven lovable dwarfs in a cozy cottage in the woods.

Meanwhile, the Queen's envy grew, leading her to concoct a poisonous apple. Disguised as an old hag, she tricked Snow White into taking a fateful bite. The princess fell into a deep slumber.

Only true love's kiss could awaken her. A prince, enchanted by Snow White's beauty, arrived just in time. His kiss broke the spell, reviving her. The wicked Queen's evil reign came to an end, and Snow White and her prince lived happily ever after, a testament to the enduring power of love and kindness.
"""
###

# save the prompt
# request_to_database(topic_prompt)
# texts = split_text_into_prompts(text, text_splits)
# for index, text in enumerate(texts):
#     generative_text_to_database(text, request_id)

# # AI: text to image
# for text_part in texts:
#     print(text_part)
#     text_to_image(text_part, request_id)

### audio to be loaded from S3
# Define file paths
# image_folder = r'C:\phase3\aivideo\trial\image\\'
# mp3_file = r'C:\phase3\aivideo\trial\audio\classical.mp3'
image_folder = 'trial/image/'
mp3_file = 'trial/audio/classical.mp3'

# Load the audio
audio = AudioFileClip(mp3_file)

# Create ImageClips for each image
image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(".png")]

# image_urls = grab_image(request_id)

audio_duration = audio.duration
images_counter = 3
images_counter = len(image_files)
duration_image = audio_duration / images_counter

# image_clips = [ImageClip(img, duration=duration_image) for img in image_files]  # Each image is displayed for 7 seconds
# image_clips = []

image_clips = [ImageClip(img, duration=duration_image) for img in image_files]  # Each image is displayed for 7 seconds


# for i, img_url in enumerate(image_urls):
#     response = requests.get(img_url)
#     img_stream = BytesIO(response.content)
#     img = Image.open(img_stream)
#     img_array = np.array(img)  # Convert to NumPy array
#     img_clip = ImageClip(img_array, duration=duration_image)
#     image_clips.append(img_clip)

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
output_file = '/app/static/videos/output_video_{timestamp}.mp4'

# Write the video to a file
final_clip.write_videofile(output_file, codec='libx264')
