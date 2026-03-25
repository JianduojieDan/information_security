┌──(jianduojie㉿killer)-[~/Desktop]
└─$ sudo adduser user1
fatal: The user `user1' already exists.
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop]
└─$ sudo adduser user2
New password: 
Retype new password: 
passwd: password updated successfully
Changing the user information for user2
Enter the new value, or press ENTER for the default
        Full Name []: Dan_user2 
        Room Number []: 2
        Work Phone []: 124123144
        Home Phone []: 12355123234
        Other []: nothing
Is the information correct? [Y/n] y
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~/Desktop]
└─$ su - user2        
Password: 
┌──(user2㉿killer)-[~]
└─$ su - jianduojie
Password: 
zsh: corrupt history file /home/jianduojie/.zsh_history
┌──(jianduojie㉿killer)-[~]
└─$ su - user2                               
Password: 
┌──(user2㉿killer)-[~]
└─$ whoami
user2

┌──(user2㉿killer)-[~]
└─$ chfn
Password: 
Changing the user information for user2
Enter the new value, or press ENTER for the default
        Full Name: Dan_user2
        Room Number [2]: 0277
        Work Phone [124123144]: 481726
        Home Phone [12355123234]: 5212341

┌──(user2㉿killer)-[~]
└─$ cat etc/passwd
cat: etc/passwd: No such file or directory

┌──(user2㉿killer)-[~]
└─$ su - user1
Password: 
su: Authentication failure

┌──(user2㉿killer)-[~]
└─$ su - user1                                                                                                                                                                                      
Password: 
su: Authentication failure

┌──(user2㉿killer)-[~]
└─$ deluser --remove-home --force user1                                                                                                                                                             
Unknown option: force
deluser [--system] [--remove-home] [--remove-all-files] [--backup]
        [--backup-to dir] [--backup-suffix str] [--conf file]
        [--quiet] [--verbose] [--debug] user

  remove a regular user from the system

deluser --group [--system] [--only-if-empty] [--conf file] [--quiet]
        [--verbose] [--debug] group
delgroup [--system] [--only-if-empty] [--conf file] [--quiet]
         [--verbose] [--debug] group
  remove a group from the system

deluser [--conf file] [--quiet] [--verbose] [--debug] user group
  remove the user from a group

┌──(user2㉿killer)-[~]
└─$ pkill -KILL -u user1

┌──(user2㉿killer)-[~]
└─$ su - user1                                                                                                                                                                                      
Password: 
su: Authentication failure

┌──(user2㉿killer)-[~]
└─$ su - user1                                                                                                                                                                                      
Password: 
su: Authentication failure

┌──(user2㉿killer)-[~]
└─$ su - jianduojie                                                                                                                                                                                 
Password: 
zsh: corrupt history file /home/jianduojie/.zsh_history
┌──(jianduojie㉿killer)-[~]
└─$ sudo deluser --remove-home user1
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ whoami     
jianduojie
                                                                                                                                                                                                    
┌──(jianduojie㉿killer)-[~]
└─$ sudo passwd user2               
New password: 
Retype new password: 
\passwd: password updated successfully

