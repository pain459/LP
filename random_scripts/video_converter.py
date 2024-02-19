# usage
# python script.py --input_folder input_folder --output_folder output_folder
# python script.py --show_codecs

import os
import threading
import sys
import argparse
from moviepy.editor import *
from loguru import logger

def get_available_codecs():
    # Video codecs supported by MoviePy
    video_codecs = ["libx264", "mpeg4", "libvpx", "libvpx-vp9", "rawvideo"]
    # Audio codecs supported by MoviePy
    audio_codecs = ["aac", "mp3", "libvorbis", "pcm_s16le"]
    return video_codecs, audio_codecs

def convert_avi_to_mp4(input_path, output_path, video_codec='libx264', audio_codec='aac'):
    video_clip = VideoFileClip(input_path)
    video_clip.write_videofile(output_path, codec=video_codec, audio_codec=audio_codec, temp_audiofile='temp-audio.m4a',
                               remove_temp=True, verbose=False)

def convert_worker(input_folder, output_folder, file, video_codec='libx264', audio_codec='aac'):
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file.replace(".avi", ".mp4"))
    convert_avi_to_mp4(input_path, output_path, video_codec, audio_codec)
    logger.info(f"Conversion completed: {output_path}")

def batch_convert_avi_to_mp4(input_folder, output_folder, video_codec='libx264', audio_codec='aac'):
    os.makedirs(output_folder, exist_ok=True)
    input_files = os.listdir(input_folder)
    avi_files = [file for file in input_files if file.endswith(".avi")]
    total_files = len(avi_files)
    threads = []
    for avi_file in avi_files:
        thread = threading.Thread(target=convert_worker, args=(input_folder, output_folder, avi_file, video_codec, audio_codec))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def main(input_folder, output_folder, video_codec='libx264', audio_codec='aac'):
    batch_convert_avi_to_mp4(input_folder, output_folder, video_codec, audio_codec)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert AVI files to MP4.")
    parser.add_argument("--input_folder", help="Path to the input folder containing AVI files.")
    parser.add_argument("--output_folder", help="Path to the output folder where MP4 files will be saved.")
    parser.add_argument("--video_codec", help="Preferred video codec for conversion. Default is libx264.", default='libx264')
    parser.add_argument("--audio_codec", help="Preferred audio codec for conversion. Default is aac.", default='aac')
    parser.add_argument("--show_codecs", help="Show available codecs for reference.", action='store_true')

    args, unknown = parser.parse_known_args()

    if args.show_codecs:
        video_codecs, audio_codecs = get_available_codecs()
        print("Available video codecs:", video_codecs)
        print("Available audio codecs:", audio_codecs)
        sys.exit()

    if not args.input_folder or not args.output_folder:
        parser.error("--input_folder and --output_folder must be provided.")

    main(args.input_folder, args.output_folder, args.video_codec, args.audio_codec)
