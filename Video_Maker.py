from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
# MAX TEXT LENGTH FOR VIDEO CLIPS = 77

def calculate_video_duration(path_to_audio : str, start_of_gameplay_clip : float) -> tuple[int]:
    with AudioFileClip(path_to_audio) as audio_obj:
        duration = audio_obj.duration
        
    return start_of_gameplay_clip, start_of_gameplay_clip + duration

def create_subtitle_clips(cap_file_path: str, caption_font_path: str = None) -> list[TextClip]:
    text_clips = []
    
    with open(cap_file_path, "r") as file:
        caption_list = eval(file.read())
        
    for sentances in caption_list:
        clip = TextClip(sentances['text'])
        clip = clip.set_position(("center","center"))
        clip = clip.set_start(sentances['start']).set_end(sentances['end'])
        text_clips.append(clip)
        
    return text_clips
        
    
def make_video(
    output_path : str,
    backround_video_path : str,
    tts_audio_path : str,
    caption_file_path: str,
    audio_codec : str = r"aac",
    video_codec : str = r"libx264",
    output_fps : int = 30,
    gameplay_video_start_offset : float = 5,
    video_size : tuple[int, int] = (1080, 1920)
    
) -> None:

    backround_video = VideoFileClip(backround_video_path).set_fps(output_fps)
    main_audio = AudioFileClip(tts_audio_path)
    
    backround_video_cut  = backround_video.subclip(*calculate_video_duration(tts_audio_path, gameplay_video_start_offset))
    
    backround_video_audio = backround_video_cut.set_audio(main_audio)
    
    dimx, dimy = backround_video_audio.size
    desx, desy = video_size
    
    width_margin = (dimx - desx) // 2
    height_margin = (dimy - desy) // 2
    
    backround_video_resized = backround_video_audio.crop(x1=width_margin, y1=height_margin, x2=dimx - width_margin, y2=dimy - height_margin)
    
    output_clip = CompositeVideoClip([backround_video_resized] + create_subtitle_clips(caption_file_path))
    
    output_clip.write_videofile(output_path, codec=video_codec, audio_codec=audio_codec)

if __name__ == "__main__":
    backround_video_path = r"backround_video\backround_video_1.mp4"
    cap_file_path = r"working_dir\caption_data"
    main_audio = r"working_dir\audio.mp3"
    output_path = r"test.mp4"
    
    output_fps = 30
    gameplay_video_start_offset = 5
    video_size = 405, 720
    make_video(output_path,backround_video_path,main_audio,cap_file_path,video_size=video_size)
