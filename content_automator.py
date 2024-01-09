from pytube import YouTube
from datetime import datetime
from moviepy.editor import VideoFileClip, CompositeVideoClip
from shutil import get_terminal_size

from random import randint
from os import listdir, remove
from os.path import join

class Log:
    def __init__(self, logfile_path: str = "log.log", time_format: str = "%d/%m/%Y %H:%M:%S") -> None:
        self.logfile_path = logfile_path
        self.time_format = time_format
    
    def log(self, message: str, include_time: bool = True) -> None:
        if include_time:
            current_time = datetime.now().strftime(self.time_format)
        else:
            current_time = ""
    
        log_msg = f"[{current_time}] {message}"
    
        print(log_msg)
    
        if self.logfile_path:
            with open(self.logfile_path, "a") as file_object:
                file_object.write(log_msg + "\n")

def get_gameplay_video(folder_path: str):
    paths = []
    for f_name in listdir(folder_path):
        paths.append(join(folder_path, f_name))
        
    rand_vid = randint(0, len(listdir(folder_path)) - 1)
    
    return paths[rand_vid]

def construct_video(video_data_dict: str):
    def get_clips(clip_path: str):
        return VideoFileClip(clip_path).set_fps(video_data_dict["fps"])
        
    def get_vid_y_dim():
        try:
            return int(video_data_dict["Video_Size"])
        except ValueError:
            return int(video_data_dict["Video_Size"].split('x')[1])
        
    def get_aspect_ratio(y_in):
        int_list = list(map(int, video_data_dict["aspect_ratio"].split(":")))
        return round(y_in * (int_list[0] / int_list[1]))
        
    def trim_clip(clip):
            return clip.subclip(video_data_dict["start_of_segment"],
            video_data_dict["start_of_segment"] + video_data_dict["duration_of_segment"])
    
    main_clip = get_clips(video_data_dict["path_to_youtube_video_file"])
    gameplay_clip = get_clips(video_data_dict["path_to_gameplay_video_file"])
    
    vid_dim_y = get_vid_y_dim()
    
    main_clip_cut = trim_clip(main_clip)

    gameplay_clip_cut = trim_clip(gameplay_clip)

    target_width = get_aspect_ratio(vid_dim_y)
    
    main_clip_resized = main_clip_cut.resize(width=target_width, height=round(vid_dim_y * video_data_dict["top_video_height"]))
    
    gameplay_clip_resized = gameplay_clip_cut.resize(width=target_width)
    
    main_clip_positioned = main_clip_resized.set_position(('center', 'top'))
    
    gameplay_clip_positioned = gameplay_clip_resized.set_position(('center', 'bottom'))
        
    combined_clip = CompositeVideoClip([main_clip_positioned, gameplay_clip_positioned], size=(target_width, vid_dim_y))
    
    combined_clip.write_videofile(video_data_dict["output_video_path"],
                                  codec=video_data_dict["output_video_codec"],
                                  audio_codec=video_data_dict["output_audio_codec"],
                                  fps=video_data_dict["fps"])


def youtube_video_download(video_url: str, output_path: str = ".", file_name: str = "vid.mp4", video_quality: str = "360p") -> None:
    try:
        stream = YouTube(video_url).streams
        video_stream = stream.filter(res=video_quality).first()
        video_stream.download(output_path, filename=file_name)
            
        return True
            
    except Exception as e:
        return e
    
def program_intro():
    txt = "ContentAutomator"
    pad_char = "="
    
    width, _ = get_terminal_size()
    pad_str = pad_char * ((width - len(txt)) // 2)
    return pad_str + txt + pad_str
    
def main(settings_dict: dict):
    log_obj = Log("log.log")
      
    url = input("Enter Video URL:")  
    is_download = youtube_video_download(video_url=url, file_name=settings_dict["temp_video_file_name_notpath"], video_quality="720p")
    
    if type(is_download) == Exception: raise Exception("YOUTUBE_DOWNLOAD_ERROR:" + is_download)
    
    dict_dynamic_data = {
        "path_to_youtube_video_file" : settings_dict["temp_video_file_name_notpath"],
        "path_to_gameplay_video_file" : get_gameplay_video(settings_dict["path_to_gameplay_clips_folder"])
    }
    
    video_data_dict = {**settings_dict, **dict_dynamic_data}
    
    construct_video(video_data_dict)
    
    for i in range(5):
        remove(settings_dict["temp_video_file_name_notpath"])
    

if __name__ == "__main__":
    STATIC_TEST_VIDEO_DATA_DICTONERY = {
        "start_of_segment" : 5,
        "duration_of_segment" : 15,
        
        "fps" : 30,
        "Video_Size" : "1080x1920",
        "aspect_ratio" : "9:16",
        "top_video_height" : 0.66,
        "temp_video_file_name_notpath" : r"tempclip.mp4",
        "path_to_gameplay_clips_folder" : r"gameplay_videos",
        "output_video_path" : r"output\vid.mp4",
        "output_video_codec" : "libx264",
        "output_audio_codec" : "aac"
    }
    
    main(STATIC_TEST_VIDEO_DATA_DICTONERY)
    
    