# Import the pytube library
from pytube import YouTube
from openai import OpenAI
from pydub import AudioSegment
import soundfile as sf
import numpy as np
import audioread


def download_video(link):
    yt = YouTube(link)
    stream = yt.streams.filter(file_extension="mp4", progressive=True).order_by("resolution").desc().first()
    stream.download(filename="videofile.mp4")

link = input("Enter the YouTube video link: ")
download_video(link)

client = OpenAI(api_key = "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")
path_mp4 = "./videofile.mp4"
target_language = "hindi"

video_file = open(path_mp4, "rb")
song = AudioSegment.from_file(video_file, format="mp4")
song.export("audio.mp3", format="mp3")

audio_file = open("audio.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)
with open(f'transcript.txt', 'w') as file:
    file.write(transcript)
print(transcript)

audio_file = open("audio.mp3", "rb")
transcript2 = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="srt"
)
with open(f'transcript.srt', 'w') as file:
    file.write(transcript2)
print(transcript2)

text = open('transcript.txt', 'r').read()

print(text)

prompt = f"translate the {text} file into {target_language}. the format of translation should be {target_language}"

print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ],
)
translated_text = completion.choices[0].message.content
print(translated_text)


response = client.audio.speech.create(
    model="tts-1-hd",
    voice="fable",
    input=translated_text,
)

response.stream_to_file("output2.mp3")


data, samplerate = sf.read("output2.mp3")

generated = audioread.audio_open("output2.mp3")
original = audioread.audio_open("audio.mp3")
duration_generated = generated.duration
duration_original = original.duration

playback_rate = round(duration_generated/duration_original,2)
print(playback_rate)

print(duration_generated,duration_original)

data = np.interp(
    np.arange(0, len(data), playback_rate), 
    np.arange(0, len(data)), 
    data)

# Play the modified audio
# sd.play(data, samplerate)
# sd.wait()
# Save the modified audio
sf.write("audio_fast.mp3", data, samplerate)
