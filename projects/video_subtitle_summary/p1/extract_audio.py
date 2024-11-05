import os
import subprocess

input_dir = '/app/input'
output_dir = '/app/output'

def extract_audio(video_file):
    audio_file = os.path.join(output_dir, os.path.splitext(video_file)[0] + ".wav")
    video_path = os.path.join(input_dir, video_file)
    command = ["ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", audio_file]
    subprocess.run(command, check=True)
    print(f"Extracted audio to {audio_file}")

if __name__ == "__main__":
    # Find the first video file in the input directory
    for file in os.listdir(input_dir):
        if file.endswith((".mp4", ".mkv", ".avi")):
            extract_audio(file)
            break
    else:
        print("No video file found in the input directory.")
