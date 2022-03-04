#!/usr/bin/env python3

with open("dnsservers.txt","r")
    dnslist = dnsfile.readlines()
    for svr in dnslist:
    	print(svr, end="")
