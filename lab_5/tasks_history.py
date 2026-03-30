                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ cat /etc/group   
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:jianduojie
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:jianduojie
fax:x:21:
voice:x:22:
cdrom:x:24:jianduojie
floppy:x:25:jianduojie
tape:x:26:
sudo:x:27:jianduojie
audio:x:29:jianduojie
dip:x:30:jianduojie
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
shadow:x:42:
utmp:x:43:
video:x:44:jianduojie
sasl:x:45:
plugdev:x:46:jianduojie
staff:x:50:
games:x:60:
users:x:100:jianduojie,user2
nogroup:x:65534:
systemd-journal:x:999:
systemd-network:x:998:
crontab:x:997:
input:x:996:
sgx:x:995:
clock:x:994:
kvm:x:993:
render:x:992:
netdev:x:101:jianduojie
mysql:x:102:
scanner:x:103:saned,jianduojie
tss:x:104:
systemd-timesync:x:991:
kismet:x:105:
_gophish:x:106:
messagebus:x:990:
tcpdump:x:107:
_ssh:x:108:
ssl-cert:x:109:postgres
redis:x:110:_gvm
i2c:x:111:
plocate:x:112:
mosquitto:x:113:
redsocks:x:114:
stunnel4:x:989:stunnel4
Debian-snmp:x:115:
bluetooth:x:116:jianduojie
sslh:x:117:
postgres:x:118:
avahi:x:119:
_gvm:x:120:
lpadmin:x:121:jianduojie
sambashare:x:988:
nm-openvpn:x:122:
inetsim:x:123:
wireshark:x:124:jianduojie
winbindd_priv:x:987:
pipewire:x:986:
nm-openconnect:x:125:
geoclue:x:126:
lightdm:x:127:
saned:x:128:
polkitd:x:985:
rtkit:x:129:
colord:x:130:
kali-trusted:x:131:
jianduojie:x:1000:
kaboxer:x:132:jianduojie
docker:x:133:
user2:x:1002:
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ sudo groupadd mytestgroup
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ cat /etc/group           
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:jianduojie
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:jianduojie
fax:x:21:
voice:x:22:
cdrom:x:24:jianduojie
floppy:x:25:jianduojie
tape:x:26:
sudo:x:27:jianduojie
audio:x:29:jianduojie
dip:x:30:jianduojie
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
shadow:x:42:
utmp:x:43:
video:x:44:jianduojie
sasl:x:45:
plugdev:x:46:jianduojie
staff:x:50:
games:x:60:
users:x:100:jianduojie,user2
nogroup:x:65534:
systemd-journal:x:999:
systemd-network:x:998:
crontab:x:997:
input:x:996:
sgx:x:995:
clock:x:994:
kvm:x:993:
render:x:992:
netdev:x:101:jianduojie
mysql:x:102:
scanner:x:103:saned,jianduojie
tss:x:104:
systemd-timesync:x:991:
kismet:x:105:
_gophish:x:106:
messagebus:x:990:
tcpdump:x:107:
_ssh:x:108:
ssl-cert:x:109:postgres
redis:x:110:_gvm
i2c:x:111:
plocate:x:112:
mosquitto:x:113:
redsocks:x:114:
stunnel4:x:989:stunnel4
Debian-snmp:x:115:
bluetooth:x:116:jianduojie
sslh:x:117:
postgres:x:118:
avahi:x:119:
_gvm:x:120:
lpadmin:x:121:jianduojie
sambashare:x:988:
nm-openvpn:x:122:
inetsim:x:123:
wireshark:x:124:jianduojie
winbindd_priv:x:987:
pipewire:x:986:
nm-openconnect:x:125:
geoclue:x:126:
lightdm:x:127:
saned:x:128:
polkitd:x:985:
rtkit:x:129:
colord:x:130:
kali-trusted:x:131:
jianduojie:x:1000:
kaboxer:x:132:jianduojie
docker:x:133:
user2:x:1002:
mytestgroup:x:1003:
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ sudo usermod -aG mytestgroup user2
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ id user2
uid=1002(user2) gid=1002(user2) groups=1002(user2),100(users),1003(mytestgroup)
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ ls
Desktop  Documents  Downloads  k9s_Linux_arm64.tar.gz  LICENSE  Music  Pictures  Public  README.md  Templates  Videos
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ cd Desktop/  
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop]
└─$ ls
github_token  labs
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop]
└─$ cd labs    
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs]
└─$ ls
lab_1  lab-2  lab_3  lab_4  README.md
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs]
└─$ mkdir lab_5         
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs]
└─$ ls
lab_1  lab-2  lab_3  lab_4  lab_5  README.md
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs]
└─$ cd lab_5
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs/lab_5]
└─$ ls
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs/lab_5]
└─$ mkdir /data_lab                   
mkdir: cannot create directory ‘/data_lab’: Permission denied
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs/lab_5]
└─$ sudo mkdir /data_lab
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs/lab_5]
└─$ ls
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs/lab_5]
└─$ ls
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs/lab_5]
└─$ sudo chgrp mytestgroup /data_lab
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs/lab_5]
└─$ sudo chmod 770 /data_lab
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs/lab_5]
└─$ su - user2              
Password: 
su: Authentication failure
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop/labs/lab_5]
└─$ su - user2
Password: 
┌──(user2㉿killer)-[~]
└─$ cd /data_lab/                                                                                                                                                                                   

┌──(user2㉿killer)-[/data_lab]
└─$ su - jianduojie
Password: 
zsh: corrupt history file /home/jianduojie/.zsh_history
┌──(jianduojie㉿killer)-[~]
└─$ cd /data_lab 
cd: permission denied: /data_lab
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ 

