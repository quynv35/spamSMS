#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

phone = input("  >> Phone : ")
if len(phone) == 0:
	f = open("phone.txt","r")
	phone = f.read()
	f.close()

url = "https://detect-vietnam-phone.p.rapidapi.com/"

querystring = {"phone_number":""} #0943687522
querystring["phone_number"] = phone
headers = {
    'x-rapidapi-host': "detect-vietnam-phone.p.rapidapi.com",
    'x-rapidapi-key': "9ad14197e0mshb760b7991e634fcp11f307jsnbc7ca7452483"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

for i in response:
	print(" (+) {0} : {1}".format(i,response[i]))
