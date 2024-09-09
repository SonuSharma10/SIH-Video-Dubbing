import soundfile as sf
import numpy as np
import audioread

data, samplerate = sf.read("output2.mp3")
# To make the speed faster, use a higher playback rate

# Open the MP3 file
generated = audioread.audio_open("output2.mp3")
original = audioread.audio_open("audio.mp3")
duration_generated = generated.duration
duration_original = original.duration

playback_rate = round(duration_generated/duration_original,2)
print(playback_rate)

print(duration_generated,duration_original)


# Resample the data to match the playback rate
data = np.interp(
    np.arange(0, len(data), playback_rate), 
    np.arange(0, len(data)), 
    data)

# Play the modified audio
# sd.play(data, samplerate)
# sd.wait()
# Save the modified audio
sf.write("audio_fast.mp3", data, samplerate)
