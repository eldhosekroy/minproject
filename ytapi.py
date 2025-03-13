#AIzaSyCUqBpEbi62STuuX5I3rKeZ-KvCjMZfD8o
import webbrowser
import yt_dlp
from googleapiclient.discovery import build

# YouTube API Key (Get it from Google Cloud Console)
API_KEY = "AIzaSyCUqBpEbi62STuuX5I3rKeZ-KvCjMZfD8o"

def search_youtube(query):
    youtube = build("youtube", "v3", developerKey=API_KEY)

    request = youtube.search().list(
        q=query, part="snippet", type="video", maxResults=1
    )
    response = request.execute()

    if "items" in response and len(response["items"]) > 0:
        video_id = response["items"][0]["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    else:
        return None

def play_video(url):
    webbrowser.open(url, new=1)  # Open video in a new browser window

if __name__ == "__main__":
    query = input("Enter your search query: ")
    video_url = search_youtube(query)

    if video_url:
        print(f"Playing: {video_url}")
        play_video(video_url)
    else:
        print("No video found.")

