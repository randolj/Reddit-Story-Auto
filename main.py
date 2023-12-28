from ttspeech import tts
from moviepy.editor import *
import numpy as np
import os

def text_to_speech(text, filename):
    # Specify the filename (optional)
    output_filename = filename

    # Specify whether to play the generated audio right away (True/False)
    play_audio = False

    # Call the tts function
    tts(text, output_filename, play_audio)

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
    text_content = "AITA for refusing to share my homemade cookies with my neighbor? I recently took up baking as a hobby and made a batch of amazing chocolate chip cookies. This morning, my neighbor knocked on my door, expressing how great they smelled and asking for a few."

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


