import os

# read mp3 files from the audio directory and list them
def read_mp3_files():
    audio_files = []
    for file in os.listdir("audio"):
        if file.endswith(".mp3"):
            audio_files.append(file)
    return audio_files

print(read_mp3_files())

'''
def read_audio_list_from_files():
    audio_list = []
    with open('audio_list.txt', 'r') as f:
        for line in f:
            audio_list.append(line.strip())
    return audio_list
    
def read_audio_list
'''
