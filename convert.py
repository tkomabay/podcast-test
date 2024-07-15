import os
import eyed3
import yaml

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
        if file.endswith('.mp3'):
            audio_file = eyed3.load(os.path.join('audio',file))
            comments = ''
            if audio_file.tag.comments:
                for comment in audio_file.tag.comments:
                    comments += comment.text + '\n'
            audio_files.append({
                'title': audio_file.tag.title,
                'comments': comments
            })
    return audio_files

print(yaml.dump(get_audio_files()))

'''
def read_audio_list_from_files():
    audio_list = []
    with open('audio_list.txt', 'r') as f:
        for line in f:
            audio_list.append(line.strip())
    return audio_list
    
def read_audio_list
'''
