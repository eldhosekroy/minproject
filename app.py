from flask import Flask, render_template, request, jsonify
import requests
import os
from googleapiclient.discovery import build

app = Flask(__name__)

# Set API Keys
GEMINI_API_KEY = "AIzaSyCG22aB1LmOdAt93vqgDeR4qY8De8jTing"
YOUTUBE_API_KEY = "AIzaSyCUqBpEbi62STuuX5I3rKeZ-KvCjMZfD8o"

# Gemini AI API URL
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def get_gemini_response(prompt):
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Sorry, I couldn't process that request."

def search_youtube(query):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(q=query, part="snippet", type="video", maxResults=1)
    response = request.execute()

    if "items" in response and len(response["items"]) > 0:
        video_id = response["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/embed/{video_id}?autoplay=1"
    else:
        return "https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1"  # Default video

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_question = data.get("question", "")

    ai_response = get_gemini_response(user_question)
    video_url = search_youtube(user_question)

    return jsonify({"response": ai_response, "video_url": video_url})

if __name__ == "__main__":
    app.run(debug=True)

