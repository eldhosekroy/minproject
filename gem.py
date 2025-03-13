import os
import requests
import json

# Set your API key (Use an environment variable for security)
#API_KEY = os.getenv("GOOGLE_API_KEY")  # Set this in your terminal
API_KEY = ("AIzaSyCG22aB1LmOdAt93vqgDeR4qY8De8jTing")  # Set this in your terminal
if not API_KEY:
    raise ValueError("API key not found! Set GOOGLE_API_KEY as an environment variable.")

# Gemini API URL
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Function to send a request
def get_gemini_response(prompt):
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Chat loop
print("Gemini AI Terminal Chat (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = get_gemini_response(user_input)
    print(f"Tutor : {response}")
