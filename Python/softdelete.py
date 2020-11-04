# to run the scirp place this scirpt,,
# in dir higher then the files you..
# which to convert
# by Armando Zincke

import glob, os , shutil
from os import path
from pydub import AudioSegment
from send2trash import send2trash


#define vars
Folders_found = 0
Files_found = 0
Num_Of_Wav = 0
Num_Of_Mp3 = 0
Total_Num_Of_Wav = 0
Total_Num_Of_Mp3 = 0
Num_Deleted = 0

Dir_Root = "testfile"
Dir_To_Search = "testfile"
Dir_Sub_Wildcard = "1295782*"
Dir_Return = ".."
Dir_current = "whateve"

User_answer=''
Can_Delete_Wav = False
Confirm_Answer = False
All_Wav_deleted= False

# define Func Here
def Delete_files():
    global Num_Deleted
    print("\n -Soft Delete-")
    for file in glob.glob("*.wav"):
        print(" deleting>>"+file)
        send2trash(file)
        Num_Deleted += 1
    #input("deleted")
        #loop ends
def count_wav():
    global Total_Num_Of_Wav
    global Num_Of_Wav
    Total_Num_Of_Wav = Total_Num_Of_Wav + Num_Of_Wav
    Num_Of_Wav = 0
def count_mp3():
    global Num_Of_Mp3
    global Total_Num_Of_Mp3
    Total_Num_Of_Mp3 = Total_Num_Of_Mp3 + Num_Of_Mp3
    Num_Of_Mp3 = 0

# Scirpt process Below {

#changes current working dir
os.chdir(Dir_Root)
#Print_below_shows_current_dir_the_script_is_Working_in_
#print(os.path.abspath(os.curdir))

print("\n --------------Start----------------")
print(" --- press enter to start sreach --- ")

for folder in glob.glob(Dir_Sub_Wildcard):

    Folders_found += 1
    #changes current working dir
    os.chdir(folder)
    print(" ")
    print(" Current Directory" + " >>> "+Dir_Root+"/"+folder+"---| ")

    #find all .WAV in current dir
    for file in glob.glob("*.wav"):
        print(" -- "+file)
        Files_found += 1
        Num_Of_Wav += 1
        #loop ends
    #find all .mp3 in current dir
    for file in glob.glob("*.mp3"):
        print(" -- "+file)
        Files_found += 1
        Num_Of_Mp3 += 1
        #loop ends

    print(" .wav:" , str(Num_Of_Wav) + " .mp3:" , str(Num_Of_Mp3) )

    if(Num_Of_Mp3==Num_Of_Wav):
        print("\n -Dir Files have even distro- ")
        Can_Delete_Wav = True
    else:
        print("\n -Dir Files does NOT have even distro- ")
        Can_Delete_Wav = False

    print(" |---"+Dir_Root+"/"+folder+"---| ")
    #Dir_current =  ("at", os.path.abspath(os.curdir))
    #print("At: ",Dir_current)

    count_wav()
    count_mp3()

    #if(Can_Delete_Wav == True):
        #while (User_answer != "y" or User_answer != "n"):
        #User_answer = input(" |----DELETE ALL (.wav) ?----| \n y/n : ")
    if(Can_Delete_Wav == True and Folders_found <= 5 ):
        Delete_files()
    if(Can_Delete_Wav == False):
        print(" Can NOT delete ")

    #return to perent dir
    os.chdir(Dir_Return)

#Stats
print(" ----------------------------------- ")
print(" Total Folders paresd: ",Folders_found)
print(" Total Files Found:  ",Files_found)
print(" Total .wav Files Found:",Total_Num_Of_Wav)
print(" Total .mp3 Files Found:",Total_Num_Of_Mp3)
print(" Total .Wav files Deleted:",Num_Deleted)
print(" ----------------------------------- ")

# } Scirpt process end
