import os
import subprocess
from pathlib import Path

lib_root = Path(__file__).parent.parent
script_path = lib_root / "video_to_audio_bot/convert_to_audio.sh"


def convert_video_to_audio(input_video, output_audio=None):
    input_video = Path(input_video)
    # Define the path to the bash script
    # script_path = os.path.join(os.path.dirname(__file__), 'convert_to_audio.sh')
    if output_audio is None:
        output_audio = input_video.with_suffix(".mp3")
    # Ensure the script is executable
    subprocess.run(["chmod", "+x", str(script_path)], check=True)

    # Run the bash script with the input video and output audio file as arguments
    result = subprocess.run(
        [str(script_path), str(input_video), str(output_audio)],
        check=True,
        capture_output=True,
        text=True,
    )

    # Print the stdout and stderr from the bash script
    # print(result.stdout)
    # if result.returncode != 0:
    #     print(result.stderr)
    #     raise Exception("Conversion failed")

    return output_audio


# Example usage
if __name__ == "__main__":
    # todo: replace with sample video
    input_video_file = "input.mp4"  # Replace with your input video file
    output_audio_file = "output.mp3"  # Replace with your desired output audio file

    convert_video_to_audio(input_video_file, output_audio_file)

    print(script_path)
