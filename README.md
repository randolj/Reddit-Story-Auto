# Reddit Story Trend Automated

THIS IS STILL IN PROGRESS

This Python script uses tik tok's text-to-speech API with the moviepy library to create the trendy vidoes on Tik Tok where a reddit story is read out loud with Minecraft parkour in the background.

## Libraries and API's used

- moviepy
- Reddit PRAW
- TikTok TTS API found [here](https://github.com/oscie57/tiktok-voice)

## Current and Future Functionality
Current:
- Takes in text and produces an audio file
- Trims the Minecraft parkour to the length of the audio file
- Adjusts the video to TikTok/YouTube Short aspect ratio
- Adds the generated audio file to the Minecraft parkour video
- Randomly selects a segment from the Minecraft parkour video
- Can edit code in redditprocess.py to select a post and have it create a video with it

Future:
- Randomly selects a Reddit Story
- Subtitles added over video

## Note on TTS API

The Tik Tok TTS API was created by another developer. I borrowed some of their code and got extracted relevant parts for my project and edited to be better suited for what I needed.
