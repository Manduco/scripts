
# giant string need to break this down:
$config_Main_Text = 'version 12.4 ' + "`n" +
'no service pad ' + "`n" +
'service timestamps debug datetime msec ' + "`n" +
'service timestamps log datetime msec ' + "`n" +
'no service password-encryption ' + "`n" +
'! ' + "`n" +
'hostname cisco28 ' + "`n" +
'! ' + "`n" +
'boot-start-marker ' + "`n" +
'boot-end-marker ' + "`n" +
'! ' + "`n" +
'logging buffered 128000 ' + "`n" +
'enable secret 5 $1$wgM4$hnI4TqvqWv8EwjDWUgsjQ1 ' + "`n" +
'enable password something ' + "`n" +
'! ' + "`n" +
'aaa new-model ' + "`n" +
'! ' + "`n" +
'aaa authentication login default local ' + "`n" +
'aaa authentication login sdm_vpn_xauth_ml_1 local ' + "`n" +
'aaa authorization exec default local ' + "`n" +
'aaa authorization network sdm_vpn_group_ml_1 local ' + "`n" +
'! ' + "`n" +
'aaa session-id common ' + "`n" +
'! ' + "`n" +
'dot11 syslog ' + "`n" +
'no ip source-route ' + "`n" +
'! ' + "`n" +
'ip cef ' + "`n" +
'! ' + "`n" +
'no ip bootp server ' + "`n" +
'ip domain name firma.com ' + "`n" +
'ip host client-vpn 10.1.1.133 ' + "`n" +
'ip name-server 10.1.1.33 ' + "`n" +
'! ' + "`n" +
'multilink bundle-name authenticated ' + "`n" +
'! ' + "`n" +
'license udi pid CISCO2821 sn FCZ012345KM ' + "`n" +
'username user1 password 0 kamil1 ' + "`n" +
'username spravce privilege 15 password 0 kamil15 ' + "`n" +
'username user2 password 0 kamil2 ' + "`n" +
'! ' + "`n" +
'redundancy ' + "`n" +
'! ' + "`n" +
'crypto ikev2 diagnose error 50 ' + "`n" +
'! ' + "`n" +
'crypto isakmp policy 1 ' + "`n" +
'encr 3des ' + "`n" +
'authentication pre-share ' + "`n" +
'group 2 ' + "`n" +
'! ' + "`n" +
'crypto isakmp policy 3 ' + "`n" +
'encr 3des ' + "`n" +
'group 2 ' + "`n" +
'! ' + "`n" +
'crypto isakmp policy 10 ' + "`n" +
'encr 3des ' + "`n" +
'hash md5 ' + "`n" +
'authentication pre-share ' + "`n" +
'group 2 ' + "`n" +
'! ' + "`n" +
'crypto isakmp policy 20 ' + "`n" +
'encr 3des ' + "`n" +
'hash md5 ' + "`n " +
'group 2 ' + "`n" +
'! ' + "`n" +
'crypto isakmp client configuration group Group159 ' + "`n" +
'key Key159Key ' + "`n" +
'pool SDM_POOL_1 ' + "`n" +
'acl 100 ' + "`n" +
'! ' + "`n" +
'crypto ipsec transform-set 3DES-MD5 esp-3des esp-md5-hmac ' + "`n" +
'! ' + "`n" +
'crypto dynamic-map SDM_DYNMAP_1 1 ' + "`n" +
'set transform-set 3DES-MD5 ' + "`n" +
'reverse-route ' + "`n" +
'! ' + "`n" +
'crypto map SDM_CMAP_1 client authentication list sdm_vpn_xauth_ml_1 ' + "`n" +
'crypto map SDM_CMAP_1 isakmp authorization list sdm_vpn_group_ml_1 ' + "`n" +
'crypto map SDM_CMAP_1 client configuration address respond ' + "`n" +
'crypto map SDM_CMAP_1 65535 ipsec-isakmp dynamic SDM_DYNMAP_1 ' + "`n" +
'! ' + "`n" +
'interface Loopback10 ' + "`n" +
'description For VPN Client ' + "`n" +
'ip address 192.168.201.1 255.255.255.0 ' + "`n" +
'! ' + "`n" +
'interface GigabitEthernet0/0 ' + "`n" +
'description $FW_OUTSIDE$ ' + "`n" +
'ip address 10.1.1.220 255.255.255.0 ' + "`n" +
'duplex auto ' + "`n" +
'speed auto ' + "`n" +
'crypto map SDM_CMAP_1 ' + "`n" +
'! ' + "`n" +
'interface GigabitEthernet0/1 ' + "`n" +
'description $ETH-LAN$$FW_INSIDE$ ' + "`n" +
'ip address 192.168.220.1 255.255.255.0 ' + "`n" +
'duplex auto ' + "`n" +
'speed auto ' + "`n" +
'! ' + "`n" +
'ip local pool SDM_POOL_1 192.168.200.1 192.168.200.10 ' + "`n" +
'ip forward-protocol nd ' + "`n" +
'ip http server ' + "`n" +
'ip http secure-server ' + "`n" +
'! ' + "`n" +
'ip route 0.0.0.0 0.0.0.0 10.1.1.1 ' + "`n" +
'! ' + "`n" +
'access-list 10 remark Prisup na router ' + "`n" +
'access-list 10 remark Pristup na router ' + "`n" +
'access-list 10 permit 10.1.1.0 0.0.0.255 ' + "`n" +
'access-list 10 permit 192.168.201.0 0.0.0.255 ' + "`n" +
'access-list 10 permit 192.168.200.0 0.0.0.255 ' + "`n" +
'access-list 100 remark SDM_ACL Category=4 ' + "`n" +
'access-list 100 permit ip 192.168.201.0 0.0.0.255 192.168.200.0 0.0.0.255 ' + "`n" +
'no cdp run ' + "`n" +
'! ' + "`n" +
'control-plane ' + "`n" +
'! ' + "`n" +
'line con 0 ' + "`n" +
'line aux 0 ' + "`n" +
'line vty 0 4 ' + "`n" +
'access-class 10 in ' + "`n" +
'exec-timeout 3600 0 ' + "`n" +
'password kamil ' + "`n" +
'transport input all ' + "`n" +
'! ' + "`n" +
'scheduler allocate 20000 1000 ' + "`n" +
'ntp server 10.1.1.1 ' + "`n" +
'! ' + "`n" +
'webvpn context Default_context ' + "`n" +
'ssl authenticate verify all ' + "`n" +
'!  ' + "`n" +
'no inservice ' + "`n" +
'! ' + "`n" +
'end'



# Create file:

#prints to text file
$config_Main_Text > 'file.txt'