import requests
import base64
import argparse
import os
import playsound
import time
import textwrap
import re
from dotenv import load_dotenv

# 006 for male, 001 for female
default_voice = 'en_us_006'
load_dotenv()
default_session_id = os.getenv("SESSION_ID")

def tts_batch(text_speaker: str = 'en_us_002', req_text: str = 'TikTok Text to Speech', filename: str = 'voice.mp3'):
    req_text = req_text.replace("+", "plus")
    req_text = req_text.replace(" ", "+")
    req_text = req_text.replace("&", "and")

    headers = {
        'User-Agent': 'com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)',
        'Cookie': f'sessionid={default_session_id}'
    }
    url = f"https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker={text_speaker}&req_text={req_text}&speaker_map_type=0&aid=1233"

    r = requests.post(url, headers=headers)

    if r.json()["message"] == "Couldn't load speech. Try again.":
        output_data = {"status": "Session ID is invalid", "status_code": 5}
        print(output_data)
        return output_data

    vstr = [r.json()["data"]["v_str"]][0]
    msg = [r.json()["message"]][0]
    scode = [r.json()["status_code"]][0]
    log = [r.json()["extra"]["log_id"]][0]
    
    dur = [r.json()["data"]["duration"]][0]
    spkr = [r.json()["data"]["speaker"]][0]

    b64d = base64.b64decode(vstr)
    
    with open(filename, "wb") as out:
        out.write(b64d)

    output_data = {
        "status": msg.capitalize(),
        "status_code": scode,
        "duration": dur,
        "speaker": spkr,
        "log": log
    }

    print(output_data)

    return output_data

def batch_create(filename: str = 'voice.mp3'):
    out = open(filename, 'wb')

    def sorted_alphanumeric(data):
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(data, key=alphanum_key)
    
    for item in sorted_alphanumeric(os.listdir('./batch/')):
        filestuff = open('./batch/' + item, 'rb').read()
        out.write(filestuff)

    out.close()

def buffer(req_text: str, filename: str = 'voice.mp3', input_file: str = None):
    chunk_size = 200
    textlist = textwrap.wrap(req_text, width=chunk_size, break_long_words=True, break_on_hyphens=False)

    os.makedirs('./batch/')

    for i, item in enumerate(textlist):
        tts_batch(default_voice, item, f'./batch/{i}.mp3')
        
    batch_create(filename)

    for item in os.listdir('./batch/'):
        os.remove('./batch/' + item)
        
    os.removedirs('./batch/')


def tts(req_text: str, filename: str = 'voice.mp3', play: bool = False, input_file: str = None):
    if input_file is not None:
        # Read text from the input file
        req_text = open(input_file, 'r', errors='ignore', encoding='utf-8').read()
        buffer(req_text, filename, input_file)
        return

    req_text = req_text.replace("+", "plus")
    req_text = req_text.replace(" ", "+")
    req_text = req_text.replace("&", "and")

    headers = {
        'User-Agent': 'com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)',
        'Cookie': f'sessionid={default_session_id}'
    }

    url = f"https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker={default_voice}&req_text={req_text}&speaker_map_type=0&aid=1233"
    
    r = requests.post(url, headers=headers)

    if r.json()["message"] == "Couldn't load speech. Try again.":
        output_data = {"status": "Session ID is invalid", "status_code": 5, "current session id": default_session_id}
        print(output_data)
        return output_data

    vstr = r.json()["data"]["v_str"]
    msg = r.json()["message"]
    scode = r.json()["status_code"]
    log = r.json()["extra"]["log_id"]
    dur = r.json()["data"]["duration"]
    spkr = r.json()["data"]["speaker"]

    b64d = base64.b64decode(vstr)

    with open(filename, "wb") as out:
        out.write(b64d)

    output_data = {
        "status": msg.capitalize(),
        "status_code": scode,
        "duration": dur,
        "speaker": spkr,
        "log": log
    }

    print(output_data["status"])
    # print("Length:", output_data["duration"], (int)output_data["duration"]/60, "m", (int)output_data["duration"]%60, "s")

    if play:
        playsound.playsound(filename)
        os.remove(filename)

    return output_data

# def main():
#     parser = argparse.ArgumentParser(description="Simple Python script to interact with the TikTok TTS API")
#     parser.add_argument("-t", "--text", help="the text to be read", required=True)
#     parser.add_argument("-s", "--session", help="account session id", required=True)
#     parser.add_argument("-p", "--play", action='store_true', help="use this if you want to play your output")

#     args = parser.parse_args()

#     print(type(args))

#     req_text = args.text

#     if args.play is not None:
#         play = args.play

#     filename = 'voice.mp3'

#     tts(args.session, req_text, filename, play)

# if __name__ == "__main__":
#     main()
 