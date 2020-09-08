
print(" --- Make configs ---")

version = 0.0


#localIP = raw_input("Enter Local IP : ")
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
def crypto():
    f.write( "no ip bootp server \n"
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
    +"! \n"
    +"crypto ikev2 diagnose error 50 \n"
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

if __name__ == "__main__":
    # execute only if run as a script

    #write()
    config1()
    secure()
    config2()
    crypto()

    close()
