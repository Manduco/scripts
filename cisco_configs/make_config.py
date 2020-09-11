import json
import getpass

#list of vars
version = 0.0
GetHost = "null"
hostname = "null"

print("---config script---")
#opens or creates config txt file
f = open("config_demo.txt", "w")

def GetJsonData():
    with open('var.json') as f:
        data = json.load(f)

    global hostname,version

    version = data["code"]["version"]
    hostname = input("enter host name :")

    if hostname in data["host"]:
        print("-hostname found")
        answer = input("create configs with current settings? y/n : ")
        if (answer == 'y'):
            Display_Current_Var()
        else:
            print("")
    else:
        print("hostname was not found")

def Display_Current_Var():
    print("display current settings")
def Get_User_Input():

    global Final_epass, Final_pass, esp_answer
    global buffered_val


    buffered_val = 0
    Temp_sped1,Temp_sped2,Temp_pswd1,Temp_pswd2 = "x","z","x","z"
    Final_epass, Final_pass = "",""

    esp = input ("encrypt service password? y/n :")
    if (esp == "y"):
        esp_answer = " "
    else:
        esp_answer = "no "

    while not int(buffered_val) in range(1,12001):
        buffered_val = input("logging buffered value, Lim: 12000 ")#choose a shift

    # while(Temp_sped1 != Temp_sped2):
    #     Temp_sped1 = getpass.getpass('secret pass:')
    #     Temp_sped2 = getpass.getpass('renter secret pass:')
    #     if(Temp_sped1 != Temp_sped2):
    #         print("-------password does not match------")

    while(Temp_pswd1 != Temp_pswd2):
        Temp_pswd1 = getpass.getpass('Password:')
        Temp_pswd2 = getpass.getpass('Renter Password:')
        if(Temp_pswd1 != Temp_pswd2):
            print("-------password does not match------")

    # if(Temp_sped1 == Temp_sped2):
    #     Final_epass = Temp_sped1
    if(Temp_pswd1 == Temp_pswd2):
        Final_pass = Temp_pswd1

    #print("x:",x ,pswd)

#cisco cmd list
def config1():
    f.write("version " + str(version) + "\n"
            + "no service pad service \n"
            + "timestamps debug datetime msec \n"
            + "service timestamps log datetime msec \n"
            + esp_answer + "service password-encryption \n"+
            "!\n")

def secure():
    f.write( "hostname "+hostname+"\n" + "!\n"
        +"boot-start-marker\n"
        +"boot-end-marker\n" +"!\n"
        +"logging buffered " + buffered_val +"\n"
        +"enable secret 5 $1$wgM4$hnI4TqvqWv8EwjDWUgsjQ1\n"
        +"enable password something\n"+"!\n")
            #remove both secret 5 key and password
def config2():
    f.write( "aaa new-model \n"+"!\n"
            +"aaa authentication login default local\n"
            +"aaa authentication login sdm_vpn_xauth_ml_1 local \n"
            +"aaa authorization exec default local \n"
            +"aaa authorization network sdm_vpn_group_ml_1 local \n!\n"
            +"aaa session-id common \n!\n"
            +"dot11 syslog no ip source-route \n!\n"
            +"ip cef \n!\n"
            +"no ip bootp server \n"
            +"ip domain name firma.com \n"+ "\n"
            +"ip host client-vpn 10.1.1.133"
            +"ip name-server 10.1.1.33"
            +"!\n"
            +"multilink bundle-name authenticated\n"
            +"!"
            +"license udi pid CISCO2821 sn FCZ012345KM \n"
            +"username user1 password 0 kamil1 \n"
            +"username spravce privilege 15 password 0 kamil15 \n"
            +"username user2 password 0 kamil2 \n"
            +"!\n"
            +"redundancy \n"
            +"! \n")
def crypto():
    f.write( "crypto ikev2 diagnose error 50 \n"
    +"!\n"
    +"crypto isakmp policy 1\n"
    +"encr 3des\n"
    +"authentication pre-share \n"
    +"group 2 \n"
    +"!\n"
    +"crypto isakmp policy 3\n"
    +"encr 3des\n"
    +"group 2\n"
    +"!\n"
    +"crypto isakmp policy 10 \n"
    +"encr 3des \n"
    +"hash md5 \n"
    +"authentication pre-share \n"
    +"group 2 \n"
    +"! \n"
    +"crypto isakmp policy 20 \n"
    +"encr 3des \n"
    +"hash md5 \n"
    +"group 2 \n"
    +"! \n"
    +"crypto isakmp client configuration group Group159 \n"
    +"key Key159Key \n"
    +"pool SDM_POOL_1 \n"
    +"acl 100 \n"
    +"! \n"
    +"crypto ipsec transform-set 3DES-MD5 esp-3des esp-md5-hmac \n"
    +"! \n"
    +"crypto dynamic-map SDM_DYNMAP_1 1 \n"
    +"set transform-set 3DES-MD5 \n"
    +"reverse-route \n"
    +"! \n"
    +"crypto map SDM_CMAP_1 client authentication list sdm_vpn_xauth_ml_1 \n"
    +"crypto map SDM_CMAP_1 isakmp authorization list sdm_vpn_group_ml_1 \n"
    +"crypto map SDM_CMAP_1 client configuration address respond \n"
    +"crypto map SDM_CMAP_1 65535 ipsec-isakmp dynamic SDM_DYNMAP_1 \n"
    +"!\n")
def config3():
    f.write( "!"
        +"redundancy\n"
        +"!\n"
        +"crypto ikev2 diagnose error 50\n"
        +"!\n"
        +"crypto isakmp policy 1\n"
        +"encr 3des\n"
        +"authentication pre-share\n"
        +"group 2\n"
        +"!\n"
        +"crypto isakmp policy 3\n"
        +"encr 3des\n"
        +"group 2\n"
        +"!\n"
        +"crypto isakmp policy 10\n"
        +"encr 3des\n"
        +"hash md5\n"
        +"authentication pre-share\n"
        +"group 2\n"
        +"!\n"
        +"crypto isakmp policy 20\n"
        +"encr 3des\n"
        +"hash md5\n"
        +"group 2\n"
        +"!\n"
        +"crypto isakmp client configuration group Group159\n"
        +"key Key159Key\n"
        +"pool SDM_POOL_1\n"
        +"acl 100\n"
        +"!\n"
        +"crypto ipsec transform-set 3DES-MD5 esp-3des esp-md5-hmac\n"
        +"!\n"
        +"crypto dynamic-map SDM_DYNMAP_1 1\n"
        +"set transform-set 3DES-MD5\n"
        +"reverse-route\n"
        +"!\n"
        +"crypto map SDM_CMAP_1 client authentication list sdm_vpn_xauth_ml_1\n"
        +"crypto map SDM_CMAP_1 isakmp authorization list sdm_vpn_group_ml_1\n"
        +"crypto map SDM_CMAP_1 client configuration address respond\n"
        +"crypto map SDM_CMAP_1 65535 ipsec-isakmp dynamic SDM_DYNMAP_1\n"
        +"!\n"
        +"interface Loopback10\n"
        +"description For VPN Client\n"
        +"ip address 192.168.201.1 255.255.255.0\n"
        +"!\n"
        +"interface GigabitEthernet0/0\n"
        +"description $FW_OUTSIDE$\n"
        +"ip address 10.1.1.220 255.255.255.0\n"
        +"duplex auto\n"
        +"speed auto\n"
        +"crypto map SDM_CMAP_1\n"
        +"!\n"
        +"interface GigabitEthernet0/1\n"
        +"description $ETH-LAN$$FW_INSIDE$\n"
        +"ip address 192.168.220.1 255.255.255.0\n"
        +"duplex auto\n"
        +"speed auto\n"
        +"!\n"
        +"ip local pool SDM_POOL_1 192.168.200.1 192.168.200.10\n"
        +"ip forward-protocol nd\n"
        +"ip http server\n"
        +"ip http secure-server\n"
        +"!\n"
        +"ip route 0.0.0.0 0.0.0.0 10.1.1.1\n"
        +"!\n"
        +"access-list 10 remark Prisup na router \n"
        +"access-list 10 remark Pristup na router\n"
        +"access-list 10 permit 10.1.1.0 0.0.0.255\n"
        +"access-list 10 permit 192.168.201.0 0.0.0.255\n"
        +"access-list 10 permit 192.168.200.0 0.0.0.255\n"
        +"access-list 100 remark SDM_ACL Category=4\n"
        +"access-list 100 permit ip 192.168.201.0 0.0.0.255 192.168.200.0 0.0.0.255\n"
        +"no cdp run\n"
        +"!\n"
        +"control-plane\n"
        +"!\n"
        +"line con 0\n"
        +"line aux 0\n"
        +"line vty 0 4\n"
        +"access-class 10 in\n"
        +"exec-timeout 3600 0\n"
        +"password kamil\n"
        +"transport input all\n"
        +"!\n"
        +"scheduler allocate 20000 1000\n"
        +"ntp server 10.1.1.1 \n"
        +"!\n"
        +"webvpn context Default_context\n"
        +"ssl authenticate verify all\n"
        +"!\n"
        +"no inservice\n"
        +"!\n"
        +"end")
def closef():

    f.close()
    print ("Configs Created")


if __name__ == "__main__":
    # execute only if run as a script

    GetJsonData()
    #write()
    Get_User_Input()
    config1()
    secure()
    config2()
    crypto()
    config3()

    closef()
