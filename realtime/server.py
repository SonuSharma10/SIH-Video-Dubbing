import socket
import pydub
from pydub import AudioSegment
from pydub.playback import play

# Network settings
host = '127.0.0.1'
port = 12345

# Function to stream audio
def stream_audio(client_socket, audio_data):
   try:
       # Convert audio data to pydub AudioSegment
       audio_segment = AudioSegment(data=audio_data, sample_width=2, channels=2, frame_rate=44100)
       
       # Play the audio
       play(audio_segment)
   except Exception as e:
       print(f"Error streaming audio: {e}")

# Start the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
   server_socket.bind((host, port))
   server_socket.listen()

   print(f"Listening on {host}:{port}")

   while True:
       client_socket, addr = server_socket.accept()
       print(f"Connection from {addr}")

       try:
           # Receive audio data from the client
           audio_data = b""
           while True:
               chunk = client_socket.recv(1024)
               if not chunk:
                  break
               audio_data += chunk

           # Stream the received audio
           stream_audio(client_socket, audio_data)

       except Exception as e:
           print(f"Error handling client connection: {e}")
       finally:
           client_socket.close()
