#!/bin/bash

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found. Please install it and try again."
    exit
fi

# Function to display usage
usage() {
    echo "Usage: $0 input_video_file output_audio_file"
    echo "Example: $0 input.mp4 output.mp3"
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    usage
fi

input_video="$1"
output_audio="$2"

# Convert video to audio
ffmpeg -i "$input_video" -q:a 0 -map a "$output_audio"

# Check if the conversion was successful
if [ $? -eq 0 ]; then
    echo "Conversion successful: $output_audio"
else
    echo "Conversion failed"
    exit 1
fi
