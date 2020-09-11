
# giant string need to break this down:


$host_name = Read-Host " enter Hostname"
$buffered_val = Read-Host " enter logging buffered value, Lim: 12000 "

$Temp_pswd1 = Read-Host "Enter device services password " -AsSecureString
$Temp_pswd2 = Read-Host "Renter Password " -AsSecureString

if($Temp_pswd1 -eq $Temp_pswd2) {
  $Final_pass = $Temp_pswd1
}else {
  $Final_pass = "|null|"
}


$domain_name = Read-Host "enter domain name "
$host_client_vpn_IP = Read-Host "enter VPN IP "
$Name_server_IP = Read-Host "enter name server IP "

$license_udi_pid = Read-Host "enter product ID "
$license_sn = Read-Host "enter device Serial number "
$username1 = Read-Host "enter a username for this device "
$username1PW = Read-Host 'Enter a password for '$username1' ' -AsSecureString
$username2 = Read-Host "enter a anoter username for this device "
$username2PW = Read-Host 'Enter a password for '$username2' ' -AsSecureString


$config_Main_Text = 'version 15.8' + "`n" +
'no service pad ' + "`n" +
'service timestamps debug datetime msec ' + "`n" +
'service timestamps log datetime msec ' + "`n" +
'no service password-encryption ' + "`n" +
'! ' + "`n" +
'hostname ' + $host_name +"`n" +
'! ' + "`n" +
'boot-start-marker ' + "`n" +
'boot-end-marker ' + "`n" +
'! ' + "`n" +
'logging buffered ' + $buffered_val + "`n" +
'enable secret 5 $1$wgM4$hnI4TqvqWv8EwjDWUgsjQ1 ' + "`n" +
'enable password ' +  $Final_pass + "`n" +
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
'ip domain name ' + $domain_name +"`n" +
'ip host client-vpn ' + $host_client_vpn_IP + "`n" +
'ip name-server ' + $Name_server_IP + "`n" +
'! ' + "`n" +
'multilink bundle-name authenticated ' + "`n" +
'! ' + "`n" +
'license udi pid ' + $license_udi_pid +' sn ' + $license_sn +"`n" +
'username ' + $username1 +' password 0 ' + $username1PW + "`n" +
'username spravce privilege 15 password 0 kamil15 ' + "`n" +
'username ' + $username2 +' password 0 ' + $username2PW +"`n" +
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
$config_Main_Text > 'config_demo_ps.txt'
