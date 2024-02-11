from openai import OpenAI
from json import loads

def genarate_subtitles(api_key : str, audio_path : str = "audio.mp3") -> str:
    UNUSED_KEYS = ['id', 'seek', 'tokens', 'temperature', 'avg_logprob', 'compression_ratio', 'no_speech_prob']
    ROUNDED_KEYS = ['start', 'end']
    
    api_object = OpenAI(api_key=api_key)
    
    with open(audio_path, "rb") as file_obj:
        response = api_object.audio.transcriptions.create(
                file=file_obj,
                model="whisper-1",
                response_format="verbose_json"
        )
   
    data = loads(response.model_dump_json())["segments"]
    
    data_strip = [{key: value for key, value in item.items() if key not in UNUSED_KEYS} for item in data]
    
    data_rounded = [{key: round(value, 2) if key in ROUNDED_KEYS else value for key, value in item.items()} for item in data_strip]
   
    return data_rounded

def genarate_tts(text : str, api_key : str, voice : str = "alloy") -> bytes:
    api_object = OpenAI(api_key=api_key)
    
    response = api_object.audio.speech.create(
        input=text,
        model="tts-1",
        voice=voice
    )
      
    response = response.read()
        
    return response

if __name__ == "__main__":
    api_key = "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"
    audio_path = r"working_dir\audio.mp3"
    text_out_path = r"working_dir\capti.file"
    sample_text = """What’s something people say to appear more intelligent than they actually are?.. Talking oddly fast, using big words, and dropping random ass acronyms. I work in IT and it's so painful hearing one of the guys explain stuff to people. You can see it in their eyes that they don't give two shits.   I go out of my way to explain everything very basic and easy so people can understand. I'm sure I make myself sound like an idiot to the other ITs but most of the people I help don't seem to mind.  And over explaining. Half of these people couldn't care less about what the DHCP is doing or the DNS doing this and that. They just want their emails to work and printers to print... Using lots of big and/or technical words and intentionally complex language is generally a sign of insecurity. Intelligent people who are at ease with their intelligence tend to speak in relatable terms.   My ex-wife was a PhD neuroscientist and the most intelligent human being I’ve ever met by a wide margin. She cursed like a sailor and could explain complicated concepts to literally anybody in a way that they could understand. Only threw around technical terms when talking to someone who she knew would understand them... My father was an actual genius. The kind of genius other geniuses call a genius.   He told me once, "When you meet someone that is an expert in their field. Only open your mouth enough to ask questions and keep them talking. There is no amount of studying that compares to a lifetime of experience and you rarely get the time to learn from people with it. So take every opportunity when it presents itself.".. Following up someone else’s statement (usually someone who actually knows what they’re talking about) with a paraphrased version of the same thing to make it seem like they thought of it 🙄 I see this all the time at work and if you’re the type to do that just know everyone notices and talks shit about it lol.. Bragging about how much education they have. I went through a 4 year degree and learned that sometimes those who succeed academically are just very hard workers and their intelligence plays a minor role. But this is not always the case... When they tell me that what I don’t understand is that a particular behavior or action is actually a grand political or sociological signifier supporting the grand unified theory which they adhere to.  Sometimes a cigar is just a cigar….. I have an IQ of (names a super high number)   First, IQ isn't always an accurate measure of intelligence.  And two, odds are that person took a random free quiz online somewhere with super easy answers instead of an actual test.  .. I've found people who want to sound smart attempt to use jargon and confuse the other person.   I've found actual smart people are able to use jargon without confusing the person they're talking to though... I find it not something they say, but how they say it. Dumb people will be very adamant that they're correct, intelligent people will admit they're often wrong or just not care if you disagree... Having overconfidence in topics they have no business really talking about. Truly intelligent people usually recognize when they don’t know something... When people start psychologically diagnosing people with certain mental illness off the basis that they’ve displayed a couple of symptoms lol.. The second I hear "do your own research" I instantly know I'm dealing with a person that has literally never done research in their life... “They asked me if I had a degree in theoretical physics. I said that I had a theoretical degree in physics and got the job.”.. I work with a guy who says “correct” to almost everything anyone says, as if nothing you tell him is news. He knows it all!.. Disagreeing for the sake of argument. A lot of people these days seem to confuse being contrarian with being intelligent... Dropping quotes from famous philosophers or scholars without a clear understanding of the context or deeper meanings..."""
    
    # with open(audio_path, "wb") as audio_obj:
    #     audio_obj.write(genarate_tts(sample_text, api_key, "alloy"))
        
    with open(text_out_path, "w") as file_obj:
        file_obj.write(repr(genarate_subtitles(api_key, audio_path)))