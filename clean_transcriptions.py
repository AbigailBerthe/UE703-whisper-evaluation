import json
import re

def clean_transcription(text):
    """Remove text within < > and [ ]"""
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'\[[^\]]*\]', '', text)
    text = re.sub(r'[=%]', '', text)
    return text

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    # the structure is a list of dictionaries with a "transcription" key
    for entry in data:
        if 'transcription_timestamp' in entry:
            entry['transcription_timestamp'] = clean_transcription(entry['transcription_timestamp'])

    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)


process_file('transcription_part1.json', 'cleaned_transcriptions.json')
