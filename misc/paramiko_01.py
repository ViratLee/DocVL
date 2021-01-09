import paramiko
import os,sys,time

ssh = paramiko.SSHClient()
#thadcdlwcm01 10.141.111.40

ssh.connect('10.141.111.40', username="aappa01", password="4rfvBGT%")
sftp = ssh.open_sftp()
localpath = 'D:\\logs\\prod\\calculation.log'
remotepath = '/logs/wcmapp01/calculation.log'
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()