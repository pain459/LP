#!/bin/bash

# Check if --show_codecs is provided
if [[ "$1" == "--show_codecs" ]]; then
    python -u main.py "$@"
else
    python -u main.py --input_folder /app/input_folder --output_folder /app/output_folder "$@"
fi
