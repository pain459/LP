# Component p2: Subtitle Generation

This component generates a subtitle file (`.srt`) from a `.wav` audio file, using OpenAI's Whisper library.

## Usage

1. Place the `.wav` file in the `input/` directory.
2. Run the component using Docker Compose.
3. The generated `.srt` file will appear in the `output/` directory.

## Dependencies

- OpenAI Whisper
- Torch

## Notes

- Supports only English for this project.
- The subtitles focus solely on voice content.
