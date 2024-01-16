import pandas as pd
import librosa
import numpy as np
import soundfile as sf

"""
This python code aims at creating one file for all sounds of same category, to have one 3 min file instead of 40 4 seconds files

"""

#read excel file
df = pd.read_excel('C:\\Users\\abiga\\Downloads\\ESC50.XLSX')

# group by type
grouped = df.groupby('category')

for type, group in grouped:
    audio_clips = []

    for filename in group['filename']:
        # load audio file
        audio, sr = librosa.load(f'C:\\Users\\abiga\\Downloads\\archive\\audio\\audio\\16000\\{filename}', sr=None)
        audio_clips.append(audio)

        # Concat the audio files
        concatenated_audio = np.concatenate(audio_clips)

        # save the file
        output_filename = f'concatenated_{type}.wav'
        sf.write(output_filename, concatenated_audio, sr)
