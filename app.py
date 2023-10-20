import os
from moviepy.editor import VideoFileClip, ImageSequenceClip
from PIL import Image
import PIL

from moviepy.editor import *

# Define file paths
image_folder = r'C:\phase3\aivideo\trial\image\\'
mp3_file = r'C:\phase3\aivideo\trial\audio\classical.mp3'

# Load the images and resize them to the same dimensions
image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(".jpg")]
image_files_resized = []

# Set a target size (adjust as needed)
target_size = (1920, 1080)

for img_path in image_files:
    img = Image.open(img_path)
    img_resized = img.resize(target_size, PIL.Image.Resampling.LANCZOS)
    img_resized.save(img_path)
    image_files_resized.append(img_path)

# Create the video
clip = ImageSequenceClip(image_files_resized, fps=1)

# Load the audio
audio = AudioFileClip(mp3_file)

# Set the audio of the clip
clip = clip.set_audio(audio)

# Set duration of the clip to match the audio duration
clip = clip.set_duration(audio.duration)

# Output file path
output_file = 'output_video.mp4'

# Write the video to a file
clip.write_videofile(output_file, codec='libx264')
