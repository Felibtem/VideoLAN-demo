import vlc
import time

# Load a media file (replace with your own mp3/mp4)
media_path = "sample.mp3"
player = vlc.MediaPlayer(media_path)

# Play media
player.play()
time.sleep(5)  # plays for 5 seconds
player.stop()
print("Media played successfully!")
