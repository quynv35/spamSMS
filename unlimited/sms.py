#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

# https://rapidapi.com/wipple/api/wipple-sms-verify-otp/

def sms(phone): #phone = 84943687522
	phone = "84"+phone[1:]
	url = "https://wipple-sms-verify-otp.p.rapidapi.com/send"
	payload = "{\n    \"app_name\": \"exampleapp\",\n    \"code_length\": 6,\n    \"code_type\": \"number\",\n    \"expiration_second\": 86000,\n    \"phone_number\": \"xxxPHONExxx\"\n}"
	payload = payload.replace("xxxPHONExxx",phone)
	headers = {
	    'content-type': "application/json",
	    'x-rapidapi-key': "0cc733e278mshc6dfccfbf2203f6p16914djsnc108e3d901f5",
	    'x-rapidapi-host': "wipple-sms-verify-otp.p.rapidapi.com"
	    }
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)

phone = input(">_ Phone : ")
print(sms(phone))
