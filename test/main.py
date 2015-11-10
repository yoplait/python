#imports
import os   
import paramiko
from paramiko import SSHClient
from scp import SCPClient

#variables
nam = '10.14.15.103'
emea = '127.0.0.1'
apac = '127.0.0.1'

user = 'ubuntu'
password = 'checkMKrandomtest'
port = '22'


#main
print ("SCP on")

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient(nam,22,user,password)
scp = SCPClient(ssh.get_transport())
#put source destiantion
#scp.put('C:\RDP\caca.txt', '/tmp/caca.txt')
#get source destination on local
#scp.get('/opt/omd/sites/mdm2/etc/check_mk/conf.d/wato/jc.mk', 'C:\RDP\\jc.mk')
#scp.close()
scp.get('/tmp/nam.txt',r'C:\RDP')
#scp.get('/tmp/nam.txt','/drives/c/rdp/')
scp.close()
print ("SCP nam")

ssh = createSSHClient(emea,2222,user,password)
scp = SCPClient(ssh.get_transport())
scp.get('/tmp/emea.txt',r'C:\RDP')
#scp.get('/tmp/emea.txt',r'/drives/c/rdp/')
scp.close()
print ("SCP emea")

ssh = createSSHClient(apac,889,user,password)
scp = SCPClient(ssh.get_transport())
scp.get('/tmp/apac.txt',r'C:\RDP')
#scp.get('/tmp/apac.txt',r'/drives/c/rdp/')
scp.close()
print ("SCP apac")
