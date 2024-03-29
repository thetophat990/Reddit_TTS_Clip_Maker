
# Reddit_TTS_Clip_Maker

> [!warning]  
> This repository is heavily work in progress, expect things to not work, or to break without warning or obvious reason

Welcome to RedditTTS, your all-in-one solution for effortlessly creating engaging Reddit-style videos. With this tool, you can seamlessly generate ready-to-upload videos featuring text-to-speech voiceovers of Reddit posts, accompanied by subtitles and a background video of your choice. This efficient tool enables you to create Reddit-style videos in minutes, and facilitates quick integration onto short-form video sharing platforms such as TikTok or Instagram Reels. 
## Features

- Fully automatic reddit post finding, filtering and downloading
- Automatic video cropping and scaling
- Ultra realistic TTS and transcripts with OpenAI Audio Modles


## Obtaining API Keys

Before starting, you must obtain API Keys for both reddit and OpenAI

- [Reddit](https://www.reddit.com/wiki/api/) (select script for app type)
- [OpenAI](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/)

## Getting Started

Firstly, clone the project to any location

```bash
  git clone https://github.com/thetophat990/Reddit_TTS_Clip_Maker.git
```

then go to the project directory

```bash
  cd Reddit_TTS_Clip_Maker
```

Lastly, install the dependencies via PIP, after this you can close the terminal

```bash
  pip install -r requirements.txt
``` 

Next, Be sure to correctly configure MoviePy, specifically be sure to install and set the paths to [imagemagick](https://www.imagemagick.org/script/index.php) and [FFMPEG](https://ffmpeg.org/), more info can be found [here](https://moviepy.readthedocs.io/en/latest/install.html)

Now you need to add the API credentials, in the project directory, find the `SETTINGS.py` file, in it you must change some of the values for the program to work, specifically, you need to change `REDDIT_API_USER_AGENT`, `REDDIT_API_CLIENT_ID`, `REDDIT_API_CLIENT_SECRET` and `OPENAI_API_KEY`. You should already have these values from [this](https://github.com/thetophat990/Reddit_TTS_Clip_Maker/edit/main/README.md#obtaining-api-keys) step, note that you can also change anyother settings you want, however this is not essential

Finally, you should place some video files in the `backround_video` folder, the videos can be any size, while any video codec should work, not that only `.mp4` files have been tested

## Acknowledgements

 - [OpenAI](https://openai.com/)
 - [PRAW](https://pypi.org/project/praw/)
 - [MoviePy](https://pypi.org/project/moviepy/)


## Authors

- [@thetophat990](https://github.com/thetophat990)

