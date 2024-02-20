# GENERAL SETTINGS
GENERAL_OUTPUT_FILENAME = r"OUT_%d-%m-%Y_%H-%M.mp4"                # This is the filename that the output file will be saved as, note that this is a time string

# REDDIT API SETTINGS
REDDIT_API_USER_AGENT = r"CHANGEME"                                # Update the next 3 settings with your reddit API User-agent, Client id and secret, more info on how to do this on main README
REDDIT_API_CLIENT_ID = r"CHANGEME"
REDDIT_API_CLIENT_SECRET = r"CHANGEME"

REDDIT_API_SUBREDDIT_LISTS = ["AskReddit"]                         # Here you can have a (python) list of different subreddits to possibly download posts from, case sensative
REDDIT_API_MAX_POSTS_TO_DOWNLOAD = 5                               # How many posts should be downloaded before one of them is picked at random
REDDIT_API_MIN_CHARS_PER_POST = 50                                 # Minimum charicters per comment that is included in the video

# OPEN-AI SETTINGS
OPENAI_API_KEY = r"CHANGEME"                                       # Update this with your OpenAI API key, more info on how to do this can be found on main README
OPENAI_AUDIO_OUTPUT_PATH = r"working_dir\audio.mp3"
OPENAI_CAPTION_OUTPUT_PATH = r"working_dir\caption_data"
OPENAI_TTS_VOICE = r"alloy"
OEPNAI_MAX_CHARS_FOR_REQUEST = 4095

#MOVIEPY SETTINGS
MOVIEPY_PATH_TO_BACKROUND_VIDEOS = r"backround_video"
MOVIEPY_VIDEO_OUTPUT_DIRECTORY = r"output"
MOVIEPY_VIDEO_CODEC = r"libx264"
MOVIEPY_AUDIO_CODEC = r"aac"
MOVIEPY_MOVIEPY_OUTPUT_FPS = 30
MOVIEPY_GAMEPLAY_START_OFFSET = 5
MOVIEPY_VIDEO_DIMENSIONS = 405, 720


