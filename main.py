from ttspeech import tts
from moviepy.editor import *
import os

def text_to_speech(text, filename):
    # Specify the filename (optional)
    output_filename = filename

    # Specify whether to play the generated audio (True/False)
    play_audio = False

    # Call the tts function
    tts(text, output_filename, play_audio)

def audio_to_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    new_audioclip = CompositeAudioClip([audio_clip])
    
    # Trim the video to match the duration of the audio
    video_clip = video_clip.subclip(0, audio_clip.duration)

    video_clip.audio = new_audioclip

    new_clip = vfx.crop(video_clip, x1=360, y1=0, width=540, height=960)

    # Write the result to a file
    new_clip.write_videofile(output_path)

def main():
    video_file = 'resources/parkour.mp4'
    text_content = 'Hello, this is the text I want to convert to speech. Thank you'

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


