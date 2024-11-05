import os
import whisper
from concurrent.futures import ThreadPoolExecutor

input_dir = '/app/input'
output_dir = '/app/output'

def generate_subtitles(audio_file):
    model = whisper.load_model("base")
    audio_path = os.path.join(input_dir, audio_file)
    
    # Use simplified model configuration to reduce duplicate entries
    result = model.transcribe(
        audio_path,
        language='en',
        temperature=0.0,      # Lower temperature for consistency
        best_of=1,            # Set best_of to 1 to avoid duplicates
        beam_size=5           # Use beam search to enhance accuracy
    )
    
    srt_file = os.path.join(output_dir, os.path.splitext(audio_file)[0] + ".srt")
    
    # Use a set to track unique segments and avoid duplicates
    unique_segments = set()
    
    with open(srt_file, 'w') as f:
        for i, segment in enumerate(result['segments']):
            start = segment['start']
            end = segment['end']
            text = segment['text'].strip()
            
            # Ensure unique text segments only
            if text not in unique_segments:
                unique_segments.add(text)
                start_time = format_time(start)
                end_time = format_time(end)
                f.write(f"{i+1}\n{start_time} --> {end_time}\n{text}\n\n")
    
    print(f"Generated subtitles for {audio_file}")

def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

def main():
    with ThreadPoolExecutor() as executor:
        for file in os.listdir(input_dir):
            if file.endswith(".wav"):
                executor.submit(generate_subtitles, file)

if __name__ == "__main__":
    main()
