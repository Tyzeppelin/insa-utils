#!/usr/bin/python

import subprocess

def fill (n) :
    if n < 0:
        return ""
    i = 0
    res = ""
    while i < n:
        res += " "
        i += 1
    return res

tab = 27

s3cr3t = open(".s3cr3t", 'r').read().split("\n")[:-1]
hosts = open("host.list", 'r').read().split("\n")[:-1]
up = 0
down = 0

print "\t+------------------------------+-------+"

for hostname in hosts :
    ping = subprocess.Popen("ping -c 1 -w 1 " + hostname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = ping.communicate()
    response = ping.returncode
    if response == 0:
        up += 1
        print "\t|\033[92m", hostname, fill(tab-len(hostname)), "\033[0m|is up  |"
    	print "\t+------------------------------+-------+"
    else:
        down += 1

