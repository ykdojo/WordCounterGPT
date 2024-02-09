import elevenlabs
elevenlabs.set_api_key('')
voices = elevenlabs.voices()
audio = elevenlabs.generate(text="Hello there!", voice=voices[0], model="eleven_multilingual_v2")
elevenlabs.play(audio)
print(type(audio))