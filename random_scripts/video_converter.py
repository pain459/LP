import os
import threading
import sys
from moviepy.editor import *
from loguru import logger

# Redirect stdout and stderr to loguru
logger.remove()  # Remove the default configuration
logger.add(sys.stdout, colorize=True)  # Add stdout to logger
logger.add("conversion_logs.txt", level="INFO")  # Add file for logs

def convert_avi_to_mp4(input_path, output_path, video_bitrate='5000k', audio_bitrate='320k'):
    video_clip = VideoFileClip(input_path)
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a',
                               remove_temp=True, bitrate=video_bitrate, audio_bitrate=audio_bitrate, verbose=False)

def convert_worker(input_folder, output_folder, file, video_bitrate='5000k', audio_bitrate='320k'):
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file.replace(".avi", ".mp4"))
    convert_avi_to_mp4(input_path, output_path, video_bitrate, audio_bitrate)
    logger.info(f"Conversion completed: {output_path}")

def batch_convert_avi_to_mp4(input_folder, output_folder, video_bitrate='5000k', audio_bitrate='320k'):
    os.makedirs(output_folder, exist_ok=True)
    input_files = os.listdir(input_folder)
    avi_files = [file for file in input_files if file.endswith(".avi")]
    total_files = len(avi_files)
    threads = []
    for avi_file in avi_files:
        thread = threading.Thread(target=convert_worker, args=(input_folder, output_folder, avi_file, video_bitrate, audio_bitrate))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

# Example usage
input_folder = "S1"
output_folder = "S1"
batch_convert_avi_to_mp4(input_folder, output_folder)
