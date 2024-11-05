# Component p1: Audio Extraction

This component extracts audio from a given video file in `.mp4`, `.mkv`, or `.avi` format and outputs it as a `.wav` file.

## Usage

1. Place the video file in the `input/` directory.
2. Run the component using Docker Compose.
3. The extracted audio will appear in the `output/` directory.

## How it Works

- The `extract_audio.py` script uses `ffmpeg` to extract audio from the video.
- This process is managed entirely within the Docker container.

## Dependencies

- Python 3.10
- `ffmpeg`
- Required Python packages are listed in `requirements.txt`.

## Notes

- Ensure only one video file is present in the `input/` directory when running the component.
