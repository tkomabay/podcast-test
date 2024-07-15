import os
import eyed3

# read mp3 files from the audio directory and list them
def read_mp3_files():
    audio_files = []
    for file in os.listdir("audio"):
        if file.endswith(".mp3"):
            audio_files.append(file)
    return audio_files

def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        audio_file = eyed3.load(os.path.join('audio',file))
        audio_files.append({
            'title': audio_file.tag.title,
            'comments': audio_file.tag.comments
        })
    return audio_files

print(get_audio_files())

'''
def read_audio_list_from_files():
    audio_list = []
    with open('audio_list.txt', 'r') as f:
        for line in f:
            audio_list.append(line.strip())
    return audio_list
    
def read_audio_list
'''
