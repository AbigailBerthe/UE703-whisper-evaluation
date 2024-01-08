import nltk
import json
from pathlib import Path
import re

#fin all files in a folder
def find_all_files(directory):
    pathlist = Path(directory).rglob('*.*')  # Research all the files
    files = []
    pattern = r'.*(CasualConversation.*)'  # Pattern regex to extract from "CasualConversation" which is where the file name start in the json transcription file

    for path in pathlist:
        path_str = str(path)
        # Replace antislashs by slashs (as they are in the json transcription file)
        path_str = path_str.replace("\\", "/")
        match = re.match(pattern, path_str)
        if match:
            # Add the extracted part from the file
            files.append(match.group(1))
        else:
            files.append(path_str)
    return files

# Function to filter data based on video_path (only keep the data for the video I'll use)
def filter_data_by_video_path(data, paths):
    filtered_data = [item for item in data if item["video_path"] in paths]
    return filtered_data

#read the json file
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

#save to a json file
def save_to_json(file_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(file_list, f, ensure_ascii=False, indent=4)


#all files names
files = find_all_files('D:\\M1 TAL\\CCV1\\CasualConversationsA')

# Path to my JSON file
json_file_path = 'C:\\Users\\abiga\\AppData\\Local\\Temp\\atom-202407-12868-1jqrro2.bi4t\\An9Qr02KoEoA9So2BUl7pQe_E1cAiXC2uCrIo9x113t6nQoIxRqSP9njNZXzqqmX9NVFY5EgxYVucx5nXL-YMvPdsI7XCdPBKIIAf7qVgRJq0vsRAdhrerCUwoo.zip\\CasualConversations_transcriptions.json'  # Replace with the actual path to your file

# Read the JSON data from the file
data_from_file = read_json_file(json_file_path)

# Filter the data from the file
filtered_data_from_file = filter_data_by_video_path(data_from_file, files)

save_to_json(filtered_data_from_file, "transcription_part1")

print(filtered_data_from_file)
