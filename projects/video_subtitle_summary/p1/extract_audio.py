import os
import subprocess
from pydub import AudioSegment
from concurrent.futures import ThreadPoolExecutor

input_dir = '/app/input'
output_dir = '/app/output'

def extract_and_amplify_audio(video_file):
    audio_file = os.path.join(output_dir, os.path.splitext(video_file)[0] + ".wav")
    video_path = os.path.join(input_dir, video_file)
    
    # Extract audio with high-pass filter
    command = ["ffmpeg", "-i", video_path, "-af", "highpass=f=200", "-q:a", "0", "-map", "a", audio_file]
    subprocess.run(command, check=True)
    
    # Amplify audio to enhance voice clarity
    sound = AudioSegment.from_wav(audio_file)
    amplified_sound = sound + 10  # Increase volume by 10dB
    amplified_sound.export(audio_file, format="wav")
    
    print(f"Processed audio saved to {audio_file}")

def main():
    with ThreadPoolExecutor() as executor:
        for file in os.listdir(input_dir):
            if file.endswith((".mp4", ".mkv", ".avi")):
                executor.submit(extract_and_amplify_audio, file)

if __name__ == "__main__":
    main()
