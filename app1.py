# image files are saved to local storage

import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from datetime import datetime


# Define file paths
image_folder = 'trial/image/'
mp3_file = 'trial/audio/classical.mp3'


# Load the audio
audio = AudioFileClip(mp3_file)

# Create ImageClips for each image
image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(".jpg")]

audio_duration = audio.duration
images_counter = len(image_files)
duration_image = audio_duration / images_counter

image_clips = [ImageClip(img, duration=duration_image) for img in image_files]  # Each image is displayed for 7 seconds

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
