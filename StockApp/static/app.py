# import pygame
# import time

# def play_audio(file_path):
#     # Initialize pygame
#     pygame.init()

#     # Load the music file
#     pygame.mixer.init()
#     pygame.mixer.music.load(file_path)

#     # Play the music on loop indefinitely
#     pygame.mixer.music.play(-1)

#     # We need to keep the script running
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         # Stop the music when Ctrl+C is pressed
#         pygame.mixer.music.stop()

# # Path to your mp3 file
# mp3_file_path = 'new_alert.mp3'

# # Play the audio on repeat
# play_audio(mp3_file_path)

# # from playsound import playsound

# # def play_audio(file_path):
# #     while True:
# #         playsound(file_path)

# # # Path to your mp3 file
# # mp3_file_path = 'new_alert.mp3'

# # # Play the audio on repeat
# # play_audio(mp3_file_path)

# from moviepy.editor import VideoFileClip

# video = VideoFileClip('videoplayback.mp4')
# video.audio.preview()
import vlc
import time

# Create a MediaPlayer with the MP4 file
player = vlc.MediaPlayer('videoplayback.mp4')

# Start playing the MP4 file
player.play()

# Wait until the player has started before exiting
time.sleep(1)  # Wait for 1 second to allow the player to start
while player.is_playing():
    time.sleep(1)
