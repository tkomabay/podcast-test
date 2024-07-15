import os
import eyed3
import yaml
import time

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
                    comments += comment.text
            duration = time.strftime('%H:%M:%S', time.gmtime(audio_file.info.time_secs))
            size = os.path.getsize(os.path.join('audio', file))
            size_str = '{:,}'.format(size)
            audio_files.append({
                'title': audio_file.tag.title,
                'comments': comments,
                'filename': '/audio/' + file,
                'duration': duration,
                'size': size_str
            })
    return audio_files

def convert_to_yaml():
    data = get_audio_files()
    yaml_data = yaml.dump(data, sort_keys=False)
    with open('episodes.yaml', 'w') as f:
        f.write(yaml_data)

convert_to_yaml()

'''
def read_audio_list_from_files():
    audio_list = []
    with open('audio_list.txt', 'r') as f:
        for line in f:
            audio_list.append(line.strip())
    return audio_list
    
def read_audio_list
'''
