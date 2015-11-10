#!/usr/bin/env python
import paramiko

hostname = '127.0.0.1'
#hostname = 'localhost'
#hostname = '10.14.15.103'
#port = 22
port = 889

username = 'ubuntu'
password = 'checkMKrandomtest'

y = "2012"
m = "02"
d = "27"

def do_it():
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())    
    s.connect(hostname, port, username, password)
    command = 'ls /home'
    (stdin, stdout, stderr) = s.exec_command(command)
    for line in stdout.readlines():
        print line
    s.close()
   
if __name__ == "__main__":
    do_it()
    exit()