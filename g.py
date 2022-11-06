print (""" 
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ ✪ PC Windows + IOS IPAD + CHOME OS + WIN10
┃ ✪ ผู้สร้าง :: เหี้ยซี 2020 ( 🄿🅁🄾 🄹🄴🄲🅃  )
┃ ✪ เวอร์ชั่น :: 10.0.0.0
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
from teambotgolf import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,subprocess,unicodedata
import subprocess, youtube_dl, humanize, traceback,asyncio
#from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
import multiprocessing as mp
from threading import Thread
_session = requests.session()
loop = asyncio.get_event_loop()

botStart = time.time()

golfbots = LINE("kjpous1140@detectu.com","zzpy8888")
#Channel(golfbots, "1602687308").getChannelResult().channelAccessToken
print("𝙻𝙾𝙶𝙸𝙽 𝙳𝙸𝙽𝙴 𝙱𝙾𝚃-𝚆𝙴𝙻𝙲𝙾𝙼𝙴")
#subprocess.Popen(["python3","kickgodFull2.py"])
golfbotsMID = golfbots.getProfile().mid

bot1 = golfbots.getProfile().mid

bot1 = golfbots.getProfile().mid

kickPoll = OEPoll(golfbots)
set={"gn":{},"gp":{},"iv":{}}
Rfu = [golfbotsMID]
Kicker = [golfbotsMID]
Exc = [golfbots]
Ton = [golfbots] 
Jsz = [golfbots]
Exc1 = [golfbots]
#=========
mainbots=Rfu+Jsz
mainbot=Exc+Jsz

#=========
#golfbots.sendMessage("u6f025bd9de0aa95cf8009edb8c9a3761", str(golfbots.authToken))
RfuBot= [golfbotsMID]

#=====================Add open admin ===================

#=====================Add open admin ===================
Family = ["ua435d92651ba9df05ad290b8df2dc72f","u12509f760e136b221ca8f8cbad512ccd","u62cd1850f9001ef6c6c2fe0bb6d88609"]
admin=["ua435d92651ba9df05ad290b8df2dc72f","u12509f760e136b221ca8f8cbad512ccd","u62cd1850f9001ef6c6c2fe0bb6d88609"] 
creator = ["ua435d92651ba9df05ad290b8df2dc72f","u12509f760e136b221ca8f8cbad512ccd","u62cd1850f9001ef6c6c2fe0bb6d88609"]
owner = ["ua435d92651ba9df05ad290b8df2dc72f","u12509f760e136b221ca8f8cbad512ccd","u62cd1850f9001ef6c6c2fe0bb6d88609"]
staff = ["ua435d92651ba9df05ad290b8df2dc72f","u12509f760e136b221ca8f8cbad512ccd","u62cd1850f9001ef6c6c2fe0bb6d88609"]
Bots = [golfbotsMID]
for id in admin:
    if id not in golfbots.getAllContactIds():
        golfbots.findAndAddContactsByMid(id)
        print("[●] ADD ADMIN CONTACT")
    else:
        print("[■] ADD CONTACT ADMIN SUCCESS !")
#=========================================

#=========================================
Saints = admin + staff
RfuFamily = RfuBot + Family + admin + creator + owner + staff
#===============Add adminbots =========================
for x in Bots:
    admin.append(x)
    print(f"bots add {x}")
#===============Add adminbots =========================

    
#===================================ADD WELCOME=========================
optypesg = {"welcomeMessage":"สวัสดีคุณ  🎎 {name} \nยินดีตอนรับเข้าสู่กลุ่ม \n 👉 {group} 👈 กรุณาตั้งข้อความก่อน","leaveMessage":"คุณ {name} ได้ออกจากกลุ่ม {group} \n🤦 อ้าวไปแล้วหรอ น่าเสียดาย พลาดโอกาสดีๆ ซะแล้ว 😅 ไว้เจอกันใหม่นะ 🌠"}
#===================================ADD WELCOME=========================
settings={"unsendMessage":False}
RfuCctv={"cyduk":{},"point":{},"sidermem":{}}
protectqr = []
protectkick = []
protecARoin = []
protectinvite = []
protectcancel = []
protectcanceljs = []
protectantijs = []
ghost = []
poradmin = []
#===========add welcome========
welcomegroup = []
leavegroup = []
#===========add welcome========
autocancel = {}
autoleaveroom = []
targets = []
tmsg_dict = {}
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
with open('server.json', 'r') as fp:
    server = json.load(fp)
for x in server['admin']:
    admin.append(x)
    print(f"admin add {x}")
with open('server2.json', 'r') as fp:
    server2 = json.load(fp)
for x in server2['staff']:
    staff.append(x)
    print(f"staff add {x}")
#==================Open admin up ===============	 
readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen)
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

settings = {
    "lang":"JP",
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "dblack": False,
    "wblack": False,
    "unsendMessage": False,
    "invite": {},
    "winvite": False,
    "block":{},
    "autoJoin": True,
    "changePictureProfile": False,
    "message": """ ระบบ🎀 Auto Block 🎀
   𝐓𝐄𝐀𝐌 𝐁𝐎𝐓 𝐏𝐘𝐓𝐇𝐎𝐍 𝐓𝐇
  
https://line.me/ti/p/~zzpy222

ɃØ₮™₮₳₲ €ĦƗ₦ØɃƗ
	""",
    "autoBlock": True,
    "changeGroupPicture": [],
}

RfuProtect = {
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

user1 = golfbotsMID
user2 = ""

mulai = time.time()

name = golfbots.getProfile()
name.displayName = "บอทไดโนเสาร์ของหนุเเมว"
golfbots.updateProfile(name)


status = golfbots.getProfile()
status.statusMessage = "🦖บอทแทคไดโนเสาร์ของหนูแมว🦖"
golfbots.updateProfile(status)


#===============================Def Backup down ===============
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = golfbots.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

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

def logError(text):
    golfbots.log("[ERROR] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendflex(to, data): 
    ratedit = LiffChatContext(to)
    ratedit1 = LiffContext(chat=ratedit)
    view = LiffViewRequest('1643771679-3LNK0BXL', ratedit1)
    token = golfbots.liff.issueLiffView(view)
    api_url = 'https://api.golfbots.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(api_url, headers=headers, data=json.dumps(data))
    

def helpbot():
      helpMessage1 = """┏━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃          คำสั่งบอทแทค/kg
┃🇬🇪 !profile (อัพรูป)
┃🐰 addadmin @
┃😸 deladmin @
┃👽 checkadmin (แอดมิน)
┃🤓 conadmin (แอดมิน)
┃👻 /k @ = สั่งบอทเตะ
┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┃          🇬🇪คำสั่งblacklist🇬🇪
┗━━━━━━━━━━━━━━━━━━━━━━━━━━
┃👹 ʙᴀɴ @ (แทคสมาชิก)
┃🙄 ᴜɴʙᴀɴ @ (แทคสมาชิก)
┃🇦🇹 ʙᴀɴ  (ส่งคท)
┃🇬🇪 ᴜɴʙᴀɴ (ส่งคท)
┃🇵🇫 ᴄʙ 
┃🇹🇭 ʙᴄ
┃🇳🇪 ʙᴀɴʟɪsᴛ
┃🇭🇷 ᴋɪʟʟʙᴀɴ
┃🇬🇪.ล้างหมด (ล้างดำทั้งหมด)
┃🇬🇪.เชคดำ (เชครายชื่อคนติดดำ)
┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┃          🇬🇪คำสั่งprotect🇬🇪
┗━━━━━━━━━━━━━━━━━━━━━━━━━━
┃กันเตะเปิด/ปิด (กันเตะ)
┃กันเชิญเปิด/ปิด (กันเชิญ)
┃กันลิ้งเปิด/ปิด (กันลิ้ง)
┃กันลิ้งเปิด/ปิด (กันเข้า)
┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┃          🇬🇪คำสั่งadminbot🇬🇪
┗━━━━━━━━━━━━━━━━━━━━━━━━━━
┃🇧🇮 bc: (ข้อความ)   
┃🇨🇦 เช็ค (เช็คสถานะบอท)
┃🇨🇭 ตั้งต้อนรับ:  ( ใส่ข้อความ )
┃🇫🇮 ตั้งออก:  ( ใสข้อความ )
┃🇩🇰 เชคต้อนรับ
┃🇬🇶 เชคออก
┃🆕 helpเข้า & helpออก
┃🔝 ต้อนรับ เปิด /  ต้อนรับ ปิด
┃🆗 ทักออก เปิด /  ทักออก ปิด
┃🔛 เลขา
┃🆕 แทค
┃🆖 ปิดลิ้ง
┃🆙 เปิดลิ้ง
┃🔄 ลิ้ง
┃🔚 เปิดเสือก/ปิดเสือก
┃🔜 cancel (ยกเชิญ
┃🚾 อัพ (ลบแชท)
┃🆔 บอทออก
┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┃    「 ติดต่อผู้สร้างระบบ 」
┃━━━━━━━━━━━━━━━━━━━━━━━━━━
┃🇬🇪🅃🄴🄰🄼 🄱🄾🅃 🄿🅈🅃🄷🄾🄽🇬🇪
┗━━━━━━━━━━━━━━━━━━━━━━━━━━"""
      return helpMessage1  

      return myHelp
def mentionMembers(to, mids=[]):
    if golfbots in mids: mids.remove(golfbots)
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
            golfbots.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
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


def kickBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoBlock"] == True:
                runautoblock = mp.Process(target=golfbots.sendMessage(op.param1,str(settings["message"])+golfbots.getContact(golfbotsMID).displayName))
                runautoblock = mp.Process(target=golfbots.findAndAddContactsByMid(op.param1))
                runautoblock.start()

        if op.type == 122:
            if op.param1 in protect["url"]["id"]:
                if op.param2 not in admin:
                    if op.param2 not in settings["blacklist"]:
                        settings["blacklist"][op.param2] = True
                    golfbots.kickoutFromGroup(op.param1,[op.param2])
                    G = golfbots.getGroup(op.param1)
                    if G.preventedJoinByTicket == True:
                        G.prevntedJoinByTicket = False
                        golfbots.updateGroup(G)
                    else:
                        if G.preventedJoinByTicket == False:
                            G.preventedJoinByTicket = True
                            golfbots.updateGroup(G)
                    
        if op.type == 124:
            if golfbotsMID in op.param3:
               # if op.param2 in admin:
                    golfbots.acceptGroupInvitation(op.param1)
                    time.sleep(0.4)
                    golfbots.sendMessage(msg.to, "cancel")
                    
            if op.param1 in protect["inv"]["id"]:
                if op.param2 not in admin or op.param3 not in admin:
                    if op.param2 not in settings["blacklist"]:
                        settings["blacklist"][op.param2] = True
                    if op.param3 not in settings["blacklist"]:
                        settings["blacklist"][op.param3] = True
                    golfbots.cancelGroupInvitation(op.param1,[op.param3])
                    golfbots.kickoutFromGroup(op.param1,[op.param2])

        if op.type == 130:
            if op.param1 in protect["join"]["id"]:
                if op.param2 not in admin:
                    if op.param2 not in settings["blacklist"]:
                        settings["blacklist"][op.param2] = True
                    golfbots.kickoutFromGroup(op.param1,[op.param2])
                    G = golfbots.getGroup(op.param1)
                    if G.preventedJoinByTicket != True:
                        G.prevntedJoinByTicket = True
                        golfbots.updateGroup(G)

        if op.type == 133:
            if op.param1 in protect["kick"]["id"]:
                if op.param2 not in admin:
                    if op.param2 not in settings["blacklist"]:
                        settings["blacklist"][op.param2] = True
                    golfbots.kickoutFromGroup(op.param1,[op.param2])

            if op.param3 in admin:
                if op.param2 not in settings["blacklist"]:
                    settings["blacklist"][op.param2] = True
                golfbots.kickoutFromGroup(op.param1,[op.param2])
                golfbots.inviteIntoGroup(op.param1,[op.param3])
            if op.param3 in golfbots.profile.mid:
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
                        golfbots.sendMessage(msg.to, "เพิ่มบัญชีนี้ในรายการblacklistเรียบร้อยแล้ว.")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        golfbots.sendMessage(msg.to, "เพิ่มบัญชีนี้ในรายการblacklistเรียบร้อยแล้ว.")
               if settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        golfbots.sendMessage(msg.to, "ลบบัญชีนี้ในรายการblacklistเรียบร้อยแล้ว.")
                        settings["dblacklist"] = False
                   else:
                        settings["dblacklist"] = False
                        golfbots.sendMessage(msg.to, "ลบบัญชีนี้ในรายการblacklistเรียบร้อยแล้ว.")
                        
      #      if msg.contentType == 13:                        
          #      if msg.toType == 2:        
               #     if msg._from in creator:							
              #          if wait["contactadmin"] == True:
                  #          target = msg.contentMetadata["mid"]      
                     #       try:
                   #             Owner['admin'][msg.to] = target
                          #      backupData()
                       #         wait["contactadmin"] = False
                            #    golfbots.sendMessage(to,"เพิ่มสิทธิ์ เป็นแอดมินหลัก เรียบร้อย\n\n คำสั่งของคุณพิม  help admin")
                           # except Exception as error:
                               # logError(error) 
                                
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
          #  txt      = text.lower()
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != golfbots.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                teambotgolfs = msg.text.lower().split(" && ")
                for teambotgolf in teambotgolfs:
                    if teambotgolf == "/g help" or teambotgolf == "/x help":
                        if msg._from in admin:
                            helpMessage1 = helpMessage()
                            runhelp = mp.Process(target=golfbots.sendMessage(to, str(helpMessage1)))
                            runhelp.start()           
                    elif msg.text.startswith('k exec ') or msg.text.startswith('l exec '):
                      if msg._from in admin:
                        try:
                            result = msg.text.replace('g exec ', '') or msg.text.replace('x exec ', '')
                            exec(result)
                        except Exception as error:
                            golfbots.sendMessage(to, '{}'.format(error))
#==========================
#==========================
                    elif teambotgolf == 'kg' or teambotgolf == 'kg':
                        if msg._from in admin:	
                           helpMessage1 = helpbot()
                           golfbots.sendMessage(msg.to, str(helpMessage1))
#==========================                       
#==========================
#==========================       
                    elif msg.text.lower().startswith("/getflex"):
                        aa = msg.text.replace(msg.text.split(' ')[0] + ' ','')
                        x = golfbots.talk.getRecentMessagesV2(to, int(aa))
                        for msg in x:
#                            print(msg)
                            if msg._from != golfbots.profile.mid:
                                if 'FLEX_JSON' in msg.contentMetadata:
                                    true = True
#                                    print(msg)
                                    data = msg.contentMetadata['FLEX_JSON']
                                    try:
                                        exec("sendTemplate(to,{'type': 'flex','altText': 'STEAL','contents': " + msg.contentMetadata['FLEX_JSON'] + "})")
                                        golfbots.sendMessage(to,str(data))
                                        time.sleep(0.9)
                                    except Exeception as e:
                                        golfbots.sendMessage(to,str(e))
                    elif msg.text.lower().startswith("cancelchat"):
                        try:
                            num = msg.text.replace(msg.text.split(' ')[0] + ' ','')
                            mesr = int(str(num))
                            M = golfbots.talk.getRecentMessagesV2(to, int(mesr))
                            MId = []
                            if mesr <= 1000:
                                for ind,i in enumerate(M):
                                    if ind == 0:
                                        pass
                                    else:
                                        if i._from == golfbots.profile.mid:
                                           MId.append(i.id)
                                           if len(MId) == mesr:
                                            break
                                for idmes in MId:
                                    golfbots.unsendMessage(idmes)
                                    continue
                                golfbots.sendMessage(to, "ยกเลิกข้อความ {} ข้อความเรียบร้อย!" .format(len(MId)))
                            else:
                                golfbots.sendMessage(to, "ไม่สามารถยกเลิกข้อความได้เกิน 1000 ข้อความ")
                        except Exception as e:
                            golfbots.sendMessage(to,str(e))
                    elif msg.text.lower() == "กันเตะเปิด":
                        if msg._from in admin:
                            if to in protect["kick"]["id"]:
                                golfbots.sendMessage(to,"Protection Kick is already Enable")
                            else:
                                protect["kick"]["id"][to] = True
                                golfbots.sendMessage(to,"Protection Kick is Enable")
                    elif msg.text.lower() == "กันเตะปิด":
                        if msg._from in admin:
                            if to in protect["kick"]["id"]:
                                del protect["kick"]["id"][to]
                                golfbots.sendMessage(to,"Protection Kick is Disable")
                            else:
                                golfbots.sendMessage(to,"Protection Kick is already Disable")
                    elif msg.text.lower() == "กันเชิญเปิด":
                        if msg._from in admin:
                            if to in protect["inv"]["id"]:
                                golfbots.sendMessage(to,"Protection Invite is already Enable")
                            else:
                                protect["inv"]["id"][to] = True
                                golfbots.sendMessage(to,"Protection Invite is Enable")
                    elif msg.text.lower() == "กันเชิญปิด":
                        if msg._from in admin:
                            if to in protect["inv"]["id"]:
                                del protect["inv"]["id"][to]
                                golfbots.sendMessage(to,"Protection Invite is Disable")
                            else:
                                golfbots.sendMessage(to,"Protection Kick is already Disable")
                    elif msg.text.lower() == "pj on":
                        if msg._from in admin:
                            if to in protect["join"]["id"]:
                                golfbots.sendMessage(to,"Protection Join is already Enable")
                            else:
                                protect["join"]["id"][to] = True
                                golfbots.sendMessage(to,"Protection Join is Enable")
                    elif msg.text.lower() == "pj off":
                        if msg._from in admin:
                            if to in protect["join"]["id"]:
                                del protect["join"]["id"][to]
                                golfbots.sendMessage(to,"Protection Join is Disable")
                            else:
                                golfbots.sendMessage(to,"Protection Join is already Disable")
                    elif msg.text.lower() == "กันลิ้งเปิด":
                        if msg._from in admin:
                            if to in protect["url"]["id"]:
                                golfbots.sendMessage(to,"Protection URL is already Enable")
                            else:
                                protect["url"]["id"][to] = True
                                golfbots.sendMessage(to,"Protection URL is Enable")
                    elif msg.text.lower() == "กันลิ้งปิด":
                        if msg._from in admin:
                            if to in protect["url"]["id"]:
                                del protect["url"]["id"][to]
                                golfbots.sendMessage(to,"Protection URL is Disable")
                            else:
                                golfbots.sendMessage(to,"Protection URL is already Disable")
                    elif teambotgolf == "Ree" or teambotgolf == "t ree":
                      if msg._from in admin:
                          golfbots.sendMessage(msg.to,  "กำลังรีบอท")
                          time.sleep(5)
                          golfbots.sendMessage(msg.to,  "รีเสร็จสิ้น")
                          restartBot()       
                          
                    elif teambotgolf == "restart" or teambotgolf == "t restart":
                      if msg._from in admin:
                          golfbots.sendMessage(to, "รีเซ็ตบอทเรียบร้อยแล้ว.")
                          python = sys.executable
                          os.execl(python, python, *sys.argv)                          

                    elif teambotgolf == "group:save" or teambotgolf == "t group:save":
                        if msg._from in admin:
                            try:
                               gid = golfbots.getGroup(to)
                               set["gn"] = str(gid.name)
                               set["gp"] = "http://dl.profile.line-cdn.net/" + str(gid.pictureStatus)
                               set["iv"] = [mem.mid if mem.mid != golfbots.profile.mid else '' for mem in gid.members]
                               golfbots.sendReplyMessage(msg.id, to,set["gn"])
                               golfbots.sendImageWithURL(to,set["gp"])
                            except Exception as e: traceback.print_exc()
                    elif teambotgolf == "group:back" or teambotgolf == "t group:back":
                      if msg._from in admin:
                          try:
                              gp = golfbots.getGroup(msg.to)
                              gp.name = set["gn"]
                              runsavegroup = mp.Process(target=golfbots.updateGroup(gp))
                              set["cgp"] = True
                              runsavegroup = mp.Process(target=golfbots.sendMessage(to,"change pictgroup"))
                              runsavegroup = mp.Process(target=golfbots.sendImageWithURL(to,set["gp"]))
                              runsavegroup = mp.Process(target=golfbots.inviteIntoGroup(to,set["iv"]))
                              runsavegroup.start()
                          except Exception as e: traceback.print_exc()
                    elif teambotgolf == "respon" or teambotgolf == "เลขา":
                      if msg._from in admin:
                            runrespon = mp.Process(target=golfbots.sendMentionV2(to, 'ฉันยังทำงานอยู่ปกติค่ะ @!',[sender]))
                            runrespon.start()
                    elif teambotgolf == "ระบบป้องกัน" or teambotgolf == "ระบบ":
                      if msg._from in admin:
                            runrespon = mp.Process(target=golfbots.sendMentionV2(to, 'ระบบงานควบคู่กับบอทป้องกันชุด2นะคะ กรุณาดึงบอทป้องกันเข้าด้วยนะคะเพื่อให้ฉันทำงานเต็มที่ ระบบที่เชื่อมต่อ เซิฟเวอร์ VPS เวอร์ชั่น 10.0.0.0 หากมีปัญญาปรึกษาผู้สร้างของฉันได้ที่ ID zzpy123',[sender]))
                            runrespon.start()
                    elif msg.text.lower().startswith("bc:"):
                      if msg._from in admin:
                                    bctxt = msg.text[len("bc:"):].strip()
                                    a = golfbots.getGroupIdsJoined()
                                    for manusia in a:
                                        gname = golfbots.getGroup(manusia).name
                                        golfbots.sendMessage(manusia,"ขออนุญาติแอดมินกลุ่ม "+gname+"\n\n"+ (bctxt))
                                    golfbots.sendMessage(receiver,"ส่งครบทุกกลุ่มแล้ว")
#=================================x setting down ========================== 
                    elif teambotgolf == 'เช็ค' or teambotgolf == 'set':
                        if msg._from in admin:
                           ret_ = "🇹🇭==[ เช็คต้อนรับว่าเปิดรึปิด ]==🇹🇭"                                                       
                           if msg.to in welcomegroup: ret_ += "\n\n🇹🇭 welcomegroup: On 【✔】"
                           else: ret_ += "\n\n🇹🇭 welcomegroup: Off 【🚫】"      
                           if msg.to in leavegroup: ret_ += "\n\n🇹🇭 leavegroup: On 【✔】"
                           else: ret_ += "\n\n🇹🇭 leavegroup: Off 【🚫】"                                                       
                           random.choice(Ton).sendMessage(to,str(ret_))
#=================================x setting up  ===========================           

                    elif teambotgolf == "speed" or teambotgolf == "สปีด":
                      if msg._from in admin:
                          def speedbot():
                              start = time.time()
                              runspeed = mp.Process(target=golfbots.getProfile())
                              elapse = time.time() - start
                              runspeed = mp.Process(target=golfbots.sendMessage(to, '%s' % str(elapse/100)))
                          speedbot = threading.Thread(target=speedbot)
                          speedbot.daemon = True
                          speedbot.start()

#===================================================== A D D Leaveall Down ===============================================================================	
                    elif teambotgolf == 'leaveall' or teambotgolf == 'บอทออก':
                        if msg._from in admin:
                            try:
                                for x in Exc1:
                                    x.leaveGroup(to)
                                golfbots.sendMessage(to, "ต้องการใช้บอทติดต่อ \n http://golfbots.me/ti/p/~noppakun_20")                                            
                            except:golfbots.sendMessage(to,"kicker ไม่ได้อยู่ในกลุ่ม")		
#===================================================== A D D Leaveall up ===============================================================================	                        

                    elif teambotgolf == "ดำ" or teambotgolf == "blacklist":
                      if msg._from in admin: 
                        settings["wblacklist"] = True
                        golfbots.sendMessage(to, "• กรุณาส่ง Contact •")
                    elif teambotgolf == "ล้างหมด" or teambotgolf == ".ลบดำ":
                      if msg._from in admin: 
                        settings["dblacklist"] = True
                        golfbots.sendMessage(to, "• กรุณาส่ง Contact •")
                    elif teambotgolf == "unbanall" or teambotgolf == ".ล้างหมด":
                      if msg._from in admin: 
                        settings["blacklist"] = {}
                        golfbots.sendMessage(to, "ล้างบัญชีblacklistเรียบร้อยแล้วค่ะ")
                    elif teambotgolf == "cb" or teambotgolf == "t cb":
                      if msg._from in admin:
                          if msg.toType == 2:
                               _name = msg.text.replace("cb","") or msg.text.replace("t cb","")
                               gs = golfbots.getGroup(msg.to)
                               golfbots.sendMessage(msg.to,"blacklistสมาชิกทุกคนในห้องนี้แล้วค่ะ.")
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                        targets.append(g.mid)
                               if targets == []:
                                    golfbots.sendMessage(msg.to,"เกิดข้อผิดพลาด")
                               else:
                                   for target in targets:
                                       if not target in Family:
                                           try:
                                               settings["blacklist"][target] = True
                                               f=codecs.open('st2__b.json','w','utf-8')
                                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                           except:
                                               golfbots.sentMessage(msg.to,"พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")
#===================Edit ban up ===============   
              #      elif teambotgolf.startswith("add1 ") or teambotgolf.startswith("t add1 "):
             #         if msg._from in creator:
                    #       targets = []
         #                  key = eval(msg.contentMetadata["MENTION"])
                #           key["MENTIONEES"] [0] ["M"]
            #               for x in key["MENTIONEES"]:
                #               targets.append(x["M"])
                 #          for target in targets:
                 #              if target not in Family:							   
                     #              try:
                        #               Owner['admin'][msg.to] = target
                             #          backupData()
                             #          random.choice(Ton).sendMessage(to, "เพิ่มสิทธิ์ เป็นแอดมินหลัก เรียบร้อย\n\n คำสั่งของคุณพิม help")
                                 #  except:
                                    #   random.choice(Ton).sendMessage(to, "ไม่พบรายชื่อติดต่อ.")

                    elif teambotgolf.startswith("ดำ ") or teambotgolf.startswith("blacklist "):
                      if msg._from in admin:
                           targets = []
                           key = eval(msg.contentMetadata["MENTION"])
                           key["MENTIONEES"] [0] ["M"]
                           for x in key["MENTIONEES"]:
                               targets.append(x["M"])
                           for target in targets:
                               if target not in RfuFamily:							   
                                   try:
                                       settings["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       golfbots.sendMessage(to, "เพิ่ม {} ในรายการblacklistเรียบร้อยแล้วค่ะ.".format(golfbots.getContact(target).displayName))
                                   except:
                                       golfbots.sendMessage(to, "ไม่พบรายชื่อติดต่อ.")
#===================Edit ban up ===============    
                    
                               
                    elif teambotgolf.startswith(".ลบดำ ") or teambotgolf.startswith("ล้างหมด "):
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
                                   golfbots.sendMessage(to, "ลบ {} ในรายการblacklistเรียบร้อยแล้วค่ะ.".format(golfbots.getContact(target).displayName))
                               except:
                                   golfbots.sendMessage(to, "ไม่พบรายชื่อติดต่อค่ะ.")
                    elif teambotgolf == "banlist" or teambotgolf == ".เชคดำ":
                      if msg._from in admin:
                        if settings["blacklist"] == {}:
                            golfbots.sendMessage(to, "ไม่พบบัญชีที่อยู่ในรายการblacklistค่ะ.")
                        else:
                            text = "บัญชีที่อยู่ในรายการblacklistค่ะ:"
                            for mi_d in settings["blacklist"]:
                                text += "\n- {}".format(golfbots.getContact(mi_d).displayName)
                            golfbots.sendMessage(to, str(text))
                    elif teambotgolf == "conban" or teambotgolf == ".คทดำ":
                      if msg._from in admin:
                        if settings["blacklist"] == {}:
                            golfbots.sendMessage(to, "ไม่พบบัญชีที่อยู่ในรายการblacklistค่ะ.")
                        else:
                            for mi_d in settings["blacklist"]:
                                golfbots.sendContact(to, mi_d)
                    elif teambotgolf == "kickban" or teambotgolf == "ส่งแขก":
                      if msg._from in admin:
                        if msg.toType == 2:
                             group = golfbots.getGroup(to)
                             gMembMids = [contact.mid for contact in group.members]
                             matched_list = []
                             for tag in settings["blacklist"]:
                                 matched_list+=[str for str in gMembMids if str == tag]
                             if matched_list == []:
                                 golfbots.sendMessage(to, "ไม่สามารถเตะblacklistออกกลุ่มได้ค่ะ เนื่องจากกลุ่มนี้ไม่พบบัญชีที่อยู่ในรายการblacklistนะคะ.")
                             else:
                                 for jj in matched_list:
                                     try:
                                         klist=[golfbots]
                                         kicker=random.choice(klist)
                                         runkickban = mp.Process(target=golfbots.kickoutFromGroup(to,[jj]))
                                         runkickban.start()
                                     except:
                                         pass
#===================Edit kick down ===============
                    elif teambotgolf.startswith("kick ") or teambotgolf.startswith("/k "):
                      if msg._from in admin:
                          targets = []
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                      for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                      for target in targets:					  
                            if target not in RfuFamily:					  					  
                                  klist=[golfbots]
                                  kicker=random.choice(klist)
                                  runkick = mp.Process(target=kicker.kickoutFromGroup(to,[target]))
                                  runkick.start()
#===================Edit kick up ===============             
                    elif teambotgolf == "cancel" or teambotgolf == "/cancel":
                      if msg._from in admin:
                          if msg.toType == 2:
                              group = golfbots.getGroup(receiver)
                              gMembMids = [contact.mid for contact in group.invitee]
                              k = len(gMembMids)//20
                              #golfbots.sendMessage(msg.to,"[ ยกค้างเชิญ {} ท่านครับ ] \n\nรอสักครู่...".format(str(len(gMembMids))))
                              num=1
                              for i in range(k+1):
                                  for j in gMembMids[i*20 : (i+1)*20]:
                                      time.sleep(random.uniform(0.5,0.4))
                                      golfbots.cancelGroupInvitation(msg.to,[j])
                                      print ("[จำนวน] "+str(num)+" => "+str(len(gMembMids))+" คนทั้งหมดหมด")
                                      num = num+1
                                  time.sleep(random.uniform(0.95,1))
                              golfbots.sendMessage(receiver,"cancelค้างเชิญ จำนวน {} คน เรียบร้อยแล้ว".format(str(len(gMembMids))))

#========================Welcome + leave Down ==========================
                    elif teambotgolf.startswith('ตั้งต้อนรับ:'):
                        if msg._from in admin:
                            text = msg.text.replace('ตั้งต้อนรับ: ',"")
                            optypesg["welcomeMessage"] = text
                            golfbots.sendMessage(msg.to, "Succeed")
                    elif teambotgolf.startswith('t welcome:add'):
                        if msg._from in admin:
                            text = msg.text.replace('t welcome:add ',"")
                            optypesg["welcomeMessage"] = text
                            golfbots.sendMessage(msg.to, "Succeed")
                    elif teambotgolf == 'เชคต้อนรับ' or teambotgolf == 't welcome:check':
                        if msg._from in admin:
                            golfbots.sendMessage(msg.to, "ข้อความตอนรับออกที่ตั้ง: "+str(optypesg["welcomeMessage"]))
                    elif teambotgolf.startswith('ตั้งออก'):
                        if msg._from in admin:
                            text = msg.text.replace('ตั้งออก ',"")
                            optypesg["leaveMessage"] = text
                            golfbots.sendMessage(msg.to, "Succeed")
                    elif teambotgolf.startswith('t leave:add'):
                        if msg._from in admin:
                            text = msg.text.replace('t leave:add ',"")
                            optypesg["leaveMessage"] = text
                            golfbots.sendMessage(msg.to, "Succeed")
                    elif teambotgolf == 'เชคออก' or teambotgolf == 't leave:check':
                        if msg._from in admin:
                            golfbots.sendMessage(msg.to, "ข้อความตอนรับเข้าที่ตั้ง: "+str(optypesg["leaveMessage"]))
                    elif teambotgolf == 'leave:help' or teambotgolf == 'helpออก':
                        if msg._from in admin:
                            text = "วิธีใช้งานคำสั่ง"
                            text += "\n- leave:add คุณ {name} ได้ออกจากกลุ่ม {group}"
                            text += "\n\n**หมายเหตุ"
                            text += "\n* {name} แสดงชื่อคนออกกลุ่ม"
                            text += "\n* {group} แสดงชื่อกลุ่มที่ออก"
                            golfbots.sendReplyMessage(msg_id, msg.to, text)
                    elif teambotgolf == 'welcome:help' or teambotgolf == 'helpเข้า':
                        if msg._from in admin:
                            text = "วิธีใช้งานคำสั่ง"
                            text += "\n- welcome:add สวัสดีคุณ {name} ยินดีตอนรับสู่ {group}"
                            text += "\n\n**หมายเหตุ"
                            text += "\n* {name} แสดงชื่อคนเข้ากลุ่ม"
                            text += "\n* {group} แสดงชื่อกลุ่มที่เข้า"
                            golfbots.sendReplyMessage(msg_id, msg.to, text)
                    elif teambotgolf.startswith('ต้อนรับ '):
                        if msg._from in admin:
                            spl = msg.text.replace('ต้อนรับ ','')
                            if spl == 'เปิด':
                                if msg.to in welcomegroup:
                                    msgs = "ตอนรับเข้าถูกเปิดใช้งานอยู่แล้ว"
                                else:
                                    welcomegroup[msg.to] = True
                                    f=codecs.open('welcomegroup.json','w','utf-8')
                                    json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                    msgs = "ตอนรับเข้าเปิดใช้งาน"
                                golfbots.sendMessage(msg.to, msgs)
                            elif spl == 'ปิด':
                                if msg.to in welcomegroup:
                                    del welcomegroup[msg.to]
                                    f=codecs.open('welcomegroup.json','w','utf-8')
                                    json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                                    msgs = "ตอนรับเข้าปิดใช้งาน"
                                else:
                                    msgs = "ตอนรับเข้าถูกปิดใช้งานอยู่แล้ว"
                                golfbots.sendMessage(msg.to, msgs)
                    elif teambotgolf.startswith('ทักออก '):
                        if msg._from in admin:
                            spl = msg.text.replace('ทักออก ','')
                            if spl == 'เปิด':
                                if msg.to in leavegroup:
                                    msgs = "ตอนรับออกถูกเปิดใช้งานอยู่แล้ว"
                                else:
                                    leavegroup[msg.to] = True
                                    f=codecs.open('leavegroup.json','w','utf-8')
                                    json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                    msgs = "ตอนรับออกเปิดใช้งาน"
                                golfbots.sendMessage(msg.to, msgs)
                            elif spl == 'ปิด':
                                if msg.to in leavegroup:
                                    del leavegroup[msg.to]
                                    f=codecs.open('leavegroup.json','w','utf-8')
                                    json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                                    msgs = "ตอนรับออกปิดใช้งาน"
                                else:
                                    msgs = "ตอนรับออกถูกปิดใช้งานอยู่แล้ว"
                                golfbots.sendMessage(msg.to, msgs)
                    elif teambotgolf.startswith('t welcome '):
                        if msg._from in admin:
                            spl = msg.text.replace('t welcome ','')
                            if spl == 'on':
                                if msg.to in welcomegroup:
                                    msgs = "ตอนรับเข้าถูกเปิดใช้งานอยู่แล้ว"
                                else:
                                    welcomegroup[msg.to] = True
                                    f=codecs.open('welcomegroup.json','w','utf-8')
                                    json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                    msgs = "ตอนรับเข้าเปิดใช้งาน"
                                golfbots.sendMessage(msg.to, msgs)
                            elif spl == 'off':
                                if msg.to in welcomegroup:
                                    del welcomegroup[msg.to]
                                    f=codecs.open('welcomegroup.json','w','utf-8')
                                    json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                                    msgs = "ตอนรับเข้าปิดใช้งาน"
                                else:
                                    msgs = "ตอนรับเข้าถูกปิดใช้งานอยู่แล้ว"
                                golfbots.sendMessage(msg.to, msgs)
                    elif teambotgolf.startswith('t leave '):
                        if msg._from in admin:
                            spl = msg.text.replace('t leave ','')
                            if spl == 'on':
                                if msg.to in leavegroup:
                                    msgs = "ตอนรับออกถูกเปิดใช้งานอยู่แล้ว"
                                else:
                                    leavegroup[msg.to] = True
                                    f=codecs.open('leavegroup.json','w','utf-8')
                                    json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                    msgs = "ตอนรับออกเปิดใช้งาน"
                                golfbots.sendMessage(msg.to, msgs)
                            elif spl == 'off':
                                if msg.to in leavegroup:
                                    del leavegroup[msg.to]
                                    f=codecs.open('leavegroup.json','w','utf-8')
                                    json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                                    msgs = "ตอนรับออกปิดใช้งาน"
                                else:
                                    msgs = "ตอนรับออกถูกปิดใช้งานอยู่แล้ว"
                                golfbots.sendMessage(msg.to, msgs)
                                
                                
#========================Welcome + leave Down ==========================	

#========================Add tagall down ===============================
                    elif teambotgolf == 'tagall' or teambotgolf == 'แทค':
                        members = []
                        if msg.toType == 1:
                            room = golfbots.getCompactRoom(to)
                            members = [mem.mid for mem in room.contacts]
                        elif msg.toType == 2:
                            group = golfbots.getCompactGroup(to)
                            members = [mem.mid for mem in group.members]
                        else:
                            return golfbots.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                        if members:
                            mentionMembers(to, members)
#========================Add tagall down ===============================   

#===============================Add admin down ===============
                    elif teambotgolf.startswith('addadmin ') or teambotgolf.startswith('t addadmin '):
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
                                    golfbots.sendMessage(to,"เพิ่มแอดมินเสร็จสิ้น \n คำสั่งของคุณคือ.  kg")
                                except:
                                    golfbots.sendMessage(msg.to, "เกิดข้อผิดพลาด")
                    elif teambotgolf.startswith('addstaff ') or teambotgolf.startswith('t addstaff '):
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
                                golfbots.sendMessage(to,"เพิ่มสตาฟเสร็จสิ้น")
                    elif teambotgolf.startswith('deladmin ') or teambotgolf.startswith('t deladmin '):
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
                                    golfbots.sendMessage(to,"ลบแอดมินเสร็จสิ้น")
                                except:
                                    golfbots.sendMessage(msg.to, "เกิดข้อผิดพลาด")
                    elif teambotgolf.startswith('delstaff ') or teambotgolf.startswith('t delstaff '):
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
                                golfbots.sendMessage(to,"ลบสตาฟเสร็จสิ้น")						
#===============================Add admin UP =============== 
                    elif teambotgolf == "/นับ":
                      if msg._from in admin:
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
                            golfbots.sendMessage(to, "✯͜͡❂ การอ่าน ถูกเปิดใช้งานแล้ว")
                        else:
                            try:
                                del read['readPoint'][to]
                                del read['readMember'][to]
                            except:
                                pass
                            read['readPoint'][to] = msg_id
                            read['readMember'][to] = []
                            golfbots.sendMessage(to, "✯͜͡❂ ตั้งจุดอ่าน : \n{}".format(readTime))

                    elif teambotgolf == "ปิดอ่าน":
                       if msg._from in admin:
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
                             golfbots.sendMessage(to,"✯͜͡❂ การอ่าน ถูกปิดการใช้งาน")
                         else:
                             try:
                                 del read['readPoint'][to]
                                 del read['readMember'][to]
                             except:
                                 pass
                             golfbots.sendMessage(to, "✯͜͡❂ ลบจุดอ่าน : \n{}".format(readTime))

                    elif teambotgolf == "อ่าน":
                       if msg._from in admin:
                         if to in read['readPoint']:
                             if read["readMember"][to] == []:
                                 return golfbots.sendMessage(to, "✯͜͡❂ ไม่มีคนอ่าน")
                             else:
                                 no = 0
                                 result = "╭───「 จำนวนคนอ่าน 」"
                                 for dataRead in read["readMember"][to]:
                                     no += 1
                                     result += "\n├ × {}. @!".format(str(no))
                                 result += "\n╰───「 ทั้งหมด {} คน 」".format(str(len(read["readMember"][to])))
                                 golfbots.sendMentionV2(to, result, read["readMember"][to])
                                 read['readMember'][to] = []
#===============================Check admin+staff down =========================
                    elif teambotgolf == 'checkadmin' or teambotgolf == 'แอดมิน':
                        if msg._from in admin:
                            text="🇹🇭===[ ʟɪsᴛ ᴀᴅᴍɪɴ ]===🇹🇭\n"
                            no=1
                            for x in admin:
                                text+=f"\n{no}. {golfbots.getContact(x).displayName}"
                                no=no+1
                            golfbots.sendMessage(to,str(text))
                    elif teambotgolf == 'checkstaff' or teambotgolf == 't checkstaff':
                        if msg._from in admin:
                            text="🇹🇭===[  ʟɪsᴛ sᴛᴀғғ  ]===🇹🇭\n"
                            no=1
                            for x in staff:
                                text+=f"\n{no}. {golfbots.getContact(x).displayName}"
                                no=no+1
                            golfbots.sendMessage(to,str(text))
                    elif teambotgolf == 'x conadmin' or teambotgolf == 'แอดมิน':
                        if msg._from in owner:
                            for x in admin:
                                golfbots.sendMessage(to, None, contentMetadata={'mid':x}, contentType=13)
                    elif teambotgolf == 'constaff' or teambotgolf == 't constaff':
                        if msg._from in admin:
                            for x in staff:
                                golfbots.sendMessage(to, None, contentMetadata={'mid':x}, contentType=13)
#===============================Check admin+staff down =========================  

#===========================ADD listprotect Down ======================================
#===========================ADD listprotect Up ======================================   
                    elif teambotgolf == 'runtime' or teambotgolf == 'ออน':
                        if msg._from in admin:
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = timeChange(runtime)
                            for x in mainbots:
                                x.sendMessage(to,str(runtime))
                                
                    elif msg.text in ["อัพ"]:							
                                    golfbots.sendMessage(msg.to,"ลบแชท เรียบร้อยแล้ว")
                                    golfbots.removeAllMessages(op.param2)
                    elif teambotgolf == 'remove:m' or teambotgolf == 't remove:m':
                        if msg._from in admin:
                            for x in mainbots:
                                x.removeAllMessages(op.param2) 
                            golfbots.sendMessage(to,"ลบทุกแชทบอทแล้ว")
#=============================URL Down ==============================================
                    elif teambotgolf == 'เปิดลิ้ง' or teambotgolf == 't url on':
                        if msg._from in owner:
                            group = golfbots.getGroup(to)
                            if group.preventedJoinByTicket == False:
                                golfbots.sendMessage(to,"ลิ้งเปิดอยู่แล้ว")
                            else:
                                group.preventedJoinByTicket = False
                                golfbots.updateGroup(group)
                            golfbots.sendMessage(to,"เปิดลิ้งแล้ว")
                    elif teambotgolf == 'ปิดลิ้ง' or teambotgolf == 't url off':
                        if msg._from in owner:
                            group = golfbots.getGroup(to)
                            if group.preventedJoinByTicket == True:
                                golfbots.sendMessage(to,"ลิ้งปิดอยู่แล้ว")
                            else:
                                group.preventedJoinByTicket = True
                                golfbots.updateGroup(group)
                            golfbots.sendMessage(to,"ปิดลิ้งแล้ว")							
                    elif teambotgolf == 'ลิ้ง' or teambotgolf == 't url':
                        if msg._from in owner:
                            group = golfbots.getGroup(to)
                            if group.preventedJoinByTicket == False:
                                ticket = golfbots.reissueGroupTicket(to)
                                golfbots.sendMessage(msg.to, "ลิ้งกลุ่มนี้:\nhttps://golfbots.me/R/ti/g/{}".format(str(ticket)))
                            else:
                                golfbots.sendMessage(to,"ยังไม่ได้เปิดลิ้งกลุ่มนี้")							
#=============================URL Down ==============================================                      
#=============================================================================ADD Protect1 ON/OFF DOWN==================
                    elif teambotgolf.startswith("wc ") or teambotgolf.startswith("t setup "):
                       if msg._from in admin:
                          spl = msg.text.replace('wc ','') or msg.text.replace('t setup ','')
                          if spl == 'on':						                                           
                              if msg.to in welcomegroup:
                                   msgs = "ตอนรับเข้าถูกเปิดใช้งานอยู่แล้ว"
                              else:
                                   welcomegroup[msg.to] = True
                                   f=codecs.open('welcomegroup.json','w','utf-8')
                                   json.dump(welcomegroup, f, sort_keys=True, indent=4,ensure_ascii=False)	
                                   ginfo = golfbots.getGroup(msg.to)                                  
                                   msgs = "ตอนรับเข้าเปิดใช้งาน : " +str(ginfo.name)
                              golfbots.sendMessage(msg.to, msgs)                                   
                                   
                              if msg.to in leavegroup:
                                   msgs = "ตอนรับออกถูกเปิดใช้งานอยู่แล้ว"
                              else:
                                   leavegroup[msg.to] = True
                                   f=codecs.open('leavegroup.json','w','utf-8')
                                   json.dump(leavegroup, f, sort_keys=True, indent=4,ensure_ascii=False)	
                                   ginfo = golfbots.getGroup(msg.to)    								   
                                   msgs = "ตอนรับออกเปิดใช้งาน : " +str(ginfo.name)
                              golfbots.sendMessage(msg.to, msgs)    


#=============================================================================ADD INSTALL ON/OFF DOWN======================================================================
                    #elif teambotgolf == 'x protect on' or teambotgolf == 'g protect on':
                        #if msg._from in admin:
                            #for p in ['protecturl','protectkick','protectjoin','protectcanceljs','protectcancel','protectinvite','js','ghost']:
                                #golfbots.sendMessage(to,'g '+str(p)+" on")
										
                    #elif teambotgolf == 'x protect off' or teambotgolf == 'g protect off':
                        #if msg._from in admin:
                            #for p in ['protecturl','protectkick','protectjoin','protectcanceljs','protectcancel','protectinvite','js','ghost']:
                                #golfbots.sendMessage(to,'g '+str(p)+" off")											
#=============================================================================ADD INSTALL ON/OFF UP========================================================================	  
                    elif teambotgolf == 'unsend on' or teambotgolf == '/เปิดจับยก':
                        if msg._from in admin:
                            settings["unsendMessage"] = True
                            golfbots.sendMessage(msg.to, "On:Succeed")
                    elif teambotgolf == 'unsend off' or teambotgolf == '/ปิดจับยก':
                        if msg._from in admin:
                            settings["unsendMessage"] = False
                            golfbots.sendMessage(msg.to, "Off:Succeed")
                    elif teambotgolf == 'เปิดเสือก' or teambotgolf == '/เปิดแอบ':
                        if msg._from in admin:
                            try:
                                del RfuCctv['point'][msg.to]
                                del RfuCctv['sidermem'][msg.to]
                                del RfuCctv['cyduk'][msg.to]
                            except:
                                pass
                            RfuCctv['point'][msg.to] = msg.id
                            RfuCctv['sidermem'][msg.to] = ""
                            RfuCctv['cyduk'][msg.to]=True
                            golfbots.sendReplyMessage(msg.id, msg.to, "เปิดระบบแสกนคนอ่านอัตโนมัติ")
                    elif teambotgolf == 'ปิดเสือก' or teambotgolf == '/ปิดแอบ':
                        if msg._from in admin:
                            if msg.to in RfuCctv['point']:
                                RfuCctv['cyduk'][msg.to]=False
                                golfbots.sendReplyMessage(msg.id, msg.to, "ปิดระบบแสกนคนอ่านแล้ว")
                            else:
                                random.choice(Ton).sendReplyMessage(msg.id, msg.to, "ปิดระบบแสกนคนอ่านแล้ว")
               
                    elif teambotgolf == "add on" or teambotgolf == "t add on":
                      if msg._from in admin:
                          settings["contactadmin"] = True
                          random.choice(Ton).sendMessage(to, "ส่ง ᴄᴏɴᴛᴀᴄᴛ คนทีจะตั้งแอดลงมา.")                               
                                 
                    elif teambotgolf == "autoblock on" or teambotgolf == "/เปิดบล็อค":
                      if msg._from in admin:
                          settings["autoBlock"] = True
                          golfbots.sendMessage(to, "เปิดเรียบร้อยแล้ว.")
                    elif teambotgolf == "autoblock off" or teambotgolf == "/ปิดบล็อค":
                      if msg._from in admin:
                          settings["autoBlock"] = False
                          golfbots.sendMessage(to, "ปิดเรียบร้อยแล้ว.")
                    elif teambotgolf == "!profile" or teambotgolf == "/อัพรูป":
                      if msg._from in owner:
                          settings["changePictureProfile"] = True
                          golfbots.sendMessage(to, "กรุณาส่ง ส่งรูปภาพ.")

            if msg.contentType == 1:
              if msg._from in owner:
                  if settings["changePictureProfile"] == True:
                      path = golfbots.downloadObjectMsg(msg_id)
                      settings["changePictureProfile"] = False
                      golfbots.updateProfilePicture(path)
                      golfbots.sendMessage(to, "เปลี่ยนรูปโปรไฟล์เรียบร้อยแล้ว.")

            if msg.toType == 2:
              if msg._from in admin:
                  if to in settings["changeGroupPicture"]:
                     path = golfbots.downloadObjectMsg(msg_id)
                     settings["changeGroupPicture"].remove(to)
                     golfbots.updateGroupPicture(to, path)
                     golfbots.sendMessage(to, "เปลี่ยนรูปโปรไฟล์กลุ่มเรียบร้อยแล้ว.")
    except TalkException as talk_error:
        print(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as error:
        print(error)

def mainkick(op):
    try:
        if op.type == 5:
            if RfuProtect["autoBlock"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    runautoblock = mp.Process(target=golfbots.sendMessage(op.param1,str(settings["message"])+golfbots.getContact(golfbotsMID).displayName))

#==============================================================================================================
#==============================================[OP TYPE 22 24 JOIN]============================================
#==============================================================================================================
                                                                                         
                
        if op.type == 55:
            if op.param2 in settings["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff and op.param2 not in RfuFamily:              
                #if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff and op.param2 not in kickgods:            	
                    random.choice(Exc).kickoutFromGroup(op.param1,[op.param2])
                    G = golfbots.getCompactGroup(op.param1)	
                    G.preventedJoinByTicket = True		
                    random.choice(Exc).updateGroup(G)
 
        if op.type == 17: 
            if op.param1 in welcomegroup:
                try:
                    contact = golfbots.getContact(op.param2)
                    group = golfbots.getGroup(op.param1)
                    sMsg = optypesg["welcomeMessage"]
                    sMsg = sMsg.replace("{name}",contact.displayName)
                    sMsg = sMsg.replace("{group}",group.name)
                    golfbots.sendMessage(op.param1, sMsg)
#=====================================================ADD PIC AND CONTACT DOWN [REVISION BY HUUMEAW]====================================================
                    #golfbots.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/"+golfbots.getContact(op.param2).pictureStatus) #รูปโปร
                    golfbots.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + golfbots.getGroup(op.param1).pictureStatus) #รูปกลุ่ม										
                    golfbots.sendContact(op.param1,op.param2) # คอทแทค
#=====================================================ADD PIC AND CONTACT UP==========================================================================                      
                except:pass
        if op.type == 15:
            if op.param1 in leavegroup:
                try:
                    contact = golfbots.getContact(op.param2)
                    group = golfbots.getGroup(op.param1)
                    sMsg = optypesg["leaveMessage"]
                    sMsg = sMsg.replace("{name}",contact.displayName)
                    sMsg = sMsg.replace("{group}",group.name)
                    golfbots.sendMessage(op.param1, sMsg)
#=====================================================ADD PIC AND CONTACT DOWN [REVISION BY HUUMEAW]==========================================================================
                    golfbots.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/"+golfbots.getContact(op.param2).pictureStatus)
                    golfbots.sendContact(op.param1,op.param2)
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
                            path = golfbots.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = golfbots.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = golfbots.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.golfbots.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
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
                            path = golfbots.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if settings["unsendMessage"] == True:
                at = op.param1
                msg_id = op.param2
                if msg_id in msg_dict:
                    ah = time.time()
                    ikkeh = golfbots.getContact(msg_dict[msg_id]["from"])
                    if "text" in msg_dict[msg_id]:
                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                        waktumsg = format_timespan(waktumsg)
                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                        rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                        golfbots.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                        del msg_dict[msg_id]
                    else:
                        if "image" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nImage :\nBelow"
                            golfbots.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                            golfbots.sendImage(at, msg_dict[msg_id]["image"])
                            del msg_dict[msg_id]
                        else:
                            if "video" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nVideo :\nBelow"
                                golfbots.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                golfbots.sendVideo(at, msg_dict[msg_id]["video"])
                                del msg_dict[msg_id]
                            else:
                                if "audio" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nAudio :\nBelow"
                                    golfbots.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                    golfbots.sendAudio(at, msg_dict[msg_id]["audio"])
                                    del msg_dict[msg_id]
                                else:
                                    if "sticker" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nSticker :\nBelow"
                                        golfbots.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                        golfbots.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "mid" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nContact :\nBelow"
                                            golfbots.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                            golfbots.sendContact(at, msg_dict[msg_id]["mid"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "location" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nLocation :\nBelow"
                                                golfbots.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                                golfbots.sendLocation(at, msg_dict[msg_id]["location"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "file" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nFile :\nBelow"
                                                    golfbots.sendMessage(at, "ข้อความที่ยกเลิก:\n\nMaker :\n"+str(rat_))
                                                    golfbots.sendFile(at, msg_dict[msg_id]["file"])
                                                    del msg_dict[msg_id]
               
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = golfbots.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            tt = Name
                            RfuCctv['sidermem'][op.param1] += "\n-" + Name
                            golfbots.sendMentionV2(op.param1, "@!\n-อ่านแล้ว", [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass

        else:pass                
                    
    except TalkException as talk_error:
        print(talk_error)

         
        
    except TalkException as talk_error:
        print(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as error:
        print(error)

def run():
    while True:
        try:
            ops = kickPoll.singleTrace(count=100)
            if ops != None:
                for op in ops:
                   kickBot(op)
                   mainkick(op)
                   kickPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run1 = mp.Process(target=run)
    run1.start()   














