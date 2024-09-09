# Import the required libraries
import openai
from openai import OpenAI
from pydub import AudioSegment


# Initialize the OpenAI client with your API key
client = OpenAI(api_key = "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")
# openai.api_key = "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"

path_mp4 = "./videoplayback.mp4"
target_language = "hindi"
'''
# Load the video file and convert it to mp3 format
video_file = open(path_mp4, "rb")
song = AudioSegment.from_file(video_file, format="mp4")
song.export("audio.mp3", format="mp3")

# Load the mp3 file and transcribe it using OpenAI


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
'''
# Get the text from the transcript
text = open('transcript.txt', 'r').read()

print(text)


# prompt = f"change this english text into {target_language} language. make it better by {target_language} but written in english alphabet for reading, as example 'namaste, kaise ho', now translate and change accordingly : {text}"

prompt = f"translate the {text} file into {target_language}. the format of translation should be {target_language}"
# Non-streaming:
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

# with open('translate.txt', 'w') as file:
#   file.write(translated_text)


'''
# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": f"change this SRT file language into hindi. make sure you dont change the time stamp. the SRT file is: {text}",
        },
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue

    print(chunk.choices[0].delta.content, end="")
'''
