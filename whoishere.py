#!/usr/bin/python

import subprocess
import paramiko

def fill (n) :
    return " "*n

tab = 27

s3cr3t = open(".s3cr3t", 'r').read().split("\n")[:-1]
hosts = open("host.list", 'r').read().split("\n")[:-1]
up = 0
down = 0

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("\t+------------------------------+-------+")

for hostname in hosts :
    ping = subprocess.Popen("ping -c 1 -w 1 " + hostname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = ping.communicate()
    response = ping.returncode
    if response == 0:
        up += 1
        print("\t|\033[92m", hostname, fill(tab-len(hostname)), "\033[0m|is up  |")

        client.connect(hostname, username=s3cr3t[0], password=s3cr3t[1])
        stdin, stdout, stderr = client.exec_command("who")
        # luv python syntax
        who = list(set([e.lstrip().split(" ")[0] for e in stdout.read().split("\n")[:-1]]))
        for user in who:
            print("\t|\t", user, fill(tab-len(user)), "\033[0m  |")

    	print("\t+------------------------------+-------+")
    else:
        down += 1

