
print(" --- Make configs ---")

version = 0.0


localIP = raw_input("Enter Local IP : ")
GetHost = " "

config1= " "


#opens or creates config txt file
f = open("config.txt", "w")

def write():
    f.write("IP given" + localIP +"\n")#
def close():

    f.close()
    print ("Configs Created")

def config1():
    f.write("version " + str(version) + "\n"
            + "no service pad service \n"
            + "timestamps debug datetime msec \n"
            + "service timestamps log datetime msec \n"
            + "no service password-encryption \n"+
            "!\n")

def secure():
    f.write( "hostname cisco28\n" + "!\n"
        +"boot-start-marker\n"
        +"boot-end-marker\n" +"!\n"
        +"logging buffered 128000 \n"
        +"enable secret 5 $1$wgM4$hnI4TqvqWv8EwjDWUgsjQ1\n"
        +"enable password something\n"+"!\n")

def config2():
    f.write( "aaa new-model \n"+"!\n"
            +"aaa authentication login default local\n"
            +"aaa authentication login sdm_vpn_xauth_ml_1 local \n"
            +"aaa authorization exec default local \n"
            +"aaa authorization network sdm_vpn_group_ml_1 local \n!\n"
            +"aaa session-id common \n!\n"
            +"dot11 syslog no ip source-route \n!\n"
            +"ip cef \n!\n")




if __name__ == "__main__":
    # execute only if run as a script

    #write()
    config1()
    secure()
    config2()



    close()
