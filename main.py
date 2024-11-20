import os
import json
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

def get_transcript(video_id):
    # Fetch transcript for the given video_id
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript

def send_to_webhook(transcript, webhook_url):
    # Send the transcript to the provided webhook URL as JSON
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, json=transcript, headers=headers)
    return response

def main():
    # Get the video ID and webhook URL from environment variables
    video_id = os.getenv("VIDEO_ID")
    webhook_url = os.getenv("WEBHOOK_URL")

    if not video_id or not webhook_url:
        print("Error: VIDEO_ID or WEBHOOK_URL is missing!")
        return

    try:
        # Get the transcript from YouTube API
        print(f"Fetching transcript for video ID: {video_id}")
        transcript = get_transcript(video_id)

        # Format the transcript as JSON
        formatter = JSONFormatter()
        formatted_transcript = formatter.format_transcript(transcript)

        # Send the formatted transcript to the webhook
        print("Sending transcript to webhook...")
        response = send_to_webhook(formatted_transcript, webhook_url)

        if response.status_code == 200:
            print(f"Transcript successfully sent to webhook: {webhook_url}")
        else:
            print(f"Failed to send transcript. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
