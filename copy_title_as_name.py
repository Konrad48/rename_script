# Script for copying file name to title property in .mp3 file
import os
import eyed3

directory = 'D:\Muzyka\Shakira greatest hits'
ext = '.MP3'
changed_files = []

for filename in os.listdir(directory):
    audiofile = eyed3.load(directory+"\\"+filename)
    if audiofile.tag.title == None:
        audiofile.tag.title = filename[:-4]
        audiofile.tag.save()
        changed_files.append(filename)

print(changed_files)
        