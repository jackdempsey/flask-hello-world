# https://github.com/jdepoix/youtube-transcript-api
from youtube_transcript_api import YouTubeTranscriptApi

# some provided subclasses, each outputs a different string format.
from youtube_transcript_api.formatters import TextFormatter

video_id = 'pVj2uyaQ_2A'

# Must be a single transcript.
transcript = YouTubeTranscriptApi.get_transcript(video_id)

formatter = TextFormatter()

text_formatted = formatter.format_transcript(transcript)


# Now we can write it out to a file.
with open('your_filename.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(text_formatted)

