from teambotgolf import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from Naked.toolshed.shell import execute_js
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,subprocess,unicodedata
import subprocess, youtube_dl, humanize, traceback,asyncio
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
import multiprocessing as mp
from threading import Thread
_session = requests.session()
loop = asyncio.get_event_loop()
import livejson, traceback, threading, subprocess, os
from datetime import datetime, timedelta
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback,livejson
_session = requests.session()
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from gtts import gTTS
botStart = time.time()
APP = "DESKTOPMAC\t6.5.2\tMAC\t10.15.1"
client = LINE('botbasx1@gmail.com','123456Z',appName="DESKTOPMAC\t6.5.2\tMAC\t10.15.1")
print("𝙻𝙾𝙶𝙸𝙽 𝙳𝙾𝙽𝙴")
client.sendMessage("cbafb31fa5ac456e56c07c47c7bcf5e67","เริ่มต้นใช้งาน")
now2 = datetime.now()
nowT = datetime.strftime(now2,"[%H:%M:%S]")
client.sendMessage("cbafb31fa5ac456e56c07c47c7bcf5e67","บอทเริ่มทำงานเวลา\n" + nowT)
clientMID = client.getProfile().mid
bot1 = client.getProfile().mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}
bot1 = client.getProfile().mid
times = {
    "clock": True,
    "name": "เทสระบบ "
}
kickPoll = OEPoll(client)
set={"gn":{},"gp":{},"iv":{}}
read = {"readPoint":{}}
RX = [clientMID]
Kicker = [clientMID]
Exc = [client]
Basx = [client] 
Jsz = [client]
Exc1 = [client]
##
pr = client.getProfile()
cl = pr.mid
contact = client.getProfile() 
backup = client.getProfile() 
backup.displayName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
#=========
mainbots=RX+Jsz
mainbot=Exc+Jsz
rr = ["'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'ปัง!'\nทันใดนั้นเสียงปืนลูกโม่ก็ได้มีเสียงดังเกิดขึ้นและลูกกระสุนได้เข้าถึงหัวคุณเต็มๆ ทำให้คุณเสียชีวิต\nThe End","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!"]
#=========
RXBot= [clientMID]
#=====================Add open admin ===================
Family = ["u8401f6854821e57b3737760a1f9df54d"]
admin = ["u8401f6854821e57b3737760a1f9df54d","ud1fb0a926c3e5fa920a2790ab81c12cb"]
creator = ["u8401f6854821e57b3737760a1f9df54"]
owner = ["u8401f6854821e57b3737760a1f9df54d"]
staff = ["u8401f6854821e57b3737760a1f9df54d","uf1046ed92bd638e6b1d36baacf0ad5bd"]
Bots = [clientMID]
for id in admin:
    if id not in client.getAllContactIds():
        client.findAndAddContactsByMid(id)
        print("[●] ADD ADMIN CONTACT")
    else:
        print("")
#=========================================
helptest = """---------------------------------------------------
↪แทค
↪โทร จำนวน (เชิญคอล)
↪ต้อนรับ เปิด/ปิด
↪เปิดแอบ/ปิดแอบ(ดูคนแอบอ่าน)
↪เปิดอ่าน/ปิดอ่าน (ดูคนอ่าน)
↪พูด คำที่จะให้พูด (สิริพูด)
↪/ยกเลิก จำนวน (ยกเลิกข้อความ)
↪คอนแทค @ (เอาคอนแทค)
↪ชื่อ @ (เอาชื่อ)
↪รูป @ (เอารูป)
↪สถานะ @ (เอาสถานะ)
↪ไอดีไลน์ ไอดี (ค้นหาไลน์)
↪ยูทูป คำที่จะหา (ค้นยูทูป)
↪เขียน ข้อความ (เขียนข้อความ)
↪ข้อมูลกลุ่ม (ดูข้อมูลกลุ่ม)
↪แอดกลุ่ม (ดูคนสร้างกลุ่ม)
↪ออน (เวลาออนไลน์บอท)
↪.ลูกเล่น (เกม)
---------------------------------------------------
↪ชื่อบอท: {bName}
↪ออนไลน์: {runtime}
---------------------------------------------------""".format(bName="{bName}",clientMID=cl,runtime="{runtime}")
#=========================================
Saints = RXBot + Family + admin + creator + owner + staff
RXFam = RXBot + Family + admin + creator + owner + staff
#===============Add adminbots =========================
#for x in Bots:
#    admin.append(x)
 #   print(f"bots add {x}")
#===============Add adminbots =========================

    
#===================================ADD WELCOME=========================
optypesg = {"welcomeMessage":"สวัสดีคุณ  🎎 {name} \nยินดีต้อนรับเข้าสู่กลุ่ม \n 👉 {group} 👈","leaveMessage":"คุณ {name} ได้ออกจากกลุ่ม {group} \n🤦 อ้าวไปแล้วหรอ น่าเสียดาย พลาดโอกาสดีๆ ซะแล้ว 😅 ไว้เจอกันใหม่นะ 🌠"}
#===================================ADD WELCOME=========================
settings={"unsendMessage":False}
RXCctv={"cyduk":{},"point":{},"sidermem":{}}
protectqr = []
protectkick = []
protecARoin = []
protectinvite = []
protectcancel = []
protectcanceljs = []
protectantijs = []
ghost = []
poradmin = []
special = []
special1 = []
protectflex = []
#===========add welcome========
welcomegroup = []
leavegroup = []
#===========add welcome========
autocancel = {}
autoleaveroom = []
targets = []
msg_id = {}
msg_dict = {}
msg_dict = {}
protect = {
    "kick": {
        "id": {}
    },
    "inv": {
        "id": {}
    },
    "join": {
        "id": {}
    },
    "url": {
        "id": {}
    }
}
emp_flood = {}

#==================Open admin down ===============
#with open('server.json', 'r') as fp:
 #   server = json.load(fp)
#for x in server['admin']:
 #   admin.append(x)
 #   print(f"admin add {x}")
#with open('server2.json', 'r') as fp:
 #   server2 = json.load(fp)
#for x in server2['staff']:
 #   staff.append(x)
 #   print(f"staff add {x}")
#==================Open admin up ===============	 
readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen) 
#
waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
#time1Open = codecs.open("time1.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
settingsOpen = codecs.open("wait.json","r","utf-8")
wait = json.load(settingsOpen)
#time1 = json.load(time1Open)
#==============ADD BACKUP DOWN =============
with open('protectqr.json', 'r') as fp:
    protectqr = json.load(fp) 	
with open('protectkick.json', 'r') as fp:
    protectkick = json.load(fp)		
with open('protecARoin.json', 'r') as fp:
    protecARoin = json.load(fp)	
#============================================
with open('protectcanceljs.json', 'r') as fp:
    protectcanceljs = json.load(fp)  
with open('protectcancel.json', 'r') as fp:
    protectcancel = json.load(fp)	
with open('protectinvite.json', 'r') as fp:
    protectinvite = json.load(fp)	
with open('protectantijs.json', 'r') as fp:
    protectantijs = json.load(fp)	
with open('ghost.json', 'r') as fp:
    ghost = json.load(fp)
with open('poradmin.json', 'r') as fp:
    poradmin = json.load(fp)
#============================================
with open('welcomegroup.json', 'r') as fp:
    welcomegroup = json.load(fp)
with open('leavegroup.json', 'r') as fp:
    leavegroup = json.load(fp) 
#================BL=========================
with open('st2__b.json', 'r') as fp:
    st2__b = json.load(fp)    
#==============ADD BACKUP UP   =============	    
temp = {"te": "#66FFFF","t": "#6633CC"}
settings = {
    "lang":"JP",
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "dblack": False,
    "wblack": False,
    "unsendMessage": False,
    "invite": {},
    "contact": False,
    "winvite": False,
    "block":{},
    "autoJoin": True,
    "changePictureProfile": False,
    "message": """🎀 Auto Block 🎀
line://ti/p/~botpray25
	""",
    "autoBlock": True,
    "changeGroupPicture": [],
}

RXProtect = {
    "autoAdd": True,
    "autoBlock": True,
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

myProfile = {
	"displayName": "",
    "coverId": "",
    "pictureStatus": "",
    "statusMessage": ""
}

user1 = clientMID
user2 = "ua435d92651ba9df05ad290b8df2dc72f"
msg_dict1 = {}
mulai = time.time()
Start = time.time()

name = client.getProfile()
name.displayName = "BotBasX"
client.updateProfile(name)


status = client.getProfile()
status.statusMessage = "Creator BotBasX"
client.updateProfile(status)


#===============================Def Backup down ===============
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
###   
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs) 
####new
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))    

def sendMessageWithMention(to, clientMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(clientMID)+'}'
        text_ = '@x '
        client.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False

def backupData():
    try:
        backup = protectqr
        f = codecs.open('protectqr.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)    
    
        backup = protectkick
        f = codecs.open('protectkick.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        
        backup = protecARoin
        f = codecs.open('protecARoin.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)        

        backup = protectcanceljs
        f = codecs.open('protectcanceljs.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
                
        backup = protectcancel
        f = codecs.open('protectcancel.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        
        backup = protectinvite
        f = codecs.open('protectinvite.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        
        backup = protectantijs
        f = codecs.open('protectantijs.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)  

        backup = ghost
        f = codecs.open('ghost.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)        
        
        backup = server
        f = codecs.open('server.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        
        backup = server2
        f = codecs.open('server2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
#==================================Backup BL================================
        backup = st2__b
        f = codecs.open('st2__b.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        print(error)
        return False
#===============================Def Backup UP   ===============
cont = client.getContact(id)
def logError(text):
    client.log("[ERROR] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendflex(to, data): 
    ratedit = LiffChatContext(to)
    ratedit1 = LiffContext(chat=ratedit)
    view = LiffViewRequest('1643771679-3LNK0BXL', ratedit1)
    token = client.liff.issueLiffView(view)
    api_url = 'https://api.client.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(api_url, headers=headers, data=json.dumps(data))
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)
def helpbot1():
      helpMessage1 = """┏━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃          คำสั่งบอท📍คำสั่ง
┗━━━━━━━━━━━━━━━━━━━━━━━━━━
┃🥰 .อัพรูป 😈(อัพรูปโปรไฟล์บอท)
┃🥰 .เพิ่มแอด @
┃🥰 .ลบแอด @
┃🥰 .แอดมิน (เชคแอดมิน)
┃🥰 .คทแอด (เช็ค คท.แอดมิน)
┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┃          🥰คำสั่งเตะ-รวบ🥰
┗━━━━━━━━━━━━━━━━━━━━━━━━━━
┃💔 .zx อักษรชื่อ    🥰(รวบชื่อ)🐥
┃💔 .bk @    💔(รวบคิก)🐥
┃🥰 .เตะ @ = สั่งบอทเตะ
┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┃          🥰คำสั่งblacklist🥰
┗━━━━━━━━━━━━━━━━━━━━━━━━━━
┃💔 ʙᴀɴ         🥰(คำสั่งหลอกควาย)??
┃💔 .คทดำ  💔(เช็ค คท ที่ติดดำ)🐥
┃?? .เตะดำ  🥰(คำสั่งเตะบัญชีดำ)🐥
┃🥰 restart    💔(คำสั่งรีสตาร์ทบอท)🐥
┃💔 offcount 🥰(ปิดนับจำนวนคนอ่าน)🐥
┃💔 count      💔(เริ่มนับจำนวนคนอ่าน)🐥
┃🥰 godown  🥰(ยัดดำคนทั้งห้อง)🐥
┃🥰 blacklist 💔(ลง คท.ที่ต้องการยัดดำ)🐥
┃💔 group:save 😈(ดึงชื่อ+รูปกลุ่ม)😈
┃💔 blacktea     💔(ส่ง คท.ดำ ที่จะล้างดำ)
┃🥰 .ยก 💔(ใสตัวเลข +10 ขึ้นไป)
┃🥰 /getflex       💔(จำนวน+4 ขึ้นไป)
┃💔 clearblacklist💔 (ล้าง คท ดำทั้งหมด)
┃💔 blackcheck   💔(เช็ครายชื่อคนติดดำ)
┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┃          🥰คำสั่งprotect🥰
┗━━━━━━━━━━━━━━━━━━━━━━━━━━
┃🥰 กันเตะเปิด/ปิด (ป้องกันคนเตะ)
┃🥰 กันเชิญเปิด/ปิด (ป้องกันคนเชิญ)
┃🥰 กันลิ้งเปิด/ปิด (ป้องกันคนเปิดลิ้ง)
┃🥰 กันเข้าเปิด/ปิด (ป้องกันคนเข้ากลุ่ม)
┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┃          🥰คำสั่งadminbot🥰
┗━━━━━━━━━━━━━━━━━━━━━━━━━━
┃🥰 xexec: (ใส่ข้อความที่จะประกาศ)   
┃🥰 เช็ค (เช็คสถานะบอท)
┃🇨🇦 ตั้งต้อนรับ:  ( ใส่ข้อความ )
┃🇨🇦 ตั้งออก:  ( ใสข้อความ )
┃🇨🇦 เชคต้อนรับ
┃😈 เชคออก
┃😈 helpเข้า & helpออก
┃😈 ต้อนรับ เปิด /  ต้อนรับ ปิด
┃💔 ทักออก เปิด /  ทักออก ปิด
┃💔 เลขา
┃💔 📍
┃🎀 b url on             😈(คำสั่งเปิดลิ้งกลุ่ม)💔
┃🎀 closelink          😈(คำสั่งปิดลิ้งกลุ่ม)🥰
┃🎀 Requestlink     😈(ขอลิ้งกลุ่ม)💔
┃🇨🇦 read                  😈(ดูรายชื่อคนอ่าน)🥰
┃🇨🇦 opensecretly    😈(ดูคนแอบอ่านเปิด)💔
┃🇨🇦 closesecretly   😈(ดูคนแอบอ่านปิด)🥰
┃🥰 cancel              😈(ยกเลิกค้างเชิญ)💔
┃🥰 Deletechat       😈(ลบแชท)🥰
┃🥰 ลาก่อย            😈(สั่งบอทออกกลุ่ม)💔
┃🥰 ลากอย🖕           😈(บินกลุ่มเล่น)💔
┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┃line://ti/p/~botpray25
┃━━━━━━━━━━━━━━━━━━━━━━━━━━"""
      return helpMessage1  

      return myHelp1
     
def helpbot2():
      helpMessage2 = """╔═══════════════════
║↪แทค
║↪โทร จำนวน (เชิญคอล)
║↪ต้อนรับ เปิด/ปิด
║↪เปิดแอบ/ปิดแอบ(ดูคนแอบอ่าน)
║↪เปิดอ่าน/ปิดอ่าน (ดูคนอ่าน)
║↪พูด คำที่จะให้พูด (สิริพูด)
║↪/ยกเลิก จำนวน (ยกเลิกข้อความ)
║↪คอนแทค @ (เอาคอนแทค)
║↪ชื่อ @ (เอาชื่อ)
║↪รูป @ (เอารูป)
║↪สถานะ @ (เอาสถานะ)
║↪ไอดีไลน์ ไอดี (ค้นหาไลน์)
║↪ยูทูป คำที่จะหา (ค้นยูทูป)
║↪เขียน ข้อความ (เขียนข้อความ)
║↪ข้อมูลกลุ่ม (ดูข้อมูลกลุ่ม)
║↪แอดกลุ่ม (ดูคนสร้างกลุ่ม)
║↪ออน (เวลาออนไลน์บอท)
║↪.ลูกเล่น (เกม)
║↪เวลาทำงาน: {}
╚════〘 BotBasX 〙══════"""
      return helpMessage2

      return myHelp2


#########
      
def helpbot3():
      helpMessage3 = """╔═════════
║↪.rps (เป่ายิ้งฉุบ)
║↪.coin (หัวก้อย)
║↪.slot (สล็อต)
║↪.dice (ทอยเต๋า)
║↪.hilo (ไฮโล)
║↪.roulette (รูเล็ตต์)
╚═〘 BotBasX 〙
"""
      return helpMessage3

      return myHelp3
      
def mentionMembers(to, mids=[]):
    if client in mids: mids.remove(client)
    parsed_len = len(mids)//20+1
    result = ''
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '%i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += ''
        if result:
            if result.endswith('\n'): result = result[:-1]
            client.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv) 
    
def timeChange(secs):
        mins, secs = divmod(secs,60)
        hours, mins = divmod(mins,60)
        days, hours = divmod(hours,24)
        weeks, days = divmod(days,7)
        months, weeks = divmod(weeks,4)
        year, months = divmod(months,12)
        text = ""
        if year != 0: text += "%02d ปี" % (year)
        if months != 0: text += "%02d เดือน" % (months)
        if weeks != 0: text += " %02d สัปดาห์" % (weeks)
        if days != 0: text += " %02d วัน" % (days)
        if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
        if mins != 0: text += " %02d นาที" % (mins)
        if secs != 0: text += " %02d วินาที" % (secs)
        if text[0] == " ":
                text = text[1:]
        return text    
        
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            botbas.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def kickBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoBlock"] == True:
                runautoblock = mp.Process(target=client.sendMessage(op.param1,str(settings["message"])+client.getContact(clientMID).displayName))
                runautoblock = mp.Process(target=client.findAndAddContactsByMid(op.param1))
                runautoblock.start()

        if op.type == 122:
            if op.param1 in protect["url"]["id"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff and op.param2 not in RXFam:
                    if op.param2 not in settings["blacklist"]:
                        settings["blacklist"][op.param2] = True
                    client.kickoutFromGroup(op.param1,[op.param2])
                    G = client.getGroup(op.param1)
                    if G.preventedJoinByTicket == True:
                        G.prevntedJoinByTicket = False
                        client.updateGroup(G)
                    else:
                        if G.preventedJoinByTicket == False:
                            G.preventedJoinByTicket = True
                            client.updateGroup(G)
        if op.type == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    client.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = client.getContact(msg.contentMetadata["mid"])
                        path = client.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line-cdn.net/'+path
                        client.sendMessage(msg.to,"- ชื่อไลน์ : " + msg.contentMetadata["displayName"] + "\n- ไอดีไลน์ : " + msg.contentMetadata["mid"] + "\n- สถานะไลน์ : " + contact.statusMessage + "\n- ลิงค์โปร : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        client.sendImageWithURL(msg.to, image)

        if op.type == 26:
            type = op.message.contentType
            to = op.message.to
            msg = op.message
            text = msg.text
            if to in special1:
                
                if type == 13:
                    client.sendMessage(msg.to, "-- ระบบป้องกันคนวางคท--")
                    client.kickoutFromGroup(to,[msg._from])
                
        if op.type == 26:
            type = op.message.contentType
            to = op.message.to
            msg = op.message
            text = msg.text
            if to in special:
                if type == 0:
                    mlow = text.lower()
                    if "http" in mlow or "https" in mlow or "line://" in mlow:
                        if re.match(regex, msg.text):
                        	
                            client.sendMessage(msg.to, "-- ระบบป้องกันคนวางลิ้ง--")
                            client.kickoutFromGroup(to,[msg._from])
                        else:
                            client.sendMessage(msg.to, "-- ระบบป้องกันคนวางลิ้ง--")
                            client.kickoutFromGroup(to,[msg._from])
              
#--------------------------#กันวางลิ้ง
      
        if op.type == 26:
            msg = op.message
            if msg.contentType == 22:
                if 'true' in msg.contentMetadata['FLEX_JSON']:
                    if msg.to in protectflex:
                        LnBots["blacklist"][msg.to] = True
                        keyword = msg.contentMetadata['FLEX_JSON']
                        result = keyword.replace('true','True')
                        client.sendMessage(msg.to, "ข้อความอัตโนมัติ:\nป้องกันใช้เฟก")
                        client.kickoutFromGroup(msg.to,[msg._from])   
                        print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ เตะเฟก] \033[0m""")
#----------------กันเชิญนะจ๊ะ-------------------                   
        
        if op.type == 124:
            if clientMID in op.param3:
               
                    client.acceptGroupInvitation(op.param1)
                    time.sleep(0.4)
                    client.sendMessage(msg.to, "cancel")
                    
            if op.param1 in protect["inv"]["id"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff and op.param2 not in RXFam:
                    if op.param2 not in settings["blacklist"]:
                        settings["blacklist"][op.param2] = True
                    if op.param3 not in settings["blacklist"]:
                        settings["blacklist"][op.param3] = True
                    client.cancelGroupInvitation(op.param1,[op.param3])
                    client.kickoutFromGroup(op.param1,[op.param2])

        if op.type == 130:
            if op.param1 in protect["join"]["id"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff and op.param2 not in RXFam:
                    if op.param2 not in settings["blacklist"]:
                        settings["blacklist"][op.param2] = True
                    client.kickoutFromGroup(op.param1,[op.param2])
                    G = client.getGroup(op.param1)
                    if G.preventedJoinByTicket != True:
                        G.prevntedJoinByTicket = True
                        client.updateGroup(G)

        if op.type == 133:
            if op.param1 in protect["kick"]["id"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff and op.param2 not in RXFam:
                    if op.param2 not in settings["blacklist"]:
                        settings["blacklist"][op.param2] = True
                    client.kickoutFromGroup(op.param1,[op.param2])

            if op.param3 in admin:
                if op.param2 not in settings["blacklist"]:
                    settings["blacklist"][op.param2] = True
                client.kickoutFromGroup(op.param1,[op.param2])
                client.inviteIntoGroup(op.param1,[op.param3])
            if op.param3 in client.profile.mid:
                if op.param2 not in admin:
                    if op.param2 not in settings["blacklist"]:
                        settings["blacklist"][op.param2] = True
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)
       
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        client.sendMessage(msg.to, "Blacklist has been recorded.")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        client.sendMessage(msg.to, "Blacklist has been recorded.")
               if settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        client.sendMessage(msg.to, "This blacklist has been deleted.")
                        settings["dblacklist"] = False
                   else:
                        settings["dblacklist"] = False
                        client.sendMessage(msg.to, "This blacklist has been deleted.")
                        
            if msg.contentType == 26:                        
                if msg.toType == 2:        
                    if msg._from in creator:							
                        if wait["contactadmin"] == True:
                            target = msg.contentMetadata["mid"]      
                            try:
                                Owner['admin'][msg.to] = target
                                backupData()
                                wait["contactadmin"] = False
                                client.sendMessage(to,"เพิ่มสิทธิ์ เป็นแอดมินหลัก เรียบร้อย\n\n คำสั่งของคุณพิม  help admin")
                            except Exception as error:
                                logError(error) 
                                
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
          #  txt      = text.lower()
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != client.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                teambotboys = msg.text.lower().split(" && ")
                for teambotboy in teambotboys:
                    if teambotboy == "ฝฝ" or teambotboy == "/x help":
                        if msg._from in admin:
                            helpMessage1 = helpMessage1()
                            runhelp = mp.Process(target=client.sendMessage(to, str(helpMessage1)))
                            runhelp.start()           
                    elif msg.text.startswith('k exec ') or msg.text.startswith('l exec '):
                      if msg._from in admin:
                        try:
                            result = msg.text.replace('g exec ', '') or msg.text.replace('x exec ', '')
                            exec(result)
                        except Exception as error:
                            client.sendMessage(to, '{}'.format(error))
#==========================FLEX#-#-$-$$+$++#+#+#((#(#(#(
                    elif text.lower() == 'คำสั่ง':
            #          if msg._from in admin:
                         totalTime = time.time() - Start
                         mins, secs = divmod(totalTime,60)
                         hours, mins = divmod(mins,60)
                         days, hours = divmod(hours, 24)
                         resTime = ""
                         if days != 00:
                             resTime += "%2d วัน " % (days)
                         if hours != 00:
                             resTime += "%2d ชั่วโมง " % (hours)
                         if mins != 00:
                             resTime += "%2d นาที " % (mins)
                         resTime += "%2d วินาที" % (secs)
                         totalTime = time.time() - Start
                         mins, secs = divmod(totalTime,60)
                         hours, mins = divmod(mins,60)
                         days, hours = divmod(hours, 24)
                         mounts, days = divmod(days, 30)
                         years, mounts = divmod(mounts, 12)                    	
                         detailShow = helptest.format(bName=client.getProfile().displayName,runtime=resTime)
                         hMsg = detailShow
                         client.sendMessage(msg.to, hMsg)
######################                       
                    elif text.lower() == "/ออน":
                        timeNow = time.time() - Start
                        runtime = timeChange(timeNow)
                        run = "「เวลาทำงาน」\n"
                        run += runtime
                        helps = "{}".format(str(run))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(run)),
                            "sentBy": {
                                 "label": "{}".format(client.getContact(clientMID).displayName),
                                 "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(clientMID).pictureStatus),
                                 "linkUrl": "line://nv/profilePopup/mid=u8401f6854821e57b3737760a1f9df54d"
                            }
                        }
                        sendTemplate(to, data)        
                        
                    elif text.lower() == "ออน":
                        timeNow = time.time() - Start
                        runtime = timeChange(timeNow)
                        contact = client.getContact(clientMID)
                        run = "⇨ เวลาออนไลน์บอท ⇦\n"
                        run += runtime
                        data = {
                            "type": "flex",
                            "altText": "{}".format(run),
                            "contents": {
                                    "type": "bubble",
                                "styles": {
                                    "body": {
                                        "backgroundColor": '#000000'
                                     },
                                },
                                "hero": {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                                "size": "full",
                                                "aspectRatio": "1:1",
                                                "aspectMode": "fit",
                                            },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [                              
                                        {
                                            "type": "text",
                                            "text": "{}".format(run),
                                            "wrap": True,
                                            "color": "#990066",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md"
                                        },
                                   ]
                               }
                            }
                        }
                        sendTemplate(to, data)                                    
                        
                    elif text.lower() == '.ชอบหี':
                                gifnya = ['https://i.pinimg.com/originals/87/a8/9b/87a89b5aeaf35ba0c8879db5a136ccbd.gif']
                                data = {
                                    "type": "template",
                                    "altText": "Image carouserl",
                                    "template": {
                                        "type": "image_carousel",
                                        "columns": [
                                            {
                                                "imageUrl": "{}".format(random.choice(gifnya)),
                                                "size": "full",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://ti/p/~botpray25"
                                                }
                                            }
                                        ]
                                    }
                                }
                                sendTemplate(to, data)
                                
                    elif msg.text.lower().startswith("เขียน "):
                        sep = text.split(" ")
                        textnya = text.replace(sep[0] + " ", "")
                        text = "{}".format(textnya)
                        contact = client.getContact(clientMID)
                        data = {
                            "type": "flex",
                            "altText": "BotBasX",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                        "backgroundColor": '#FFFFFF'
                                        },
                                     },
                                "hero": {
                                    "type": "image",
                                    "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                    "size": "full",
                                    "aspectRatio":"1:1",
                                    "aspectMode":"cover"
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "{}".format(text),
                                            "color":"#000000",
                                            "wrap": True,
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "xl"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)        
                        
                    elif msg.text.lower().startswith("ยูทูป"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyApzHZ18jUd3BdkhL_xcwAI_zxqwb9fuy4".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                            "type": "bubble",
                                            "styles": {
                                                "header": {
                                                    "backgroundColor": "#66FF99" ##CCFF33
                                                },
                                                "body": {
                                                   "backgroundColor": "#66FF99", #66FFFF
                                                   "separator": True,
                                                   "separatorColor": "#66FF99"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#000000", #CCFF33
                                                    "separator": True,
                                                   "separatorColor": "#66FF99"
                                               }
                                            },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                   {
                                                        "type": "text",
                                                        "text": "Youtube",
                                                        "weight": "bold",
                                                        "color": "#000000", #FF00FF
                                                        "size": "sm"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                "size": "full",
                                                "aspectRatio": "20:13",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://nv/profilePopup/mid=ub90fee136a68d4602aa10f734f24ff42"
                                                }
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "image",
                                                        "url": "https://obs.line-scdn.net/{}".format(client.getContact(clientMID).pictureStatus),
                                                        "aspectMode": "cover",
                                                        "gravity": "bottom",
                                                        "size": "sm",
                                                        "aspectRatio": "1:1",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                        }
                                                    }]
                                                }, {
                                                    "type": "separator",
                                                    "color": "#000000" #111111
                                                }, {
                                                    "type": "box",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "BotBasX",
                                                        "color": "#000000", #0000EE
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#000000", #005500
                                                        "size": "sm",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 2,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 2,
                                                        "style": "primary",
                                                        "color": "#66FF99", #3333FF
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "กดเพื่อดู",
                                                            "uri": "https://youtu.be/{}".format(str(music['id']['videoId']))
                                                        }
                                                    }, {
                                                        "flex": 3,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#FF3333", #111111
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "ปิดปรับปรุง",
                                                            "uri": "line://ti/p/~botpray25"
                                                        }
                                                    }]
                                                }, {
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#66FF99", #111111
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "ติดต่อผู้สร้าง",
                                                        "uri": "line://ti/p/~botpray25"
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append('https://youtu.be/' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)                        
            
                    elif msg.text.lower().startswith("ไอดีไลน์ "):
                            sep = text.split(" ")
                            bastxt = text.replace(sep[0] + " ", "")
                            bot = client.findContactsByUserid(bastxt)
                            line = bot.mid
                            client.sendMessage(to,"line://ti/p/~" + bastxt)   
                            client.sendContact(to, line)           

                    elif text.lower() == 'คนสร้างกลุ่ม' or text.lower() == "แอดกลุ่ม":
                        group = client.getGroup(to)
                        GS = group.creator
                        adminroom = GS.mid
                        name = GS.displayName
                        pp = GS.pictureStatus
                        data = {
                            "type": "flex",
                            "altText": "BotBasX",
                            "contents": {
                                "type": "bubble",
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type":"text",
                                            "text":"ผู้สร้างกลุ่มนี้",
                                            "size":"md",
                                            "weight":"bold",
                                            "color":"#000000",
                                            "align":"center"
                                        },
                                        {
                                            "type":"text",
                                            "text": " "
                                        },
                                        {
                                            "type": "image",
                                            "url": "https://profile.line-scdn.net/" + str(pp),
                                            "size": "lg"
                                        },
                                        {
                                            "type":"text",
                                            "text":" "
                                        },
                                        {
                                            "type":"text",
                                            "text":"{}".format(name),
                                            "size":"md",
                                            "weight":"bold",
                                            "color":"#000000",
                                            "align":"center"
                                       },
                                   ]
                                }
                            }
                        }
                        sendTemplate(to, data)     
                        client.sendContact(to, adminroom)          

                    elif msg.text.lower() == 'ข้อมูลกลุ่ม':
                        group = client.getCompactGroup(msg.to)
                        try:
                            ccreator = group.creator.mid
                            gcreator = group.creator.displayName
                        except:
                            ccreator = None
                            gcreator = 'ไม่พบผู้สร้างกลุ่ม'
                        if not group.invitee:
                            pendings = 0
                        else:
                            pendings = len(group.invitee)
                        qr = 'ปิด' if group.preventedJoinByTicket else 'เปิด'
                        if group.preventedJoinByTicket:
                            ticket = 'URL ปิดอยู่'
                        else:
                            ticket = 'https://line.me/R/ti/g/' + str(client.reissueGroupTicket(group.id))
                        created = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
                        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
                        res = ''
                        res += 'ชื่อกลุ่ม: ' + group.name
                        res += '\nGID: ' + group.id
                        res += '\nผู้สร้างกลุ่ม: ' + gcreator
                        res += '\nเวลาสร้างกลุ่ม: ' + created
                        res += '\nสมาชิกทั้งหมด: ' + str(len(group.members))
                        res += '\nค้างเชิญทั้งหมด: ' + str(pendings)
                        res += '\nสถานะ URL: ' + qr
                        res += '\nURL: ' + ticket
                        client.sendMessage(group.id, res)                                                                         
#########################################
                    elif msg.text.lower().startswith("พูด "):
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ", "")
                            lang = 'th'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("hasil.mp3")
                            client.sendAudio(msg.to, "hasil.mp3")  
##
                    elif msg.text.startswith("/spam "):
                       sep = text.split(" ")
                       number = text.replace(sep[0] + " ","")
                       if len(number) > 0:
                          if number.isdigit():
                              number = int(number)
                              if number > 200:                                             
                                    client.sendMessage(to,"สูงสุด200อย่ามาตลกไอสัส")
                              else:
                                    for i in range(0,number):
                                         data = {'type':'text','text':str(number)}
                                         sendTemplate(msg.to, data)
                                         number -= 1
                                         time.sleep(0.001)
                                         data = {'type':'text','text':str(i+1)}
                                         sendTemplate(msg.to, data)
                                         i += 1+1
                                         time.sleep(0.001)
                          else:
                             client.sendMessage(to,"กรุณาใส่จำนวน")
                             
                    elif msg.text.startswith(".say "):
                      if msg._from in admin:
                         spl = msg.text.split(" ")
                         try:
                             amount = spl[1]
                         except:
                             return client.sendMessage(msg.to,'วิธีการใช้งาน:\n/say [จำวนวน] [ข้อความ]')
                         if amount.isdigit():
                             amount = int(amount)       	                    
                         else:
                            return client.sendMessage(msg.to,"วิธีการใช้งาน:\n.say [จำนวน] [ข้อความ]")
                         hMsg = msg.text.replace(spl[0] + " " + str(amount) + " ", "")
                         if len(hMsg.split(" ")) == 2:
                             return client.sendMessage(msg.to,"วิธีการใช้งาน:\n.say [จำนวน] [ข้อความ]")
                         for i in range(amount):
                             client.sendMessage(msg.to, hMsg)    
                              
                    elif msg.text.startswith("/ยกเลิก "):
                        try:
                            iWant = text.split(" ")[1]
                        except:
                            return client.sendMessage(msg.to, 'วิธีการใช้งาน\n/ยกเลิก [จำนวน]')
                        if iWant.isdigit():
                            amount = int(iWant)
                        else:
                            return client.sendMessage(msg.to, 'วิธีการใช้งาน\n/ยกเลิก [จำนวน]')
                        nowGet = 0
                        M = client.getRecentMessagesV2(msg.to, amount)
                        MsgID = []
                        for x, i in enumerate(M):
                            if x != 0:
                                if i._from == cl:
                                    MsgID.append(i.id)
                                    if len(MsgID) == amount:
                                        break
                        IDS = 0
                        for i in MsgID:
                            try:
                              client.unsendMessage(i)
                              IDS = IDS + 1
                            except:
                                continue
                        client.sendMessage(msg.to, "ยกเลิก {} ข้อความเรียบร้อยแล้ว".format(IDS))                              
#==========================
#                    elif text.lower() == 'คำสั่ง':
#                           helpMessage2 = helpbot2()
 #                          client.sendMessage(msg.to, str(helpMessage2))
                    elif text.lower() == '.ลูกเล่น':
                           helpMessage3 = helpbot3()
                           client.sendMessage(msg.to, str(helpMessage3))                           
                    elif teambotboy == 'คำสั่ง1' or teambotboy == 'kg':
                        if msg._from in admin:	
                           helpMessage1 = helpbot1()
                           client.sendMessage(msg.to, str(helpMessage1))                         
####             
                    elif msg.text.lower().startswith("คอนแทค "):
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = client.getContact(ls)
                                mi_d = contact.mid
                                client.sendContact(msg.to, mi_d)
                    elif msg.text.lower().startswith("ไอดี "):
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            ret_ = "[ ❥Mid ]"
                            for ls in lists:
                                ret_ += "\n{}" + ls
                            client.sendMessage(msg.to, str(ret_))               
                    elif msg.text.lower().startswith("ชื่อ "):
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = client.getContact(ls)
                                client.sendMessage(msg.to, "[ชื่อ]\n" + contact.displayName)
                    elif msg.text.lower().startswith("สถานะ "):
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = client.getContact(ls)
                                client.sendMessage(msg.to, "[สถานะ]\n{}" + contact.statusMessage)
                    elif msg.text.lower().startswith("รูป "):
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = "http://dl.profile.line.naver.jp/" + client.getContact(ls).pictureStatus
                                client.sendImageWithURL(msg.to, str(path))
                    elif ".หารูป " in msg.text.lower():
                        separate = msg.text.split(" ")
                        search = msg.text.replace(separate[0] + " ","")
                        with requests.session() as web:
                            r = web.get("https://api.boteater.co/googleimg?search={}".format(urllib.parse.quote(search)))
                            data = r.text
                            data = json.loads(data)
                            if data["result"] != []:
                                items = data["result"]
                                path = random.choice(items)
                                a = items.index(path)
                                b = len(items)
                                client.sendImageWithURL(to, str(path))
#== ===================
                    elif text.lower() == ".เชคบัค":
                    	if msg._from in admin:
                         try:client.inviteIntoGroup(to, [clientMID]);has = "OK"
                         except:has = "NOT"
                         try:client.kickoutFromGroup(to, [clientMID]);has1 = "OK"
                         except:has1 = "NOT"
                         if has == "OK":sil = "ไม่บัค"
                         else:sil = "บัค"
                         if has1 == "OK":sil1 = "บัค"
                         else:sil1 = "ไม่บัค"
                         client.sendMessage(to, "✴🔥[เชคระบบบัค]🔥✴\n✪➣ เตะ : {}".format(sil1,sil))
                    elif text.lower() == '.ลูกเล่น': 
                       client.sendReplyMessage(msg.id, msg.to,help())
                    elif text.lower() == '.rps':
                        s = random.choice(["ค้อน","กระดาษ","กรรไกร","ค้อน","กระดาษ","กรรไกร"])
                        client.sendReplyMessage(msg.id, msg.to,"ผลการเป่ายิ้งฉุบ : "+ s)
                    elif text.lower() == '.coin':
                        n = random.choice(["หัว","ก้อย","หัว","ก้อย"])
                        client.sendReplyMessage(msg.id, msg.to,"คุณกำลังโยนเหรียญ. . .")
                        client.sendMessage(msg.to,"ผลการโยนเหรียญ : "+ n)
                    elif text.lower() == '.slot':
                        s = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑🍒')
                        t = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑??')
                        r = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑🍒')
                        v = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑🍒')
                        a = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑??')
                        client.sendReplyMessage(msg.id, msg.to,"คุณกำลังหมุนเครื่องสล็อตแมชชีน. . .")
                        client.sendMessage(msg.to,"ผลเครื่องสล็อตแมชชีน :\n"+" | "+s+" | "+t+" | "+r+" | "+v+" | "+a+" | ")
                    elif text.lower() == '.dice':
                        f = random.choice('123456')
                        client.sendReplyMessage(msg.id, msg.to,"คุณกำลังทอยลูกเต๋าอยู่. . .")
                        client.sendMessage(msg.to,"ผลการทอยลูกเต๋า : "+f+" แต้ม")
                    elif text.lower() == '.hilo':
                        f = random.choice('123456')
                        r = random.choice('123456')
                        t = random.choice('123456')
                        d = int(f) + int(r) + int(t)
                        client.sendReplyMessage(msg.id, msg.to, "คุณกำลังทอยลูกเต๋าทั้ง3ลูก. . .")
                        client.sendMessage(msg.to, "🎲ผลการทอยทั้งหมด🎲\n\n"+"ลูกที่ 1 : "+f+" แต้ม"+"\n"+"ลูกที่ 2 : "+r+" แต้ม"+"\n"+"ลูกที่ 3 : "+t+" แต้ม"+"\n\n"+"แต้มรวมทั้งหมด "+str(d)+" แต้ม")
                    elif text.lower() == '.roulette':
                        s = random.choice(rr)
                        client.sendReplyMessage(msg.id, msg.to, "คุณได้ทำการลั่นไกไปที่ปืนลูกโม่ปรากฎว่า...")
                        client.sendMessage(msg.to, s)
###############################2222#฿22*฿7฿7%-%8฿8#8฿8%+฿+#(#++%%++฿฿++฿2+2+2+
                    elif msg.text.lower().startswith("ข้อมูล "):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = client.getContact(ls)
                                client.sendMessage(msg.to, contact.displayName)
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                                contact = client.getContact(ls)
                                client.sendMessage(msg.to, contact.statusMessage)
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            ret_ = ""
                            for ls in lists:
                                ret_ += ls
                            client.sendMessage(msg.to, str(ret_))
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = "http://dl.profile.line-cdn.net/" + client.getContact(ls).pictureStatus
                                client.sendImageWithURL(msg.to, str(path))                                
#==========================
                    elif text.lower().startswith("/exec\n") or "/exec" in msg.text:
                       try:
                           code = msg.text.replace("/exec\n", "")
                           exec(code)
                       except Exception as error:
                           client.sendMessage(to, "Error : {}".format(error))
                    elif "qr " in msg.text.lower():
                                data = re.split("qr ",msg.text,flags=re.IGNORECASE)
                                if data[0] == "":
                                    if msg.toType != 0:
                                        client.sendImageWithURL(msg.to,"https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl="+data[1])
                                    else:
                                        client.sendImageWithURL(msg.from_,"https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl="+data[1])
                    elif msg.text in ["ลากอย🖕"]:
                      xyz = client.getGroup(to)
                      mem = [c.mid for c in xyz.members]
                      targets = []
                      for x in mem:
                        if x not in [admin,owner,creator,client.profile.mid]:targets.append(x)
                      if targets:
                        imnoob = 'simple.js gid={} token={} app={}'.format(to, client.authToken, "DESKTOPMAC\t6.5.2\tMAC\t10.15.1")
                        for x in targets:
                                if x not in owner and x not in admin not in RXFam:
                                    imnoob += ' uid={}'.format(x)
                        success = execute_js(imnoob)
                    
                    elif text.lower().startswith(".zx "):
                        if msg._from in admin:
                            sep = text.split(" ")
                            midn = text.replace(sep[0] + " ","")
                            hmm = text.lower()
                            G = client.getGroup(msg.to)
                            members = [G.mid for G in G.members]
                            targets = []
                            imclient = 'simple.js gid={} token={} app={}'.format(to, client.authToken, "DESKTOPMAC\t6.5.2\tMAC\t10.15.1")
                            for x in members:
                                contact = client.getContact(x)
                                msg = op.message
                                testt = contact.displayName.lower()
                                if midn in testt:targets.append(contact.mid)
                            if targets == []:return client.sendMessage(to,"ไม่พบสมาชิกที่ชื่อ " + midn + " ในกลุ่มนี้")
                            for target in targets:
                                #print(target,targets)
                                imclient += ' uid={}'.format(target)
                            success = execute_js(imclient)
                            client.sendMessage(to,"เตะสมาชิกทั้งหมดที่มี " + midn + " อยู่ในชื่อเรียบร้อยแล้ว")
                    elif msg.text.lower().startswith('.bk '):
                        if msg._from in admin:
                            no = 0
                            if 'MENTION' in msg.contentMetadata.keys():
                                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
#                                if len(mentions['MENTIONEES']) == 1:
#                                    mid = mentions['MENTIONEES'][0]['M']
#                                    return client.kickoutFromGroup(to, [mid])
                                target = []
                                for mention in mentions['MENTIONEES']:
                                    mid = mention['M']
                                    #print(mid)
                                    target.append(mid)
                                imclient = 'simple.js gid={} token={} app={}'.format(to, client.authToken, "DESKTOPMAC\t6.5.2\tMAC\t10.15.1")
                                for tg in target:
                                    #print(tg,target)
                                    imclient += " uid={}".format(tg)
                                execute_js(imclient)
                                client.sendMessage(to,"KICK(s) !")
                            else:
                                client.sendMessage(to, 'TAG(s) !')

                    elif msg.text.lower() == "/mid":
                        client.sendMessage(to,str(msg._from))
                    elif msg.text.lower().startswith(".เชค "):
                        mid = msg.text.split(" ")[1]
                        client.sendContact(to,mid)
                    elif msg.text.lower() == ".ตัส":
                        client.sendMessage(to,str(client.getContact(msg._from).statusMessage))
                    elif msg.text.lower().startswith("/getflex"):
                        if msg._from not in admin:return
                        aa = msg.text.replace(msg.text.split(' ')[0] + ' ','')
                        x = client.talk.getRecentMessagesV2(to, int(aa))
                        for msg in x:
#                            print(msg)
                            if msg._from != client.profile.mid:
                                if 'FLEX_JSON' in msg.contentMetadata:
                                    true = True
#                                    print(msg)
                                    data = msg.contentMetadata['FLEX_JSON']
                                    try:
                                        exec("sendTemplate(to,{'type': 'flex','altText': 'STEAL','contents': " + msg.contentMetadata['FLEX_JSON'] + "})")
                                        client.sendMessage(to,str(data))
                                        time.sleep(0.9)
                                    except Exeception as e:
                                        client.sendMessage(to,str(e))
                    elif msg.text.lower() == "!groups":
                        if msg._from in admin:
                            no = 1
                            text = ""
                            name = client.profile.displayName
                            groups = client.getGroupIdsJoined()
                            for group in groups:
                                g = client.getGroup(group)
                                text += "%s. %s\n" % (str(no),str(g.name))
                                no += 1
                            client.sendMessage(to,"%s in group:\n%s\nTotal %s Group(s)" % (str(name),str(text),str(len(groups))))
                    elif ("ดึงข้อมูล " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin[msg.to]:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = client.getContact(key1)
                               client.sendMessage(msg.to, "☆ Name : "+str(mi.displayName)+"\n ☆Mid : " +key1+"\n☆ Status Msg"+str(mi.statusMessage))
                               client.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(client.getContact(key1)):
                                   client.sendVideoWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+str(mi.picturePath)+'/vp.small')
                               else:
                                   client.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+str(mi.picturePath))

                    elif msg.text.lower().startswith("ยก"):
                          if msg._from in admin:
                               args = msg.text.replace("ยก","")
                               mes = 0
                               try:
                                  mes = int(args[1])
                               except:
                                  mes = 0
                               M = client.getRecentMessagesV2(receiver, 500)
                               MId = []
                               for ind,i in enumerate(M):
                                   if ind == 1:
                                      pass
                                   else:
                                       if i._from == client.profile.mid:
                                           MId.append(i.id)
                                           if len(MId) == mes:
                                               break
                               def unsMes(id):
                                   client.unsendMessage(id)
                               for i in MId:
                                   thread1 = threading.Thread(target=unsMes, args=(i,))
                                   thread1.start()
                                   thread1.join()
                    elif msg.text.lower() == ".กันเตะเปิด":
                        if msg._from in admin:
                            if to in protect["kick"]["id"]:
                                client.sendMessage(to,"Protection Kick is already Enable")
                            else:
                                protect["kick"]["id"][to] = True
                                client.sendMessage(to,"Protection Kick is Enable")
                    elif msg.text.lower() == ".กันเตะปิด":
                        if msg._from in admin:
                            if to in protect["kick"]["id"]:
                                del protect["kick"]["id"][to]
                                client.sendMessage(to,"Protection Kick is Disable")
                            else:
                                client.sendMessage(to,"Protection Kick is already Disable")
                    elif msg.text.lower() == ".กันเชิญเปิด":
                        if msg._from in admin:
                            if to in protect["inv"]["id"]:
                                client.sendMessage(to,"Protection Invite is already Enable")
                            else:
                                protect["inv"]["id"][to] = True
                                client.sendMessage(to,"Protection Invite is Enable")
                    elif msg.text.lower() == ".กันเชิญปิด":
                        if msg._from in admin:
                            if to in protect["inv"]["id"]:
                                del protect["inv"]["id"][to]
                                client.sendMessage(to,"Protection Invite is Disable")
                            else:
                                client.sendMessage(to,"Protection Kick is already Disable")
                    elif msg.text.lower() == ".กันเข้าเปิด":
                        if msg._from in admin:
                            if to in protect["join"]["id"]:
                                client.sendMessage(to,"Protection Join is already Enable")
                            else:
                                protect["join"]["id"][to] = True
                                client.sendMessage(to,"Protection Join is Enable")
                    elif msg.text.lower() == ".กันเข้าปิด":
                        if msg._from in admin:
                            if to in protect["join"]["id"]:
                                del protect["join"]["id"][to]
                                client.sendMessage(to,"Protection Join is Disable")
                            else:
                                client.sendMessage(to,"Protection Join is already Disable")
                    elif msg.text.lower() == ".กันลิ้งเปิด":
                        if msg._from in admin:
                            if to in protect["url"]["id"]:
                                client.sendMessage(to,"Protection URL is already Enable")
                            else:
                                protect["url"]["id"][to] = True
                                client.sendMessage(to,"Protection URL is Enable")
                    elif msg.text.lower() == ".กันลิ้งปิด":
                        if msg._from in admin:
                            if to in protect["url"]["id"]:
                                del protect["url"]["id"][to]
                                client.sendMessage(to,"Protection URL is Disable")
                            else:
                                client.sendMessage(to,"Protection URL is already Disable")
                    elif teambotboy == ".รีบอท" or teambotboy == "t ree":
                      if msg._from in admin:
                          client.sendMessage(msg.to,  "I'm rushing DOT.")
                          time.sleep(5)
                          client.sendMessage(msg.to,  "Rebate is done.")
                          restartBot()       
                          
                    elif teambotboy == "restart" or teambotboy == "t restart":
                      if msg._from in admin:
                          client.sendMessage(to, "The bot has been reset successfully.")
                          python = sys.executable
                          os.execl(python, python, *sys.argv)                          

                    elif teambotboy == "group:save" or teambotboy == "t group:save":
                        if msg._from in admin:
                            try:
                               gid = client.getGroup(to)
                               set["gn"] = str(gid.name)
                               set["gp"] = "http://dl.profile.line-cdn.net/" + str(gid.pictureStatus)
                               set["iv"] = [mem.mid if mem.mid != client.profile.mid else '' for mem in gid.members]
                               client.sendReplyMessage(msg.id, to,set["gn"])
                               client.sendImageWithURL(to,set["gp"])
                            except Exception as e: traceback.print_exc()
                    elif teambotboy == "group:back" or teambotboy == "t group:back":
                      if msg._from in admin:
                          try:
                              gp = client.getGroup(msg.to)
                              gp.name = set["gn"]
                              runsavegroup = mp.Process(target=client.updateGroup(gp))
                              set["cgp"] = True
                              runsavegroup = mp.Process(target=client.sendMessage(to,"change pictgroup"))
                              runsavegroup = mp.Process(target=client.sendImageWithURL(to,set["gp"]))
                              runsavegroup = mp.Process(target=client.inviteIntoGroup(to,set["iv"]))
                              runsavegroup.start()
                          except Exception as e: traceback.print_exc()
                    elif teambotboy == "respon" or teambotboy == "เลขา":
                      
                            runrespon = mp.Process(target=client.sendMentionV2(to, ' ครับนายท่าน @!',[sender]))
                            runrespon.start()
                    elif teambotboy == "respon" or teambotboy == "เลขา":
                      if msg._from in admin:
                            runrespon = mp.Process(target=client.sendMentionV2(to, 'ครับนายท่าน @!',[sender]))
                            runrespon.start()
                    elif teambotboy == "respon" or teambotboy == "เลขา ":
                      if msg._from in admin:
                            runrespon = mp.Process(target=client.sendMentionV2(to, 'ครับ @!',[sender]))
                            runrespon.start()
                    elif teambotboy == "respon" or teambotboy == "เลขา  ":
                      if msg._from in admin:
                            runrespon = mp.Process(target=client.sendMentionV2(to, 'เลขามาแล้ว @!',[sender]))
                            runrespon.start()
                    elif teambotboy == "respon" or teambotboy == "เลขาจ๋า":
                      if msg._from in admin: 
                            runrespon = mp.Process(target=client.sendMentionV2(to, 'เรียกทำไมสัส  @!',[sender]))
                            runrespon.start()
                    elif teambotboy == "ระบบป้องกัน" or teambotboy == "ระบบ":
                      if msg._from in admin:
                            runrespon = mp.Process(target=client.sendMentionV2(to, 'xd @!',[sender]))
                            runrespon.start()
                    elif msg.text.lower().startswith("xexec:"):
                      if msg._from in admin:
                                    bctxt = msg.text[len("xexec:"):].strip()
                                    a = client.getGroupIdsJoined()
                                    for manusia in a:
                                        gname = client.getGroup(manusia).name
                                        client.sendMessage(manusia,"🙏ขออนุญาตแอดมินค่ะ🙏"+gname+"\n\n"+ (bctxt))
                                    client.sendMessage(receiver,"✴️ส่งประกาศเสร็จสิ้น💯")
#=================================x setting down ========================== 
                    elif teambotboy == 'เช็ค' or teambotboy == 'set':
                        if msg._from in admin:
                           ret_ = "🇹🇭==[ เช็คต้อนรับว่าเปิดรึปิด ]==🇹🇭"                                                       
                           if msg.to in welcomegroup: ret_ += "\n\n🇹🇭 welcomegroup: On 【✔】"
                           else: ret_ += "\n\n🇹🇭 welcomegroup: Off 【🚫】"      
                           if msg.to in leavegroup: ret_ += "\n\n🇹🇭 leavegroup: On 【✔】"
                           else: ret_ += "\n\n🇹🇭 leavegroup: Off 【🚫】"                                                       
                           random.choice(Basx).sendMessage(to,str(ret_))
#=================================x setting up  ===========================           

                    elif teambotboy == "speed" or teambotboy == "สปีด":
                      if msg._from in admin:
                          def speedbot():
                              start = time.time()
                              runspeed = mp.Process(target=client.getProfile())
                              elapse = time.time() - start
                              runspeed = mp.Process(target=client.sendMessage(to, '%s' % str(elapse/100)))
                          speedbot = threading.Thread(target=speedbot)
                          speedbot.daemon = True
                          speedbot.start()

#===================================================== A D D Leaveall Down ===============================================================================	
#===================================================== A D D Leaveall up ===============================================================================	                        

                    elif teambotboy == ".ดำ" or teambotboy == "blacklist":
                      if msg._from in admin: 
                        settings["wblacklist"] = True
                        client.sendMessage(to, "• Please send the contactor down. •")
                    elif teambotboy == ".ขาว" or teambotboy == "blacktea":
                      if msg._from in admin: 
                        settings["dblacklist"] = True
                        client.sendMessage(to, "• Please send the contactor down. •")
                    elif teambotboy == "/ล้างดำ" or teambotboy == "ล้างดำ1":
                      if msg._from in admin: 
                        settings["blacklist"] = {}
                        client.sendMessage(to, "The blacklist has been cleared.")
                    elif teambotboy == "godown" or teambotboy == "t cb":
                      if msg._from in admin:
                          if msg.toType == 2:
                               _name = msg.text.replace("godown","") or msg.text.replace("t cb","")
                               gs = client.getGroup(msg.to)
                               client.sendMessage(msg.to,"The whole group is already stuffed.")
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                        targets.append(g.mid)
                               if targets == []:
                                    client.sendMessage(msg.to,"Something went wrong")
                               else:
                                   for target in targets:
                                       if not target in Family:
                                           try:
                                               settings["blacklist"][target] = True
                                               f=codecs.open('st2__b.json','w','utf-8')
                                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                           except:
                                               client.sentMessage(msg.to,"An unknown error was encountered.")
#===================Edit ban up ===============   
                    elif teambotboy.startswith("add1 ") or teambotboy.startswith("t add1 "):
                      if msg._from in creator:
                           targets = []
                           key = eval(msg.contentMetadata["MENTION"])
                           key["MENTIONEES"] [0] ["M"]
                           for x in key["MENTIONEES"]:
                               targets.append(x["M"])
                           for target in targets:
                               if target in Family:							   
                                   try:
                                       Owner['admin'][msg.to] = target
                                       backupData()
                                       random.choice(Basx).sendMessage(to, "เพิ่มสิทธิ์ เป็นแอดมินหลัก เรียบร้อย\n\n คำสั่งของคุณพิม help")
                                   except:
                                       random.choice(Basx).sendMessage(to, "ไม่พบรายชื่อติดต่อ.")

                    elif teambotboy.startswith(".ดำ ") or teambotboy.startswith("blacklist "):
                      if msg._from in admin:
                           targets = []
                           key = eval(msg.contentMetadata["MENTION"])
                           key["MENTIONEES"] [0] ["M"]
                           for x in key["MENTIONEES"]:
                               targets.append(x["M"])
                           for target in targets:
                               if target not in RXFam:							   
                                   try:
                                       settings["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       client.sendMessage(to, "เพิ่ม {} ในรายการblacklistเรียบร้อยแล้วค่ะ.".format(client.getContact(target).displayName))
                                   except:
                                       client.sendMessage(to, "Can't find the blacklist list.")
#===================Edit ban up ===============    
                    
                               
                    elif teambotboy.startswith("blacktea ") or teambotboy.startswith("ขาว "):
                      if msg._from in admin:
                           targets = []
                           key = eval(msg.contentMetadata["MENTION"])
                           key["MENTIONEES"] [0] ["M"]
                           for x in key["MENTIONEES"]:
                               targets.append(x["M"])
                           for target in targets:
                               try:
                                   del settings["blacklist"][target]
                                   f=codecs.open('st2__b.json','w','utf-8')
                                   json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                   client.sendMessage(to, "ลบ {} ในรายการblacklistเรียบร้อยแล้วค่ะ.".format(client.getContact(target).displayName))
                               except:
                                   client.sendMessage(to, "I can't find my contact.")
                    elif teambotboy == "banlist" or teambotboy == "blackcheck":
                      if msg._from in admin:
                        if settings["blacklist"] == {}:
                            client.sendMessage(to, "Can't find the blacklist list.")
                        else:
                            text = "Blacklisted list.:"
                            for mi_d in settings["blacklist"]:
                                text += "\n- {}".format(client.getContact(mi_d).displayName)
                            client.sendMessage(to, str(text))
                    elif "โทร " in msg.text.lower():
                             if msg.toType == 2:
                                 sep = msg.text.split(" ")
                                 r = msg.text.replace(sep[0] + " ","")
                                 num = int(r)
                                 try:
                                     client.sendMessage(msg.to,"กำลังดำเนินการ...")
                                 except:
                                     pass
                                 for var in range(num):
                                     group = client.getGroup(msg.to)
                                     members = [mem.mid for mem in group.members]
                                     client.acquireGroupCallRoute(msg.to)
                                     client.inviteIntoGroupCall(msg.to, contactIds=members)
                                 client.sendMessage(msg.to,"เชิญโทรสำเร็จแล้ว....☎️")
    #                elif text.lower() == "เชคบัค":
     #               	if msg._from in admin:
     #                    try:client.inviteIntoGroup(to, [clientMID]);has = "OK"
     #                    except:has = "NOT"
     #                    try:client.kickoutFromGroup(to, [clientMID]);has1 = "OK"
     ##                    except:has1 = "NOT"
     #                    if has == "OK":sil = "ไม่บัคค่ะ🥰"
     #                    else:sil = "บัคแล้วค่ะ🥺"
     #                    if has1 == "OK":sil1 = "บัคแล้วค่ะ🥺"
     #                    else:sil1 = "ไม่บัคค่ะ🥰"
     #                    client.sendMessage(to, "{}".format(sil1,sil))
                    elif teambotboy == "banlist" or teambotboy == "/เชคดำ":
                      if msg._from in admin:
                        if settings["blacklist"] == {}:
                            client.sendMessage(to, "Can't find the blacklist list.")
                        else:
                            text = "Blacklisted list.:"
                            for mi_d in settings["blacklist"]:
                                text += "\n- {}".format(client.getContact(mi_d).displayName)
                            client.sendMessage(to, str(text))
                    elif teambotboy == ".คทดำ" or teambotboy == "Cb":
                      if msg._from in admin:
                        if settings["blacklist"] == {}:
                            client.sendMessage(to, "Can't find the blacklist list.")
                        else:
                            for mi_d in settings["blacklist"]:
                                client.sendContact(to, mi_d)
                    elif teambotboy == ".เตะดำ" or teambotboy == "เตะดำ":
                      if msg._from in admin:
                        if msg.toType == 2:
                             group = client.getGroup(to)
                             gMembMids = [contact.mid for contact in group.members]
                             matched_list = []
                             for tag in settings["blacklist"]:
                                 matched_list+=[str for str in gMembMids if str == tag]
                             if matched_list == []:
                                 client.sendMessage(to, "I could not find the blacklist.")
                             else:
                                 for jj in matched_list:
                                     try:
                                         klist=[client]
                                         kicker=random.choice(klist)
                                         runkickban = mp.Process(target=client.kickoutFromGroup(to,[jj]))
                                         runkickban.start()
                                     except:
                                         pass
#===================Edit kick down ===============
                    elif teambotboy.startswith("ตบ ") or teambotboy.startswith("แจะ "):
                      if msg._from in admin:
                          targets = []
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:					  
                            if target not in RXFam:					  					  
                                  klist=[client]
                                  kicker=random.choice(klist)
                                  runkick = mp.Process(target=kicker.kickoutFromGroup(to,[target]))
                                  runkick.start()
                    elif teambotboy.startswith("kick ") or teambotboy.startswith("kk "):
                      if msg._from in admin:
                          targets = []
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:					  
                            if target not in RXFam:					  					  
                                  klist=[client]
                                  kicker=random.choice(klist)
                                  runkick = mp.Process(target=kicker.kickoutFromGroup(to,[target]))
                                  runkick.start()
#===================Edit kick up ===============             

                    

#========================Welcome + leave Down ==========================
                    elif teambotboy.startswith('ตั้งต้อนรับ:'):
                        if msg._from in admin:
                            text = msg.text.replace('ตั้งต้อนรับ: ',"")
                            optypesg["welcomeMessage"] = text
                            client.sendMessage(msg.to, "Succeed")
                    elif teambotboy.startswith('t welcome:add'):
                        if msg._from in admin:
                            text = msg.text.replace('t welcome:add ',"")
                            optypesg["welcomeMessage"] = text
                            client.sendMessage(msg.to, "Succeed")
                    elif teambotboy == 'เชคต้อนรับ' or teambotboy == 't welcome:check':
                        if msg._from in admin:
                            client.sendMessage(msg.to, "ข้อความต้อนรับออกที่ตั้ง: "+str(optypesg["welcomeMessage"]))
                    elif teambotboy.startswith('ตั้งออก'):
                        if msg._from in admin:
                            text = msg.text.replace('ตั้งออก ',"")
                            optypesg["leaveMessage"] = text
                            client.sendMessage(msg.to, "Succeed")
                    elif teambotboy.startswith('t leave:add'):
                        if msg._from in admin:
                            text = msg.text.replace('t leave:add ',"")
                            optypesg["leaveMessage"] = text
                            client.sendMessage(msg.to, "Succeed")
                    elif teambotboy == 'เชคออก' or teambotboy == 't leave:check':
                        if msg._from in admin:
                            client.sendMessage(msg.to, "ข้อความต้อนรับเข้าที่ตั้ง: "+str(optypesg["leaveMessage"]))
                    elif teambotboy == 'leave:help' or teambotboy == 'helpออก':
                        if msg._from in admin:
                            text = "วิธีใช้งานคำสั่ง"
                            text += "\n- leave:add คุณ {name} ได้ออกจากกลุ่ม {group}"
                            text += "\n\n**หมายเหตุ"
                            text += "\n* {name} แสดงชื่อคนออกกลุ่ม"
                            text += "\n* {group} แสดงชื่อกลุ่มที่ออก"
                            client.sendReplyMessage(msg_id, msg.to, text)
                    elif teambotboy == 'welcome:help' or teambotboy == 'helpเข้า':
                        if msg._from in admin:
                            text = "วิธีใช้งานคำสั่ง"
                            text += "\n- welcome:add สวัสดีคุณ {name} ยินดีต้อนรับสู่ {group}"
                            text += "\n\n**หมายเหตุ"
                            text += "\n* {name} แสดงชื่อคนเข้ากลุ่ม"
                            text += "\n* {group} แสดงชื่อกลุ่มที่เข้า"
                            client.sendReplyMessage(msg_id, msg.to, text)
                    elif teambotboy.startswith('ต้อนรับ '):
                        
                            spl = msg.text.replace('ต้อนรับ ','')
                            if spl == 'เปิด':
                                if msg.to in welcomegroup:
                                    msgs = "ต้อนรับเข้าถูกเปิดใช้งานอยู่แล้ว"
                                else:
                                    welcomegroup[msg.to] = True
                                    f=codecs.open('welcomegroup.json','w','utf-8')
                                    json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                    msgs = "ต้อนรับเข้าเปิดใช้งาน"
                                client.sendMessage(msg.to, msgs)
                            elif spl == 'ปิด':
                                if msg.to in welcomegroup:
                                    del welcomegroup[msg.to]
                                    f=codecs.open('welcomegroup.json','w','utf-8')
                                    json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                                    msgs = "ต้อนรับเข้าปิดใช้งาน"
                                else:
                                    msgs = "ต้อนรับเข้าถูกปิดใช้งานอยู่แล้ว"
                                client.sendMessage(msg.to, msgs)
                    elif teambotboy.startswith('ทักออก '):
                        if msg._from in admin:
                            spl = msg.text.replace('ทักออก ','')
                            if spl == 'เปิด':
                                if msg.to in leavegroup:
                                    msgs = "ต้อนรับออกถูกเปิดใช้งานอยู่แล้ว"
                                else:
                                    leavegroup[msg.to] = True
                                    f=codecs.open('leavegroup.json','w','utf-8')
                                    json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                    msgs = "ต้อนรับออกเปิดใช้งาน"
                                client.sendMessage(msg.to, msgs)
                            elif spl == 'ปิด':
                                if msg.to in leavegroup:
                                    del leavegroup[msg.to]
                                    f=codecs.open('leavegroup.json','w','utf-8')
                                    json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                                    msgs = "ต้อนรับออกปิดใช้งาน"
                                else:
                                    msgs = "ต้อนรับออกถูกปิดใช้งานอยู่แล้ว"
                                client.sendMessage(msg.to, msgs)
                    elif teambotboy.startswith('t welcome '):
                        if msg._from in admin:
                            spl = msg.text.replace('t welcome ','')
                            if spl == 'on':
                                if msg.to in welcomegroup:
                                    msgs = "ต้อนรับเข้าถูกเปิดใช้งานอยู่แล้ว"
                                else:
                                    welcomegroup[msg.to] = True
                                    f=codecs.open('welcomegroup.json','w','utf-8')
                                    json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                    msgs = "ต้อนรับเข้าเปิดใช้งาน"
                                client.sendMessage(msg.to, msgs)
                            elif spl == 'off':
                                if msg.to in welcomegroup:
                                    del welcomegroup[msg.to]
                                    f=codecs.open('welcomegroup.json','w','utf-8')
                                    json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                                    msgs = "ต้อนรับเข้าปิดใช้งาน"
                                else:
                                    msgs = "ต้อนรับเข้าถูกปิดใช้งานอยู่แล้ว"
                                client.sendMessage(msg.to, msgs)
                    elif teambotboy.startswith('t leave '):
                        if msg._from in admin:
                            spl = msg.text.replace('t leave ','')
                            if spl == 'on':
                                if msg.to in leavegroup:
                                    msgs = "ต้อนรับออกถูกเปิดใช้งานอยู่แล้ว"
                                else:
                                    leavegroup[msg.to] = True
                                    f=codecs.open('leavegroup.json','w','utf-8')
                                    json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                    msgs = "ต้อนรับออกเปิดใช้งาน"
                                client.sendMessage(msg.to, msgs)
                            elif spl == 'off':
                                if msg.to in leavegroup:
                                    del leavegroup[msg.to]
                                    f=codecs.open('leavegroup.json','w','utf-8')
                                    json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                                    msgs = "ต้อนรับออกปิดใช้งาน"
                                else:
                                    msgs = "ต้อนรับออกถูกปิดใช้งานอยู่แล้ว"
                                client.sendMessage(msg.to, msgs)
                                
                                
#========================Welcome + leave Down ==========================	

#========================Add tagall down ===============================
                    elif teambotboy == '.แทค' or teambotboy == 'แทค':
                     # if msg._from in admin:
                        members = []
                        if msg.toType == 1:
                            room = client.getCompactRoom(to)
                            members = [mem.mid for mem in room.contacts]
                        elif msg.toType == 2:
                            group = client.getCompactGroup(to)
                            members = [mem.mid for mem in group.members]
                        else:
                            return client.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                        if members:
                            mentionMembers(to, members)
#========================Add tagall down ===============================   

#===============================Add admin down ===============
                    elif teambotboy.startswith('.เพิ่มแอด ') or teambotboy.startswith('t addadmin '):
                        if msg._from in owner:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                try:
                                    server["admin"].append(target)
                                    admin.append(target)
                                    f=codecs.open('server.json','w','utf-8')
                                    json.dump(server, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    client.sendMessage(to,"เพิ่มแอดมินเสร็จสิ้น")
                                except:
                                    client.sendMessage(msg.to, "Something went wrong")
                    elif teambotboy.startswith('addstaff ') or teambotboy.startswith('t addstaff '):
                        if msg._from in admin or msg._from in owner:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                server2["staff"].append(target)
                                staff.append(target)
                                f=codecs.open('server2.json','w','utf-8')
                                json.dump(server2, f, sort_keys=True, indent=4,ensure_ascii=False)
                                client.sendMessage(to,"เพิ่มสตาฟเสร็จสิ้น")
                    elif teambotboy.startswith('.ลบแอด ') or teambotboy.startswith('t deladmin '):
                        if msg._from in owner:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                try:
                                    server["admin"].remove(target)
                                    admin.remove(target)
                                    f=codecs.open('server.json','w','utf-8')
                                    json.dump(server, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    client.sendMessage(to,"ลบแอดมินเสร็จสิ้น")
                                except:
                                    client.sendMessage(msg.to, "Something went wrong")
                    elif teambotboy.startswith('delstaff ') or teambotboy.startswith('t delstaff '):
                        if msg._from in admin or msg._from in owner:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                server2["staff"].remove(target)
                                staff.remove(target)
                                f=codecs.open('server2.json','w','utf-8')
                                json.dump(server2, f, sort_keys=True, indent=4,ensure_ascii=False)
                                client.sendMessage(to,"ลบสตาฟเสร็จสิ้น")						
#===============================Add admin UP =============== 
                    elif teambotboy == "เปิดอ่าน":
                        tz = pytz.timezone("Asia/Makassar")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["อาทิตย์", "จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if to in read['readPoint']:
                            try:
                                del read['readPoint'][to]
                                del read['readMember'][to]
                            except:
                                pass
                            read['readPoint'][to] = msg_id
                            read['readMember'][to] = []
                            client.sendMessage(to, "✯͜͡❂ การอ่าน ถูกเปิดการใช้งานอยู่เเล้ว")
                        else:
                            try:
                                del read['readPoint'][to]
                                del read['readMember'][to]
                            except:
                                pass
                            read['readPoint'][to] = msg_id
                            read['readMember'][to] = []
                            client.sendMessage(to, "✯͜͡❂ ตั้งจุดอ่าน : \n{}".format(readTime))
                            client.sendMessage(to, "พิมพ์! อ่าน เพื่อดูคนอ่าน")
                    elif teambotboy == "ปิดอ่าน":
                         tz = pytz.timezone("Asia/Makassar")
                         timeNow = datetime.now(tz=tz)
                         day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                         hari = ["อาทิตย์", "จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์"]
                         bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                         hr = timeNow.strftime("%A")
                         bln = timeNow.strftime("%m")
                         for i in range(len(day)):
                             if hr == day[i]: hasil = hari[i]
                         for k in range(0, len(bulan)):
                             if bln == str(k): bln = bulan[k-1]
                         readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                         if to not in read['readPoint']:
                             client.sendMessage(to,"✯͜͡❂ การอ่าน ถูกปิดการใช้งานอยู่เเล้ว")
                         else:
                             try:
                                 del read['readPoint'][to]
                                 del read['readMember'][to]
                             except:
                                 pass
                             client.sendMessage(to, "✯͜͡❂ ลบจุดอ่าน : \n{}".format(readTime))

                    elif teambotboy == "อ่าน":
                         if to in read['readPoint']:
                             if read["readMember"][to] == []:
                                 return client.sendMessage(to, "✯͜͡❂ ไม่มีคนอ่าน")
                             else:
                                 no = 0
                                 result = "╭───「 คนอ่าน 」"
                                 for dataRead in read["readMember"][to]:
                                     no += 1
                                     result += "\n├ × {}. @!".format(str(no))
                                 result += "\n╰───「 ทั้งหมด {} คน 」".format(str(len(read["readMember"][to])))
                                 client.sendMentionV2(to, result, read["readMember"][to])
                                 read['readMember'][to] = []
#===============================Check admin+staff down =========================
                    elif teambotboy == '.แอดมิน' or teambotboy == 'แอดมิน':
                        if msg._from in admin:
                            text="🇹🇭===[ ʟɪsᴛ ᴀᴅᴍɪɴ ]===🇹🇭\n"
                            no=1
                            for x in admin:
                                text+=f"\n{no}. {client.getContact(x).displayName}"
                                no=no+1
                            client.sendMessage(to,str(text))
                    elif teambotboy == 'checkstaff' or teambotboy == 't checkstaff':
                        if msg._from in admin:
                            text="🇹🇭===[  ʟɪsᴛ sᴛᴀғғ  ]===🇹🇭\n"
                            no=1
                            for x in staff:
                                text+=f"\n{no}. {client.getContact(x).displayName}"
                                no=no+1
                            client.sendMessage(to,str(text))
                    
                    elif msg.text.lower() == '.คทแอด' or msg.text.lower() == 'แอดมิน':
                        if msg._from in owner:
                            for x in admin:
                                print(x)
                                client.sendContact(to,x)
#                                client.sendMessage(to, None, contentMetadata={'mid':x}, contentType=13)
                    elif teambotboy == 'constaff' or teambotboy == 't constaff':
                        if msg._from in admin:
                            for x in staff:
                                client.sendMessage(to, None, contentMetadata={'mid':x}, contentType=13)
#===============================Check admin+staff down =========================  

#===========================ADD listprotect Down ======================================
#=======
                    
                    elif msg.text in ["Deletechat"]:							
                                    client.sendMessage(msg.to,"The chat has been deleted.")
                                    client.removeAllMessages(op.param2)
                    elif teambotboy == 'remove:m' or teambotboy == 't remove:m':
                        if msg._from in admin:
                            for x in mainbots:
                                x.removeAllMessages(op.param2) 
                            client.sendMessage(to,"The chat has been deleted.")
#=============================URL Down ==============================================
                    elif teambotboy == 'b url on' or teambotboy == 't url on':
                        if msg._from in owner:
                            group = client.getGroup(to)
                            if group.preventedJoinByTicket == False:
                                client.sendMessage(to,"The link has been opened.")
                            else:
                                group.preventedJoinByTicket = False
                                client.updateGroup(group)
                            client.sendMessage(to,"The link is already open.")
                    elif teambotboy == 'closelink' or teambotboy == 't url off':
                        if msg._from in owner:
                            group = client.getGroup(to)
                            if group.preventedJoinByTicket == True:
                                client.sendMessage(to,"Rea hundred link closed.")
                            else:
                                group.preventedJoinByTicket = True
                                client.updateGroup(group)
                            client.sendMessage(to,"The link is closed.")							
                    elif teambotboy == 'requestlink' or teambotboy == 't url':
                        if msg._from in owner:
                            group = client.getGroup(to)
                            if group.preventedJoinByTicket == False:
                                ticket = client.reissueGroupTicket(to)
                                client.sendMessage(msg.to, "ลิ้งกลุ่มนี้:\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                            else:
                                client.sendMessage(to,"ยังไม่ได้เปิดลิ้งกลุ่มนี้")							
#=============================URL Down ==============================================                      
#=============================================================================ADD Protect1 ON/OFF DOWN==================
                    elif teambotboy.startswith("wc ") or teambotboy.startswith("t setup "):
                       if msg._from in admin:
                          spl = msg.text.replace('wc ','') or msg.text.replace('t setup ','')
                          if spl == 'on':						                                           
                              if msg.to in welcomegroup:
                                   msgs = "ต้อนรับเข้าถูกเปิดใช้งานอยู่แล้ว"
                              else:
                                   welcomegroup[msg.to] = True
                                   f=codecs.open('welcomegroup.json','w','utf-8')
                                   json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)	
                                   ginfo = client.getGroup(msg.to)                                  
                                   msgs = "ต้อนรับเข้าเปิดใช้งาน : " +str(ginfo.name)
                              client.sendMessage(msg.to, msgs)                                   
                                   
                              if msg.to in leavegroup:
                                   msgs = "ต้อนรับออกถูกเปิดใช้งานอยู่แล้ว"
                              else:
                                   leavegroup[msg.to] = True
                                   f=codecs.open('leavegroup.json','w','utf-8')
                                   json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)	
                                   ginfo = client.getGroup(msg.to)    								   
                                   msgs = "ต้อนรับออกเปิดใช้งาน : " +str(ginfo.name)
                              client.sendMessage(msg.to, msgs)    


#=============================================================================ADD INSTALL ON/OFF DOWN======================================================================
                    elif teambotboy == 'x protect on' or teambotboy == 'g protect on':
                        if msg._from in admin:
                            for p in ['protecturl','protectkick','protectjoin','protectcanceljs','protectcancel','protectinvite','js','ghost']:
                                client.sendMessage(to,'g '+str(p)+" on")
										
                    elif teambotboy == 'x protect off' or teambotboy == 'g protect off':
                        if msg._from in admin:
                            for p in ['protecturl','protectkick','protectjoin','protectcanceljs','protectcancel','protectinvite','js','ghost']:
                                client.sendMessage(to,'g '+str(p)+" off")											
#=============================================================================ADD INSTALL ON/OFF UP========================================================================	  
                    elif teambotboy == 'unsend on' or teambotboy == 'เปิดจับยก':
                        
                            settings["unsendMessage"] = True
                            client.sendMessage(msg.to, "On:Succeed")
                    elif teambotboy == 'unsend off' or teambotboy == 'ปิดจับยก':
                        
                            settings["unsendMessage"] = False
                            client.sendMessage(msg.to, "Off:Succeed")
                    elif teambotboy == 'opensecretly' or teambotboy == 'เปิดแอบ':
                        
                            try:
                                del RXCctv['point'][msg.to]
                                del RXCctv['sidermem'][msg.to]
                                del RXCctv['cyduk'][msg.to]
                            except:
                                pass
                            RXCctv['point'][msg.to] = msg.id
                            RXCctv['sidermem'][msg.to] = ""
                            RXCctv['cyduk'][msg.to]=True
                            client.sendReplyMessage(msg.id, msg.to, "Open the reader to scan")
                    elif teambotboy == 'closesecretly' or teambotboy == 'ปิดแอบ':
                        
                            if msg.to in RXCctv['point']:
                                RXCctv['cyduk'][msg.to]=False
                                client.sendReplyMessage(msg.id, msg.to, "Turn off scanning of readers")
                            else:
                                random.choice(Basx).sendReplyMessage(msg.id, msg.to, "Turn off scanning of readers")
               
                    elif teambotboy == "add on" or teambotboy == "t add on":
                      if msg._from in admin:
                          settings["contactadmin"] = True
                          random.choice(Basx).sendMessage(to, "ส่ง ᴄᴏɴᴛᴀᴄᴛ คนทีจะตั้งแอดลงมา.")                               
                                 
                    elif teambotboy == "autoblock on" or teambotboy == "/เปิดบล็อค":
                      if msg._from in admin:
                          settings["autoBlock"] = True
                          client.sendMessage(to, "The block has been opened.")
                    elif teambotboy == "autoblock off" or teambotboy == "/ปิดบล็อค":
                      if msg._from in admin:
                          settings["autoBlock"] = False
                          client.sendMessage(to, "The block has been closed.")
                    elif teambotboy == ".อัพรูป" or teambotboy == "/อัพรูป":
                      if msg._from in owner:
                          settings["changePictureProfile"] = True
                          client.sendMessage(to, "Please send us pictures.")

            if msg.contentType == 1:
                 
                   if settings["changePictureProfile"] == True:
                     path1 = client.downloadObjectMsg(msg_id)                     
                     settings["changePictureProfile"] = False
                     client.updateProfilePicture(path1)
                     client.sendMessage(msg.to, "done")

            if msg.toType == 2:
              if msg._from in admin:
                  if to in settings["changeGroupPicture"]:
                     path = client.downloadObjectMsg(msg_id)
                     settings["changeGroupPicture"].remove(to)
                     client.updateGroupPicture(to, path)
                     client.sendMessage(to, "เปลี่ยนรูปโปรไฟล์กลุ่มเรียบร้อยแล้ว.")
    except TalkException as talk_error:
        print(talk_error)
        #if talk_error.code in [7, 8, 20]:
        #    sys.exit(1)
        e = traceback.format_exc()
        print(e)
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as error:
        e = traceback.format_exc()
        print(e)

def mainkick(op):
    try:
        if op.type == 5:
            if RXProtect["autoBlock"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    runautoblock = mp.Process(target=client.sendMessage(op.param1,str(settings["message"])+client.getContact(clientMID).displayName))

#==============================================================================================================
#==============================================[OP TYPE 22 24 JOIN]============================================
#==============================================================================================================
                                                                                         
                
        
 
        if op.type == 130: 
            if op.param1 in welcomegroup:
                try:
                    contact = client.getContact(op.param2)
                    group = client.getGroup(op.param1)
                    sMsg = optypesg["welcomeMessage"]
                    sMsg = sMsg.replace("{name}",contact.displayName)
                    sMsg = sMsg.replace("{group}",group.name)
                    client.sendMessage(op.param1, sMsg)
#=====================================================ADD PIC AND CONTACT DOWN [REVISION BY HUUMEAW]====================================================
                    client.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/"+client.getContact(op.param2).pictureStatus) #รูปโปร
                 #   client.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + client.getGroup(op.param1).pictureStatus) #รูปกลุ่ม										
                   # client.sendContact(op.param1,op.param2) # คอทแทค
#=====================================================ADD PIC AND CONTACT UP==========================================================================                      
                except:pass
        if op.type == 15:
            if op.param1 in leavegroup:
                try:
                    contact = client.getContact(op.param2)
                    group = client.getGroup(op.param1)
                    sMsg = optypesg["leaveMessage"]
                    sMsg = sMsg.replace("{name}",contact.displayName)
                    sMsg = sMsg.replace("{group}",group.name)
                    client.sendMessage(op.param1, sMsg)
#=====================================================ADD PIC AND CONTACT DOWN [REVISION BY HUUMEAW]==========================================================================
                    client.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/"+client.getContact(op.param2).pictureStatus)
                    client.sendContact(op.param1,op.param2)
#=====================================================ADD PIC AND CONTACT DOWN==========================================================================  
                except:pass   

        
 
        if op.type == 26:
            if op.message != None and op.message.text != None:
                msg      = op.message
                text     = msg.text
                msg_id   = msg.id
                to       = msg.to
                sender   = msg._from
                if msg.contentType == 0:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = client.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = client.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = client.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.client.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = client.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 25 or op.type == 26:
           
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            #setup_admin(msg.to)
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = client.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n--- ข้อมูลสติ๊กเกอร์ ---"
                   ret_ += "\n- รหัสสติ๊กเกอร์ : {}".format(stk_id)
                   ret_ += "\n- เวอร์ชั่นสติกเกอร์ : {}".format(stk_ver)
                   ret_ += "\n- แพคเกจสติกเกอร์ : {}".format(pkg_id)
                   ret_ += "\n- ᴜʀʟ สติ๊กเกอร์ : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = client.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = client.getGroup(at)
                                arifAR = client.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "--- ภาพถูกลบ ---\n- ผู้ส่ง : "
                                ret_ = "- ชื่อกลุ่ม : {}".format(str(ginfo.name))
                                ret_ += "\n- เวลาส่ง : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(arifAR.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':arifAR.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                client.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                client.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = client.getGroup(at)
                                arifAR = client.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "--- ข้อความถูกลบ ---\n"
                                ret_ += "- ผู้ส่ง : {}".format(str(arifAR.displayName))
                                ret_ += "\n- ชื่อกลุ่ม : {}".format(str(ginfo.name))
                                ret_ += "\n- เวลาส่ง : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n- ข้อความที่ลบ : {}".format(str(msg_dict[msg_id]["text"]))
                                client.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 65:
            if settings["unsendMessage"] == True:
                at = op.param1
                msg_id = op.param2
                if msg_id in msg_dict:
                    ah = time.time()
                    ikkeh = client.getContact(msg_dict[msg_id]["from"])
                    if "text" in msg_dict[msg_id]:
                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                        waktumsg = format_timespan(waktumsg)
                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                        rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                        client.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                        del msg_dict[msg_id]
                    else:
                        if "image" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nImage :\nBelow"
                            client.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                            client.sendImage(at, msg_dict[msg_id]["image"])
                            del msg_dict[msg_id]
                        else:
                            if "video" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nVideo :\nBelow"
                                client.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                client.sendVideo(at, msg_dict[msg_id]["video"])
                                del msg_dict[msg_id]
                            else:
                                if "audio" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nAudio :\nBelow"
                                    client.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                    client.sendAudio(at, msg_dict[msg_id]["audio"])
                                    del msg_dict[msg_id]
                                else:
                                    if "sticker" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nSticker :\nBelow"
                                        client.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                        client.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "mid" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nContact :\nBelow"
                                            client.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                            client.sendContact(at, msg_dict[msg_id]["mid"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "location" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nLocation :\nBelow"
                                                client.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                                client.sendLocation(at, msg_dict[msg_id]["location"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "file" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nFile :\nBelow"
                                                    client.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                                    client.sendFile(at, msg_dict[msg_id]["file"])
                                                    del msg_dict[msg_id]
        if op.type == 13:
            if client in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin[op.param1] and op.param2 not in staff:
                        client.acceptGroupInvitation(op.param1)
                        ginfo = client.getGroup(op.param1)
                    else:
                        client.acceptGroupInvitation(op.param1)
                        ginfo = client.getGroup(op.param1)
        if op.type == 55:
            try:
                if RXCctv['cyduk'][op.param1]==True:
                    if op.param1 in RXCctv['point']:
                        Name = client.getContact(op.param2).displayName
                        if not Name in RXCctv['sidermem'][op.param1]:
                            tt = Name
                            RXCctv['sidermem'][op.param1] += "\n-" + Name
                            client.sendMentionV2(op.param1, "@!\n🥰สวัสดีสายแอบ🥰", [op.param2])
            except:pass
    except Exception:
        e = traceback.format_exc()
        print(e)
        pass

    except TalkException as talk_error:
        print(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
    except:
        e = traceback.format_exc()
        print(e)

def nameUpdate():
    while True:
        try:
            if times["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"{%H:%M}")
                client.updateProfileAttribute(2,times["name"] + "" + nowT)
            time.sleep(90)
        except Exception as e:
            print(e)
            exit()
threading.Thread(target=nameUpdate).start()
def run():
    while True:
        try:
            ops = kickPoll.singleTrace(count=100)
            if ops != None:
                for op in ops:
                   kickBot(op)
                   mainkick(op)
#                   print(op)
                   kickPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()
