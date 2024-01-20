from moviepy.editor import *
from pathlib import Path
import re

#fin all files in a folder and its subfolders
def find_all_files(directory):
    pathlist = Path(directory).rglob('*.*')  # Research all the files
    files = []

    for path in pathlist:
        path_str = str(path)
        # Replace antislashs by slashs (as they are in the json transcription file)
        path_str = path_str.replace("\\", "\\\\")

        files.append(path_str)
    return files


#all files names
files = find_all_files('D:\\M1 TAL\\CCV1\\CasualConversationsA')
#pattern for naming the file
pattern = r'.*(\d{4}_\d{2}).MP4'

for file in files:
        match = re.match(pattern, file)
        #print(match.group(1))
        # upload MP4 file
        video = VideoFileClip(file)
        # extract audio
        audio = video.audio
        # save as WAV file
        audio.write_audiofile(f"D:\\M1 TAL\\CCV1\\wav_data\\{match.group(1)}.wav")
