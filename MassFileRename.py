# Python3 code to rename multiple
# files in a directory or folder
#
# file must be named in order
# os.listdir will put name_10 after name_1
#
# tested 2019/06/06
# by Armando Zincke


# importing os module
from sys import argv
import os

# Function to rename multiple files
def main():


    NameList = ['Aja','Alan','Alana','Alejandro','Armando',
    'Ashley','Audrey','Ben','Bentley','Bill','Bob','Brook','Cara',
    'Cathy','ChrisBatcho','ChrisGero','ChrisVigilante','Christine','Christopher',
    'Collin','Danielle','Darren','DavidDean','DavidKoehler',
    'DavidSmith','DeAnna','DeeDee','Derrick','Donna','Electric',
    'Erika','Evelio','Frederick','Gary','Hyung Park','India Sugar','James Abels','James Rawlings','Jason Sigler',
    'Jason Zierman','Jay Rosen','Jeremy Shinn','Jessica Norrell','Jim Bledsoe','John McDaniel',
    'Juddson Ivines','Kaitlyn Dougherty','Kayla Kasza','Ken Scholz','Kevin Almanzar','Kevin Byrne',
    'Kyle DeGroff','Lily Woodard','Linda Brink','LuAnn Carter','Malka Jackson','Mark Lakin','Mary Kestner',
    'Melissa Kestner','Michael Connors','Michael Heuss','Michael Merritt','Nancy Meagher',
    'Nate Henjes','Paige Cumbest','Pate Henderson','Paul E Prusakowski','Pete Clark','Philip Blackmon',
    'Pragnesh Patel','Priya Rudradas','Rita Blumenberg','Robert Mullally','Ryan Kerwin','Sandy Howell',
    'Sarah Thomas','Scott Williamson','Sean Dodds','Shannon Sechrest','Shirley Mogensen','Steve Kaercher',
    'Steve McMullen','Susanne Kasza','Tammy Dyess','Tee Tetrick','Trina Whitton','Tyler Trushin','Valerie Vastola']
    # getting length of list
    # length = len(NameList)
    i = 0

    # Iterating using while loop

 #  for NAME in NameList:
 #     print(NAME)
 #     print(i)
 #     i += 1
      ## print the numbers from 0 through 99

    for filename in os.listdir(".\\"+"FunOfExceSig"+"\\"):
         dst1 = NameList[i] + "-NewSig" + ".htm"
         src =  ".\\"+'FunOfExceSig'+"\\"+filename
         dst =  ".\\"+'FunOfExceSig'+"\\"+ dst1
         os.rename(src, dst)
         print("File", i ," FileName: ", filename ," Renamed to:", dst )
         i = i+1
       # rename() function will
       # rename all the files

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
