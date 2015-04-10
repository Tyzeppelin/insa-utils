#!/usr/bin/python

import os

def fill (n) :
    if n < 0:
        return ""
    i = 0
    res = ""
    while i < n:
        res += " "
        i += 1
    return res


os.system("""cat host.educ.insa | cut -d " " -f 1 > host.list""")

hosts =  open("depart.list", 'r').read().split("\n")[:-1]

up = 0
down = 0

#hosts = ["cavalier.educ.insa", "10.133.26.251"]

tab = 27

print "\t+------------------------------+-------+"

for hostname in hosts :
    response = os.system("ping -c 1 -w 1 " + hostname+" >/dev/null 2>&1")
    if response == 0:
        up += 1
        print "\t|\033[92m", hostname, fill(tab-len(hostname)), "\033[0m|is up  |"
    else:
        down += 1
        print "\t|\033[91m", hostname, fill(tab-len(hostname)), "\033[0m|is down|"
    print "\t+------------------------------+-------+"

print "up ->", up, "down ->", down
