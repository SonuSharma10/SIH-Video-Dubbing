import socket
import pydub
from pydub import AudioSegment

# Network settings
host = '127.0.0.1'
port = 12345

# Function to send audio data
def send_audio(client_socket, audio_data):
  try:
      client_socket.sendall(audio_data)
  except Exception as e:
      print(f"Error sending audio: {e}")

# Open an audio file for streaming
audio_path = r"C:\Users\rushi\OneDrive\Desktop\realtime\realtime\output2.mp3"
audio_segment = AudioSegment.from_mp3(audio_path)

# Convert the audio to raw PCM data
audio_data = audio_segment.raw_data

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
  client_socket.connect((host, port))

  # Send audio data to the server
  send_audio(client_socket, audio_data)
