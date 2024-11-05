# Component p3: Subtitle Summary Generation

This component generates a summary (approximately 100 words) from a subtitle file (`.srt`) using Hugging Face Transformers.

## Usage

1. Place the `.srt` file in the `input/` directory.
2. Run the component using Docker Compose.
3. The generated summary file will appear in the `output/` directory.

## Dependencies

- Transformers
- PyTorch with CUDA support

## Notes

- This component utilizes GPU for faster summarization.
- Multi-threaded to handle multiple `.srt` files concurrently.
