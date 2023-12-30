from ttspeech import tts
from moviepy.editor import *
from redditprocess import getBody
import numpy as np
import os

def text_to_speech(text, filename):
    # Specify the filename (optional)
    output_filename = filename

    # Specify whether to play the generated audio right away (True/False)
    play_audio = False

    input_file_path = "resources/input.txt"

    # Call the tts function
    tts(text, output_filename, play_audio, input_file_path)

def audio_to_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    new_audioclip = CompositeAudioClip([audio_clip])
    
    # Randomize section of video
    audio_length = audio_clip.duration
    max_start = video_clip.duration - audio_length
    random_start = max(0, min(max_start, np.random.uniform(0, max_start)))

    # Trim the video to match the duration of the audio
    video_clip = video_clip.subclip(random_start, random_start + audio_clip.duration)

    # Set video audio to new audio
    video_clip.audio = new_audioclip

    # Change video aspect ratio
    new_clip = vfx.crop(video_clip, x1=360, y1=0, width=540, height=960)

    # Write the result to a file
    new_clip.write_videofile(output_path)

def main():
    video_file = 'resources/parkour.mp4'
    text_content = "OOP! Something went wrong"

    with open('resources/input.txt', 'w') as file:
        # Write text to file
        file.write(getBody())

    # Save the TTS-generated audio as a temporary file
    temp_audio_file = 'temp_audio.mp3'
    text_to_speech(text_content, temp_audio_file)

    # Output video file
    output_file = 'result.mp4'

    # Add TTS audio to the video without extending the video duration
    audio_to_video(video_file, temp_audio_file, output_file)

    # Remove the temporary audio file
    os.remove(temp_audio_file)

if __name__ == "__main__":
    main()


