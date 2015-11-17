#!/usr/bin/python
import paramiko
import cmd
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.3.164.226', username='ubuntu', password='checkMKrandomtest')

stdin, stdout, stderr = ssh.exec_command("uptime")
stdin.close()

#print(stdin)
print stdin.read()

#print(stdout)    
#print stdout.read()


#print(stderr)

#type(stdin)
#type(stdout)
#type(stderr)

#stdout.readlines()

