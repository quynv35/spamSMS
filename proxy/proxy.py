#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs

link = "https://free-proxy-list.net"

data = list(bs(requests.get(link).text,"html.parser").find_all("tr"))[1:21]

f = open("proxy.txt","w")

for i in data:
	i = bs(str(i),"html.parser").find_all("td")
	proxy = ""
	Proxy = []
	for j in i:
		j = bs(str(j),"html.parser").find("td").text
		proxy = proxy + j + ":"
	Proxy = proxy.split(":")
	if Proxy[6] == "yes":
		Proxy[6] = "https"
	else:
		Proxy[6] = "http"
	f.write(Proxy[6]+":"+Proxy[0]+":"+Proxy[1]+":"+Proxy[2]+":"+Proxy[3])
	f.write("\n")
f.close()

# import re
# regex = "<td>(\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3})</td><td>(\\d{1,6})</td>(.*)<td class='hx'>(\\A{1,3})(.*)ago</td></tr>"
# proxy = re.findall(regex,data)

def proxy(file):
	proxies= []
	f = open(file,"r")
	for i in f:
		proxy = {}
		j = i.split(":")
		proxy[j[0]] = j[0]+"://"+j[1]+":"+j[2]
		proxies.append(proxy)
	f.close()
	return(proxies)