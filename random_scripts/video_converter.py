import os
import threading
import sys
import argparse
from moviepy.editor import *
from loguru import logger

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

def main(input_folder, output_folder):
    batch_convert_avi_to_mp4(input_folder, output_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert AVI files to MP4.")
    parser.add_argument("--input_folder", help="Path to the input folder containing AVI files.", required=True)
    parser.add_argument("--output_folder", help="Path to the output folder where MP4 files will be saved.", required=True)
    args = parser.parse_args()

    main(args.input_folder, args.output_folder)
