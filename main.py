import requests
from youtube_transcript_api import YouTubeTranscriptApi

# Replace with your video ID and webhook URL
video_id = "GPLImB-I71w"
webhook_url = "https://primary-production-6a78.up.railway.app/webhook-test/88083a26-a34a-41cd-9340-bb99db04a0cb"

# Fetch the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Define the output file name
output_file = f"{video_id}_transcript.txt"

# Write the transcript to a file
with open(output_file, "w", encoding="utf-8") as file:
    for entry in transcript:
        file.write(f"{entry['start']:.2f}s ({entry['duration']:.2f}s): {entry['text']}\n")

print(f"Transcript saved to {output_file}")

# Send the file to the webhook
with open(output_file, "rb") as file:
    response = requests.post(webhook_url, files={"file": file})

# Check the webhook response
if response.status_code == 200:
    print("Transcript sent successfully!")
else:
    print(f"Failed to send transcript. Status code: {response.status_code}, Response: {response.text}")