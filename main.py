from open_ai_services import genarate_subtitles, genarate_tts
from reddit_api_services import get_comment_string
from Video_Maker import make_video
import SETTINGS

from os import listdir
from os.path import join
from random import randint
from datetime import datetime

def rand_video_clip(path_to_backround_videos):
    backround_videos_list = listdir(path_to_backround_videos)
    random_video = backround_videos_list[randint(0, len(backround_videos_list) - 1)]
    random_video_path = join(path_to_backround_videos, random_video)
    return random_video_path

output_filename = datetime.now().strftime(SETTINGS.GENERAL_OUTPUT_FILENAME)
output_path = join(SETTINGS.MOVIEPY_VIDEO_OUTPUT_DIRECTORY, output_filename)

reddit_comments = get_comment_string(
    SETTINGS.REDDIT_API_USER_AGENT,
    SETTINGS.REDDIT_API_CLIENT_ID,
    SETTINGS.REDDIT_API_CLIENT_SECRET,
    SETTINGS.REDDIT_API_SUBREDDIT_LISTS,
    SETTINGS.REDDIT_API_MAX_POSTS_TO_DOWNLOAD,
    SETTINGS.REDDIT_API_MIN_CHARS_PER_POST
    )

with open(SETTINGS.OPENAI_AUDIO_OUTPUT_PATH, "wb") as file_object:
    tts_audio = genarate_tts(reddit_comments, SETTINGS.OPENAI_API_KEY, SETTINGS.OPENAI_TTS_VOICE, SETTINGS.OEPNAI_MAX_CHARS_FOR_REQUEST)
    file_object.write(tts_audio)
    
with open(SETTINGS.OPENAI_CAPTION_OUTPUT_PATH, "w") as file_object:
    caption_data = genarate_subtitles(SETTINGS.OPENAI_API_KEY, SETTINGS.OPENAI_AUDIO_OUTPUT_PATH)
    file_object.write(repr(caption_data))
    
make_video(output_path,
           rand_video_clip(SETTINGS.MOVIEPY_PATH_TO_BACKROUND_VIDEOS),
           SETTINGS.OPENAI_AUDIO_OUTPUT_PATH,
           SETTINGS.OPENAI_CAPTION_OUTPUT_PATH,
           SETTINGS.MOVIEPY_AUDIO_CODEC,
           SETTINGS.MOVIEPY_VIDEO_CODEC,
           SETTINGS.MOVIEPY_MOVIEPY_OUTPUT_FPS,
           SETTINGS.MOVIEPY_GAMEPLAY_START_OFFSET,
           SETTINGS.MOVIEPY_VIDEO_DIMENSIONS)



