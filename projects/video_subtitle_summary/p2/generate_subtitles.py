import os
import whisper

input_dir = '/app/input'
output_dir = '/app/output'

def generate_subtitles(audio_file):
    model = whisper.load_model("base")
    audio_path = os.path.join(input_dir, audio_file)
    result = model.transcribe(audio_path, language='en')
    
    # Write subtitles to .srt file
    srt_file = os.path.join(output_dir, os.path.splitext(audio_file)[0] + ".srt")
    with open(srt_file, 'w') as f:
        for i, segment in enumerate(result['segments']):
            start = segment['start']
            end = segment['end']
            text = segment['text']
            
            # Format time for .srt file
            start_time = format_time(start)
            end_time = format_time(end)
            f.write(f"{i+1}\n{start_time} --> {end_time}\n{text}\n\n")
    
    print(f"Generated subtitles to {srt_file}")

def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

if __name__ == "__main__":
    # Find the first .wav file in the input directory
    for file in os.listdir(input_dir):
        if file.endswith(".wav"):
            generate_subtitles(file)
            break
    else:
        print("No .wav file found in the input directory.")
