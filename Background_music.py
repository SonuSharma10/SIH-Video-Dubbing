# Import the required libraries
import librosa
import soundfile as sf

# Load the audio file as a waveform
y, sr = librosa.load("audio.mp3", sr=None, mono=True)

# Compute the short-time Fourier transform of the waveform
S = librosa.stft(y)

# Separate the magnitude and phase components of the spectrum
magnitude, phase = librosa.magphase(S)

# Use harmonic-percussive source separation to split the magnitude into harmonic and percussive components
S_harmonic, S_percussive = librosa.decompose.hpss(magnitude)

# Use non-negative matrix factorization to decompose the harmonic component into a set of basis vectors and activations
W, H = librosa.decompose.decompose(S_harmonic, n_components=16, sort=True)

# Assume that the vocals are the most dominant component in the harmonic spectrum and select the first basis vector and activation
W_vocal = W[:, 0:1]
H_vocal = H[0:1, :]

# Reconstruct the vocal spectrum by multiplying the vocal basis and activation
S_vocal = W_vocal @ H_vocal

# Reconstruct the background spectrum by subtracting the vocal spectrum from the harmonic spectrum
S_background = S_harmonic - S_vocal

# Convert the vocal and background spectra back to waveforms using the original phase
y_vocal = librosa.istft(S_vocal * phase)
y_background = librosa.istft(S_background * phase)

# Save the vocal and background waveforms as separate audio files
sf.write("vocal.wav", y_vocal, samplerate=sr)
sf.write("background.wav", y_background, samplerate=sr)
