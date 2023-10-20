import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

# Define file paths
image_folder = r'C:\phase3\aivideo\trial\image\\'
mp3_file = r'C:\phase3\aivideo\trial\audio\classical.mp3'

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
final_clip.fps = 5  # Adjust the value if needed

# Output file path
output_file = 'output_video_images.mp4'

# Write the video to a file
final_clip.write_videofile(output_file, codec='libx264')
