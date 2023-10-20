import os
from moviepy.editor import VideoFileClip, ImageSequenceClip, AudioFileClip

# Define file paths
image_folder = r'C:\phase3\aivideo\trial\image\\'
mp3_file = r'C:\phase3\aivideo\trial\audio\sample.mp3'


# Load the images and resize them to the same dimensions
image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(".jpg")]
image_files_resized = []


# Load the images
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".jpg")])
clip = ImageSequenceClip([image_folder + img for img in image_files], fps=24)

# Load the audio
audio = AudioFileClip(mp3_file)

# Set the audio of the clip
clip = clip.set_audio(audio)

# Set duration of the clip to match the audio duration
clip = clip.set_duration(audio.duration)

print('line 21')

# Output file path
output_file = 'output_video.mp4'

# Write the video to a file
clip.write_videofile(output_file, codec='libx264')
