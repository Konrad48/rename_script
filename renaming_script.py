# Script renames mp3 files downloaded via: https://mp3dl.cc/
import os, re

print('Hi mom')
directory = 'D:\Muzyka\Shakira greatest hits'
ext = '.MP3'
output_filenames = []

pattern = re.compile("\[MP3DL\.CC\].*-320k")
for filename in os.listdir(directory):
    if filename.endswith(ext) and pattern.match(filename):
        out_filename = re.sub('(^\[MP3DL\.CC\]\s)','', filename)
        out_filename = re.sub('(-320k)','', out_filename)
        output_filenames.append(out_filename)
        os.rename(directory+"\\"+filename, directory+"\\"+out_filename)
    else:
        continue
print(output_filenames)

