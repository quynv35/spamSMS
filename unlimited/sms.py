#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

def sms(phone,msg):
	url = "https://sms-international.p.rapidapi.com/WebTool/SMStoCountry/sms84"
	querystring = {"phonenum":"","msg":""}
	querystring["msg"] = msg
	querystring["phonenum"] = "84"+phone[1:]
	headers = {
	    'x-rapidapi-host': "sms-international.p.rapidapi.com",
	    'x-rapidapi-key': "9ad14197e0mshb760b7991e634fcp11f307jsnbc7ca7452483"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.json()["msg"].split("|")[0]
	data = "{0}\n{1}\n{2}\n".format(phone,msg,result)
	return(data)

phone = input(">_ Phone : ")
msg = input(">_ Message : ")
print(sms(phone,msg))
