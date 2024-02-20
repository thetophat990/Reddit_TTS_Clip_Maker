from openai import OpenAI
from json import loads

def genarate_subtitles(api_key : str, audio_path : str = "audio.mp3") -> list[dict[float, str]]:
    return_list = []
    
    api_object = OpenAI(api_key=api_key)
    
    with open(audio_path, "rb") as file_obj:
        response = api_object.audio.transcriptions.create(
                file=file_obj,
                model="whisper-1",
                response_format="verbose_json"
        )
   
    data = loads(response.model_dump_json())["segments"]
    
    for subtitles in data:
        words = subtitles['text'].split(' ')
        duration = subtitles['end'] - subtitles['start']
        time_buffer = subtitles['start']
        for word in words:
            if word in ['', ' ', '.', ',', '\n']: continue
            calc_speak_time = (len(word) / len(subtitles['text'])) * duration
            
            return_list.append({'start' : round(time_buffer, 2), 'end' : round(time_buffer + calc_speak_time, 2), 'text' : word})
            time_buffer += calc_speak_time

    return return_list

def genarate_tts(text : str, api_key : str, voice : str = "alloy", max_chars : int = 4095) -> bytes:
    api_object = OpenAI(api_key=api_key)
    
    if len(text) >= max_chars:
        text = text[:max_chars]
    
    response = api_object.audio.speech.create(
        input=text,
        model="tts-1",
        voice=voice
    )
      
    response = response.read()
        
    return response

if __name__ == "__main__":
    pass
