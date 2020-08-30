#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def grab(phone): #84943687522
	link = "https://api.grab.com/grabid/v1/oauth2/otp"
	data = {
		"client_id":"4da4649307cc4bfaa16b08d03432535e",
		"transaction_ctx":"null",
		"country_code":"VN",
		"method":"CALL",
		"num_digits":"6",
		"phone_number":""
		}
	data["phone_number"] = "84"+phone[1:]
	req = requests.post(link,json=data)
	return(req,req.text)


def airbnb(phone): #phone = 84943687522
	link = "https://www.airbnb.co.in/api/v2/phone_one_time_passwords?currency=VND&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=vi"
	data = {
		"phoneNumber":"",
		"workFlow":"GLOBAL_SIGNUP_LOGIN",
		"otpMethod":"CALL"
		}
	data["phoneNumber"] = "84" + phone[1:]
	res = requests.post(link, json = data)
	return(res, res.text)

phone = input(">_ Phone : ")

print(grab(phone))
print(airbnb(phone))