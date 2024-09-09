from moviepy.editor import VideoFileClip

# Load the video clip
videoclip = VideoFileClip("videoplayback.mp4")

# Remove the audio track
new_clip = videoclip.without_audio()

# Save the new clip
new_clip.write_videofile("video_no_vocals.mp4")
