# to run the scirp place this scirpt,,
# in dir higher then the files you..
# which to convert
# by Armando Zincke

import glob, os
from os import path
from pydub import AudioSegment

Folders_found = 0
Files_found = 0

Dir_Root = "testfile"
Dir_To_Search = "testfile"
Dir_Sub_Wildcard = "1295782*"
Dir_Return = ".."
Dir_current = "whateve"

# Scirpt process Below {

#changes current working dir
#print(os.path.abspath(os.curdir))
os.chdir(Dir_Root)

print(" ")
print(" --------------Start---------------")
print(" ")

for folder in glob.glob(Dir_Sub_Wildcard):

    Folders_found += 1
    #changes current working dir
    os.chdir(folder)
    print(" ")
    print(" Path =" , os.path.abspath(os.curdir))
    print(" ")

    for file in glob.glob("*.wav"):

        #dst = "convert"+str(count)+".mp3"

        name_of_file = file.split(".")
        name_convert = name_of_file[0] + ".mp3"
        sound = AudioSegment.from_wav(file)
        sound.export(name_convert, format = "mp3")
        print(" -- "+file + " >> " + name_convert)
        Files_found += 1


    #Dir_current =  ("at", os.path.abspath(os.curdir))
    #print("At: ",Dir_current)
    os.chdir(Dir_Return)

print(" ")
print(" Total Folders Found:",Folders_found)
print(" Total Files Found:",Files_found)
print("- end -")

# } Scirpt process end
