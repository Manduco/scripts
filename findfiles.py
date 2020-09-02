import glob, os
from os import path
from pydub import AudioSegment

count = 0
#working dir
Dir_To_Search = "testfile"
os.chdir(Dir_To_Search)

print(" Converting..")
for file in glob.glob("*.wav"):
    #print("found :",file)
    dst = "convert"+str(count)+".mp3"
    name_of_file = file.split(".")
    name_convert = name_of_file[0] +".mp3"

    sound = AudioSegment.from_wav(file)
    sound.export(name_convert, format="mp3")

    print(file+ " >> "+name_convert)
    count+= 1
