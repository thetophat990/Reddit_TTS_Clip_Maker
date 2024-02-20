from openai import OpenAI        # Used to make the OpenAI API calls
from json import loads           # Used to load response of subtitles into python dictonery

def genarate_subtitles(api_key : str, audio_path : str = "audio.mp3") -> list[dict[float, str]]:
    return_list = []
    
    api_object = OpenAI(api_key=api_key)    # Create openAI API object
    
    with open(audio_path, "rb") as file_obj:    # Read audio data from TTS output
        response = api_object.audio.transcriptions.create(    # Call transcription model
                file=file_obj,
                model="whisper-1",    # TODO change this to a setting instead of hard coded
                response_format="verbose_json"
        )
   
    data = loads(response.model_dump_json())["segments"]    # Loads segmants section into python
    
    for subtitles in data:
        words = subtitles['text'].split(' ')    # Split the sentance into individual words
        duration = subtitles['end'] - subtitles['start']    # Calculate duration
        time_buffer = subtitles['start']    # Buffer used to store last time, initalised at start of subtitles
        for word in words:
            if word in ['', ' ', '.', ',', '\n']: continue    # Remove non words, e.g empty strings
            calc_speak_time = (len(word) / len(subtitles['text'])) * duration    # calculate time to speak for each word
            
            return_list.append({'start' : round(time_buffer, 2), 'end' : round(time_buffer + calc_speak_time, 2), 'text' : word}) # Append new subitle data to list, and rounding values
            time_buffer += calc_speak_time

    return return_list

def genarate_tts(text : str, api_key : str, voice : str = "alloy", max_chars : int = 4095) -> bytes:
    api_object = OpenAI(api_key=api_key)    # Create openAI API object
    
    if len(text) >= max_chars:              # Check if charicters in string exceed maximum charicter length, if so, trim the string 
        text = text[:max_chars]
    
    response = api_object.audio.speech.create(    # Call TTS Model
        input=text,
        model="tts-1",
        voice=voice
    )
      
    response = response.read()    # Decode response into audio format
        
    return response

if __name__ == "__main__":    # TODO add module test
    pass
