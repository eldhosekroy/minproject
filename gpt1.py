import yt_dlp
import vlc
import time

def get_video_url(query):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)
        if 'entries' in info and len(info['entries']) > 0:
            return info['entries'][0]['url']
    
    return None

def play_video(video_url):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(video_url)
    player.set_media(media)

    player.set_fullscreen(True)  # Fullscreen mode
    player.play()

    while player.get_state() not in [vlc.State.Ended, vlc.State.Stopped]:
        time.sleep(1)

if __name__ == "__main__":
    query = input("Enter your search query: ")
    video_url = get_video_url(query)

    if video_url:
        print(f"Playing video: {video_url}")
        play_video(video_url)
    else:
        print("No video found.")

