from Video_Maker import make_video

from random import randint
from os import listdir
from os.path import join

MOCK_DATA = """mock data, mock data, my name is walter hartwell whight and i live at 305 negra aroya lane albuqurci new mexio"""
TEMP_AUDIO_PATH = r"audio.mp3"
OUTPUT_PATH = r"output.mp4"
GAMEPLAY_FOLDER_PATH = r"backround_video"
OUTPUT_FPS = 60

rand_gameplay_path = join(GAMEPLAY_FOLDER_PATH, listdir(GAMEPLAY_FOLDER_PATH)[randint(0, len(listdir(GAMEPLAY_FOLDER_PATH)) - 1)])

# UPDATE FOR NEW TTS CODEBASE

make_video(OUTPUT_PATH,rand_gameplay_path,OUTPUT_FPS,randint(0,25),TEMP_AUDIO_PATH)