from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World, Jack'

@app.route('/transcript/<video_id>')
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = TextFormatter()
    transcript_text = formatter.format_transcript(transcript)
    return transcript_text

