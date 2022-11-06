from linepy import *
from multiprocessing import Pool, Process
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
#from loginqr.gen import login
from newqr import NewQRLogin
from urllib.parse import urlencode
#from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
from Naked.toolshed.shell import execute_js
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import traceback
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#==============================================================================#
#try:
#    with open('token.txt','r') as tokens:
#        token = tokens.read()
#    print(str(token))
#except Exception as e:
#    linux = LINE(token)
#linux = LINE()
#linux.log("Auth Token : " + str(linux.authToken))
#linux = LINE(token,appName="DESKTOPMAC\t5.11.2\tHackzsaw\t11.0")
#DESKTOPMAC\t5.21.3\tMAC\t10.0
#APP = "IOSIPAD\t9.18.1\tiPhone X\t12.4.1"
#======== LOGIN LINK QR ======================================================================#
#from newqr import NewQRLogin
newqr = NewQRLogin()
tokens = newqr.loginWithQrCode("ios_ipad")
linux = LINE(tokens, appName=newqr.HEADERS["ios_ipad"]["X-Line-Application"])
#linux = LINE("","")

waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
apaloOpen = codecs.open("LnBots.json","r","utf-8")
LnBots = json.load(apaloOpen)
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#========================================#
linuxMID = linux.profile.mid
linuxProfile = linux.getProfile()
linuxSettings = linux.getSettings()
#==============================================================================#
linuxMID = linux.profile.mid
linuxProfile = linux.getProfile()
linuxSettings = linux.getSettings()
#==============================================================================#
#Zmid = g1.profile.mid
#Amid = g2.profile.mid
#Bmid = k1.profile.mid
#KAC = [linux,Bmid]
#KICKER = [Zmid,Amid]           
#Bots = [linux,Zmid,Amid]
#Setbot = codecs.open("max.json","r","utf-8")
#Setmain = json.load(Setbot)
#==============================================================================#
Rfu = [linux]
linuxPoll = OEPoll(linux)
linuxMID = linux.getProfile().mid
admin = [linuxMID]
botStart = time.time()
#admin = ["u28b8c966bac59aab7db1736bddc38371"]
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']
mc = {"wr":{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
welcomeout = []
welcome = []
welcomeo = []
welcomet = []
welcomeb = []
welcomes = []
msg_dict = {}
temp_flood = {}
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel =[]
protectantijs = []
#==============================================================================#
true = True
false = False
list = {"con":false, "uncon":false}
set={"spamGroup":True}
sets = {
    'autoCancel':{"on":True,"members":5},
    "leaveRoom": True,	
    "autoRead": True,
    "pict": True,
    "sti2": False,
    "tagsticker": False,
    "Sticker": False,
    "autoJoinTicket": False,
    "autoJoin": True,
    "autoblock": True,
    "image": {
        "name": "",
    },
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
    "ilstpict": {},    
}    
spamc = {
    "spamcall": False, 
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}
uck = {
    "uck1":"#00FFFF",
    "uck2":"#FFFFFF",
    "uck3":"#00FFFF",
    "uck4":"#000000"
}
uu = {
    "uuu":"line://ti/p/~anan789anan"
}
usa = {
    "us":" ",
    "us1":" ",
    "us2":" ",
    "usa":"https://sv1.picz.in.th/images/2020/06/29/5t6LOa.jpg",
    "usa1":"https://sv1.picz.in.th/images/2020/06/29/5t6LOa.jpg",
    "usa2":"https://sv1.picz.in.th/images/2020/06/29/5t6LOa.jpg",
}
anyun = {
    "addTikel": {
        "name": "",
        "status": False
        }
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
LnBots = {
    "Talkblacklist": {},
    "wblacklist": False,
    "dblacklist": False,
    "Talkdblacklist": False,
    "Talkwblacklist": False,
    "blacklist": {},
    "talkban": True,
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "ไม่อยู่ ไม่ว่าง ไม่คุย ไม่ตอบ",
    "add": "『มองหาพ่อมุงหรอ』\nสวัสดีครับ ยินดีที่ได้รู้จัก",
    "badd": "ยินดีที่ได้รู้จักจ้า 😁",
    "wctext": "🙏 สวัสดีครับยินดีต้อนรับจ้า 🙏",
    "lv": "บ๊ายบาย >< ขอให้โชคดีจ้า >_< ",
    "b": "AUTO BOTLINE\nระบบออโต้บล็อคเปิดใช้งาน\nกรุณารอการอนุมัติจากผู้ใช้งาน",
    "c":"Auto Like By. 『มองหาพ่อมุงหรอ』",
    "m": "",
}
apalo = {
    "bc":{},
}
temp = {"te": "#00FFFF","t": "#000000"}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "autoRead":{},
    "ROM": {}
}
reads = {
    "autoRead": False,
}
mimics = {
    "copy": False,
    "status": True,
    "target": {},
    }
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hoho = {
    "savefile": False,
    "namefile": "",
}
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
bed = {
    "bed": True,
    "bed1": "ลิ้งรูป",
    "bed2": "ลิ้งรูป",
    "bed3": "ลิ้งรูป",
    "tetx": "กรุณาตั้งประกาศออโต้",
    "tetx2": "กรุณาตั้งประกาศออโต้",
    "tetx3": "กรุณาตั้งประกาศออโต้",   
    "TIME": "3600"
}

user1 = linuxMID
user2 = ""
allrepositories = [linux]
setTime = {}
setTime = rfuSet['setTime']

contact = linux.getProfile() 
backup = linux.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = linuxProfile.displayName
settings["myProfile"]["statusMessage"] = linuxProfile.statusMessage
settings["myProfile"]["pictureStatus"] = linuxProfile.pictureStatus
cont = linux.getContact(linuxMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = linux.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = linuxProfile.statusMessage
ProfileMe["pictureStatus"] = linuxProfile.pictureStatus
coverId = linux.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("linux.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("linux2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        linux.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    linux.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    linux.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = linux.getContact(mid)
    if contact.videoProfile == None:
        linux.cloneContactProfile(mid)
    else:
        profile = linux.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        linux.updateProfile(profile)
        pict = linux.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = linux.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = linux.getProfileDetail(mid)['result']['objectId']
    linux.updateProfileCoverById(coverId)
def backupProfile():
    profile = linux.getContact(linuxMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = linux.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = linux.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        linux.updateProfileAttribute(8, profile.pictureStatus)
        linux.updateProfile(profile)
    else:
        linux.updateProfile(profile)
        pict = linux.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = linux.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    linux.updateProfileCoverById(coverId)
def NoteCreate(to,pesan,msg):
    h = []
    s = []
    if pesan == 'mentionnote':
        sakui = linux.getProfile()
        group = linux.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
        data = nama
        k = len(data)//20
        for aa in range(k+1):
            nos = 0
            if aa == 0:dd = '╭「 Mention Note 」─';no=aa
            else:dd = '├「 Mention Note 」─';no=aa*20
            msgas = dd
            for i in data[aa*20 : (aa+1)*20]:
                no+=1
                if no == len(data):msgas+='\n╰{}. @'.format(no)
                else:msgas+='\n│{}. @'.format(no)
            msgas = msgas
            for i in data[aa*20 : (aa+1)*20]:
                gg = []
                dd = ''
                for ss in msgas:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
                nos +=1
            h = linux.createPostGroup(msgas,msg.to,holdingTime=None,textMeta=s)
    else:
        pesan = pesan.replace('create note ','')
        if 'MENTION' in msg.contentMetadata.keys()!= None:
            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
            mentionees = mention['MENTIONEES']
            no = 0
            for mention in mentionees:
                ask = no
                nama = str(linux.getContact(mention["M"]).displayName)
                h.append(str(pesan.replace('create note @{}'.format(nama),'')))
                for b in h:
                    pesan = str(b)
                gg = []
                dd = ''
                for ss in pesan:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[no], 'end': gg[no]+1, 'mid': str(mention["M"])})
                no +=1
        h = linux.createPostGroup(pesan,to,holdingTime=None,textMeta=s)            
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        linux.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = linux.getGroup(msg.to).name
    sd = linux.waktunjir()
    linux.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = linux.getContact(to)
        profile = linux.profile
        profileName = linux.profile
        profileStatus = linux.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        linux.updateProfile(profileName)
        linux.updateProfile(profileStatus)
        profile.pictureStatus = linux.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if linux.getProfileCoverId(to) is not None:
            linux.updateProfileCoverById(linux.getProfileCoverId(to))
        linux.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return linux.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        linux.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
#maxg = "ua053fcd4c52917706ae60c811e39d3ea"
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(linux.getContact(linuxMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(linux.getContact(linuxMID).pictureStatus)
        ticket = "http://line.me/ti/p/~anan789anan"
        linux.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        linux.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def ggggg(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    return '%02d วัน\n───────────\n%02d ชั่วโมง\n───────────\n%02d นาที\n───────────\n' %(days ,hours, mins)

def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@linux  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    linux.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(linux.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + linux.getContact("u74f266049009b8329a62fc2e016222b7").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = linux.genOBSParams({'oid': linuxMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = linux.server.postContent('{}/talk/vp/upload.nhn'.format(str(linux.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        linux.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = linux.liff.issueLiffView(view)
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
    token = linux.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    linux.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        linux.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        linux.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = linux.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        linux.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        linux.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d สัปดาห์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def restartBot():
    print ("กำลังรีบอท..")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
#    with open("stickerz.json","r") as fp:
#        stickerz = json.load(fp)
def black(target):
    if target not in LnBots["blacklist"]:
        LnBots["blacklist"][target] = True
        banned()
def anuchai(max, text):
    cover = linux.getProfileCoverURL(linuxMID)
    data = {
    "type": "flex",
    "altText": "มาอ่านเอา",
    "contents": {
    "type": "bubble",
    "styles": {
    "body": {
    "backgroundColor": '#000000'
    }
    },    
    "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
    {
    "type": "box",
    "layout": "horizontal",
    "contents": [
    {
    "type": "image",
    "url":  "https://obs.line-scdn.net/{}".format(str(linux.getContact(linuxMID).pictureStatus)),
    "size": "sm",
    },
    {
    "type": "separator",
    "color": "#00F5FF"
    },
    {
    "type": "image",
    "url":  str(cover),
    "size": "sm",
    },
    ]
    },
    {
    "type": "separator",
    "color": "#00F5FF"
    },
    {
    "type": "text",
    "text": "{}".format(contact.displayName),
    "color": "#00F5FF",
    "weight": "bold",
    "align":"center",
    "size": "md"
    },
    {
    "type": "separator",
    "color": "#00F5FF"
    },
    {
    "type":"text",
    "text": " ",
    },
    {
    "type": "text",
    "text": str(text),
    "color": "#00F5FF",
    "gravity": "center",
    "align":"center",
    "wrap": True,
    "size": "md"
    },
    {
    "type": "separator",
    "color": "#00F5FF"
    },
    {
    "type":"text",
    "text": " ",
    },
    ]
    }
    }
    }
    sendTemplate(max,data)
def duc1(to, duc1):
    data={
"type": "flex",
"altText": duc1,
"contents": {
"type": "bubble",
"styles": {
"footer": {"backgroundColor": "#000000"},
},
"footer": {
"type": "box",
"layout": "vertical",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
"size": "md"
},
{
"type": "text",
"text": duc1,
"color":"#00F5FF",
"gravity": "center",
"align":"center",
"wrap": True,
"size": "md"
},
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
"size": "md"
},
]
}
]
}
}
}
    sendTemplate(to, data)
def flexOff(to, text1):
#    group = client.getGroup(op.param1)
    contact = linux.getContact(linuxMID)
    data = {
"type": "flex",
"altText": "AuTo LiKe",
"contents": 
{
"type": "bubble",
"styles": {
"body": {
"backgroundColor": "#708090",
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
"size": "lg"
},
{
"type": "text",
"text": text1,
"color": "#FFFF00",
# "sparator": True,
"size": "sm",
"weight": "bold"
}
]
}
],
}
}
}
    sendTemplate(to, data) 
def sendAutolike(to,text):
    data = {
"type": "template",
"altText": "AUTO LIKE DONE",
"template": {
"type": "carousel",
"actions": [],
"columns": [
{
"thumbnailImageUrl": "https://uppic.cc/d/5raZ",
"imageBackgroundColor": "#002727",
"title": "{}".format(linux.getContact(linuxMID).displayName),
"text": text,
"color": "#7B68EE",
"size": "sm",
"weight": "bold",
"actions": [
{
"type": "uri",
"label": "CREATOR",
"uri": "http://line.me/ti/p/~{}".format(linux.getProfile().userid),
}
]
}
]
}
}
    sendTemplate(to, data)   
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    linux.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': linux.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + linux.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    linux.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            linux.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def command(text):
    pesan = text.lower()
    return pesan        
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd   
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]
def sendMessageWithMention(to, linuxMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(linuxMID)+'}'
        text_ = '@x '
        linux.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)    
#=====================================================================
def banned():
    with open('LnBots.json', 'w') as fp:
        json.dump(LnBots, fp, sort_keys=True, indent=4)
def backupData():
    try:
        backup = settings
        f = codecs.open('max.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('Max2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = LnBots
        f = codecs.open('LnBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#

async def linuxBot(op):
    try:
        if settings["restartPoint"] != None:
            linux.sendMessage(settings["restartPoint"], 'ล็อคอินแล้วเรียบร้อย ><')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
              if op.param2 in admin:
                  return
              linux.findAndAddContactsByMid(op.param1)
              linux.sendMessage(op.param1,"{}".format(tagadd["add"]))
              msgSticker = sets["messageSticker"]["listSticker"]["add"]
              if msgSticker != None:
                  sid = msgSticker["STKID"]
                  spkg = msgSticker["STKPKGID"]
                  sver = msgSticker["STKVER"]
                  sendSticker(op.param1, sver, spkg, sid)
              print ("[ 5 ] AUTO ADD")
        if op.type == 5:
            if settings["autoblock"] == True:
              linux.sendMessage(op.param1,"{}".format(tagadd["b"]))
              block001 = threading.Thread(target=linux.blockContact(op.param1))
              block001.start()
              block001.join()            
              print("blockContact") 

#        if op.type == 5:
#            if settings["autoblock"] == True:
#              if op.param2 in admin:
#                  return
#              linux.blockContact(op.param1)                   
#              linux.sendMessage(op.param1,tagadd["b"])
#              msgSticker = sets["messageSticker"]["listSticker"]["block"]
#              if msgSticker != None:
#                  sid = msgSticker["STKID"]
#                  spkg = msgSticker["STKPKGID"]
#                  sver = msgSticker["STKVER"]
#                  sendSticker(op.param1, sver, spkg, sid)
#                  linux.sendMessage(op.param1,tagaad["b"])
#              linux.blockContact(op.param1)
#              print ("[ 5 ] AUTO BLOCK")
#        if op.type == 25:
#            msg = op.message
#            if msg.contentType == 13:
#            	if settings["winvite"] == True:
#                     if msg._from in admin:
#                         _name = msg.contentMetadata["displayName"]
#                         invite = msg.contentMetadata["mid"]
#                         groups = linux.getGroup(msg.to)
#                         pending = groups.invitee
#                         targets = []
#                         for s in groups.members:
#                             if _name in s.displayName:
#                                 linux.sendMessage(msg.to,"-> " + _name + " ทำการเชิญสำเร็จ")
#                                 break
#                             elif invite in settings["blacklist"]:
#                                 linux.sendMessage(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
#                                 linux.sendMessage(msg.to,"ใช้คำสั่ง!,ล้างดำ,ดึง" )
#                                 break                             
#                             else:
#                                 targets.append(invite)
#                         if targets == []:
#                             pass
#                         else:
#                             for target in targets:
#                                 try:
#                                     linux.findAndAddContactsByMid(target)
#                                     linux.inviteIntoGroup(msg.to,[target])
#                                     linux.sendMessage(msg.to,"เชิญ :" + _name + "เรียบร้อย")
#                                     settings["winvite"] = False
#                                     break
#                                 except:
#                                     try:
#                                         linux.findAndAddContactsByMid(invite)
#                                         linux.inviteIntoGroup(op.param1,[invite])
#                                         settings["winvite"] = False
#                                     except:
#                                         linux.sendMessage(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
#                                         settings["winvite"] = False
#                                         break 

        if op.type == 13:
            if set['spamGroup'] == True:
                group = linux.getGroup(op.param1)
                group.members = [] if not group.members else group.members
                if len(group.members) <= 3:
                    linux.acceptGroupInvitation(op.param1)
                    time.sleep(0.65)
                    linux.leaveGroup(op.param1)
#        if op.type == 13:
#            if linuxMID in op.param3:
#                G = linux.getGroup(op.param1)
#                if settings["autoJoin"] == True:
#                    if sets["autoCancel"]["on"] == True:
#                        if len(G.members) <= sets["autoCancel"]["members"]:
#                            time.sleep(0.65)
#                            linux.acceptGroupInvitation(op.param1)
#                        else:
#                            linux.leaveGroup(op.param1)
#                    else:
#                        linux.acceptGroupInvitation(op.param1)
#                elif sets["autoCancel"]["on"] == True:
#                    if len(G.members) <= sets["autoCancel"]["members"]:
#                        linux.acceptGroupInvitation(op.param1)
#                        time.sleep(0.65)
#                        linux.leaveGroup(op.param1)
#            else:
#                Inviter = op.param3.replace("",',')
#                InviterX = Inviter.split(",")
#                matched_list = []
#                for tag in LnBots["blacklist"]:
#                    matched_list+=[str for str in InviterX if str == tag]
#                if matched_list == []:
#                    pass
 #               else:
#                    linux.acceptGroupInvitation(op.param1, matched_list)
#                    linux.leaveGroup(op.param1, matched_list)
#                    print ("[ 17 ] LEAVE GROUP")
        if op.type == 13:
            if linuxMID in op.param3:
                G = linux.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    linux.acceptGroupInvitation(op.param1)
        if op.type == 22:
            if sets["leaveRoom"] == True:
                linux.leaveRoom(op.param1)
        if op.type == 24:
            if sets["leaveRoom"] == True:
                linux.leaveRoom(op.param1) 
            if msg.toType == 1:
                if sets["leaveRoom"] == True:
                    linux.leaveRoom(msg.to)                    
        if op.type == 15:
          if op.param1 in welcomeout:
            if op.param2 in admin:
                return
            ginfo = linux.getGroup(op.param1)
            contact = linux.getContact(op.param2)
            name = contact.displayName
            pp = contact.pictureStatus
            s = name + " " + tagadd["lv"]
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#000000'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#00F5FF",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~"+str(linux.getProfile().userid),
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 15:
          if op.param1 in welcomes:
              ginfo = linux.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["lv"]
              if msg != None:
                  contact = linux.getContact(linuxMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
        if op.type == 17:
#          if op.param2 not in LnBot and op.param2 not in admin:
            if op.param2 in LnBots["blacklist"]:
                linux.kickoutFromGroup(op.param1,[op.param2])
                G = linux.getGroup(op.param1)
                G.preventedJoinByTicket = True
                linux.updateGroup(G)
                LnBots["blacklist"][op.param2] = True
#                linux.sendMessage(op.param1, "มึงติดดำกู มึงเข้ามาทำไม..Fuck")
        if op.type == 17:
          if op.param1 in welcome:
            if op.param2 in admin:
                return
            g = linux.getGroup(op.param1)
            contact = linux.getContact(op.param2)
            gname = g.name
            name = contact.displayName
            pp = contact.pictureStatus
            s = "〖 Group Welcome 〗\n"
            s += "\n• ชื่อกลุ่ม : {}".format(gname)
            s += "\n• ชื่อคนเข้ากลุ่ม : {}\n\n".format(name)
            s += tagadd["wctext"]
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#000000'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#00F5FF",
                                "align": "center",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~"+str(linux.getProfile().userid),
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if op.param1 in welcomeb:
            if op.param2 in admin:
                return
            ginfo = linux.getGroup(op.param1)
            contact = linux.getContact(op.param2)
            cover = linux.getProfileCoverURL(op.param2)
            names = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    'styles': {
                        "body": {
                            "backgroundColor": '#000000'
                        },
                     },
                     "hero": {
                         "type":"image",
                         "url": cover,
                         "size":"full",
                         "aspectRatio":"20:13",
                         "aspectMode":"cover"
                     },
                     "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
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
                                 "text":"{}".format(names),
                                 "size":"xl",
                                 "weight":"bold",
                                 "color":"#00F5FF",
                                 "align":"center"
                             },
                             {
                                 "type": "text",
                                 "text": status,
                                 "wrap": True,
                                 "align": "center",
                                 "gravity": "center",
                                 "color": "#00F5FF",
                                 "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
         if op.param1 in welcomet:
              ginfo = linux.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["wc"]
              if msg != None:
                  contact = linux.getContact(linuxMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in linuxMID:
                    LnBots["blacklist"][op.param2] = True
                    linux.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
                                 
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in linuxMID:
                    LnBots["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in LnBots["blacklist"]:
                        	linux.kickoutFromGroup(op.param1,[op.param2])
                    except:
                    	pass
#----------------กันเชิญนะจ๊ะ-------------------                   
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in linuxMID:
                   LnBots["blacklist"][op.param2] = True
                   linux.cancelGroupInvitation(op.param1,[op.param3])
                   linux.kickoutFromGroup(op.param1,[op.param2])
           
                            
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if linux.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in linuxMID:
                            linux.reissueGroupTicket(op.param1)
                            X = linux.getCompactGroup(op.param1)
                            X.preventedJoinByTicket = True
                            linux.kickoutFromGroup(op.param1,[op.param2])
                            linux.updateGroup(X)
                except:
                    pass
#
#        if op.type == 32:
#            if op.param1 in protectcancel:
#              if op.param3 in Bots:    
#                if op.param2 not in Bots:
#                    LnBots["blacklist"][op.param2] = True
#                    try:
#                        if op.param3 not in LnBots["blacklist"]:
#                            linux.kickoutFromGroup(op.param1,[op.param2])
#                            linux.inviteIntoGroup(op.param1,[Zmid])
#                            linux.sendMessage(op.param1, None, contentMetadata={'mid': op.param2})									
#                    except:
#                    	pass
#
#                return
#
#        if op.type == 19:
#            if op.param1 in protectantijs:
#                if linuxMID in op.param3:
#                    if op.param2 not in Bots:
#                        try:
#                            g1.acceptGroupInvitation(op.param1)
#                            g1.inviteIntoGroup(op.param1,[linuxMID,Amid])
#                            g2.acceptGroupInvitation(op.param1)
#                            LnBots["blacklist"][op.param2] = True
#                            g2.kickoutFromGroup(op.param1,[op.param2])
#                            linux.acceptGroupInvitation(op.param1)
#                            g1.leaveGroup(op.param1)
##                            g2.inviteIntoGroup(op.param1,[Zmid])
#                            g2.leaveGroup(op.param1)
#                        except:
#                            pass
#                            
#                            
#            if op.param3 in Zmid:
#                if op.param2 not in Bots:
#                        linux.kickoutFromGroup(op.param1,[op.param2])
#                        linux.findAndAddContactsByMid(op.param3)
#                        linux.inviteIntoGroup(op.param1,[Zmid])
#                else:
#                        g2.kickoutFromGroup(op.param1,[op.param2])
#                        g2.findAndAddContactsByMid(op.param3)
#                        g2.inviteIntoGroup(op.param1,[Zmid])
#
#            if op.param3 in Amid:
#                if op.param2 not in Bots:
#                        linux.kickoutFromGroup(op.param1,[op.param2])
#                        linux.findAndAddContactsByMid(op.param3)
#                        linux.inviteIntoGroup(op.param1,[Amid])
#                else:
#                        g1.kickoutFromGroup(op.param1,[op.param2])
#                        g1.findAndAddContactsByMid(op.param3)
#                        g1.inviteIntoGroup(op.param1,[Amid])
#
#                if op.param2 not in Bots:
#                    if op.param3 in admin:
#                        if op.param1 in protectantijs:
#                            LnBots["blacklist"][op.param2] = True
#                            linux.kickoutFromGroup(op.param1,[op.param2])
#                            linux.findAndAddContactsByMid(op.param3)
#                            linux.inviteIntoGroup(op.param1,[op.param3])
#                else:
#                    pass
#            
#            if op.param1 in protectantijs:
#                if Zmid in op.param3:
#                    if op.param2 not in Bots:
#                        LnBots["blacklist"][op.param2] = True
#                        try:
#                            k1.inviteIntoGroup(op.param1,[Zmid])
#                            k1.kickoutFromGroup(op.param1,[op.param2])
#                        except:
#                            try:
#                                linux.inviteIntoGroup(op.param1,[Zmid])
#                                linux.kickoutFromGroup(op.param1,[op.param2])
#                            except:
#                                try:
#                                	g2.inviteIntoGroup(op.param1,[Zmid])
#                                	g2.kickoutFromGroup(op.param1,[op.param2])
#                                except:
#                                	pass
#            if op.param1 in protectantijs:
#                if Amid in op.param3:
#                    if op.param2 not in Bots:
#                        LnBots["blacklist"][op.param2] = True
#                        try:
#                            k1.inviteIntoGroup(op.param1,[Amid])
#                            k1.kickoutFromGroup(op.param1,[op.param2])
#                        except:
#                            try:
#                                linux.inviteIntoGroup(op.param1,[Amid])
#                                linux.kickoutFromGroup(op.param1,[op.param2])
#                            except:
#                                try:
#                                	g1.inviteIntoGroup(op.param1,[Amid])
#                                	g1.kickoutFromGroup(op.param1,[op.param2])
#                                except:
#                                	pass
##=====================================================================                        
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)
        if op.type == 55:
      	    if op.param2 not in linuxMID and op.param2 not in admin:
                if op.param2 in LnBots["blacklist"]:
                    linux.kickoutFromGroup(op.param1,[op.param2])
                    linux.sendMention(msg.to, [msg._from])
#=====================================================================                                                     
#=====================================================================
       # if op.type == 26:
         #   print ("[ 26 ] RECEIVE MESSAGE")
         #   msg = op.message
         #   text = str(msg.text)
         #   msg_id = msg.id
         #   receiver = msg.to
         #   sender = msg._from
         #   cmd = command(text)
         #   setKey = settings["keyCommand"].title()
         #   if settings["setKey"] == False: setKey = ""
         #   isValid = True
         #   if isValid != False:
               # if msg.toType == 0 and sender != linuxMID: to = sender
               # else: to = receiver
               # if msg.toType == 0 and settings["replays"] and sender != linuxMID:
                   # contact = linux.getContact(sender)
                    #if contact.attributes != 32 and "[ auto reply ]" not in text.lower():
                     #   msgSticker = sets["messageSticker"]["listSticker"]["replay"]
                     #   if msgSticker != None:
                     #       sid = msgSticker["STKID"]
                     #       spkg = msgSticker["STKPKGID"]
                     #       sver = msgSticker["STKVER"]
                     #       sendSticker(to, sver, spkg, sid)
                     #   if "@!" in settings["reply"]:
                     #       msg_ = settings["reply"].split("@!")
                     #       sendMention(to, sender, "「 แทคส่วนตัว 」\n" + msg_[0], msg_[1])
                     #   linux.sendMessage(to, "「 แทคส่วนตัว 」\n", settings["reply"])
        if op.type == 25:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.to not in unsendchat:
                unsendchat[msg.to] = {}
            if msg_id not in unsendchat[msg.to]:
                unsendchat[msg.to][msg_id] = msg_id
            msgdikirim[msg_id] = {"text":text}
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [linuxMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != linuxMID: to = sender
                else: to = receiver
                if msg._from not in linuxMID:
                  if LnBots["talkban"] == True:
                    if msg._from in LnBots["Talkblacklist"]:
                        linux.kickoutFromGroup(msg.to, [msg._from]) 
                if msg.contentType == 13:
                  if LnBots["wblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in LnBots["blacklist"]:
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 เพิ่มบัญชีดำเรียบร้อยแล้ว 🌸")
                          LnBots["wblacklist"] = True
                      else:
                          LnBots["blacklist"][msg.contentMetadata["mid"]] = True
                          LnBots["wblacklist"] = True
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 เพิ่มบัญชีดำเรียบร้อยแล้ว 🌸")
                          banned()
                          
                  if LnBots["Talkwblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in LnBots["Talkblacklist"]:
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 มีรายชื่อบัญชีดำอยู่แล้ว 🌸")
                          LnBots["Talkwblacklist"] = True
                      else:
                          LnBots["Talkblacklist"][msg.contentMetadata["mid"]] = True
                          LnBots["Talkwblacklist"] = True
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 เพิ่มบัญชีดำเรียบร้อยแล้ว 🌸")
                          banned()

                  if LnBots["dblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in LnBots["blacklist"]:
                          del LnBots["blacklist"][msg.contentMetadata["mid"]]
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 ลบบัญชีดำเรียบร้อย 🌸")
                      else:
                          LnBots["dblacklist"] = True
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 ลบบัญชีดำเรียบร้อย 🌸")
                          banned()

                  if LnBots["Talkdblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in LnBots["Talkblacklist"]:
                          del LnBots["Talkblacklist"][msg.contentMetadata["mid"]]
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 ไม่สามารถลบออกจากบัญชีดำ 🌸")
                      else:
                          LnBots["Talkdblacklist"] = True
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 ลบบัญชีดำเรียบร้อย 🌸")
                          banned()
#                if msg.contentType == 16:
#                    if msg.toType in [2,1,0]:
#                        print ("AutoLikeCommat")
#                        try:
#                            if settings["autolike"] == True:
#                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
#                                if purl[1] not in wait['postId']:
#                                    linux.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
#                                if settings["com"] == True:
#                                    linux.createComment(purl[0], purl[1], settings["commet"])
#                                    wait['postId'].append(purl[1])
#                                else:
#                                    pass
#                        except Exception as e:
#                                if settings["autolike"] == True:
#                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
#                                    if purl[1] not in wait['postId']:
#                                        linux.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
#                                    if settings["com"] == True:
#                                        linux.createComment(msg._from, purl[1], settings["commet"])
#                                        wait['postId'].append(purl[1])
#                                    else:pass
        if op.type in [25,26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            if isValid != False:
                if msg.toType == 0 and sender != linuxMID: to = sender
                else: to = receiver
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        print ("AutoLikeCommat")
                        try:
                            if settings["autolike"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                if purl[1] not in settings['postId']:
                                    linux.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                    linux.sendMessage(to,"🌸 ไลค์ให้แล้วนะกิกิ้ว 🌸")
                                if settings["com"] == True:
                                    linux.createComment(purl[0], purl[1], settings["commet"])
                                    settings['postId'].append(purl[1])                                    
                                else:
                                    pass
                        except Exception as e:
                                if settings["autolike"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    if purl[1] not in settings['postId']:
                                        linux.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
                                        linux.sendMessage(to,"🌸 ไลค์ให้แล้วนะกิกิ้วว 🌸")
                                    if settings["com"] == True:
                                        linux.createComment(msg._from, purl[1], settings["commet"])
                                        settings['postId'].append(purl[1])                                      
                                    else:pass                    	
                    else:pass                                          
#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != linux.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "ตั้งออโต้":
                    sa="วิธีใช้ ประกาศออโต้"
                    sa+="\n- ตั้งเวลา [ เวลาเป็นวินาที ]​"
                    sa+="\n- ตัวอย่าง&วิธีตั้งเวลา\n- ตั้งเวลา 120 [ 120วิ = 2นาที ]​"
                    sa+="\n- ปัจจุบันตั้งเวลาประกาศทุกๆ 1 ชม.\n**ระวังบัค [ อย่าตั้งเวลาน้อยเกินไป ]​**"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u483e96e999cbcda7130543540dd72adf"}}
                    sendTemplate(to,data)
                if text.lower() == "ตั้งapi":
                    sa = "วีธีใช้ api >\\<"
                    sa += "\n- ตั้งapi คีย์เวิร์ด;;ตอบกลับ"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- ตั้งapi เทส;;เทสทำไม"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u483e96e999cbcda7130543540dd72adf"}}
                    sendTemplate(to,data)
                if text.lower() == "stag":
                    sa = "วิธีใช้ stag >\\<"
                    sa += "\n- stag [เลขที่ต้องการ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- stag 1 @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u483e96e999cbcda7130543540dd72adf"}}
                    sendTemplate(to,data)
                if text.lower() == "สะกดกิต":
                    sa = "วิธีใช้ สะกดกิต >\\<"
                    sa += "\n- สะกดกิต [ข้อความ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- สะกดกิต รักนะ @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u483e96e999cbcda7130543540dd72adf"}}
                    sendTemplate(to,data)                     
                if msg.text.lower().startswith('ลงโน๊ต '):
                    if msg._from in admin:
                        text = text.replace('ลงโน๊ต ','')
                        NoteCreate(to,text,msg)
                if text.lower() == "mentionnote":
                    if msg._from in admin:
                        NoteCreate(to,text,msg) 
                if text.lower() == "เชคค่า" or text.lower() == "set":
                    sas = "การตั้งค่า เปิด/ปิด"
                    if settings["autoAdd"] == True: sa = "\n🌸 ออโต้แอด            『 ☑️ 』"
                    else:sa = "\n🌸 ออโต้แอด            『 ❎ 』"
                    if settings["autoblock"] == True: sa += "\n🌸 ออโต้บล็อค        『 ☑️ 』"
                    else:sa += "\n🌸 ออโต้บล็อค          『 ❎ 』"
                    if sets["autoCancel"]["on"] == True: sa +="\n🌸 ยกเชิญที่มีสมาชิกต่ำกว่า: " + str(sets["autoCancel"]["members"])
                    else:sa += "\n🌸 ปฏิเสธกลุ่มเชิญ       『 ❎ 』"
                    if tagadd["tags"] == True: sa += "\n🌸 ตอบกลับคนแทค           『 ☑️ 』"
                    else:sa += "\n🌸 ตอบกลับคนแทค      『 ❎ 』"
                    if tagadd["tagss"] == True: sa += "\n🌸 ตอบกลับคนแทค2         『 ☑️ 』"
                    else:sa += "\n🌸 ตอบกลับคนแทค2     『 ❎ 』"
                    if sets["tagsticker"] == True: sa += "\n🌸 แทคสติ๊กเกอร์         『 ☑️ 』"
                    else:sa += "\n🌸 แทคสติ๊กเกอร์        『 ❎ 』"
                    if settings["autolike"] == True: sa += "\n🌸 ออโต้ไลค์          『 ☑️ 』"
                    else:sa += "\n🌸 ออโต้ไลค์           『 ❎ 』"
                    if settings["com"] == True: sa += "\n🌸 คอมเม้นโพส             『 ☑️ 』"
                    else:sa += "\n🌸 คอมเม้นโพส         『 ❎ 』"
                    if settings["unsendMessage"] == True: sa += "\n🌸 ตรวจจับยกเลิก 『 ☑️ 』"
                    else:sa += "\n🌸 ตรวจจับยกเลิก       『 ❎ 』"
                    if settings["Sticker"] == True: sa += "\n🌸 เชคติ๊กใหญ่API      『 ☑️ 』"
                    else:sa += "\n🌸 เชคติ๊กใหญ่API      『 ❎ 』"
                    if sets["Sticker"] == True: sa += "\n🌸 เชคโค๊ดสติ๊กเกอร์         『 ☑️ 』"
                    else:sa += "\n🌸 เชคโค๊ดสติ๊กเกอร์     『 ❎ 』"
                    if sets["sti2"] == True: sa += "\n🌸 สติ๊กเกอร์ใหญ่              『 ☑️ 』"
                    else:sa += "\n🌸 สติ๊กเกอร์ใหญ่       『 ❎ 』"
                    if spamc["spamcall"] == True: sa += "\n🌸 กันสแปม            『 ☑️ 』"
                    else:sa += "\n🌸 กันสแปม          『 ❎ 』"       
                    if sets["autoJoinTicket"] == True: sa += "\n🌸 มุดลิ้งออโต้            『 ☑️ 』"
                    else:sa += "\n🌸 มุดลิ้งออโต้          『 ❎ 』"
                    if reads["autoRead"] == True: sa += "\n🌸 อ่านข้อความออโต้     『 ☑️ 』"
                    else:sa += "\n🌸 อ่านข้อความออโต้     『 ❎ 』"
                    if sets["leaveRoom"] == True: sa += "\n🌸 ออกแชทรวม   『 ☑️ 』"
                    else:sa += "\n🌸 ออกแชทรวม   『 ❎ 』"        
                    
                    data = {
"type":"flex",
"altText": "{}".format(sas),
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"body": {"backgroundColor": "#000000"},
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://sv1.picz.in.th/images/2020/07/04/5RGnS2.jpg",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"gravity": "top"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": sas,
"color": "#FFFFFF",
"align": "center",
"weight": "bold",
"size": "xl"
},
{
"text": "{}".format(sa),
"size": "md",
"margin": "none",
"color": str(uck["uck2"]),
"wrap": True,
"weight": "bold",
"type": "text"
}
]
}
],
"position": "absolute",
"offsetTop": "18px",
"offsetStart": "18px"
}
],
"paddingAll": "0px",
"borderWidth":"2px",
"borderColor":str(uck["uck4"]),
"cornerRadius":"xl"
}
}
]
}
}
                    sendTemplate(to,data)              
#=========================================================================                                  

#==========================================================================================================================================             
                elif text.lower() == 'cbb' or text.lower() == "ล้างดำ":
                      LnBots["blacklist"] = {}
                      linux.sendMessage(to, "🌸 ล้างบัญชีดำเรียบร้อย >_< 🌸")
                      banned()
                elif msg.text in ["ดึง"]:
                        settings["winvite"] = True
                        linux.unsendMessage(msg_id)
                        linux.sendMessage(to, "🌸 กรุณาส่ง คท. ที่ต้องการเชิญ 🌸")                       
                elif msg.text.lower().startswith("ยกเชิญ"):                                
                                    if msg.toType == 2:
                                        group = linux.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//30
                                        linux.sendMessage(msg.to,"「 ยกค้างเชิญ จำนวน {} คน 」\nรอสักครู่...".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*30 : (i+1)*30]:
                                                time.sleep(random.uniform(0.5,0.4))
                                                linux.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            linux.sendMessage(receiver,"รอสักครู่🕛เดียวยกต่อ 30 คน ")
                                            time.sleep(random.uniform(15,10))
                                        linux.sendMessage(receiver,"「 ยกค้างเชิญ จำนวน {} คน เรียบร้อยแล้ว👏 」".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        linux.sendMessage(receiver, None, contentMetadata={"STKID": "52002735","STKPKGID": "11537","STKVER": "1" }, contentType=7)
                                        gname = linux.getGroup(receiver).name
                                        linux.sendMessage(Notify,"「 ยกค้างเชิญ >> "+gname+"  << 」\n จำนวน {} คน เรียบร้อยแล้ว👏".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        linux.leaveGroup(receiver)
                                								
                                    linux.sendMessage(receiver,"「 ไม่พบค้างเชิญในกลุ่มนี้❗」")
                                    linux.sendMessage(receiver, None, contentMetadata={"STKID": "52114123","STKPKGID": "11539","STKVER": "1" }, contentType=7)
                                    linux.leaveGroup(receiver)                                    
                elif text.lower() == 'bbc' or text.lower() == "คทดำ":
                    if msg._from in linuxMID:
                        if LnBots["blacklist"] == {}:
                            linux.unsendMessage(msg_id)
                            linux.sendMessage(to, "🌸 ไม่พบรายชื่อบัญชีดำ 🌸")
                        else:
                            for bl in LnBots["blacklist"]:
                                linux.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif msg.text.lower().startswith("อัพสีme "):
                            text_ = removeCmd("อัพสีme", text)
                            try:
                                temp["t"] = text_
                                linux.sendMessage(to,"「 โค้ดสีเชล 」\nรหัสสีคือ: " + text_)
                            except:
                                linux.sendMessage(to,"อัพสีเชลเรียบร้อย")
                elif msg.text.lower().startswith("อัพสีอักษร "):
                            text_ = removeCmd("อัพสีอักษร", text)
                            try:
                                temp["te"] = text_
                                linux.sendMessage(to,"「 โค้ดสีอักษร 」\nรหัสสีคือ: " + text_)
                            except:
                                linux.sendMessage(to,"อัพสีอักษรเรียบร้อย")
                elif msg.text.lower() == "รหัสสี":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="**ตัวอย่างที่1**\nคำสั่งเปลี่ยนสีMe\nพิม'อัพสีme #FFFFFF'\n**ตัวอย่างที่2**\nคำสั่งเปลี่ยนสีอักษร\nพิม'อัพสีอักษร #FFFFFF'"
                            linux.sendImageWithURL(to,c)
                            linux.sendImageWithURL(to,p)
                            linux.sendMessage(to,m)
                elif msg.text.lower() == "รหัสสีกรอบ":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="**ตัวอย่างที่1**\nคำสั่งเปลี่ยนสีMe\nพิม'ตั้งสีme #FFFFFF'\n**ตัวอย่างที่2**\nคำสั่งเปลี่ยนสีอักษร\nพิม'ตั้งสีอักษร #FFFFFF\n**ตัวอย่างที่3**\nคำสั่งเปลี่ยนกรอบเชล\nพิม'ตั้งสีขอบ #FFFFFF'"
                            linux.sendImageWithURL(to,c)
                            linux.sendImageWithURL(to,p)
                            linux.sendMessage(to,m)                            
                elif msg.text.lower().startswith("ตั้งบล็อค "):
                            text_ = removeCmd("ตั้งบล็อค", text)
                            try:
                                tagadd["b"] = text_
                                linux.sendMessage(to,"「 ตั้งบล็อคอัตโนมัติ 」\nคือ : " + text_)
                            except:
                                linux.unsendMessage(msg_id)
                                linux.sendMessage(to, "🌸 ตั้งข้อความบล็อคสำเร็จแล้ว 🌸")
                elif text.lower().startswith("ตั้งกันรัน "):
                            text_ = removeCmd("ตั้งกันรัน", text)
                            try:
                                sets["autoCancel"]["members"] = text_
                                linux.sendMessage(to,"「 ตั้งปฏิเสธการเชิญ 」\nจำนวนคนน้อยกว่า : " + text_)
                            except:
                                linux.unsendMessage(msg_id)
                                linux.sendMessage(to, "🌸 ตั้งข้อความกันสแปมสำเร็จแล้ว 🌸")
                elif "Allban" in msg.text.lower():
                  if msg._from in admin:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.lower().replace("Allban","")
                           gs = linux.getGroup(msg.to)
                           linux.sendReplyMessage(msg.id,to,"Ban Group Done...")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                linux.sendReplyMessage(msg.id,to,"Done..")
                           else:
                               for target in targets:
                                   if not target in admin:
                                       try:
                                           LnBots["blacklist"][target] = True
                                           f=codecs.open('b.json','w','utf-8')
                                           json.dump(LnBots["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           linux.sendReplyMessage(msg.id,to,"พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")
                                           
                if text.lower() == "เปิดดำ":
                  if msg._from in admin:
                      LnBots["wblacklist"] = True
                      linux.unsendMessage(msg_id)
                      linux.sendMessage(to, "🌸 กรุณาส่ง คท 🌸")
                      linux.sendMessage(to, "[ อย่าลืมเชคดำเพื่อความแน่ใจ ]\nพิมพ์ “ ปิดดำ ” เพื่อปิดรับ คท")
                if text.lower() == "ปิดดำ":
                  if msg._from in admin:
                      LnBots["wblacklist"] = False
                      linux.sendMessage(to, "🌸 ปิดรับ คท เรียบร้อย 🌸")

                if text.lower() == "ขาว:เปิด":
                  if msg._from in admin:
                      LnBots["dblacklist"] = True
                      linux.unsendMessage(msg_id)
                      linux.sendMessage(to, "🌸 กรุณาส่ง คท 🌸")
                      linux.sendMessage(to, "[ อย่าลืมเชคเพื่อความแน่ใจ ]\nพิมพ์ “ ขาว:ปิด ” เพื่อปิดรับ คท")
                if text.lower() == "ขาว:ปิด":
                  if msg._from in admin:
                      LnBots["dblacklist"] = False
                      linux.sendMessage(to, "🌸 ปิดรับ คท เรียบร้อย 🌸")
#                if text.lower() == "ดำ":
 #                 if msg._from in admin:
#                      LnBots["Talkwblacklist"] = True
#                      linux.unsendMessage(msg_id)
#                      linux.sendMessage(to, "🌸 กรุณาส่ง คท ที่ต้องการแบน 🌸")
#                if text.lower() == "ขาว":
#                  if msg._from in admin:
#                      LnBots["Talkdblacklist"] = True
#                      linux.unsendMessage(msg_id)
#                      linux.sendMessage(to, "?? กรุณาส่ง คท ที่ต้องปลดแบน 🌸")
                elif "ลงดำ" in msg.text:
#                  if msg._from in Rfu:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("ลงดำ","")
                           gs = linux.getGroup(msg.to)
                           linux.sendMessage(to, "🌸 ยัดดำทั้งกลุ่มเรียบร้อย 🌸")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                linux.sendMessage(to, "Maaf")
                           else:
                               for target in targets:
#                                   if not target in Rfu:
                                       try:
                                           LnBots["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(LnBots["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           linux.sendMessage(to, "พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")                      
                elif text.lower().startswith("/exec\n") or "/exec" in msg.text:
                    try:
                        code = msg.text.replace("/exec\n", "")
                        exec(code)
                    except Exception as error:
                        linux.sendMessage(to, "Error : {}".format(error))
                elif msg.text.lower().startswith("ตั้งแทค "):
                      text_ = removeCmd("ตั้งแทค", text)
                      try:
                          tagadd["tag"] = text_
                          sa = "「 ข้อความตอบแทค 」\nคือ:  " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ufdd706a81ff7557b83592e3b134c6e61"}}
                          sendTemplate(to,data)
                      except:
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 ตั้งแทคเรียบร้อย >_< 🌸")
                elif msg.text.lower().startswith("ตั้งแทคแชท "):
                      text_ = removeCmd("ตั้งแทคแชท", text)
                      try:
                          settings["reply"] = text_
                          sa = "「 ข้อความแทคแชท 」\nคือ:  " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ufdd706a81ff7557b83592e3b134c6e61"}}
                          sendTemplate(to,data)
                      except:
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 ตั้งแทคแชทเรียบร้อย >_< 🌸")
                elif msg.text.lower().startswith("ตั้งต้อนรับ "):
                      text_ = removeCmd("ตั้งต้อนรับ", text)
                      try:
                          tagadd["wctext"] = text_
                          sa = "「 ข้อความต้อนรับ 」\nคือ:  " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ufdd706a81ff7557b83592e3b134c6e61"}}
                          sendTemplate(to,data)
                      except:
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 ตั้งต้อนรับเสร็จแล้ว >_< 🌸")
                elif msg.text.lower().startswith("ตั้งคนออก "):
                            text_ = removeCmd("ตั้งคนออก", text)
                            try:
                                tagadd["lv"] = text_
                                linux.sendMessage(to,"「 ข้อความคนออก 」\nคือ:  " + text_)
                            except:
                                linux.unsendMessage(msg_id)
                                linux.sendMessage(to, "🌸 ตั้งคนออกกลุ่มเสร็จแล้ว >_< 🌸")
                elif msg.text.lower().startswith("ตั้งแอด "):
                      text_ = removeCmd("ตั้งแอด", text)
                      try:
                          tagadd["add"] = text_
                          sa = "「 ข้อความแอด 」\nคือ:  " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ufdd706a81ff7557b83592e3b134c6e61"}}
                          sendTemplate(to,data)
                      except:
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 ตั้งแอดเสร็จแล้ว >_< 🌸")
                elif msg.text.lower().startswith("ตั้งคอมเม้น "):
                      text_ = removeCmd("ตั้งคอมเม้น", text)
                      try:
                          settings["commet"] = text_
                          sa = "「 ตั้งคอมเม้น 」\nคือ:  " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ufdd706a81ff7557b83592e3b134c6e61"}}
                          sendTemplate(to,data)
                      except:
                          linux.unsendMessage(msg_id)
                          linux.sendMessage(to, "🌸 ตั้งคอมเม้นเสร็จแล้ว >_< 🌸")

#                elif text.lower() == "ดำเปิด":
#                          if sender in admin:
#                            LnBots["Talkwblacklist"] = True
#                            linux.sendMessage(to, "✯͜͡❂ แบนผู้ติดต่อ\n✯͜͡❂ ส่งที่อยู่ติดต่อ")

#                elif text.lower() == "ดำปิด":
#                          if sender in admin:
#                            if LnBots["Talkwblacklist"] == False:
#                                linux.sendMessage(to, "✯͜͡❂ แบนผู้ติดต่อถูกปิดใช้งาน")
#                            else:
#                                LnBots["Talkwblacklist"] = False
#                                linux.sendMessage(to, "✯͜͡❂ แบนผู้ติดต่อถูกปิดใช้งาน")
          
                if text.lower() == "/เชค":
                    add = tagadd["add"]
                    badd = tagadd["badd"]
                    tag = tagadd["tag"]
                    like = settings["commet"]
                    wc = tagadd["wctext"]
                    lv = tagadd["lv"]
                    c = sets["autoCancel"]["members"]
                    b = tagadd["b"]
                    Re = settings["reply"]
                    linux.generateReplyMessage(msg.id)
                    linux.sendMessage(to, "ข้อความแอด :\n"+str(add)+"\n\nข้อความแอด :\n"+str(badd)+"\n\nข้อความแทค :\n"+str(tag)+"\n\nข้อความเม้น :\n"+str(like)+"\n\nข้อความต้อนรับ :\n"+str(wc)+"\n\nข้อความคนออก :\n"+str(lv)+"\n\nจำนวนค้างเชิญ :\n"+str(c)+" จำนวน\n\nข้อความบล็อค :\n"+str(b))
#                    linux.sendMessage(to, "ข้อความแอด :\n"+str(add)+"\n\nข้อความแอด :\n"+str(badd)+"\n\nข้อความแทค :\n"+str(tag)+"\n\nข้อความเม้น :\n"+str(like)+"\n\nข้อความต้อนรับ :\n"+str(wc)+"\n\nข้อความคนออก :\n"+str(lv)+"\n\nจำนวนค้างเชิญ :\n"+str(c)+" จำนวน\n\nข้อความบล็อค :\n"+str(b))
#
                if text.lower() == "!helpbot" or text.lower() == "คำสั่ง2":
                            contact = linux.getContact(linuxMID)
                            linux.unsendMessage(msg_id)
                            #s = temp["te"]
                            #a = temp["t"]
                            #true = True
                            timeNow = time.time() - Start
                            runtime = timeChange(timeNow)
                            run = " "
                            run += runtime
                            s = temp["te"]
                            a = temp["t"]
                            true = True
                            duck2Help ="\n🌸 me, ////me"
                            duck2Help +="\n🌸 คท [ คอนแทค ]​"
                            duck2Help +="\n🌸 ไอดีเรา [ เชคMidเรา ]​"
                            duck2Help +="\n🌸 ชื่อเรา "
                            duck2Help +="\n🌸 ตัสเรา "
                            duck2Help +="\n🌸 ดิสเรา, รูปเรา "
                            duck2Help +="\n🌸 ปกเรา "
                            duck2Help +="\n🌸 ข้อมูล [ เชคข้อมูลส่วนตัวเรา ]​ "
                            duck2Help +="\n🌸 รีบอท [ รีสตาร์ทเชล ]​"
                            duck2Help +="\n🌸 ออน [ เชคเวลาทำงานเชล ]​"
                            duck2Help +="\n🌸 เชครัน [ เชคกลุ่มค้างเชิญ ]​"
                            duck2Help +="\n🌸 ลบรัน, /ลบรัน [ ลบกลุ่มค้างเชิญ ]​"
                            duck2Help +="\n🌸 เชคค่า, set [ เชคค่าเปิด/ปิด ]​"
                            duck2Help +="\n🌸 ลงโน๊ต +ข้อความ [ ลงโน๊ตกลุ่ม ]​"
                            duck2Help +="\n🌸 mentionnote [ แทคชื่อลงโน๊ตกลุ่ม ]"
                            duck2Help +="\n🌸 แทค [ แทคทั้งกลุ่ม ]​ "
                            duck2Help +="\n🌸 เทส [ เทสระบบเชล ]​"
#
                            duck3Help ="\n🌸 ลบแชท [ ลบแชททั้งหมด ]​"
                            duck3Help +="\n🌸 คอล +จำนวน [ เชิญคอลกลุ่ม ]​"
                            duck3Help +="\n🌸 โทร +จำนวน @ [ เชิญคอล ]​"
                            duck3Help +="\n🌸 ก็อป @ [ ก็อปปี้ ]​"
                            duck3Help +="\n🌸 กลับร่าง [ กลับร่างเดิม ]​"
                            duck3Help +="\n🌸 ขอรูป +ชื่อ [ ค้นหารูป ]​"
                            duck3Help +="\n🌸 แปรงคท +mid [ แปรงคอนแทค ]​"
                            duck3Help +="\n🌸 ยูทูป +ชื่อ [ ค้นหาในยูทูป ]​"
                            duck3Help +="\n🌸 ขอเพลง +ชื่อ  [ ค้นหาเพลง ]"
                            duck3Help +="\n🌸 ประกาศ: +ข้อความ [ ประกาศ ]"
                            duck3Help +="\n🌸 ประกาศ +ข้อความ [ ประกาศเฟก ]"
                            duck3Help +="\n🌸 ยกเลิก [ เว้นวรรค ]"
                            duck3Help +="\n🌸 ปลดบล็อค +Mid [ ปลดบล็อค ]"
                            duck3Help +="\n🌸 เชคบล็อค [ เชคคนบล็อค ]​"
                            duck3Help +="\n🌸 เพิ่มเพื่อน @ [ แอดเพื่อน ]​"
                            duck3Help +="\n🌸 ลบเพื่อน @ [ ลบเพื่อน ]​"
                            duck3Help +="\n🌸 บล็อค @ [ บล็อคเพื่อน ]​"
#
                            duck4Help ="\n🌸 /เปิดลิ้ง +เลข [ เ​ปิดลิ้งกลุ่ม ]"
                            duck4Help +="\n🌸 เชคกลุ่ม @user [เชคกลุ่มคนแทค] "
                            duck4Help +="\n🌸 ตั้งไลค์ [ ข้อความ ]​"
                            duck4Help +="\n🌸 ตั้งต้อนรับ [ ข้อความ ]"
                            duck4Help +="\n🌸 ตั้งคนออก [ ข้อความ ]"
                            duck4Help +="\n🌸 ตั้งแอด [ ข้อความ ]"
                            duck4Help +="\n🌸 ตั้งแทค [ ข้อความ ]"
                            duck4Help +="\n🌸 ตั้งแทค2 [ ข้อความ ]"
                            duck4Help +="\n🌸 ตั้งแทค3 [ ข้อความ ]"
                            duck4Help +="\n🌸 ตั้งคอมเม้น [ ข้อความ ]"
                            duck4Help +="\n🌸 ตั้งกันรัน [ จำนวน ]"
                            duck4Help +="\n🌸 ตั้งมุดลิ้ง [ ข้อความ ]"
                            duck4Help +="\n🌸 ตั้งบล็อค [ ข้อความ ]"
                            duck4Help +="\n🌸 รหัสสี [ เชครหัสสีต่างๆ ]"
                            duck4Help +="\n🌸 ดึงหมด @ [ ดึงข้อมูล ]"
                            duck4Help +="\n🌸 ดึง @ [ เชิญเข้ากลุ่ม ]​ "
                            duck4Help +="\n🌸 ดึง [ เชิญเข้ากลุ่มแบบลง คท. ]​ "
#
                            duck5Help ="\n🌸 Ssp, speed [ เชคสปีดบอท ]​"
                            duck5Help +="\n🌸 คท   [ คอนแทคเรา ]​"
                            duck5Help +="\n🌸 ชื่อเรา  [ เชคชื่อเรา ]​"
                            duck5Help +="\n🌸 ตัสเรา  [ เชคตัสเรา ]​"
                            duck5Help +="\n🌸 ปกเรา  [ เชคปกเรา ]​"
                            duck5Help +="\n🌸 รูปเรา, ดิสเรา  [ เชครูปเรา ]​"
                            duck5Help +="\n🌸 mid, ไอดี   [ ไอดีประจำตัวเรา ]​"
                            duck5Help +="\n🌸 เครื่องคิดเลข [ ใช้เครื่องคิดเลข ]​"
                            duck5Help +="\n🌸 พูด +ข้อความ [ สิริพูดข้อความ ]"
                            duck5Help +="\n🌸 ยก +เว้นวรรค   [ ยกเลิกข้อความ ]​"
                            duck5Help +="\n🌸 ไอดีไลน์ [ idline ]"
                            duck5Help +="\n🌸 อัพดิสวิดีโอ +ลิงค์ [โปรไฟล์วีดีโอ]​"
                            duck5Help +="\n🌸 เช็คคำห้ามพิม"
                            duck5Help +="\n🌸 คำห้ามพิม [ คำที่ห้าม ]"
                            duck5Help +="\n🌸 ลบคำห้ามพิม [ คำที่ห้าม ] "
                            duck5Help +="\n🌸 บัค [ เชคสถานะเฟก ] "
                            duck5Help +="\n🌸 เชคบัค [ เชคสถานะ ]  "
#
                            duck6Help ="\n🌸 คท「 @ 」    [ ดึงคอนแทค ]​"
                            duck6Help +="\n🌸 ไอดี 「 @ 」    [ ดึงmid ]​"
                            duck6Help +="\n🌸 ชื่อ 「 @ 」  [ ดึงชื่อ ]​"
                            duck6Help +="\n🌸 ตัส   「 @ 」   [ ดึงตัส ]​"
                            duck6Help +="\n🌸 ปก   「 @ 」    [ ดึงปก ]​"
                            duck6Help +="\n🌸 รูป, ดิส  「 @ 」   [ ดึงรูป ]​"
                            duck6Help +="\n🌸 แจก @ +จำนวน / [ ส่งเข้าส่วนตัว ] "
                            duck6Help +="\n🌸 โหล @ +จำนวน / [ สแปมแทค ] "
                            duck6Help +="\n🌸 รันแชท @ [ รันแชทส่วนตัว ]​"
                            duck6Help +="\n🌸 อัพชื่อไวรัส [ ใส่ชือ ]"
                            duck6Help +="\n🌸 อัพชื่อ [ ใส่ชื่อ ]"
                            duck6Help +="\n🌸 อัพตัส [ ใส่ชื่อตัส ]"
                            duck6Help +="\n🌸 ไอดีกลุ่ม [ รหัสกลุ่ม ]"
                            duck6Help +="\n🌸 รูปกลุ่ม, ดิสกลุ่ม [ เชครูปกลุ่ม ]"
                            duck6Help +="\n🌸 ชื่อกลุ่ม [ เชคชื่อกลุ่ม ]"
                            duck6Help +="\n🌸 แอด [ เชคคนสร้างกลุ่ม ]"
                            duck6Help +="\n🌸 .speed [speedflex"
#
                            duck7Help ="\n🌸 เปิด/ปิดบล็อค "
                            duck7Help +="\n🌸 เปิด/ปิดแอด"
                            duck7Help +="\n🌸 เปิด/ปิดแทค"
                            duck7Help +="\n🌸 เปิด/ปิดคอมเม้น"
                            duck7Help +="\n🌸 เปิด/ปิดไลค์"
                            duck7Help +="\n🌸 เปิด/ปิดมุด"
                            duck7Help +="\n🌸 เปิดข้อความบล็อค"
                            duck7Help +="\n🌸 ปิดข้อความบล็อค"
                            duck7Help +="\n🌸 ตั้งบล็อค: +ข้อความ"
                            duck7Help +="\n🌸 ตั้งแทค: +ข้อความ"
                            duck7Help +="\n🌸 ตั้งเข้า: +ข้อความ"
                            duck7Help +="\n🌸 ตั้งออก: +ข้อความ"
                            duck7Help +="\n🌸 ตั้งแอด: +ข้อความ"
                            duck7Help +="\n🌸 เชคค่า [ ดูคำสั่งตั้งค่าทั้งหมด ]"
                            duck7Help +="\n🌸 เปิดลิ้ง [ เปิดลิ้งกลุ่ม ]​"
                            duck7Help +="\n🌸 ปิดลิ้ง [ ปิดลิ้งกลุ่ม ]​"
                            duck7Help +="\n🌸 ลิ้ง [ ขอลิ้งกลุ่ม ]​"
#                    
                            duck8Help ="\n🌸 st1 on/off 「 ติ๊กคนเข้า 」"
                            duck8Help +="\n🌸 st2 on/off 「 ติ๊กคนเข้า 」"
                            duck8Help +="\n🌸 in  on/off「 ต้อนรับคนเข้า 」"
                            duck8Help +="\n🌸 in1 on/off「 ต้อนรับคนเข้า2 」"
                            duck8Help +="\n🌸 out on/off「 ข้อความออก 」"
                            duck8Help +="\n「 🌸ต้อนรับเป็นแบบแยกกลุ่ม🌸 」"
                            duck8Help +="\n🌸 กันลิ้ง เปิด/ปิด「 ป้องกันลิ้ง 」"
                            duck8Help +="\n🌸 กันเข้า เปิด/ปิด「 ป้องกันคนเข้า 」"
                            duck8Help +="\n🌸 กันเชิญ เปิด/ปิด「ป้องกันเชิญ 」"
                            duck8Help +="\n🌸 กันเตะ เปิด/ปิด「 ป้องกันเตะ 」"
                            duck8Help +="\n🌸 ป้องกัน เปิด/ปิด「 เปิด/ปิดป้องกัน」"
                            duck8Help +="\n🌸 เชคป้องกัน「 เชคกลุ่มป้องกัน 」"
                            duck8Help +="\n🌸 เปิด/ปิดยกเลิก「 เชคยกเลิก 」"
                            duck8Help +="\n🌸 เปิด/ปิดแอบ「 เชคคนอ่าน 」"
                            duck8Help +="\n🌸 ทัก +จำนวน( ส่วนตัว )​「 สแปม 」"
                            duck8Help +="\n🌸 เชครัน [ เชคกลุ่มค้างเชิญเรา ]​"
#
                            duck9Help ="\n🌸 ดำ @  [ ยัดดำ ]​"
                            duck9Help +="\n🌸 ขาว @  [ ล้างบัญชีดำ ]​"
                            duck9Help +="\n🌸 เปิดดำ/ปิด [ ส่ง คท.ทีเดียว ]​"
                            duck9Help +="\n🌸 ขาว:เปิด/ปิด [ล้างดำแบบส่ง คท.]​"
                            duck9Help +="\n🌸 Bc, คทดำ [ เชค คท. ดำ ]​"
                            duck9Help +="\n🌸 Cb, ล้างดำ [ล้างบัญชีดำทั้งหมด]​"
                            duck9Help +="\n🌸 เชคดำ [ เชคชื่อบัญชีดำ ]​"
                            duck9Help +="\n🌸 เตะดำ, Kb [ เตะดำในกลุ่ม ]​"
                            duck9Help +="\n🌸 kick @ [ เตะสมาชิก ]​"
                            duck9Help +="\n🌸 สับ +อักษร [ เตะรวบชื่อ ]​"
                            duck9Help +="\n🌸 /ปลิว @ [ เตะรวบแทค ]"
                            duck9Help +="\n🌸 /หาย [ บินกลุ่ม ]"
                            duck9Help +="\n🌸 /ลุย [ บินกลุ่ม ]​"
                            duck9Help +="\n🌸 /ลาก่อน [ ยกเชิญ+บิน ]​"
                            duck9Help +="\n🌸 เที่ยว  [ บินกลุ่ม js ]​"
                            duck9Help +="\n🌸 เชคบัค [ เชคสถานะ ]​"
                            duck9Help +="\n🌸 บัค [ เชคสถานะเฟก ]​"
#                    
                            duck10Help ="\n🌸 /นับ +จำนวน [ สแปมนับเลข ]​"
                            duck10Help +="\n🌸 /เชคยก [ เชคข้อความยกเลิก ]​"
                            duck10Help +="\n🌸 H1 [ คำสั่งระบบคลิกปุ่ม ]​"
                            duck10Help +="\n🌸 H2 [ คำสั่งระบบคลิกปุ่ม2 ]​"
                            duck10Help +="\n🌸 หมุด [ คำสั่งหมุด ]​"
                            duck10Help +="\n🌸 spam [ คำสั่งสแปม ]​"
                            duck10Help +="\n🌸 sticker [ โหมดตั้งค่าสติ้กเกอร์ ]​"
                            duck10Help +="\n🌸 ลูกเล่น [ เกมส์หรรษา ]​"
                            duck10Help +="\n🌸 ระบบเตะ [ คำสั่งเตะทั้งหมด ]​"
                            duck10Help +="\n🌸 protect [ คำสั่งป้องกันกลุ่ม ]​"
                            duck10Help +="\n🌸 js [ คำสั่งพิเศษ ]"
                            duck10Help +="\n🌸 blacklist [ คำสั่ง ขาว/ดำ ]"
                            duck10Help +="\n🌸 ตั้งค่าเรา [ ตั้งค่าเปิด/ปิด ]​"
                            duck10Help +="\n🌸 ประกาศ [ คำสั่งประกาศ ]​"
                            duck10Help +="\n🌸 อัพดิส [อัพโปรไฟล์] "
                            duck10Help +="\n🌸 ยกเชิญ[ยกค้างเชิญ]"
                            duck10Help +="\n🌸 ล่า [ล่าดำทุกกลุ่ม]"
                            data = {
"type": "flex",
"altText": "SELFBOT",
"contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {
"backgroundColor": a
},
"hero": {
"backgroundColor": a
},
"body": {
"backgroundColor": a,
"separator": true,
"separatorColor": s
},
"footer": {
"backgroundColor": a,
"separator": true
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐇𝐄𝐋𝐏𝐌𝐄𝐍𝐔",
"weight": "bold",
"size": "xl",
"color": s,
"margin": "md"
},
{
"type": "text",
"text": "ᴀᴜᴛᴏ ʙᴏᴛ ʟɪɴᴇ",
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "ɴᴀᴍᴇ:{}".format(linux.getContact(sender).displayName),
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "🌸ʀᴜɴᴛɪᴍᴇ🌸\n"+runtime,
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
#},
#{
#"type": "separator",
#"margin": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(sender).pictureStatus),
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px",
"action": {
"uri": "line://ti/p/~anan789anan",
"type": "uri",
}
}
],
"position": "absolute",
"borderWidth": "1px",
"borderColor": a,
"cornerRadius": "10px",
"offsetTop": "50px",
"offsetStart": "206px",
"height": "80px",
"width": "80px"
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "box",
"layout": "vertical",
"margin": "md",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": duck2Help,
"wrap": True,
"align": "start",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
}
]
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "text",
"text": "มองหาพ่อมุงหรอ",
"wrap": True,
"align": "center",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
},
]
}
],
"paddingAll": "15px",
"borderColor": str(uck["uck1"]),
"cornerRadius": "18px",
"borderWidth": "1px",
"backgroundColor": a
}
},
{
"type": "bubble",
"styles": {
"header": {
"backgroundColor": a
},
"hero": {
"backgroundColor": a
},
"body": {
"backgroundColor": a,
"separator": true,
"separatorColor": s
},
"footer": {
"backgroundColor": s,
"separator": true
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐇𝐄𝐋𝐏𝐌𝐄𝐍𝐔",
"weight": "bold",
"size": "xl",
"color": s,
"margin": "md"
},
{
"type": "text",
"text": "ᴀᴜᴛᴏ ʙᴏᴛ ʟɪɴᴇ",
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "ɴᴀᴍᴇ:{}".format(linux.getContact(sender).displayName),
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "🌸ʀᴜɴᴛɪᴍᴇ🌸\n"+runtime,
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
#},
#{
#"type": "separator",
#"margin": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(sender).pictureStatus),
"gravity": "top",
"size": "sm",
"aspectMode": "cover",
#"aspectRatio": "1:1",
"offsetTop": "0px",
"action": {
"uri": "line://ti/p/~anan789anan",
"type": "uri",
}
}
],
"position": "absolute",
"borderWidth": "1px",
"borderColor": a,
"cornerRadius": "10px",
"offsetTop": "50px",
"offsetStart": "206px",
"height": "80px",
"width": "80px"
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "box",
"layout": "vertical",
"margin": "md",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": duck3Help,
"wrap": True,
"align": "start",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
}
]
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "text",
"text": "มองหาพ่อมุงหรอ",
"wrap": True,
"align": "center",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
},
]
}
],
"paddingAll": "15px",
"borderColor": str(uck["uck1"]),
"cornerRadius": "18px",
"borderWidth": "1px",
"backgroundColor": a
}
},
{
"type": "bubble",
"styles": {
"header": {
"backgroundColor": a
},
"hero": {
"backgroundColor": a
},
"body": {
"backgroundColor": a,
"separator": true,
"separatorColor": s
},
"footer": {
"backgroundColor": a,
"separator": true
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐇𝐄𝐋𝐏𝐌𝐄𝐍𝐔",
"weight": "bold",
"size": "xl",
"color": s,
"margin": "md"
},
{
"type": "text",
"text": "ᴀᴜᴛᴏ ʙᴏᴛ ʟɪɴᴇ",
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "ɴᴀᴍᴇ:{}".format(linux.getContact(sender).displayName),
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "🌸ʀᴜɴᴛɪᴍᴇ🌸\n"+runtime,
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
#},
#{
#"type": "separator",
#"margin": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(sender).pictureStatus),
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px",
"action": {
"uri": "line://ti/p/~anan789anan",
"type": "uri",
}
}
],
"position": "absolute",
"borderWidth": "1px",
"borderColor": a,
"cornerRadius": "10px",
"offsetTop": "50px",
"offsetStart": "206px",
"height": "80px",
"width": "80px"
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "box",
"layout": "vertical",
"margin": "md",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": duck4Help,
"wrap": True,
"align": "start",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
}
]
},
{
"type": "separator",
"margin": "xl"
},
{
"type": "text",
"text": "มองหาพ่อมุงหรอ",
"wrap": True,
"align": "center",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
},
]
}
],
"paddingAll": "15px",
"borderColor": str(uck["uck1"]),
"cornerRadius": "18px",
"borderWidth": "1px",
"backgroundColor": a
}
},
{
"type": "bubble",
"styles": {
"header": {
"backgroundColor": a
},
"hero": {
"backgroundColor": a
},
"body": {
"backgroundColor": a,
"separator": true,
"separatorColor": s
},
"footer": {
"backgroundColor": a,
"separator": true
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐇𝐄𝐋𝐏𝐌𝐄𝐍𝐔",
"weight": "bold",
"size": "xl",
"color": s,
"margin": "md"
},
{
"type": "text",
"text": "ᴀᴜᴛᴏ ʙᴏᴛ ʟɪɴᴇ",
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "ɴᴀᴍᴇ:{}".format(linux.getContact(sender).displayName),
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "🌸ʀᴜɴᴛɪᴍᴇ🌸\n"+runtime,
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
#},
#{
#"type": "separator",
#"margin": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(sender).pictureStatus),
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px",
"action": {
"uri": "line://ti/p/~anan789anan",
"type": "uri",
}
}
],
"position": "absolute",
"borderWidth": "1px",
"borderColor": a,
"cornerRadius": "10px",
"offsetTop": "50px",
"offsetStart": "206px",
"height": "80px",
"width": "80px"
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "box",
"layout": "vertical",
"margin": "md",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": duck5Help,
"wrap": True,
"align": "start",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
}
]
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "text",
"text": "มองหาพ่อมุงหรอ",
"wrap": True,
"align": "center",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
},
]
}
],
"paddingAll": "15px",
"borderColor": str(uck["uck1"]),
"cornerRadius": "18px",
"borderWidth": "1px",
"backgroundColor": a
}
},
{
"type": "bubble",
"styles": {
"header": {
"backgroundColor": a
},
"hero": {
"backgroundColor": a
},
"body": {
"backgroundColor": a,
"separator": true,
"separatorColor": s
},
"footer": {
"backgroundColor": a,
"separator": true
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐇𝐄𝐋𝐏𝐌𝐄𝐍𝐔",
"weight": "bold",
"size": "xl",
"color": s,
"margin": "md"
},
{
"type": "text",
"text": "ᴀᴜᴛᴏ ʙᴏᴛ ʟɪɴᴇ",
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "ɴᴀᴍᴇ:{}".format(linux.getContact(sender).displayName),
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "🌸ʀᴜɴᴛɪᴍᴇ🌸\n"+runtime,
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
#},
#{
#"type": "separator",
#"margin": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(sender).pictureStatus),
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px",
"action": {
"uri": "line://ti/p/~anan789anan",
"type": "uri",
}
}
],
"position": "absolute",
"borderWidth": "1px",
"borderColor": a,
"cornerRadius": "10px",
"offsetTop": "50px",
"offsetStart": "206px",
"height": "80px",
"width": "80px"
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "box",
"layout": "vertical",
"margin": "md",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": duck6Help,
"wrap": True,
"align": "start",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
}
]
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "text",
"text": "มองหาพ่อมุงหรอ",
"wrap": True,
"align": "center",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
},
]
}
],
"paddingAll": "15px",
"borderColor": str(uck["uck1"]),
"cornerRadius": "18px",
"borderWidth": "1px",
"backgroundColor": a
}
},
{
"type": "bubble",
"styles": {
"header": {
"backgroundColor": a
},
"hero": {
"backgroundColor": a
},
"body": {
"backgroundColor": a,
"separator": true,
"separatorColor": s
},
"footer": {
"backgroundColor": a,
"separator": true
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐇𝐄𝐋𝐏𝐌𝐄𝐍𝐔",
"weight": "bold",
"size": "xl",
"color": s,
"margin": "md"
},
{
"type": "text",
"text": "ᴀᴜᴛᴏ ʙᴏᴛ ʟɪɴᴇ",
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "ɴᴀᴍᴇ:{}".format(linux.getContact(sender).displayName),
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "🌸ʀᴜɴᴛɪᴍᴇ🌸\n"+runtime,
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
#},
#{
#"type": "separator",
#"margin": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(sender).pictureStatus),
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px",
"action": {
"uri": "line://ti/p/~anan789anan",
"type": "uri",
}
}
],
"position": "absolute",
"borderWidth": "1px",
"borderColor": a,
"cornerRadius": "10px",
"offsetTop": "50px",
"offsetStart": "206px",
"height": "80px",
"width": "80px"
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "box",
"layout": "vertical",
"margin": "md",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": duck7Help,
"wrap": True,
"align": "start",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
}
]
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "text",
"text": "มองหาพ่อมุงหรอ",
"wrap": True,
"align": "center",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
},
]
}
],
"paddingAll": "15px",
"borderColor": str(uck["uck1"]),
"cornerRadius": "18px",
"borderWidth": "1px",
"backgroundColor": a
}
},
{
"type": "bubble",
"styles": {
"header": {
"backgroundColor": a
},
"hero": {
"backgroundColor": a
},
"body": {
"backgroundColor": a,
"separator": true,
"separatorColor": s
},
"footer": {
"backgroundColor": a,
"separator": true
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐇𝐄𝐋𝐏𝐌𝐄𝐍𝐔",
"weight": "bold",
"size": "xl",
"color": s,
"margin": "md"
},
{
"type": "text",
"text": "ᴀᴜᴛᴏ ʙᴏᴛ ʟɪɴᴇ",
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "ɴᴀᴍᴇ:{}".format(linux.getContact(sender).displayName),
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "🌸ʀᴜɴᴛɪᴍᴇ🌸\n"+runtime,
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
#},
#{
#"type": "separator",
#"margin": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(sender).pictureStatus),
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px",
"action": {
"uri": "line://ti/p/~anan789anan",
"type": "uri",
}
}
],
"position": "absolute",
"borderWidth": "1px",
"borderColor": a,
"cornerRadius": "10px",
"offsetTop": "50px",
"offsetStart": "206px",
"height": "80px",
"width": "80px"
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "box",
"layout": "vertical",
"margin": "md",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": duck8Help,
"wrap": True,
"align": "start",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
}
]
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "text",
"text": "มองหาพ่อมุงหรอ",
"wrap": True,
"align": "center",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
},
]
}
],
"paddingAll": "15px",
"borderColor": str(uck["uck1"]),
"cornerRadius": "18px",
"borderWidth": "1px",
"backgroundColor": a
}
},
{
"type": "bubble",
"styles": {
"header": {
"backgroundColor": a
},
"hero": {
"backgroundColor": a
},
"body": {
"backgroundColor": a,
"separator": true,
"separatorColor": s
},
"footer": {
"backgroundColor": s,
"separator": true
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐇𝐄𝐋𝐏𝐌𝐄𝐍𝐔",
"weight": "bold",
"size": "xl",
"color": s,
"margin": "md"
},
{
"type": "text",
"text": "ᴀᴜᴛᴏ ʙᴏᴛ ʟɪɴᴇ",
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "ɴᴀᴍᴇ:{}".format(linux.getContact(sender).displayName),
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "🌸ʀᴜɴᴛɪᴍᴇ🌸\n"+runtime,
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
#},
#{
#"type": "separator",
#"margin": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(sender).pictureStatus),
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px",
"action": {
"uri": "line://ti/p/~anan789anan",
"type": "uri",
}
}
],
"position": "absolute",
"borderWidth": "1px",
"borderColor": a,
"cornerRadius": "10px",
"offsetTop": "50px",
"offsetStart": "206px",
"height": "80px",
"width": "80px"
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "box",
"layout": "vertical",
"margin": "md",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": duck9Help,
"wrap": True,
"align": "start",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
}
]
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "text",
"text": "มองหาพ่อมุงหรอ",
"wrap": True,
"align": "center",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
},
]
}
],
"paddingAll": "15px",
"borderColor": str(uck["uck1"]),
"cornerRadius": "18px",
"borderWidth": "1px",
"backgroundColor": a
}
},
{
"type": "bubble",
"styles": {
"header": {
"backgroundColor": a
},
"hero": {
"backgroundColor": a
},
"body": {
"backgroundColor": a,
"separator": true,
"separatorColor": s
},
"footer": {
"backgroundColor": a,
"separator": true
}
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐇𝐄𝐋𝐏𝐌𝐄𝐍𝐔",
"weight": "bold",
"size": "xl",
"color": s,
"margin": "md"
},
{
"type": "text",
"text": "ᴀᴜᴛᴏ ʙᴏᴛ ʟɪɴᴇ",
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "ɴᴀᴍᴇ:{}".format(linux.getContact(sender).displayName),
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
},
{
"type": "text",
"text": "🌸ʀᴜɴᴛɪᴍᴇ🌸\n"+runtime,
"weight": "bold",
"size": "sm",
"color": s,
"wrap": true
#},
#{
#"type": "separator",
#"margin": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(sender).pictureStatus),
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px",
"action": {
"uri": "line://ti/p/~anan789anan",
"type": "uri",
}
}
],
"position": "absolute",
"borderWidth": "1px",
"borderColor": a,
"cornerRadius": "10px",
"offsetTop": "50px",
"offsetStart": "206px",
"height": "80px",
"width": "80px"
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "box",
"layout": "vertical",
"margin": "md",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": duck10Help,
"wrap": True,
"align": "start",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
}
]
},
{
"type": "separator",
"margin": "xxl"
},
{
"type": "text",
"text": "มองหาพ่อมุงหรอ",
"wrap": True,
"align": "center",
"gravity": "center",
"weight": "bold",
"color": s,
"size": "sm"
},
]
}
],
"paddingAll": "15px",
"borderColor": str(uck["uck1"]),
"cornerRadius": "18px",
"borderWidth": "1px",
"backgroundColor": a
}
}
]
}
}
                            sendTemplate(to, data)                         
                    
                elif text.lower() == "hhhelp" or text.lower() == "คำสั่ง":
                                data = {
                                        "type": "flex",
                                        "altText": "『มองหาพ่อมุงหรอ』",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://sv1.picz.in.th/images/2020/07/04/5x6viJ.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "𝐇𝐄𝐋𝐏 𝐌𝐄𝐒𝐒𝐀𝐆𝐄",
                    "size": "xxl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 คำสั่ง2",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 me, ////me",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 คท [ คอนแทค ]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ไอดีเรา [ เชคMidเรา ]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ชื่อเรา,ตัสเรา",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ดิสเรา,ปกเรา",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ข้อมูล [ข้อมูลส่วนตัวเรา]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 รีบอท [รีสตาร์ทเชล]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ออน [เชคเวลาทำงานเชล]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ลบรัน,/ลบรัน [ลบกลุ่มค้างเชิญ]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เชคค่า,set [เชคค่าเปิด/ปิด]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ลงโน๊ต +ข้อความ [ลงโน๊ตกลุ่ม]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 mentionnote [แทคโน๊ตกลุ่ม]",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "🐶มองหาพ่อมุงหรอ🐶",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~anan789anan"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
#            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "17px",
        "borderColor": "#00FFFF",
        "borderWidth": "3px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://sv1.picz.in.th/images/2020/07/04/5x6viJ.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "𝐇𝐄𝐋𝐏 𝐌𝐄𝐒𝐒𝐀𝐆𝐄",
                    "size": "xxl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เปิดดำ/ปิด [ส่ง คท.ทีเดียว]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ขาว:เปิด/ปิด [ล้างดำแบบส่ง คท.]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ล่า [เตะดำทุกกลุ่ม]",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 Bc, คทดำ [เชค คท. ดำ]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 Cb,ล้างดำ [ล้างดำทั้งหมด]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เชคดำ [เชคชื่อบัญชีดำ]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เตะดำ,Kb [เตะดำในกลุ่ม]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 สับ +อักษร [เตะรวบชื่อ]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 /ปลิว @ [เตะรวบแทค]",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 รวบ +อักษร [เตะรวบตัส]",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 /หาย [บินกลุ่ม]",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เที่ยว  [บินกลุ่ม js]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เชคบัค [เชคสถานะ]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": " ₣₡มองหาพ่อมุงหรอ",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~anan789anan"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
#            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "17px",
        "borderColor": "#00FFFF",
        "borderWidth": "3px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://sv1.picz.in.th/images/2020/07/04/5x6viJ.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "𝐇𝐄𝐋𝐏 𝐌𝐄𝐒𝐒𝐀𝐆𝐄",
                    "size": "xxl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เปิด/ปิดบล็อค",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เปิด/ปิดแอด",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เปิด/ปิดแทค",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เปิด/ปิดคอมเม้น",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เปิด/ปิดไลค์",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เปิด/ปิดมุดลิ้ง",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เปิด/ปิดยกเลิก",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เปิด/ปิด:แอบ",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 กันลิ้ง เปิด/ปิด",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 กันเข้า เปิด/ปิด",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 กันเชิญ เปิด/ปิด",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 กันเตะ เปิด/ปิด",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ป้องกัน เปิด/ปิด",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "₣₡มองหาพ่อมุงหรอ",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~anan789anan"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
#            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "17px",
        "borderColor": "#00FFFF",
        "borderWidth": "3px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://sv1.picz.in.th/images/2020/07/04/5x6viJ.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "𝐇𝐄𝐋𝐏 𝐌𝐄𝐒𝐒𝐀𝐆𝐄",
                    "size": "xxl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 เชคป้องกัน [เชคกลุ่มป้องกัน]",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 /เชคยก [เชคยกเลิก]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 หมุด [คำสั่งหมุด]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 spam [คำสั่งสแปม]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 sticker [โหมดตั้งค่าสติ้กเกอร์]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ลูกเล่น [เกมส์หรรษา]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ระบบเตะ [คำสั่งเตะทั้งหมด]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 protect [คำสั่งป้องกันกลุ่ม]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 js [คำสั่งพิเศษ]",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 blacklist [คำสั่ง ขาว/ดำ]",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ตั้งค่าเรา [ตั้งค่าเปิด/ปิด]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 ประกาศ [คำสั่งประกาศ]​",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "🌸 /แทค [แทคกลุ่ม]",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "₣₡มองหาพ่อมุงหรอ",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~anan789anan"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
#            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "17px",
        "borderColor": "#00FFFF",
        "borderWidth": "3px"
      }
    }
  ]
}
}
                                sendTemplate(to, data) 

                if text.lower() == "คำสั่ง3" or text.lower() == "//help2":
                    sy = "•🍀 คท @\n"
                    sy += "•🍀 ดิส @ \n"
                    sy += "•🍀 ปก @\n"
                    sy += "•🍀 ไอดี @\n"
                    sy += "•🍀 ดึงหมด @\n"
                    sp = "•🍀 ใคร [แปรงคท]\n"
                    sp += "•🍀 /speed\n"
                    sp += "•🍀 ก็อป @\n"
                    sp += "•🍀 กลับร่าง\n"
                    sp += "•🍀 spam on [จำนวน]\n"
                    sh = "•🍀 ยูทูป [ชื่อ]\n"
                    sh += "•🍀 youtube [ชื่อ]\n"
                    sh += "•🍀 ขอรูป [ชื่อ]\n"
                    sh += "•🍀 image [ชื่อ]\n"
                    sh += "•🍀 ยก [ยกเลิกข้อความ]\n"
                    sl = "•🍀 บล็อค @\n"
                    sl += "•🍀 เพิ่มเพื่อน @\n"
                    sl += "•🍀 ลบเพื่อน @\n"
                    sl += "•🍀 เชคบล็อค \n"
                    sl += "•🍀 ปลดบล็อค +mid\n"
                    sk = "•🍀 /เปิดลิ้ง +mid\n"
                    sk += "•🍀 ตั้งไลค์ +ข้อความ\n"
                    sk += "•🍀 ตั้งต้อนรับ +ข้อความ\n"
                    sk += "•🍀 ตั้งคนออก +ข้อความ\n"
                    sk += "•🍀 ตั้งแอด +ข้อความ\n"
                    sq = "•🍀 ตั้งแทค +ข้อความ\n"
                    sq += "•🍀 ตั้งแทค2 +ข้อความ\n"
                    sq += "•🍀 ตั้งแทค3 +ข้อความ\n"
                    sq += "•🍀 ตั้งคอมเม้น +ข้อความ\n"
                    sq += "•🍀 ตั้งกันรัน +ข้อความ\n"
                    sg = "•🍀 อัพชื่อ [ชื่อ]\n"
                    sg += "•🍀 อัพตัส [ชื่อ]\n"
                    sg += "•🍀 อัพดิส \n"
                    sg += "•🍀 อัพปก \n"
                    sg += "•🍀 อัพดิสวิดีโอ\n"
                    dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "• help menu2 •",
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#00FFFF"
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sy,
                                                "color": "#00FFFF", 
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#000000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"『มองหาพ่อมุงหรอ』 ",
                                                     "uri":"line://nv/profilePopup/mid=u5212bf4a8e3b64cb7307e89e4588929f"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "• help menu2 •",
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#00FFFF"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sp, 
                                                "color": "#00FFFF",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#000000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"『Ẫµŧø ฿øŧĹįח€』",
                                                     "uri":"line://nv/profilePopup/mid=u5212bf4a8e3b64cb7307e89e4588929f"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "• help menu2 •",
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#00FFFF"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sh, 
                                                "color": "#00FFFF",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#000000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"มองหาพ่อมุงหรอ』",
                                                     "uri":"line://nv/profilePopup/mid=u5212bf4a8e3b64cb7307e89e4588929f"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
									"type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "• help menu2 •",
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#00FFFF"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                           #     "text": " "
                                         #   },
                                         #   {
                                            #    "type": "text",
                                           #     "text": " "
                                          #  },
                                            {
                                                "type": "text",
                                                "text": sl, 
                                                "color": "#00FFFF",
                                           #     "size": "lg",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            #{
                                            #    "type": "text",
                                            #    "text": " "
                                           # },
                                          #  {
                                           #     "type": "text",
                                            #    "text": " "
                                           # },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                          #      "text": "สนใจบอท ติดต่อได้ที่ปุ่มเลยค้ะ >_<",
                                          #      "color": "#B5B5B5",
                                          #      "size": "xs"
                                          #  },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#000000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"มองหาพ่อมุงหรอ』 ",
                                                     "uri":"line://nv/profilePopup/mid=u5212bf4a8e3b64cb7307e89e4588929f"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "• help menu2 •",
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#00FFFF"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sk, 
                                                "color": "#00FFFF",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#000000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"มองหาพ่อมุงหรอ』 ",
                                                     "uri":"line://nv/profilePopup/mid=u5212bf4a8e3b64cb7307e89e4588929f"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "• help menu2 •",
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#00FFFF"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sq, 
                                                "color": "#00FFFF",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#000000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"『มองหาพ่อมุงหรอ』 ",
                                                     "uri":"line://nv/profilePopup/mid=u5212bf4a8e3b64cb7307e89e4588929f"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "• help menu2 •",
                                                "size": "xl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#00FFFF"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sg, 
                                                "color": "#00FFFF",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#000000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"『มองหาพ่อมุงหรอ』 ",
                                                     "uri":"line://nv/profilePopup/mid=u5212bf4a8e3b64cb7307e89e4588929f"
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                    data = {
                                "type": "flex",
                                "altText": "Help Message",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                    sendTemplate(to, data)

                if text.lower() == "////help" or text.lower() == "/////คำสั่ง":
                            sa = "•🍀 Me\n"
                            sa += "•🍀 คท [ คอนแทค ]​\n"
                            sa += "•🍀 ไอดีเรา [ Midเรา ]​\n"
                            sa += "•🍀 ชื่อเรา\n"
                            sa += "•🍀 ตัสเรา\n"
                            sa += "•🍀 ดิสเรา, รูปเรา\n"
                            sa += "•🍀 ปกเรา\n"
                            sa += "•🍀 ข้อมูล [ ข้อมูลเรา ]​\n"
                            sa += "•🍀 รีบอท [ รีสตาร์ท ]​\n"
                            sa += "•🍀 ออน\n"
                            sa += "•🍀 เชครัน [ ค้างเชิญ ]​\n"
                            sa += "•🍀 ลบรัน, /ลบรัน\n"
                            sa += "•🍀 เชคค่า, set\n"
                            sa += "•🍀 ลงโน๊ต +ข้อความ\n"
                            sa += "•🍀 mentionnote\n"
                            sa += "•🍀 แทค [ แทคทั้งกลุ่ม ]​\n"
                            ss = "•🍀 ลบแชท [ ทั้งหมด ]​\n"
                            ss += "•🍀 มาคลอ +จำนวน [คอลกลุ่ม ]​\n"
                            ss += "•🍀 /โทร +จำนวน @ [ เชิญคอล ]​\n"
                            ss += "•🍀 ก็อป @ [ ก็อปปี้ ]​\n"
                            ss += "•🍀 กลับร่าง [ กลับร่างเดิม ]​\n"
                            ss += "•🍀 ขอรูป +ชื่อ [ ค้นหารูป ]​\n"
                            ss += "•🍀 แปรงคท +mid\n"
                            ss += "•🍀 ยูทูป +ชื่อ [ ค้นหายูทูป ]​\n"
                            ss += "•🍀 ขอเพลง +ชื่อ  [ ค้นหาเพลง ]\n"
                            ss += "•🍀 ประกาศ: +ข้อความ\n"
                            ss += "•🍀 ประกาศ +ข้อความ[เฟค]\n"
                            ss += "•🍀 ยกเลิก [ เว้นวรรค ]\n"
                            ss += "•🍀 ปลดบล็อค +Mid\n"
                            ss += "•🍀 เชคบล็อค [ เชคคนบล็อค ]​\n"
                            ss += "•🍀 เพิ่มเพื่อน @ [ แอดเพื่อน ]​\n"
                            ss += "•🍀 บล็อค @ [ บล็อคเพื่อน ]​\n"
                            se = "•🍀 ดำ @  [ ยัดดำ ]​.\n"
                            se += "•🍀 ขาว @  [ ล้างดำ ]​\n"
                            se += "•🍀 เปิดดำ\ปิดดำ\n"
                            se += "•🍀 ขาว:เปิด\ขาว:ปิด\n"
                            se += "•🍀 Bc, คทดำ [ เชค คท. ดำ ]​\n"
                            se += "•🍀 Cb, ล้างดำ [ ล้างดำทั้งหมด ]​\n"
                            se += "•🍀 เชคดำ [ เชคบัญชีดำ \n"
                            se += "•🍀 เตะดำ, Kb [ เตะดำในกลุ่ม ]​\n"
                            se += "•🍀 kick @ [ เตะสมาชิก ]​\n"
                            se += "•🍀 สับ +อักษร [ เตะรวบชื่อ ]​\n"
                            se += "•🍀 /ปลิว @ [ เตะรวบแทค ]\n"
                            se += "•🍀 /หาย [ บินกลุ่ม ]\n"
                            se += "•🍀 เที่ยว  [ บินกลุ่ม js ]​\n"
                            se += "•🍀 เชคบัค [ เชคสถานะ ]​\n"
                            se += "•🍀 บัค [ เชคสถานะเฟก ]​\n"
                            sd = "•🍀 เปิด/ปิดบล็อค\n"
                            sd += "•🍀 เปิด/ปิดแอด\n"
                            sd += "•🍀 เปิด/ปิดแทค\n"
                            sd += "•🍀 เปิด/ปิดคอมเม้น\n"
                            sd += "•🍀 เปิด/ปิดไลค์\n"
                            sd += "•🍀 เปิด/ปิดมุด\n"
                            sd += "•🍀 กันลิ้ง เปิด/ปิด\n"
                            sd += "•🍀 กันเข้า เปิด/ปิด\n"
                            sd += "•🍀 กันเชิญ เปิด/ปิด\n"
                            sd += "•🍀 กันเตะ เปิด/ปิด\n"
                            sd += "•🍀 ป้องกัน เปิด/ปิด\n"
                            sd += "•🍀 เชคป้องกัน[เชคกลุ่มป้องกัน]\n"
                            sd += "•🍀 เปิด/ปิดยกเลิก\n"
                            sd += "•🍀 เปิด/ปิดแอบ[เชคคนอ่าน]\n"
                            sd += "•🍀 ทัก +จำนวน( ส่วนตัว )​\n"
                            sd += "•🍀 ปิดลิ้ง/เปิดลิ้ง\n"
                            sti = "•🍀 /นับ +จำนวน\n"
                            sti += "•🍀  /เชคยก [ เชคยกเลิก ]​\n"
                            sti += "•🍀 H1 [ คำสั่งระบบคลิกปุ่ม ]​\n"
                            sti += "•🍀 H2 [ คำสั่งระบบคลิกปุ่ม ]​\n"
                       #     sti += "• ตั้งติ๊กแทคแชท\n"
                       #     sti += "• ลบติ๊กแทคแชท\n"
                            sti += "•🍀 หมุด [ คำสั่งหมุด ]​\n"
                            sti += "•🍀 spam [ คำสั่งสแปม ]​\n"
                            sti += "•🍀 sticker [ โหมดตั้งค่าsticker ]​\n"
                            sti += "•🍀 ลูกเล่น [ เกมส์หรรษา ]​\n"
                            sti += "•🍀 ระบบเตะ [ คำสั่งเตะ ]​\n"
                            sti += "•🍀 protect\n"
                            se += "•🍀 js [ คำสั่งพิเศษ ]\n"
                            sti += "•🍀 blacklist [ คำสั่ง ขาว/ดำ ]\n"
                            sti += "•🍀 ตั้งค่าเรา [ ตั้งค่าเปิด/ปิด ]​\n"
                            sti += "•🍀 ประกาศ [ คำสั่งประกาศ ]​\n"
                            sti += "•🍀 ลบเพื่อน @user\n"
                            sti += "•🍀 รวบ +อักษร[เตะรวบตัส]\n"
                            sti += "•🍀 ล่า [ล่าดำทุกกลุ่ม]\n"
                            contact = linux.getContact(sender)
                            sendTemplate(to,{"type":"flex","altText": "Help Message","contents":{"type":"carousel","contents":[{"type":"bubble","footer":{"type":"box","layout":"baseline","contents":[{"color": "#00FFFF","size":"md","wrap":True,"action":{"type":"uri","uri":"http://line.me/ti/p/~anan789anan"},"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51566.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51555.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51564.png"},{"type":"separator","color":"#00FFFF"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#00FFFF"},{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"xs","wrap":True,"type":"text","text":"🕉нĕlρв૦t¹🕉","weight":"bold"},{"type":"text","text":sa,"size":"xxs","wrap":True,"color":"#00FFFF"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"}},{"type":"bubble","footer":{"type":"box","layout":"baseline","contents":[{"color":"#00FFFF","size":"md","wrap":True,"action":{"type":"uri","uri":"https://line.me/R/ti/p/~anan789anan"},"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/03/12/51566.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51555.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51564.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/11905.png"},{"type":"separator","color":"#00FFFF"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#00FFFF"},{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"xs","wrap":True,"type":"text","text":"🕉нĕlρв૦t¹🕉","weight":"bold"},{"type":"text","text":ss,"size":"xxs","wrap":True,"color":"#00FFFF"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"}},{"type":"bubble","footer":{"type":"box","layout":"baseline","contents":[{"color":"#00FFFF","size":"md","wrap":True,"action":{"type":"uri","uri":"https://line.me/R/ti/p/~anan789anan"},"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/03/12/51566.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51555.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51564.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/11905.png"},{"type":"separator","color":"#00FFFF"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#00FFFF"},{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"xs","wrap":True,"type":"text","text":"🕉нĕlρв૦t¹🕉","weight":"bold"},{"type":"text","text":se,"size":"xxs","wrap":True,"color":"#00FFFF"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"}},{"type":"bubble","footer":{"type":"box","layout":"baseline","contents":[{"color":"#00FFFF","size":"md","wrap":True,"action":{"type":"uri","uri":"https://line.me/R/ti/p/~anan789anan"},"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/03/12/51566.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51555.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51564.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/11905.png"},{"type":"separator","color":"#00FFFF"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#00FFFF"},{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"xs","wrap":True,"type":"text","text":"🕉нĕlρв૦t¹🕉","weight":"bold"},{"type":"text","text":sd,"size":"xxs","wrap":True,"color":"#00FFFF"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"}},{"type":"bubble","footer":{"type":"box","layout":"baseline","contents":[{"color":"#00FFFF","size":"md","wrap":True,"action":{"type":"uri","uri":"https://line.me/R/ti/p/~anan789anan"},"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/03/12/51566.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51555.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/51564.png"},{"type":"separator","color":"#00FFFF"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/03/12/11905.png"},{"type":"separator","color":"#00FFFF"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#00FFFF"},{"type":"box","contents":[{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#00FFFF"},{"color":"#00FFFF","size":"xs","wrap":True,"type":"text","text":"🕉нĕlρв૦t¹🕉","weight":"bold"},{"type":"text","text":sti,"size":"xxs","wrap":True,"color":"#00FFFF"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"}}]}})
#=====================================================================
#=====================================================================
                elif msg.text.lower().startswith("ทัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    for x in range(jml):
                        name = linux.getContact(to)
                        RhyN_(to, name.mid)
                elif msg.text.lower().startswith("ก็อป "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = linux.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = linux.getContact(she);ClonerV2(she)
                                    sendMention(to, contact.mid, "=͟͟͞͞➳ คุณกำลังก็อปปี้", "สำเร็จแล้ว >_<");linux.sendContact(to, str(BackupProfile.mid));linux.sendContact(to, str(contact.mid))
                elif text.lower() == "กลับร่าง":
                            try:
                                linuxstatus = linux.getProfile()
                                linuxName = linux.getProfile()
                                linuxName.statusMessage = ProfileMe["statusMessage"]
                                linuxName.pictureStatus = str(ProfileMe["pictureStatus"])
                                linux.updateProfile(linuxstatus)
                                linuxName.displayName = ProfileMe["NameMe"]
                                linux.updateProfile(linuxName)
                                path = linux.downloadFileURL(ProfileMe["PictureMe"])
                                linux.updateProfilePicture(path)
                                coverId = ProfileMe["coverId"]
                                linux.updateProfileCoverById(coverId)
                                BackupProfile = linux.getContact(sender)
                                sendMention(to, BackupProfile.mid, "=͟͟͞͞➳ กลับบัญชีเดิมเรียบร้อย", ">_<");linux.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
#                            	linux.sendMessage(to,"คุณยังไม่ได้ก็อปปี้ User >_<")
                                linux.unsendMessage(msg_id)
                                linux.sendMessage(to, "🌸 คุณยังไม่ได้ก็อปปี้ User 🌸")
#==========================================================================================================================================             
                elif text.lower() == 'ลิ้งเฟก' or text.lower() == "กดเฟก":
                	linux.sendMessage(msg.to, "line://app/1602687308-GXq4Vvk9?type=text&text=ನาછ௫าຣUิюਹิನาю")
                elif text.lower() == 'ลิ้งออน' or text.lower() == "ลิ้งเชล":
                	linux.sendMessage(msg.to, "line://app/1602687308-GXq4Vvk9?type=text&text=ออน")
                elif text.lower() == 'ลิ้งบอท' or text.lower() == "ลิ้งเซล":
                	linux.sendMessage(msg.to, "line://app/1602687308-GXq4Vvk9?type=text&text=คำสั่ง")      
#==========================================================================================================================================                                                    
                if text.lower() == "คท":
                    linux.generateReplyMessage(msg.id) 
                    linux.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': linuxMID}, contentType=13)
                if text.lower() == "mid" or text.lower() == "ไอดีเรา":
                    linux.generateReplyMessage(msg.id)
                    linux.sendReplyMessage(msg.id, to,linuxMID)
                elif text.lower() == "myname" or text.lower() == "ชื่อเรา":
                            h = linux.getContact(linuxMID)
                            linux.generateReplyMessage(msg.id)
                            linux.sendReplyMessage(msg.id, to, "「 ชื่อของคุณ 」\n"+str(h.displayName))
                elif text.lower() == "mybio" or text.lower() == "ตัสเรา":
                            h = linux.getContact(linuxMID)
                            linux.generateReplyMessage(msg.id)
                            linux.sendReplyMessage(msg.id, to, "「 ตัสของคุณ 」\n"+str(h.statusMessage))
                elif text.lower() == "mypicture" or text.lower() == "รูปเรา":
                            h = linux.getContact(linuxMID)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            linux.generateReplyMessage(msg.id)
                            linux.sendReplyImageWithURL(msg.id, to, image)
                elif text.lower() == "myvideo" or text.lower() == "รูปวีดีโอเรา":
                            h = linux.getContact(linuxMID)
                            if h.videoProfile == None:
                            	return linux.sendMessage(to, "คุณไม่ได้ใส่รูปวีดีโอ >_<")
                            linux.generateReplyMessage(msg.id)
                            linux.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                elif text.lower() == "mycover" or text.lower() == "ปกเรา":
                            h = linux.getContact(linuxMID)
                            cu = linux.getProfileCoverURL(linuxMID)
                            image = str(cu)
                            linux.generateReplyMessage(msg.id)
                            linux.sendReplyImageWithURL(msg.id, to, image)
                if text.lower() == "////me":
                    cover = linux.getProfileCoverURL(linux.profile.mid)
                    pp = linux.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = linux.getProfile().displayName
                    status = linux.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText":"{} sendFlex".format(name),"contents":{"type":"bubble",'styles': {"body":{"backgroundColor":a}},"hero":{"type":"image","url":cover,"size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":" "},{"type":"image","url":profile,"size":"lg"},{"type":"text","text":" "},{"type":"text","text":name,"size":"xl","weight":"bold","color":s,"align":"center"},{"type":"text","text":" "},{"type":"text","text":status,"align":"center","size":"xs","color":s,"wrap":True},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#FF00FF","action":{"type":"uri","label":"ADD ME","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://i.pinimg.com/originals/63/c4/12/63c412c55c99b6e0742bebaf53dd40d6.jpg"}}]}}}
                    sendTemplate(to, data)

                elif cmd == "me":
                            contact = linux.getContact(linuxMID)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + linuxMID
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + linuxMID + "/vp"
                            data = {
                                "type": "flex",
                                "altText": "{} Send Flex".format(linux.getProfile().displayName),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#000000'
                                            },
                                            "body": {
                                                "backgroundColor": '#000000'
                                            },
                                            "footer": {
                                                "backgroundColor": '#000000'
                                            },
                                        },
                                    "header": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "weight": "bold",
                                                "color": "#00F5FF",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://nv/profilePopup/mid=u483e96e999cbcda7130543540dd72adf"
                                        }
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "Name :",
                                                                "color": "#00F5FF",
                                                                "size": "sm",
                                                                "flex": 0
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(contact.displayName),
                                                                "color": "#00F5FF",
                                                                "size": "sm",
                                                                "flex": 1
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "Status :",
                                                                "color": "#00F5FF",
                                                                "size": "sm",
                                                                "flex": 0
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(contact.statusMessage),
                                                                "color": "#00F5FF",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 1
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "MyProfile",
                                                    "uri": "http://line.me/ti/p/~anan789anan"
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0
                                    }
                                }
                            }
                            sendTemplate(to, data)
#---------------เฟก..-------------------------------------------------------------------------------------
                elif text.lower() == 'โปรไฟล์':
                    me = linux.getContact(linuxMID)
                    cover = linux.getProfileCoverURL()
                    pp = me.pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = "\n" + me.displayName
                    status = linux.getProfile().statusMessage
                    d = linuxMID
                    data={
"type":"flex",
"altText":"🍎My Profile🍎",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"body": {"backgroundColor": "#000000"},
"footer": {"backgroundColor": "#000000"},
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "image",
"url": cover,
"size": "full",
"aspectMode": "cover",
"aspectRatio": "150:98",
"position": "relative",
"margin": "none",
"align": "center",
"flex": 1
}
]
},
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": profile,
"size": "xl",
"position": "relative",
"margin": "none",
"align": "end",
"gravity": "top",
"aspectMode": "cover"
}
],
"cornerRadius": "100px",
"width": "72px",
"height": "72px",
"margin": "xxl",
"spacing": "xxl",
"position": "relative",
"borderColor": str(uck['uck1']),
"borderWidth": "1px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "text",
"text": " "
}
],
"spacing": "sm",
"margin": "md"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": name,
"size": "sm",
"color": str(uck['uck3'])
},
{
"text": "   🌸 My Profile 🌸 ",
"size": "xs",
"margin": "none",
"color": str(uck["uck2"]),
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"spacing": "sm",
"margin": "md"
}
]
}
],
"spacing": "xl",
"paddingAll": "20px",
"paddingTop": "10px",
"paddingBottom": "10px",
"paddingStart": "20px",
"paddingEnd": "20px",
"borderColor": str(uck['uck1']),
"paddingAll": "3px",
"borderColor": str(uck['uck1']),
"cornerRadius": "20px",
"flex": 1,
"borderWidth": "1px"
}
],
"paddingAll": "3px",
"backgroundColor": "#000000",
"borderWidth":"2px",
"borderColor":str(uck['uck1']),
"cornerRadius":"xl"
}
}
]
}
}
                    sendTemplate(to,data)
#----------------------------------------------------------------------------------------------------                            

                elif text.lower() == "/runtime" or text.lower() == "runtime":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "「 เวลาออน 」\n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(linux.getContact(linuxMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=u483e96e999cbcda7130543540dd72adf"
                        }
                    }
                    sendTemplate(to, data)


                if text.lower() == 'ออน':
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = " "
                    run += runtime
                    data = {
"type":"flex",
"altText":" มีคนกล่าวถึงคุณ ",
"contents":{
"type":"bubble",
"body":{
"type":"box",
"layout":"vertical",
"contents":[
{
"type": "text",
"text": " มองหาพ่อมุงหรอ ",
"color":str(uck["uck2"]),
"gravity": "center",
"align":"center",
"wrap": True,
"size": "sm"
},
{
"type": "text",
"text": "{}".format(run),
"color": str(uck['uck3']),
"gravity": "center",
"align":"center",
"wrap": True,
"size": "md"
},
{
"type":"box",
"layout":"vertical",
"margin":"lg",
"contents":[
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
"size":"full",
"aspectMode":"cover"
}
],
"width":"40px",
"height":"40px",
"cornerRadius":"100px",
"borderColor":str(uck['uck1']),
"borderWidth":"2px"
},
{
"type":"text",
"text":"                ติดต่อ",
"color":str(uck["uck2"]),
"align":"start",
"gravity":"center",
"size":"sm",
"action": {
"uri": "line://ti/p/~"+str(linux.getProfile().userid),
#"uri": str(uu['uuu']),
"type": "uri"
},
"margin":"xl",
"weight":"bold"
}
]
}
],
"spacing": "xl",
"paddingAll": "20px",
"paddingTop": "10px",
"paddingBottom": "10px",
"paddingStart": "20px",
"paddingEnd": "20px",
"paddingAll": "3px",
"borderColor": str(uck['uck1']),
"cornerRadius": "20px",
"flex": 1,
"borderWidth": "1px"
}
],
"paddingAll": "3px",
"backgroundColor": "#000000",
"borderWidth":"2px",
"borderColor":str(uck['uck1']),
"cornerRadius":"xl"
}
}
}
                    sendTemplate(to, data)
                        
                elif text.lower() == "รีบอท" or text.lower() == "reset":
                    gifnya = ["https://sv1.picz.in.th/images/2019/08/02/KagdAP.gif"]
                    data = {
                        "type": "template",
                        "altText": "กำลังรีบอท...",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~anan789anan"
                                     }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, data)
                    time.sleep(1)
                    ga = "สำเร็จแล้ว (｀・ω・´)"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(ga)),
                        "sentBy": {
                             "label": "รีบอทสำเร็จ...",
                             "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=u483e96e999cbcda7130543540dd72adf"
                        }
                    }
                    sendTemplate(to, data)
                    restartBot()
                elif text.lower() == ":ree" or text.lower() == "!ree":
                    linux.sendMessage(to, "🆙อัพเดทระบบ🆙")                
                    linux.sendMessage(to, "กรุณารอสักครู่❗")
                    linux.sendMessage(to, "รีสตาร์ทเรียบร้อย ✓") 
                    restartBot()                                   
                if text.lower() == "/speed" or text.lower() == ".sp" or text.lower() == "/สปีด":
                    start = time.time()
#                    linux.sendMessage("ufdd706a81ff7557b83592e3b134c6e61","speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "speed vps: %.10f ᴍs" % (took)
                    data = {"type": "text","text": "{}".format(a),"sentBy": {"label": "%.10f" % (elapsed_time), "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u483e96e999cbcda7130543540dd72adf"}}
                    #
                    sendTemplate(to,data)
                if text.lower() == "ssp" or text.lower() == "สปีด2" or text.lower() == "/spb":
                    start = time.time()                                        
                    elapsed_time = time.time() - start
                    linux.sendMessage(to, " %.10f ᴍs" % (elapsed_time)) 
                if text.lower() == "speed" or text.lower() == "สปีด" or text.lower() == "เร็ว":
#                    linuxbotTemplate(to, "♡╬╬♡•ຟနุ้७ຟနิ้७•♡╬╬♡")                    
#                    linuxbotTemplate(to, "•─ ͜͡✯͜͡S͜͡p͜͡e͜͡e͜͡e͜͡d✯͜͡ѕ͜͡є͜͡ʟ͜͡ғ͜͡в͜͡о͜͡т͜͡✯─•")                    
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    linux.sendMessage(to, "%s ᴍs" % (elapsed_time)) 
                if text.lower() == "sp" or text.lower() == "/สปีด2" or text.lower() == "เร็วจัง":
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    linux.sendMessage(to, "%s ᴍs" % (elapsed_time)) 
                if text.lower() == "spb" or text.lower() == "/สปีด3" or text.lower() == "เร็วจัง2":
                    start = time.time()
                    time.sleep(0.01)
                    elapsed_time = time.time() - start
                    linux.sendMessage(to, "%.6f ᴍs" % (elapsed_time))         
                if text.lower() == "/speed" or text.lower() == "สปีดบอท":
                    contact = linux.getContact(linuxMID)
                    start = time.time()
#                    linux.sendMessage("ufdd706a81ff7557b83592e3b134c6e61","test speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "ความเร็ว : %.10f วินาที" % (took)
                    data = {
                        "type": "flex",
                        "altText": "BotSpeed",
                        "contents": {
                            "type": "bubble",
                            "hero": {
                                "type":"image",
                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                "size": "full",
                                "aspectRatio": "1:1",
                                "aspectMode": "fit"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": a,
                                        "wrap": True,
                                        "color":"#00F5FF",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "xl"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "/speed" or text.lower() == "//สปีด":                       
                    contact = linux.getContact(sender)
                    start = time.time()
#                    linux.sendMessage(to, "ทดสอบความเร็ว")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "Speed..\nความเร็วคงที่\nTook: %.10f ms \nสปีดความเร็วบอท: %10f " % (took,elapsed_time)
                    LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                    LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"                            
                    data = {
                        "type": "flex",
                                "altText": "{}".format(a),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#003366'
                                            },
                                            "footer": {
                                                "backgroundColor": '#003366'
                                                 },
                                              },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                                "size": "full",
                                                "aspectRatio": "1:1",
                                                "aspectMode": "fit",
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text":  "{}".format(a),
                                                                "color": "#8DEEEE",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 1    
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "🅰🆄🆃🅾 🅱🅾🆃🅻🅸🅽🅴",
                                                    "uri": "http://line.me/ti/p/~anan789anan"
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0        
                                    }
                                }
                            }
                    sendTemplate(to, data)     
                elif "อ่านแชท @" in msg.text:
                    _name = msg.text.replace("อ่านแชท @","")
                    _nametarget = _name.rstrip(' ')
                    gs = linux.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           linux.sendMessage(g.mid,"/ไวรัส")
                           linux.sendMessage(g.mid,"/ไวรัส")
                           linux.sendMessage(g.mid,"/ไวรัส")
                           linux.sendMessage(g.mid,"/ไวรัส")
                           linux.sendMessage(g.mid,"/ไวรัส")
                           linux.sendMessage(g.mid,"หวัดดีจ้า.. 😁")
                           print (" Spammed !")
                elif "รันแชท @" in msg.text:
                    _name = msg.text.replace("รันแชท @","")
                    _nametarget = _name.rstrip(' ')
                    gs = linux.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(g.mid,"💖 มาส่งรักนะ จุ๊ฟๆ")
                           linux.sendMessage(msg.to, "เรียบร้อย")
                           print (" Spammed !")
                elif msg.text in ["/เปิดแอบ"]:
                    try:
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        linux.sendMessage(to, "👑 เปิดระบบจับคนแอบ 👑\n\n👑วันที่ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n👑 เวลา 👑 [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                        del cctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    linux.sendMessage(msg.to,"👑เปิดระบบแสกนคนอ่านอัตโนมัติ👑")

                elif msg.text == "/ปิดแอบ":
                  if msg.to in RfuCctv['point']:
                      tz = pytz.timezone("Asia/Jakarta")
                      timeNow = datetime.now(tz=tz)
                      RfuCctv['cyduk'][msg.to]=False
                      linux.sendMessage(to, "👑 ปิดระบบจับคนแอบ 👑\n\n👑วันที่ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n👑 เวลา 👑 [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                  else:
                      linux.sendMessage(to, "👑ระบบปิดอยู่👑")
                elif msg.text in [".ดึง"]:
                        settings["winvite"] = True
#                        linux.unsendMessage(msg_id)
                        linux.sendMessage(to, "👑 กรุณาส่งคท ที่ต้องการเชิญ 👑")                       
                elif text.lower() == 'ข้อมูล' or text.lower() == "about":
                    try:
                        arr = []
                        owner = "u121f13781bbdfdd3e9e550ca120b5372"
                        creator = linux.getContact(owner)
                        contact = linux.getContact(linuxMID)
                        grouplist = linux.getGroupIdsJoined()
                        contactlist = linux.getAllContactIds()
                        blockedlist = linux.getBlockedContactIds()
                        IdsInvit = linux.getGroupIdsInvited()
                        times = time.time() - Start
                        runtime = timeChange(times)
                        ret_ = "╭───「 About Your 」"
                        ret_ += "\n├ ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n├ กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n├ เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n├ บล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n├ ค้างเชิญ : {}".format(str(len(IdsInvit)))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ เวลาออนบอท :"
                        ret_ += "\n├ {}".format(str(runtime))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ ผู้สร้าง : {}".format(str(creator.displayName))
                        ret_ += "\n╰───「 About Your 」"
                        feds = "{}".format(str(ret_))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret_)),
                            "sentBy": {
                                 "label": "{}".format(linux.getContact(linuxMID).displayName),
                                 "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
                                 "linkUrl": "http://line.me/ti/p/~anan789anan"
                            }
                        }
                        sendTemplate(to, data)
                        linux.sendContact(msg.to, creator.mid)
                    except Exception as e:
                        linux.sendMessage(msg.to, str(e))
                        
                elif msg.text in ["ดิสสมาชิก"]:
                    group = linux.getGroup(to)
                    group = group.members
                    picall = []
                    for ids in group:
                       if len(picall) >= 400:
                         pass
                       else:
                         picall.append({
                        "imageUrl": "https://os.line.naver.jp/os/p/{}".format(linuxMID),
                        "action": {
                          "type": "uri",
                          "uri": "http://line.me/ti/p/~anan789anan" }  } )
                    k = len(picall)//10
                    for aa in range(k+1):
                      data = {
                      "type": "template",
                      "altText": "『มองหาพ่อมุงหรอ』",                                         
                      "template": {
                         "type": "image_carousel",
                         "columns": picall[aa*10 : (aa+1)*10]
                      }}
                      sendTemplate(to, data)
                        
                elif text.lower() == "xxxx":
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
                                                "uri": "http://line.me/ti/p/~anan789anan"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "xxxxx" or text.lower() == "xxxxx":
                            gifnya = ['https://i.pinimg.com/originals/25/bf/35/25bf35850f22b00ff04505f173e16ec8.gif']
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
                                                "uri": "http://line.me/ti/p/~anan789anan"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text.lower().startswith("อัพดิสวีดีโอ"):
                            link = removeCmd("อัพดิสวีดีโอ", text)
                            contact = linux.getContact(sender)
                            linux.sendMessage(to, "ประเภท: โปรไฟล์\n • รายละเอียด: เปลี่ยน URL วิดีโอ\n • สถานะ: ดาวน์โหลด ...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = linux.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            changeVideoAndPictureProfile(pict, vids)
                            linux.sendMessage(to, "ประเภท: โปรไฟล์\n • รายละเอียด: เปลี่ยน URL วิดีโอ\n • สถานะ: สำเร็จ")
                            os.remove("TeamAnuBot.mp4")
#=====================================================================
                elif msg.text.lower().startswith("ดำ "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        LnBots["blacklist"][ls] = True
                                        linux.sendMessage(to, '🌸 ลงบัญชีดำเรียบร้อย 🌸')
                                    except:
                                        pass
                elif msg.text.lower().startswith("ขาว "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del LnBots["blacklist"][ls]
                                        linux.sendMessage(to, '🌸 ลบออกจากบัญชีดำ 🌸')
                                    except:
                                        pass                            
#=====================================================================
                elif msg.text.lower().startswith("คท "):
#                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:    
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = linux.getContact(ls)
                            mi_d = contact.mid
                            linux.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("ไอดี "):
#                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:    
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        linux.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
#                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                    if 'MENTION' in msg.contentMetadata.keys()!= None: 
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = linux.getContact(ls)
                            linux.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ดิส "):
#                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                    if 'MENTION' in msg.contentMetadata.keys()!= None: 
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + linux.getContact(ls).pictureStatus
                            linux.sendImageWithURL(msg.to, str(path))                                
                elif msg.text.lower().startswith("ตัส "):
#                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = linux.getContact(ls)
                            linux.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("ปก "):
                    if linux != None:
#                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = linux.getProfileCoverURL(ls)
                                linux.sendImageWithURL(msg.to, str(path))
                elif msg.text.startswith("ดึงหมด "):
                    if linux != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                                for ls in lists:
                                    me = linux.getContact(ls)
                                    path = linux.getProfileCoverURL(ls)
                                    path = str(path)
                                    if settings["server"] == "VPS":
                                        linux.sendMessage(msg.to,"「ชื่อที่แสดง」\n" + me.displayName)
                                        linux.sendMessage(msg.to,"「 สถานะข้อความ 」\n" + me.statusMessage)
                                        linux.sendMessage(msg.to,"「 MID 」\n" +  to)
                                        linux.sendMessage(to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                        linux.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                        linux.sendImageWithURL(to, str(path))
                                        linux.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                    else:
                                        linux.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                        linux.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                        linux.sendMessage(msg.to,"「 MID 」\n" + ls)
                                        linux.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                        linux.sendImageWithURL(to, str(path))
                                else:
                                    linux.sendMessage(to, "Talk Exception You are not Related to LineChannel")
                        else:
                            linux.sendMessage(to, "Talk Exception You are not Related to LineChannel")
                elif "ข้อมูล " in msg.text.lower():
                    spl = re.split("ข้อมูล ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = linux.getContact(uid)
                            try:
                                linux.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net{}".format(userData.picturePath))
                            except:
                                pass
                            linux.sendMessage(to, "🌸•••••••••❂🌸✯🌸❂••••••••••🌸\n   ♡ ข้อมูลคนหน้าม่อคับ ♡\n🌸•••••••••❂🌸✯🌸❂••••••••••🌸")
                            linux.sendMessage(to, "✯::: ♡•ชื่อคนหน้าม่อคับ•♡ :::✯\nชื่อ❂➣ "+userData.displayName)
                            linux.sendMessage(to, "✯::: ♡•ตัสคนหน้าม่อคับ•♡ :::✯\nตัส❂➣ "+userData.statusMessage)
                            linux.sendMessage(msg.to,"✯::: ♡•ไอดีคนหน้าม่อคับ•♡ :::✯\n"+userData.mid)
                elif cmd == "กลุ่ม":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = linux.getGroupIdsJoined()
                               for i in gid:
                                   G = linux.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               linux.sendMessage(msg.to,"╔══[ รายชื่อ กลุ่ม ]\n║\n"+ma+"║\n╚══[ ทั้งหมด「"+str(len(gid))+"」กลุ่ม ]")
#--------------------------------------------------------------------------------------------------------------------------------                               
                elif "/run" in msg.text:
                    thisgroup = linux.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    linux.createGroup("ไม่มีสมาชิกในห้องแชท1", mi_d)
                    linux.sendMessage(msg.to,"ไม่มีสมาชิกในห้องแชท1")
                    linux.createGroup("ไม่มีสมาชิกในห้องแชท2", mi_d)
                    linux.sendMessage(msg.to,"ไม่มีสมาชิกในห้องแชท2")         
                    linux.createGroup("ไม่มีสมาชิกในห้องแชท3", mi_d)
                    linux.sendMessage(msg.to,"ไม่มีสมาชิกในห้องแชท3")
                    linux.createGroup("ไม่มีสมาชิกในห้องแชท4", mi_d)
                    linux.sendMessage(msg.to,"ไม่มีสมาชิกในห้องแชท4")         
                    linux.createGroup("ไม่มีสมาชิกในห้องแชท5", mi_d)
                    linux.sendMessage(msg.to,"ไม่มีสมาชิกในห้องแชท5")
#--------------------------------------------------------------------------------------------------------------------------------
                elif text.lower() == 'logout':
                    linux.sendMessage(to, "🌸 ปิดระบบเชลบอทเรียบร้อย 🌸")                                        
                    print ("Selfbot Off")
                    exit(1)
                if cmd == "ออกระบบ":
                    if msg._from in admin:
                    	wait["selfbot"] = True
                    	linux.sendMessage(msg.to, "ออกระบบเรียบร้อย...")
                                
                elif cmd == "ล็อคอิน":
                    if msg._from in admin:
                    	wait["selfbot"] = False
                    	linux.sendMessage(msg.to, "ล็อคอินเรียบร้อย...")

#--------------------------------------------------------------------------------------------------------------------------------                               
                elif "งาน1" in msg.text:
                    thisgroup = linux.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    linux.createGroup("💉ซื้อขายงานเกรดA1💊", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n💉ซื้อขายงานเกรดA1💊")
                    linux.createGroup("💉ซื้อขายงานเกรดA2💊", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n💉ซื้อขายงานเกรดA2💊")         
                    linux.createGroup("💉ซื้อขายงานเกรดA3💊", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n💉ซื้อขายงานเกรดA3💊")
                elif "งาน2" in msg.text:
                    thisgroup = linux.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]                    
                    linux.createGroup("💉ซื้อขายงานเกรดA4💊", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n💉ซื้อขายงานเกรดA4💊")         
                    linux.createGroup("💉ซื้อขายงานเกรดA5💊", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n💉ซื้อขายงานเกรดA5💊") 
                    linux.createGroup("💉ซื้อขายงานเกรดA6💊", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n💉ซื้อขายงานเกรดA6💊")
                elif "งาน3" in msg.text:
                    thisgroup = linux.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]                    
                    linux.createGroup("💉ซื้อขายงานเกรดA7💊", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n💉ซื้อขายงานเกรดA7💊")         
                    linux.createGroup("💉ซื้อขายงานเกรดA8💊", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n💉ซื้อขายงานเกรดA8💊")
                    linux.createGroup("💉ซื้อขายงานเกรดA9💊", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n💉ซื้อขายงานเกรดA9💊") 
                elif "งาน3" in msg.text:
                    thisgroup = linux.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]        
                    linux.createGroup("👑ตลาดมืดสีเทา👑V1", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n👑ตลาดมืดสีเทา👑V1")
                    linux.createGroup("👑ตลาดมืดสีเทา👑V2", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n👑ตลาดมืดสีเทา👑V2")
                    linux.createGroup("👑ตลาดมืดสีเทา👑V3", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n👑ตลาดมืดสีเทา👑V3")
                elif "งาน4" in msg.text:
                    thisgroup = linux.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]                    
                    linux.createGroup("👑ตลาดมืดสีเทา👑V4", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n👑ตลาดมืดสีเทา👑V4")
                    linux.createGroup("👑ตลาดมืดสีเทา👑V5", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n👑ตลาดมืดสีเทา👑V5")
                    linux.createGroup("👑ตลาดมืดสีเทา👑V6", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n👑ตลาดมืดสีเทา👑V6")
                elif "งาน5" in msg.text:
                    thisgroup = linux.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    linux.createGroup("🍁ตลาดเสรี🍁V1", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n🍁ตลาดเสรี🍁V1")
                    linux.createGroup("🍁ตลาดเสรี🍁V2", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n🍁ตลาดเสรี🍁V2")
                    linux.createGroup("🍁ตลาดเสรี🍁V3", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n🍁ตลาดเสรี🍁V3")
                elif "งาน6" in msg.text:
                    thisgroup = linux.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]                    
                    linux.createGroup("🍁ตลาดเสรี🍁V4", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n🍁ตลาดเสรี🍁V4")
                    linux.createGroup("🍁ตลาดเสรี🍁V5", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n🍁ตลาดเสรี🍁V5")
                    linux.createGroup("🍁ตลาดเสรี🍁V6", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n🍁ตลาดเสรี🍁V6")
                elif "งาน7" in msg.text:
                    thisgroup = linux.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]                    
                    linux.createGroup("🍁ตลาดเสรี🍁V7", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n🍁ตลาดเสรี🍁V7")
                    linux.createGroup("🍁ตลาดเสรี🍁V8", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n🍁ตลาดเสรี🍁V8")
                    linux.createGroup("🍁ตลาดเสรี🍁V9", mi_d)
                    linux.sendMessage(msg.to,"มีคำเชิญคุณเข้ากลุ่ม❗\n🍁ตลาดเสรี🍁V9")                    
#--------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["สุ่ม"]:
                    try:
#                        data={"type":"template","altText":"มีคนกล่าวถึงคุณ","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/02/12/Tlpdev.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=🎲🎲🎲",}}]}}
#                        sendTemplate(to, data)
                        data={"type":"template","altText":"มีคนกล่าวถึงคุณ","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/02/14/TPeFmJ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=เสี่ยงทาย",}}]}}
                        sendTemplate(to, data)
                        f = random.choice('123456')
                        r = random.choice('123456')
                        t = random.choice('123456')
                        d = int(f) + int(r) + int(t)
                        linux.sendReplyMessage(msg.id, msg.to, "🎲 คลิกที่รูปเพื่อทำการเสี่ยงทาย 🎲.")
#                        linux.sendMessage(msg.id, msg.to, "🎲 คลิกที่รูปเพื่อทำการเสี่ยงทาย 🎲.")
                        f = "🎲•🎲•🎲•🎲\n" + random.choice(card) + "\n🎲•🎲•🎲•🎲"
                        linux.sendMessage.sendMessage(to, str(f))
                        r = "🎲•🎲•🎲•🎲\n" + random.choice(card) + "\n🎲•🎲•🎲•🎲"
                        linux.sendMessage.sendMessage(to, str(r))
                        t = "🎲•🎲•🎲•🎲\n" + random.choice(card) + "\n🎲•🎲•🎲•🎲"
                        linux.sendMessage.sendMessage(to, str(t))
                    except Exception as e:
                        linux.sendMessage.sendMessage(msg.to, str(d))
                elif msg.text in ["โยน"]:
                    try:
                        data={"type":"template","altText":"มีคนกล่าวถึงคุณ","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/02/12/Tlpdev.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=เสี่ยงทาย",}}]}}
                        sendTemplate(to, data)
#                        data={"type":"template","altText":"มีคนกล่าวถึงคุณ","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/02/14/TPeFmJ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=/ไฮโล",}}]}}
#                        sendTemplate(to, data)
                        f = random.choice('123456')
                        r = random.choice('123456')
                        t = random.choice('123456')
                        d = int(f) + int(r) + int(t)
                        linux.sendReplyMessage(msg.id, msg.to, "🎲 คลิกที่รูปเพื่อทำการเสี่ยงทาย 🎲.")
#                        linux.sendMessage.sendReplyMessage(msg.id, msg.to, "🎲 คลิกที่รูปเพื่อทำการเสี่ยงทาย 🎲.")
                        f = "🎲•🎲•🎲•🎲\n" + random.choice(card) + "\n🎲•🎲•🎲•🎲"
                        linux.sendMessage.sendMessage(to, str(f))
                        r = "🎲•🎲•🎲•🎲\n" + random.choice(card) + "\n🎲•🎲•🎲•🎲"
                        linux.sendMessage.sendMessage(to, str(r))
                        t = "🎲•🎲•🎲•🎲\n" + random.choice(card) + "\n🎲•🎲•🎲•🎲"
                        linux.sendMessage.sendMessage(to, str(t))
                    except Exception as e:
                        linux.sendMessage.sendMessage(msg.to, str(d))                                                   
#
                elif text.lower() == '/ยิ้งฉุป':
                    s = random.choice(["⚒️ค้อน⚒️","🖐️กระดาษ🖐️","✂️กรรไกร✂️","⚒️ค้อน⚒️","🖐️กระดาษ🖐️","✂️กรรไกร✂️"])
                    linux.sendReplyMessage(msg.id, msg.to,"ผลการเป่ายิ้งฉุบ...❗")
                    linux.sendMessage(to,"  "+ s)
                elif text.lower() == '/โยน':
                    n = random.choice(["หัว","ก้อย","หัว","ก้อย"])
                    linux.sendReplyMessage(msg.id, msg.to,"โยนเหรียญ...❗")
                    linux.sendMessage(to," "+ n)
                elif text.lower() == '/หมุน':
                   s = random.choice('🍇🍇🍉🍑🍒🍉🍇🍋🍑🍎🍋🍑🍒🍑🍎🍒🍉🍋🍑🍎')
                   t = random.choice(' 🍇🍇🍉🍑🍒🍉🍇🍋🍑🍎🍋🍑🍒🍑🍎🍒🍉🍋🍑🍎')
                   r = random.choice(' 🍇🍇🍉🍑🍒🍉🍇🍋🍑🍎🍋🍑🍒🍑🍎🍒🍉🍋🍑🍎')
                   v = random.choice('🍇🍇🍉🍑🍒🍉🍇🍋🍑🍎🍋🍑🍒🍑🍎🍒🍉🍋🍑🍎')
                   a = random.choice('🍇🍇🍉🍑🍒🍉🍇🍋🍑🍎🍋🍑🍒🍑🍎🍒🍉🍋🍑🍎')
                   linux.sendReplyMessage(msg.id, msg.to,"ผลเครื่องสล็อตแมชชีน...🎰")
                   linux.sendMessage(to," | "+s+" | "+a+" | "+v+" | "+t+" | "+r+" |\n| "+t+" | "+r+" | "+a+" | "+v+" | "+v+" |\n| "+a+" | "+s+" | "+s+" | "+t+" | "+a+" |\n| "+t+" | "+r+" | "+a+" | "+v+" | "+s+" |\n| "+v+" | "+t+" | "+t+" | "+t+" | "+r+" | ")
                elif text.lower() == '/สุ่ม':
                   s = random.choice('🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍')
                   t = random.choice(' 🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍')
                   r = random.choice(' 🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍')
                   v = random.choice('🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍')
                   a = random.choice('🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍🍎🍊🍇🍏🍓🍍')
                   linux.sendReplyMessage(msg.id, msg.to,"คุณได้ทำการเขย่า....🎲")
                   linux.sendMessage(to," | "+s+" | "+t+" | "+a+" | "+v+" | "+r+" |\n| "+t+" | "+r+" | "+a+" | "+v+" | "+s+" |\n| "+a+" | "+s+" | "+v+" | "+t+" | "+a+" |\n| "+t+" | "+r+" | "+a+" | "+v+" | "+s+" |\n| "+v+" | "+a+" | "+s+" | "+t+" | "+r+" | ")                   
                elif text.lower() == '/ยิง':
                    s = random.choice(rr)
                    linux.sendReplyMessage(msg.id, msg.to, "คุณได้ทำการลั่นไกไปที่ปืนลูกโม่ปรากฎว่า...")
                    linux.sendMessage(msg.to, s)
                elif text.lower() == '/เขย่า':
                    f = random.choice('123456')
                    linux.sendReplyMessage(msg.id, msg.to,"ทอยลูกเต๋า 🎲. . .")
                    linux.sendMessage(to," "+f+" แต้ม")
                elif text.lower() == '/ไฮโล':
                    f = random.choice('123456')
                    r = random.choice('123456')
                    t = random.choice('123456')
                    d = int(f) + int(r) + int(t)
                    linux.sendReplyMessage(msg.id, msg.to, "🎲 ผลการทอยทั้งหมด 🎲.")
                    linux.sendMessage(to," "+"เต๋าลูกที่ 🎲 = "+f+" แต้ม"+"\n"+"เต๋าลูกที่ 🎲🎲 = "+r+" แต้ม"+"\n"+"เต๋าลูกที่ 🎲🎲🎲 = "+t+" แต้ม"+"\n"+"แต้มรวมทั้งหมด "+str(d)+" แต้ม")
                elif text.lower() == 'เสี่ยงทาย':
                    f = random.choice('123456')
                    r = random.choice('123456')
                    t = random.choice('123456')
                    d = int(f) + int(r) + int(t)
#                    linux.sendReplyMessage(msg.id, msg.to, "🎲 🎲 🎲")
                    linux.sendMessage(to," "+"เต๋าลูกที่ 🎲 = "+f+" แต้ม"+"\n"+"เต๋าลูกที่ 🎲🎲 = "+r+" แต้ม"+"\n"+"เต๋าลูกที่ 🎲🎲🎲 = "+t+" แต้ม"+"\n"+"แต้มรวมทั้งหมด "+str(d)+" แต้ม")                    
                elif text.lower() == '/จก':
                    linux.sendMessage(msg.to, "ไพ่ที่คุณได้รับหลังจากการสับ :\n\n"+random.choice(card)+"\n"+random.choice(card)+"\n\nพิมพ์ /draw เพื่อจั่วไพ่")
                elif text.lower() == '/จั่ว':
                    linux.sendReplyMessage(msg.to,"ไพ่ที่คุณได้รับหลังการจั่ว : \n\n"+random.choice(card))
                    
#                elif msg.text in ["Ssp"]:
#                    start = time.time()                                        
#                    elapsed_time = time.time() - start
#                    linux.sendMessage(to, " %.10f ᴍs" % (elapsed_time))
#                elif msg.text in ["Spb"]:
#                    start = time.time()                                        
#                    elapsed_time = time.time() - start
#                    linux.sendMessage(to, " %.10f ᴍs" % (elapsed_time))                     
                    
#                    restartBot()
#                elif msg.text in ["Ree"]:
#                    linux.sendMessage(to, "??อัพเดทระบบ🆙")                
#                    linux.sendMessage(to, "??กรุณารอสักครู่🌸")
#                    linux.sendMessage(to, "🌸รีสตาร์ทเรียบร้อย🌸")                  
#                    
                elif cmd.startswith("/ออก ") and sender == linuxMID:
                    number = removeCmd("/ออก", text)
                    groups = linux.getGroupIdsJoined()
                    try:
                        group = groups[int(number)-1]
                        G = linux.getGroup(group)
                        try:
                            linux.leaveGroup(G.id)
                        except:
                            linux.leaveGroup(G.id)
                        linux.sendMessage(to, "「ออก 」\nกลุ่ม: " + G.name)
                    except Exception as error:
                        linux.sendMessage(to, str(error))   
                elif cmd.startswith("/เปิดลิ้ง "):
                    number = removeCmd("/เปิดลิ้ง", text)
                    groups = linux.getGroupIdsJoined()
                    try:
                        group = groups[int(number)-1]
                        G = linux.getGroup(group)
                        try:
                            G.preventedJoinByTicket = False
                            linux.updateGroup(G)
                            gurl = "https://line.me/R/ti/g/{}".format(str(linux.reissueGroupTicket(G.id)))
                        except:
                            G.preventedJoinByTicket = False
                            linux.updateGroup(G)
                            gurl = "https://line.me/R/ti/g/{}".format(str(linux.reissueGroupTicket(G.id)))
                        linux.sendMessage(to, "「 เปิดลิงค์ 」\nลิ้งกลุ่ม: " + G.name + "\nลิงค์กลุ่ม: " + gurl)
                    except Exception as error:
                        linux.sendMessage(to, str(error)) 
#=====================================================================
                elif text.lower() == "เชคดำ":
                            if LnBots["blacklist"] == {}:
                              linux.unsendMessage(msg_id)
                              linux.sendMessage(to, "🌸 ไม่พบคนที่เรายัดดำ 🌸")
                            else:
                              ma = ""
                              a = 0
                              for m_id in LnBots["blacklist"]:
                                  a = a + 1
                                  end = '\n'
                                  ma += str(a) + ". " +linux.getContact(m_id).displayName + "\n"
                              linux.sendMessage(to,"รายชื่อคนติดดำ :\n\n"+ma+"\nจำนวน %s คนติดดำ" %(str(len(LnBots["blacklist"]))))
                         
#=====================================================================
#                              \\ COMMAND Kick //
#                            
                elif text.lower() == "protect":
                    ret = "🌸โหมด ป้องกันกลุ่ม🌸\n\n"
                    ret += "🌸 กันลิ้ง เปิด/ปิด「 กันลิ้งกลุ่ม 」 \n"
                    ret += "🌸 กันเตะ เปิด/ปิด「 กันเตะกลุ่ม 」 \n"
                    ret += "🌸 กันเชิญ เปิด/ปิด「 กันเชิญกลุ่ม 」\n"
                    ret += "🌸 กันยก เปิด/ปิด「 กันยกค้างเชิญ 」\n"
                    ret += "🌸 กันเข้า เปิด/ปิด「 กันคนเข้ากลุ่ม 」\n"
                    ret += "🌸 ป้องกัน เปิด/ปิด「 กันกลุ่ม 」\n"
                    ret += "🌸 เชคป้องกัน「 เชคกลุ่มป้องกัน 」 \n"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": "ป้องกันกลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
#
                elif text.lower() == "ลูกเล่น":
                    ret = "🌸โหมด เครื่องเล่นหรรษา🌸\n\n"
                    ret += "🎰  /ยิ้งฉุป [ เกมเป่ายิ้งฉุป ] \n"
                    ret += "🎰  /โยน [ โยนเหรียญ หัว,ก้อย ]\n"
                    ret += "🎰  /เขย่า [ ทอยลูกเต๋า ]\n"
                    ret += "🎰  /หมุน [ หมุนเครื่องสล็อต ]\n" 
                    ret += "🎰  /สุ่ม [ เกมรัสเซียนรูเล็ต ]\n"
                    ret += "🎰  /ไฮโล [ เกมไฮโล ]\n"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": "คำสั่งลูกเล่น",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
#
                elif text.lower() == "ระบบเตะ":
                    ret = "🌸โหมด คำสั่งเตะ🌸\n\n"
                    ret += "🌸  kick @ [ เตะสมาชิก ] \n"
                    ret += "🌸  แตก  [ เตะสมาชิก ]\n"
                    ret += "🌸  ตีกระหรี่ [ เตะดำ ]\n"
                    ret += "🌸  เตะดำ [ เตะดำ ]\n" 
                    ret += "🌸  ล้อเล่น @ [ เตะเชิญ ]\n" 
                    ret += "🌸  ประกาศ: เตะดำ [ เตะทุกกลุ่ม ]\n"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": "ระบบเตะ",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)     
#
                elif text.lower() == "/เลียนแบบ":
                    ret = " 👑โหมด: เลียนแบบ👑\n\n"
                    ret += " 🍇 ลิสเลียนแบบ \n"
                    ret += " 🌸 เลียนแบบ @ \n"
                    ret += " 🌸 ลบเลียนแบบ @ \n"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": "คำสั่งเลียนแบบ",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)                   
                elif text.lower() == "หมุด":
                    ret = "    📍โหมด คำสั่งหมุด📍\n\n"
                    ret += "📍  ปักหมุด [ ปักหมุดกลุ่ม ] \n"
                    ret += "📍  ลบหมุด [ ลบหมุดกลุ่ม ]\n"
                    ret += "📍  เชคหมุด [ เชคกลุ่มปักหมุด ]\n"
                    ret += "📍  ประกาศหมุด +ข้อความประกาศ\n"
                    ret += "📍  ##🔺[ ประกาศกลุ่มหมุด ]🔺##\n"
                    ret += "📍  ประกาศ: ปักหมุด\n" 
                    ret += "📍  ##🔺[ ปักหมุดทุกกลุ่ม ]🔺##\n" 
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": "คำสั่งหมุด",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)                                 
#
                elif text.lower() == "sticker":
                    ret = " 🌸 โหมด ตั้งค่าสติ้กเกอร์ 🌸\n\n"
                    ret += "🌸  ตั้งติ๊กคนแทค [ ตอบแทคสติ้ก ] \n"
                    ret += "🌸  ลบติ๊กคนแทค [ ลบแทคสติ้ก ] \n"
                    ret += "🌸  ตั้งติ๊กคนเข้า [ สติ้กคนเข้า ]\n"
                    ret += "🌸  ลบติ๊กคนเข้า [ ลบสติ้กคนเข้า ]\n"
                    ret += "🌸  ตั้งติ๊กคนออก [ สติ้กคนออก ]\n"
                    ret += "🌸  ลบติ๊กคนออก [ ลบสติ้กคนออก ]\n"
                    ret += "🌸  ตั้งติ๊กคนแอด [ ส่งติ้กคนแอด สต. ] \n"
                    ret += "🌸  ลบติ๊กคนแอด [ ลบติ้กคนแอด สต. ] \n"
                    ret += "🌸  ตั้งติ๊กมุดลิ้ง [ ส่งติ้กทักมุดลิ้ง ]\n"
                    ret += "🌸  ลบติ๊กมุดลิ้ง [ ลบติ้กทักมุดลิ้ง ]\n"
                    ret += "🌸  เปิด/ปิดติ๊กใหญ่ [ ส่งติ้กตัวใหญ่ ]\n"
                    ret += "🌸  เปิด/ปิดติ๊กapi [ ส่งติ้กคู่ ]\n"
                    ret += "🌸  เปิด/ปิดโค๊ดติ๊ก [ แสดงโค๊ดสติ้ก ]\n"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": "Sticker",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)          
#                            
                elif text.lower() == "spam":
                    ret = "🌸โหมด สแปม&นับเลข🌸\n"
                    ret += "➡️ spam on 10 ตัวอย่าง ⬅️\n\n"
                    ret += "🌸 stag [ จำนวน ] [ @user ]\n"
                    ret += "## [ สแปมแทค ]\n"
                    ret += "🌸 Fuck [จำนวน]\n"
                    ret += "## [ สแปมนับเลขสลับ ]\n"
                    ret += "🌸 spam on [ จำนวน ] [ @user ]\n"
                    ret += "## [ สแปมข้อความ ]\n"
                    ret += "🌸 spam 2 [ จำนวน ]\n"
                    ret += "## [ สแปมคท.คนในห้อง (สุ่ม) ]\n"
                    ret += "🌸 spam 3 [ จำนวน ] [ @user ]\n"
                    ret += "## [ สแปมของขวัญใน สต. ]\n"
                    ret += "🌸 /นับ +จำนวน [ สแปมเลขแชท ]​\n"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": "Order Spam",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)   
#                    
                elif text.lower() == "blacklist":
                    ret = "   🌸 โหมด คำสั่งขาว/ดำ 🌸\n\n"
                    ret += "🌸  ดำ  [ ส่งคท ] \n"
                    ret += "🌸  ดำ @ [ ยัดดำกลุ่ม ]\n"
                    ret += "🌸  ลงดำ [ ยัดดำทั้งกลุ่ม ]\n"
                    ret += "🌸  ขาว [ ส่งคท ]​\n"
                    ret += "🌸  ขาว @ [ ล้างบัญชีดำ ]​\n"
                    ret += "🌸  Bc, คทดำ [ เ​ช​ค คท ดำ ]​\n"
                    ret += "🌸  เชคดำ [ เชคชื่อบัญชีดำ ]​\n"
                    ret += "🌸  Cb, ล้างดำ [ ล้างดำทั้งหมด ]​\n"
                    ret += "🌸  เตะดำ, Kb [ เตะดำในกลุ่ม ]​\n" 
                    ret += "🌸  ตีกระหรี่ [ เตะดำเฟก ]​\n" 
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": " 🌸 BLACKLIST 🌸",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data) 
#                    
                elif text.lower() == "/ออโต้":
                    ret = "   👑 คำสั่งประกาศข้อความออโต้ 👑\n\n"
                    ret += "👑  ลิ้งรูปประกาศ1 +ลิ้งรูปประกาศ\n"
                    ret += "👑  ลิ้งรูปประกาศ2 +ลิ้งรูปประกาศ\n"
                    ret += "👑  ลิ้งรูปประกาศ3 +ลิ้งรูปประกาศ\n"
                    ret += "👑  ตั้งประกาศ1 +ข้อความประกาศ\n"
                    ret += "👑  ตั้งประกาศ2 +ข้อความประกาศ\n"
                    ret += "👑  ตั้งประกาศ3 +ข้อความประกาศ\n"
                    ret += "👑  เปิดประกาศ [ เปิดประกาศออโต้ ]​\n"
                    ret += "👑  ปิดประกาศ [ ปิดประกาศออโต้ ]​\n"
                    ret += "👑  ประกาศจะส่งทุกๆ 1 ชั่วโมง \n"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": " 👑 ประกาศออโต้ 👑",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)                     
#                    
                elif text.lower() == "ประกาศ":
                    ret = "   📢 คำสั่งประกาศกลุ่ม 📣\n\n"
                    ret += "🔊  ประกาศ: +ข้อความ [ ปกติ ] \n"
                    ret += "🔊  ประกาศแชท: +ข้อความ[แชทเพื่อน]\n"
                    ret += "🔊  ประกาศ +ข้อความ [ เฟก ]\n"
                    ret += "🔊  ประกาศ1 +ข้อความ [ เฟก ]\n"
                    ret += "🔊  ประกาศ3 +ข้อความ [ รูปเฟก ]\n"
                    ret += "🔊  ตั้งรูป1: +ลิ้งรูป [ เฟก ]\n"
                    ret += "🔊  ตั้งรูป2: +ลิ้งรูป [ เฟก ]\n"
                    ret += "🔊  ตั้งรูป3: +ลิ้งรูป [ เฟก ]\n"
                    ret += "🔊  ตั้งขาย1: +ข้อความ [ เฟก ]\n"
                    ret += "🔊  ตั้งขาย2: +ข้อความ [ เฟก ]\n"
                    ret += "🔊  ตั้งขาย3: +ข้อความ [ เฟก ]\n"
                    ret += "🔊  ลิ้งติดต่อ +ลิ้งไลน์ [ ลิ้งติดต่อเรา ]\n"
                    ret += "🔊  ประกาศเฟก [ ประกาศรูป3แผ่น ]​\n" 
                    ret += "🔊  ส่งรูป1 [ ประกาศรูป1แผ่น ]​\n"
                    ret += "🔊  ส่งรูป [ ประกาศขายเชล ]​\n"
                    ret += "🔊  ส่งประกาศ [ ประกาศรูปโปรไฟล์ ]​\n"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": " 👑 ประกาศกลุ่ม 👑",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)                                                     
#                            
                elif text.lower() == "ตั้งค่าเรา":
                    ret = "  🌸 โหมด คำสั่งตั้งค่าเปิด/ปิด 🌸\n\n"
                    ret += " 🌸  เปิด/ปิดแทค「 ตอบคนแทค 」\n"
                    ret += " 🌸  เปิด/ปิดแทค2「 ตอบคนแทค2 」\n"
                    ret += " 🌸  เปิด/ปิดไลค์「 ออโต้ไลค์ 」\n"
                    ret += " 🌸  เปิด/ปิดคอมเม้น「 ออโต้เม้น 」\n"
                    ret += " 🌸  เปิด/ปิดบล็อค「 ออโต้บล็อค 」\n "
                    ret += "🌸  เปิด/ปิดมุดลิ้ง「 เข้าลิ้งออโต้ 」\n"
                    ret += " 🌸  เปิด/ปิดออกแชทรวม「 กินห้อง 」\n"
                    ret += " 🌸  เปิด/ปิดกันสแปม「 กันสแปม 」\n "
                    ret += "🌸  เปิด/ปิดกันรัน「 กันเชิญ 」\n "
                    ret += "🌸  เปิด/ปิดยกเลิก「 เชคยกเลิก 」\n"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": "🌸ตั้งค่าส่วนตัว🌸",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)           
#                            
                elif text.lower() == "js":
                    ret = "🌸โหมด คำสั่งพิเศษ🌸\n\n"
                    ret += " 🌸  เที่ยว「 บินกลุ่ม 」\n"
                    ret += " 🌸  /ลาก่อน「 บิน&ยกเชิญ 」 \n"
                    ret += " 🌸    รวบ +อักษร「 เตะรวบตัส 」\n"
                    ret += " 🌸    สับ +อักษร「 เตะรวบชื่อ 」\n"
                    ret += " 🌸  /ลุย 「 บินกลุ่ม 」\n"
                    ret += " 🌸  /หาย「 บินธรรมดา 」\n "
                    ret += "🌸  /ปลิว @「 เตะรวบแทค 」"
                    hello = "{}".format(str(ret))
                    data = {
                        "type": "flex",
                        "altText": "🌸help js🌸",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(hello),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)        
                elif msg.text in ["เที่ยว"]:
                  xyz = linux.getGroup(to)
                  mem = [c.mid for c in xyz.members]
                  targets = []
                  for x in mem:
                    if x not in ["u28b8c966bac59aab7db1736bddc38371","u3e9a269993bbb67a4fb84d8aa6a6457f","u25288fd83a0c9bb623c1ee26dc7624a2","uc21bdc27684c225fb5ca3ee3128a67a9","u879c35a5d9254451329b0056844f6120","u4772714e1db7a4da1f899310a5bb7d25","u9b1a48c5b6051c2dd6ef37070162a8c0","u5f657b08b95367e4b28843f7859a25f5",linux.profile.mid]:targets.append(x)
                  if targets:
                    imnoob = 'simple.js gid={} token={} app={}'.format(to, linux.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
                    for target in targets:
                      imnoob += ' uid={}'.format(target)
                    success = execute_js(imnoob)
                    if success:linux.sendMessage(to, "Success kick %i members." % len(targets))
                    else:linux.sendMessage(to, "Failed kick %i members." % len(targets))
                  else:linux.sendMessage(to, "Target not found.")
                elif msg.text in ["linuxclub"]:
                  xyz = linux.getGroup(to)
                  mem = [c.mid for c in xyz.members]
                  targets = []
                  for x in mem:
                    if x not in ["u28b8c966bac59aab7db1736bddc38371",linux.profile.mid]:targets.append(x)
                  if targets:
                    imnoob = 'simple.js gid={} token={} app={}'.format(to, linux.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
                    for target in targets:
                      imnoob += ' uid={}'.format(target)
                    success = execute_js(imnoob)
                    if success:linux.sendMessage(to, "Success kick %i members." % len(targets))
                    else:linux.sendMessage(to, "Failed kick %i members." % len(targets))
                  else:linux.sendMessage(to, "Target not found.")                  
                elif msg.text in ["/ลาก่อน"]:
                  xyz = linux.getGroup(to)
                  if xyz.invitee == None:pends = []
                  else:pends = [c.mid for c in xyz.invitee]
                  targp = []
                  for x in pends:
                    if x not in ["u28b8c966bac59aab7db1736bddc38371",linux.profile.mid]:targp.append(x)
                  mems = [c.mid for c in xyz.members]
                  targk = []
                  for x in mems:
                    if x not in ["u28b8c966bac59aab7db1736bddc38371",linux.profile.mid]:targk.append(x)
                  imnoob = 'dual.js gid={} token={}'.format(to, linux.authToken)
                  for x in targp:imnoob += ' uid={}'.format(x)
                  for x in targk:imnoob += ' uik={}'.format(x)
                  execute_js(imnoob) 

                elif text.lower().startswith("สับ "):
                   sep = text.split(" ")
                   midn = text.replace(sep[0] + " ","")
                   hmm = text.lower()
                   G = linux.getGroup(msg.to)
                   members = [G.mid for G in G.members]
                   targets = []
                   imnoob = 'simple.js gid={} token={} app={}'.format(to, linux.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
                   for x in members:
                       contact = linux.getContact(x)
                       msg = op.message
                       testt = contact.displayName.lower()
                           #print(testt)
                       if midn in testt:targets.append(contact.mid)
                   if targets == []:return linux.sendMessage(to,"not found name "+midn)
                   for target in targets:
                     imnoob += ' uid={}'.format(target)
                   success = execute_js(imnoob)
#                            

                elif text.lower().startswith("รวบ "):
                   sep = text.split(" ")
                   midn = text.replace(sep[0] + " ","")
                   hmm = text.lower()
                   G = linux.getGroup(msg.to)
                   members = [G.mid for G in G.members]
                   targets = []
                   imnoob = 'simple.js gid={} token={} app={}'.format(to, linux.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
                   for x in members:
                       contact = linux.getContact(x)
                       msg = op.message
                       testt = contact.statusMessage.lower()
                           #print(testt)
                       if midn in testt:targets.append(contact.mid)
                   if targets == []:return linux.sendMessage(to,"not found name "+midn)
                   for target in targets:
                     imnoob += ' uid={}'.format(target)
                   success = execute_js(imnoob)
#                            

                elif msg.text in ["แตก"]:
                	if msg.toType == 2:
                         group = linux.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         imnoob = 'simple.js gid={} token={} app={}'.format(receiver, linux.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
                         for tag in LnBots["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                            pass
                         for jj in matched_list:
                           imnoob += ' uid={}'.format(jj)
                         success = execute_js(imnoob)
                         print("KICK JS")
                         if success:linux.sendMessage(to, "Success kick %i members." % len(matched_list))
#                               
                elif ("/ปลิว " in msg.text):
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       imnoob = 'simple.js gid={} token={} app={}'.format(to, linux.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
                       for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                       for target in targets:
                           imnoob += ' uid={}'.format(target)
                       success = execute_js(imnoob)
                         
#
#                elif text.lower() == "ghost":
#                    ret = "🌸โหมด คำสั่งพิเศษ🌸\n\n"
#                    ret += " 🌸 เที่ยว1\2「 บินกลุ่มjs 」\n"
#                    ret += " 🌸 ผีรวบ +อักษร「 เตะรวบชื่อ 」\n"
#                    ret += " 🌸 ผีสับ +อักษร「 เตะรวบชื่อ 」\n"
#                    ret += " 🌸 ไป/มา 「 เรียกผี 」\n"
#                    ret += " 🌸กันเรา เปิด/ปิด「 กันบินjs 」\n "
#                    ret += "🌸  /ผีปลิว @「 เตะรวบแทค 」"
#                    hello = "{}".format(str(ret))
#                    data = {
#                        "type": "flex",
#                        "altText": "🌸HELP GHOST🌸",
#                        "contents": {
#                            "type": "bubble",
#                            "styles": {
#                                "body": {
#                                    "backgroundColor": '#000000'
#                                },
#                            },
#                            "body": {
#                                "type": "box",
#                                "layout": "vertical",
#                                "contents": [
#                                    {
#                                        "type": "text",
#                                        "text": "{}".format(hello),
#                                        "wrap": True,
#                                        "color": "#00F5FF",
#                                        "gravity": "center",
#                                        "size": "md"
#                                    },
#                                ]
#                            },
#                        }
#                    }
#                    sendTemplate(to, data)        
#                elif msg.text in ["เที่ยว1"]:
#                  xyz = linux.getGroup(to)
#                  mem = [c.mid for c in xyz.members]
#                  targets = []
#                  for x in mem:
#                    if x not in ["u28b8c966bac59aab7db1736bddc38371",g1.profile.mid]:targets.append(x)
#                  if targets:
#                    imnoob = 'simple.js gid={} token={} app={}'.format(to, g1.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
#                    for target in targets:
#                      imnoob += ' uid={}'.format(target)
#                    success = execute_js(imnoob)
##                    if success:linux.sendMessage(to, "Success kick %i members." % len(targets))
##                    else:linux.sendMessage(to, "Failed kick %i members." % len(targets))
##                  else:linux.sendMessage(to, "Target not found.")
#                elif msg.text in ["เที่ยว2"]:
#                  xyz = linux.getGroup(to)
#                  mem = [c.mid for c in xyz.members]
#                  targets = []
#                  for x in mem:
#                    if x not in ["u28b8c966bac59aab7db1736bddc38371",g2.profile.mid]:targets.append(x)
#                  if targets:
#                    imnoob = 'simple.js gid={} token={} app={}'.format(to, g2.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
#                    for target in targets:
#                      imnoob += ' uid={}'.format(target)
#                    success = execute_js(imnoob)
##                    if success:linux.sendMessage(to, "Success kick %i members." % len(targets))
##                    else:linux.sendMessage(to, "Failed kick %i members." % len(targets))
##                  else:linux.sendMessage(to, "Target not found.")
#                elif text.lower().startswith("ผีสับ "):
#                   sep = text.split(" ")
#                   midn = text.replace(sep[0] + " ","")
#                   hmm = text.lower()
#                   G = linux.getGroup(msg.to)
#                   members = [G.mid for G in G.members]
#                   targets = []
#                   imnoob = 'simple.js gid={} token={} app={}'.format(to, g1.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
#                   for x in members:
#                       contact = g1.getContact(x)
#                       msg = op.message
#                       testt = contact.displayName.lower()
#                           #print(testt)
#                       if midn in testt:targets.append(contact.mid)
#                   if targets == []:return linux.sendMessage(to,"not found name "+midn)
#                   for target in targets:
#                     imnoob += ' uid={}'.format(target)
#                   success = execute_js(imnoob)
##                            
#                elif text.lower().startswith("ผีรวบ "):
#                   sep = text.split(" ")
#                   midn = text.replace(sep[0] + " ","")
#                   hmm = text.lower()
#                   G = linux.getGroup(msg.to)
#                   members = [G.mid for G in G.members]
#                   targets = []
#                   imnoob = 'simple.js gid={} token={} app={}'.format(to, g1.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
#                   for x in members:
#                       contact = g1.getContact(x)
#                       msg = op.message
#                       testt = contact.statusMessage.lower()
#                           #print(testt)
#                       if midn in testt:targets.append(contact.mid)
#                   if targets == []:return linux.sendMessage(to,"not found name "+midn)
#                   for target in targets:
#                     imnoob += ' uid={}'.format(target)
#                   success = execute_js(imnoob)
#
#                elif ("/ผีปลิว " in msg.text):
#                       key = eval(msg.contentMetadata["MENTION"])
#                       key["MENTIONEES"][0]["M"]
#                       targets = []
#                       imnoob = 'simple.js gid={} token={} app={}'.format(to, g1.authToken, "IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
#                       for x in key["MENTIONEES"]:
#                            targets.append(x["M"])
#                       for target in targets:
#                           imnoob += ' uid={}'.format(target)
#                       success = execute_js(imnoob)
#
                elif text.lower() == "บัค":
                    if msg._from in admin or msg._from in Family:
                       try:linux.inviteIntoGroup(to, [linuxMID]);has = "OK"
                       except:has = "NOT"
                       try:linux.kickoutFromGroup(to, [linuxMID]);has1 = "OK"
                       except:has1 = "NOT"
                       if has == "OK":sil = " ʀᴇᴀᴅʏ ✔"
                       else:sil = " ʟɪᴍɪᴛ 💊"
                       if has1 == "OK":sil1 = " ʀᴇᴀᴅʏ ✔"
                       else:sil1 = " ʟɪᴍɪᴛ 💊"
                       linux.sendMessage(to, "╭═『มองหาพ่อมุงหรอ』═╮\n 🔴 ระบบเตะ : {} \n 🔴 ระบบเชิญ : {}\n╰══════════╯".format(sil1,sil))
#
                elif text.lower() == "เชคบัค":
                    if msg._from in admin or msg._from in Bots:
                       try:linux.inviteIntoGroup(to, [linuxMID]);has = "OK"
                       except:has = "NOT"
                       try:linux.kickoutFromGroup(to, [linuxMID]);has1 = "OK"
                       except:has1 = "NOT"
                       if has == "OK":sil = " ʀᴇᴀᴅʏ ✔"
                       else:sil = " ʟɪᴍɪᴛ 💊"
                       if has1 == "OK":sil1 = " ʀᴇᴀᴅʏ ✔"
                       else:sil1 = " ʟɪᴍɪᴛ 💊"
                       linux.sendMessage(to, "╭═『มองหาพ่อมุงหรอ』═╮\n 🔴 ระบบเตะ : {} \n 🔴 ระบบเชิญ : {}\n╰══════════╯".format(sil1,sil))            
#                       try:g1.inviteIntoGroup(to, [Zmid]);has = "OK"
##                       except:has = "NOT"
#                       try:g1.kickoutFromGroup(to, [Zmid]);has1 = "OK"
#                       except:has1 = "NOT"
#                       if has == "OK":sil = " ʀᴇᴀᴅʏ ✔"
#                       else:sil = " ʟɪᴍɪᴛ 💊"
#                       if has1 == "OK":sil1 = " ʀᴇᴀᴅʏ ✔"
#                       else:sil1 = " ʟɪᴍɪᴛ 💊"
#                       g1.sendMessage(to, "╭═『มองหาพ่อมุงหรอ』═╮\n 🔴 ระบบเตะ : {} \n 🔴 ระบบเชิญ : {}\n╰══════════╯".format(sil1,sil))            
#                       try:g2.inviteIntoGroup(to, [Amid]);has = "OK"
#                       except:has = "NOT"
##                       try:g2.kickoutFromGroup(to, [Amid]);has1 = "OK"
#                       except:has1 = "NOT"
#                       if has == "OK":sil = " ʀᴇᴀᴅʏ ✔"
#                       else:sil = " ʟɪᴍɪᴛ 💊"
#                       if has1 == "OK":sil1 = " ʀᴇᴀᴅʏ ✔"
#                       else:sil1 = " ʟɪᴍɪᴛ 💊"
#                       g2.sendMessage(to, "╭═『มองหาพ่อมุงหรอ』═╮\n 🔴 ระบบเตะ : {} \n 🔴 ระบบเชิญ : {}\n╰══════════╯".format(sil1,sil))            
                elif msg.text in ["/หาย"]:
                        if msg.toType == 2:
                         _name = msg.text.replace("/หาย","")
                         gs = linux.getGroup(receiver)
                         linux.sendMessage(to, "🌸••••••••••❂🌸✯🌸❂•••••••••••🌸\n ♡ต้อนรับสู่สนามบินนานาชาติ♡\n🌸••••••••••❂🌸✯🌸❂•••••••••••🌸 \n •➣ สายบินแห่งความฟรุ้งฟริ้ง\n •➣ เที่ยวบินที่ : 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™\n\n🌸••••••••••❂🌸✯🌸❂•••••••••••🌸\n  💚เดินทางโดยสวัสดิภาพคับ💚")
                         linux.sendMessage(to, "●•โชคดี➤➤➤➤➤➤➤")
                         linux.sendMessage(to, "❂บ๊าบบาย•➣➣➣➣➣➣➣")
                         linux.sendMessage(to, "●•ลาก่อน➤➤➤➤➤➤➤➤")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             linux.sendMessage(receiver,"🌸••••••••••❂🌸✯🌸❂•••••••••••🌸\n  ♡ น้ำมันหมด งดเที่ยวบินคับ ♡\n🌸••••••••••❂🌸✯🌸❂•••••••••••🌸")
                         else:
                             for target in targets:
                                if not target in Rfu:
                                     try:
                                         klist=[linux]
                                         kicker=random.choice(klist)
                                         sleep(0.0001)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         linux.sendMessage(receiver,"💖ขอบคุณทุกท่านที่ใช้บริการ💖\n       ✈ A~jang Airpört ✈")
                                         print ("Cleanse Group")
                elif "/ลุย" in msg.text:
                  if msg._from in admin:
                   if msg.toType == 2:
                      print("ok")
                      _name = msg.text.replace("/ลุย","")
                      gs = linux.getGroup(msg.to)
                      gs = linux.getGroup(msg.to)
                      gs = linux.getGroup(msg.to)
                      targets = []
                      for g in gs.members:
                         if _name in g.displayName:
                             targets.append(g.mid)
                      if targets == []:
                         linux.sendText(msg.to,"Tidak Ditemukan.")
                      else:
                          for target in targets:
#                           if not target in admin and Bots:
                              try:
                                  klist=[linux]
                                  kicker=random.choice(klist)
                                  kicker.kickoutFromGroup(msg.to,[target])
                                  print (msg.to,[g.mid])
                              except Exception as e:
                                  break
                elif "/ลุย2" in msg.text:
                  if msg._from in admin:
                   if msg.toType == 2:
                      print("ok")
                      _name = msg.text.replace("/ลุย2","")
                      gs = linux.getGroup(msg.to)
                      gs = linux.getGroup(msg.to)
                      gs = linux.getGroup(msg.to)
                      targets = []
                      for g in gs.members:
                         if _name in g.displayName:
                             targets.append(g.mid)
                      if targets == []:
                         linux.sendText(msg.to,"Tidak Ditemukan.")
                      else:
                          for target in targets:
#                           if not target in admin and Bots:
                              try:
                                  klist=[linux]
                                  kicker=random.choice(klist)
                                  kicker.kickoutFromGroup(msg.to,[target])
                                  print (msg.to,[g.mid])
                              except Exception as e:
                                  break
                elif cmd.startswith("ล้อเล่น "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            try:
                                linux.kickoutFromGroup(to, [ls])
                                linux.findAndAddContactsByMid(ls)
                                linux.inviteIntoGroup(to, [ls])
                            except:
                               linux.unsendMessage(msg_id)
                               linux.sendMessage(to, "🌸 จำกัดการเชิญ 🌸")
                elif ("เตะ1 " in msg.text):
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                       for target in targets:
                               try:
                                   linux.kickoutFromGroup(msg.to, [target])
                               except:
                                   pass
                                   
                elif msg.text in ["ตีกระหรี่"]:
                	if msg.toType == 2:
                         group = linux.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in LnBots["Talkblacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             linux.unsendMessage(msg_id)
                             linux.sendMessage(to, "🌸 ไม่พบกระหรี่ให้ตี 🌸")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[linux]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     linux.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")   
                elif msg.text in ["เตะดำ"]:
                	if msg.toType == 2:
                         group = linux.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in LnBots["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             linux.unsendMessage(msg_id)
                             linux(to, "🌸 ไม่พบดำในห้องนี้ 🌸")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[linux]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     linux.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")                                                                                                    
                elif msg.text in ["ล่า"]:
                            groups = linux.getGroupIdsJoined()
                            for x in groups:
                                found = []
                                mem = [m.mid for m in linux.getGroup(x).members]
                                for mid in LnBots["blacklist"]:
                                    if mid in mem: found.append(mid)
                                if found:
                                    for blc in found:
                                        try:
                                            linux.kickoutFromGroup(x, [blc])
                                        except: linux.sendMessage("u5212bf4a8e3b64cb7307e89e4588929f","บัคเตะแล้ว");break
                                    linux.sendMessage(x, "おまえ... は もう 死んでいる")
                            linux.sendMessage(to, "🌸ล่าดำทุกกลุ่มเรียบร้อย🌸")                      
                            
                elif msg.text in ["Kb"]:
                	if msg.toType == 2:
                         group = linux.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in LnBots["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             linux.unsendMessage(msg_id)
                             linux(to, "🌸 ไม่พบดำในห้องนี้ 🌸")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[linux]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     linux.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")                                                                                                                                          
                elif "มาคลอ" == msg.text.lower():
                    linux.inviteIntoGroupCall(msg.to,[uid.mid for uid in linux.getGroup(msg.to).members if uid.mid != linux.getProfile().mid])
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เชิญเข้าร่วมการโทรสำเร็จ 🌸")
                elif "/คลอ" in msg.text.lower():
                    if msg.toType == 2:
                        sep = msg.text.split(" ")
                        resp = msg.text.replace(sep[0] + " ","")
                        num = int(resp)
                        try:
                            linux.unsendMessage(msg_id)
                            linux.sendMessage(to, "🌸 กำลังดำเนินการ... 🌸")
                        except:
                            pass
                        for var in range(num):
                            group = linux.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            linux.acquireGroupCallRoute(msg.to)
                            linux.inviteIntoGroupCall(msg.to, contactIds=members)
                        linux.unsendMessage(msg_id)
                        linux.sendMessage(to, "🌸 เชิญคอลสำเร็จแล้ว... 🌸")
                elif msg.text.startswith("คอล"):
                   dan = text.split(" ")
                   num = int(dan[1])
                   ret_ = "╭──[ เชิญโทรสำเร็จ ]"
                   if 'MENTION' in msg.contentMetadata.keys()!= None:
                       names = re.findall(r'@(\w+)', text)
                       mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                       mentionees = mention['MENTIONEES']
                       lists = []
                       for mention in mentionees:
                           if mention["M"] not in lists:
                               lists.append(mention["M"])
                       for ls in lists:
                           for var in range(0,num):
                               group = linux.getGroup(to)
                               members = [ls]
                               linux.acquireGroupCallRoute(to)
                               linux.inviteIntoGroupCall(to, contactIds=members)
                           ret_ += "\n├> @!"
                       ret_ += "\n╰──────────"
                       linux.sendMessage(to, ret_, lists)                          
#
                
                elif msg.text.startswith("/โทร"):
                   dan = text.split(" ")
                   num = int(dan[1])
                   ret_ = "╭──[ เชิญโทรสำเร็จ ]"
                   if 'MENTION' in msg.contentMetadata.keys()!= None:
                       names = re.findall(r'@(\w+)', text)
                       mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                       mentionees = mention['MENTIONEES']
                       lists = []
                       for mention in mentionees:
                           if mention["M"] not in lists:
                               lists.append(mention["M"])
                       for ls in lists:
                           for var in range(0,num):
                               group = linux.getGroup(to)
                               members = [ls]
                               linux.acquireGroupCallRoute(to)
                               linux.inviteIntoGroupCall(to, contactIds=members)
                           ret_ += "\n├> @!"
                       ret_ += "\n╰──────────"
                       linux.sendMessage(to, "🌸 สแปมคลอเรียบร้อย 🌸")
                       #linux.sendMessage(to, ret_, lists) 
                elif "โทร" in msg.text.lower():
                    if msg.toType == 2:
                        sep = msg.text.split(" ")
                        resp = msg.text.replace(sep[0] + " ","")
                        num = int(resp)
                        try:
                            linux.sendMessage(msg.to,"กำลังดำเนินการ...")
                        except:
                            pass
                        for var in range(num):
                            group = linux.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            linux.acquireGroupCallRoute(msg.to)
                            linux.inviteIntoGroupCall(msg.to, contactIds=members)
                        linux.sendMessage(msg.to,"เชิญคอลสำเร็จแล้ว(｀・ω・´)")                        
                elif msg.text.lower().startswith("โหล "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = linux.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = linux.getContact(receiver)
                                RhyN_(to, contact.mid)

                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ", "")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    linux.sendAudio(msg.to, "hasil.mp3")  
                if text.lower() == "เทส":
                    rainbow1 = ("#0008FF","#FF99FF","#3333CC","#000088","#CC9933","#33FFCC","#0000EE","#AAAAAA","#000000","#FF0000","#DE00D4","#05092A","#310206","#5300FC","#FF00FF","#6600CC","#0000AA","#FFFF00","#66FFFF","#66FF66","#66CCFF","#CC0033")
                    rainbow = random.choice(rainbow1)
                    rainbow2 = ("#0008FF","#FF99FF","#3333CC","#000088","#CC9933","#33FFCC","#0000EE","#AAAAAA","#000000","#FF0000","#DE00D4","#05092A","#310206","#5300FC","#FF00FF","#6600CC","#0000AA","#FFFF00","#66FFFF","#66FF66","#66CCFF","#CC0033")
                    rainbo2 = random.choice(rainbow2)
                    rainbow3 = ("#0008FF","#FF99FF","#3333CC","#000088","#CC9933","#33FFCC","#0000EE","#AAAAAA","#000000","#FF0000","#DE00D4","#05092A","#310206","#5300FC","#FF00FF","#6600CC","#0000AA","#FFFF00","#66FFFF","#66FF66","#66CCFF","#CC0033")
                    rainbo3 = random.choice(rainbow3)
                    rainbow4 = ("#0008FF","#FF99FF","#3333CC","#000088","#CC9933","#33FFCC","#0000EE","#AAAAAA","#000000","#FF0000","#DE00D4","#05092A","#310206","#5300FC","#FF00FF","#6600CC","#0000AA","#FFFF00","#66FFFF","#66FF66","#66CCFF","#CC0033")
                    rainbo4 = random.choice(rainbow4)
                    rainbow5 = ("#0008FF","#FF99FF","#3333CC","#000088","#CC9933","#33FFCC","#0000EE","#AAAAAA","#000000","#FF0000","#DE00D4","#05092A","#310206","#5300FC","#FF00FF","#6600CC","#0000AA","#FFFF00","#66FFFF","#66FF66","#66CCFF","#CC0033")
                    rainbo5 = random.choice(rainbow5)
                    data={
#                if text.lower() == 'เทส':#FF0000","#FFFFFF","#0000FF","#00FF33","#000000
#                	rainbow1 = ("#0008FF","#FF99FF","#3333CC","#000088","#CC9933","#33FFCC","#0000EE","#AAAAAA","#000000","#FF0000","#DE00D4","#05092A","#310206","#5300FC","#FF00FF","#6600CC","#0000AA","#FFFF00","#66FFFF","#66FF66","#66CCFF","#CC0033")
#                	rainbow = random.choice(rainbow1)
#                	data = {              
                                        "type": "flex",
                                        "altText": "🌸กำลังโหลด...🌸",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "10%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "10%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbow,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
    "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "20%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "20%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbo2,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
    "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "30%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "30%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbo3,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "40%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "40%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#FAD2A76E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbo4,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
    "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "50%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "50%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbo5,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
    "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "60%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "60%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbo2,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
    "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "70%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "70%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbo3,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
    "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "80%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "80%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbo5,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "90%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "90%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#FAD2A76E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbo4,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🌸ᴅᴏᴡʟᴏᴀᴅ🌸",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "100%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "100%",
                "backgroundColor": "#FFFFFF",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": rainbow,
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "🌸กำลังโหลด🌸",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": True
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    }
  ]
}
}
                    sendTemplate(to, data)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = linux.getGroup(to)
                    linux.sendMessage(to, " " + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = linux.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    linux.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = linux.getGroup(to)
                    linux.sendMessage(to, "ชื่อกลุ่ม -> \n" + gid.name)    
#                    
#                elif msg.text in ["เปิดอ่าน"]:
#                    read["autoRead"] = True
#                    linux.sendMessage(to, "aütoRead : on •➣➣")
#                    linux.sendMessage(to, "❂• เปิดอ่านข้อความอัติโนมัติคับ •❂")
#                elif msg.text in ["ปิดอ่าน"]:
#                    read["autoRead"] = False
#                    linux.sendMessage(to, "aütoRead : off •➣➣")
#                    linux.sendMessage(to, "❂• ปิดอ่านข้อความอัติโนมัติคับ •❂")
#                      
#                elif 'กันเรา ' in msg.text:
#                   if msg._from in admin:
#                      spl = msg.text.replace('กันเรา ','')
#                      if spl == 'เปิด':
#                          if msg.to in protectantijs:
#                              msgs = ""
#                          else:
#                              protectantijs.append(msg.to)
#                          if msg.to in protectcancel:
#                              ginfo = linux.getGroup(msg.to)
#                              msgs = "สถานะ : [ เปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
#                              msgs += "\nเปิดกันตัวเราทั้งหมดอยู่แล้ว"
#                          else:
#                              protectcancel.append(msg.to)
#                              ginfo = linux.getGroup(msg.to)
#                              msgs = "สถานะ : [ เปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
#                              msgs += "\nเปิดกันตัวเราทั้งหมด"
#                          linux.sendMessage(msg.to, "「 การป้องกันตัวเรา 」\n" + msgs)
#                          try:
#                          	linux.inviteIntoGroup(msg.to,[Zmid])
#                          except:
#                          	pass
#                      elif spl == 'ปิด':
#                            if msg.to in protectantijs:
#                            	protectantijs.remove(msg.to)
#                            	ginfo = linux.getGroup(msg.to)
#                            	msgs = "สถานะ : [ ปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
#                            else:
#                            	msghs = ""
#                            if msg.to in protectcancel:
#                            	protectcancel.remove(msg.to)
#                            	ginfo = linux.getGroup(msg.to)
#                            	msgs = "สถานะ : [ ปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
#                            	msgs += "\nปิดกันตัวเราทั้งหมดอยู่แล้ว"
#                            else:
#                            	ginfo = linux.getGroup(msg.to)
#                            	msgs = "สถานะ : [ ปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
#                            	msgs += "\nปิดกันตัวเราทั้งหมด"
#                            linux.sendMessage(msg.to, "「 การป้องกันตัวเรา 」\n" + msgs)
#                            
#                elif 'ช่วยกัน ' in msg.text:
#                   if msg._from in admin:
#                      spl = msg.text.replace('ช่วยกัน ','')
#                      if spl == 'เปิด':
#                          if msg.to in protectantijs:
#                              msgs = ""
#                          else:
#                              protectantijs.append(msg.to)
#                          if msg.to in protectcancel:
#                              ginfo = linux.getGroup(msg.to)
#                              msgs = "สถานะ : [ เปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
#                              msgs += "\nเปิดกันตัวเราทั้งหมดอยู่แล้ว"
#                          else:
#                              protectcancel.append(msg.to)
#                              ginfo = linux.getGroup(msg.to)
#                              msgs = "สถานะ : [ เปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
#                              msgs += "\nเปิดกันตัวเราทั้งหมด"
#                          linux.sendMessage(msg.to, "「 การป้องกันตัวเรา 」\n" + msgs)
#                          try:
#                          	k1.inviteIntoGroup(msg.to,[Zmid])
#                          except:
#                          	pass
#                      elif spl == 'ปิด':
#                            if msg.to in protectantijs:
#                            	protectantijs.remove(msg.to)
#                            	ginfo = linux.getGroup(msg.to)
#                            	msgs = "สถานะ : [ ปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
#                            else:
#                            	msghs = ""
#                            if msg.to in protectcancel:
#                            	protectcancel.remove(msg.to)
##                            	ginfo = linux.getGroup(msg.to)
#                            	msgs = "สถานะ : [ ปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
###                            	msgs += "\nปิดกันตัวเราทั้งหมดอยู่แล้ว"
#                            else:
#                            	ginfo = linux.getGroup(msg.to)
#                            	msgs = "สถานะ : [ ปิดใช้งาน ]\nชื่อกลุ่ม : " +str(ginfo.name)
#                            	msgs += "\nปิดกันตัวเราทั้งหมด"
##                            linux.sendMessage(msg.to, "「 การป้องกันตัวเรา 」\n" + msgs)
#
##                elif msg.text.lower() == "มา":
#                  if wait["selfbot"] == True:
#                    if msg._from in admin:
#                        try:
#                            linux.inviteIntoGroup(msg.to,[Zmid,Amid])
#                            g1.acceptGroupInvitation(msg.to)
#                            g2.acceptGroupInvitation(msg.to)
#                        except:
#                            pass
#                elif cmd == "ไป":
#                  if wait["selfbot"] == True:
#                   if msg._from in admin:
#                       G = linux.getGroup(msg.to)
#                       g1.leaveGroup(msg.to)
#                       g2.leaveGroup(msg.to)
#
##                elif cmd == "ผชมา":
#                  if msg._from in admin:
#                   if msg.toType == 2:
#                       group = linux.getGroup(to)
#                       group.preventedJoinByTicket = False
##                       linux.updateGroup(group)
###                       invsend = 0
#                       ticket = linux.reissueGroupTicket(to)
#                       k1.acceptGroupInvitationByTicket(to,format(str(ticket)))
#                       time.sleep(0.01)
#                       group = k1.getGroup(to)
#                       group.preventedJoinByTicket = True
#                       k1.updateGroup(group)
#                       
#                elif cmd == "ผชไป":
#                  if wait["selfbot"] == True:
#                   if msg._from in admin:
#                       G = linux.getGroup(msg.to)
#                       k1.leaveGroup(msg.to)
#                       
                elif msg.text.lower().startswith("ตาม "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            linux.sendMessage(to,"🌸 ระบบเริ่มการเลียนแบบ 🌸")
                            break
                        except:
                            linux.sendMessage(to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("เลิกตาม "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            linux.sendMessage(to,"🌸 ระบบเลิกการพูดตาม 🌸")
                            break
                        except:
                            linux.sendMessage(to,"Deleted Target Fail !")
                            break

                elif text.lower() == 'เชคตัวอย่าง':
                    if settings["mimic"]["target"] == {}:
                        linux.sendMessage(to, "🌸 รายชื่อเลียนแบบ  " +datetime.today().strftime('%H:%M:%S')+ "™ 🌸") 
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+linux.getContact(mi_d).displayName
                        linux.sendMessage(to + "\n╚══[ Finish ]")

                elif "เลียนแบบ" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "เปิด":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            linux.sendMessage(to, "🌸 เปิดเลียนแบบ 🌸")
                    elif mic == "ปิด":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            linux.sendMessage(to, "🌸 ปิดเลียนแบบ 🌸")
#                            
                elif "อัพชื่อไวรัส " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","􀰂􀰂")
                        na = "􏿿"
                        profile_A = linux.getProfile()
                        profile_A.displayName = string + str(na)
                        linux.updateProfile(profile_A)
                        linux.sendMessage(to,"Update to :\n" + string + str(na))
                        print ("Update Name")
                elif msg.text.lower().startswith("ชื่อไวรัส "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","􀰂􀰂")
                    ss = "􏿿"
                    linux.sendMessage(msg.to, textnya + str(ss))                         
                elif "อัพชื่อ " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = linux.getProfile()
                        profile_A.displayName = string
                        linux.updateProfile(profile_A)
                        linux.sendMessage(to,"🔻เปลี่ยนชื่อเป็น🔻\n" + string)
                        print ("Update Name")
                elif msg.text.lower().startswith("อัพตัส "):
                    string = msg.text.lower().replace("อัพตัส", "")
                    if len(string) <= 10000000000:
                        pname = linux.getContact(sender).statusMessage
                        profile = linux.getProfile()
                        profile.statusMessage = string
                        linux.updateProfile(profile)
                        userid = "https://line.me/ti/p/~" + linux.profile.userid
#----------------------------------------------------------------------------#                        
                elif cmd == "อัพปก":
                    settings["changeProfileCover"] = True
                    linux.sendMessage(to, "🌸ส่งรูปภาพที่ต้องการลงมา🌸")
                elif text.lower() == "อัพดิส":
                    settings["changePictureProfile"] = True
                    linux.sendMessage(to, "🌸ส่งรูปภาพที่ต้องการลงมา🌸")
#----------------------------------------------------------------------------#                                                
                elif cmd == "/เชคออน":
                    proses = os.popen("screen -list")
                    a = proses.read()
                    linux.sendMessage(to, "{}\n-「『Ẫµŧø ฿øŧĹįח€』 」-".format(str(a)))
                    proses.close() 
                elif cmd.startswith("ขอเพลง "):
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl=("https://www.youtube.com" + results['href'])
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = "Youtube - Video :\n"
                                    hasil += "\nTitle : {}".format(str(vid.title))
                                    hasil += "\nSubscriber From : {}".format(str(vid.author))
                                linux.generateReplyMessage(msg.id)
                                linux.sendReplyMessage(msg.id, to,hasil)
                                linux.sendVideoWithURL(msg.to,vin)
                                print("[YOUTUBE]MP4 Succes")
                            except Exception as e:
                                linux.generateReplyMessage(msg.id)
                                linux.sendReplyMessage(msg.id, to,str(e))
                elif cmd.startswith("/นับ "):
                  #          if msg._from in "u51f2d901e6ae79ea2649062da18176df":
                               number = removeCmd("/นับ", text)
                               if len(number) > 0:
                                   if number.isdigit():
                                       number = int(number)
                                       if number > 1000000:                                             
                                           linux.sendMessage(to,"invalid >_< ! Max: 1000000.")
                                       else:
                                           for i in range(0,number):
                                               linux.sendMessage(to,str(number))
                                               number -= 1
                                               time.sleep(0.01)
                                   else:
                                      linux.sendMessage(to,"Please specify a valid number.")
#---------------------------------------------------------------------------------------------------------------------------#
#📌📌  ปักหมุด modifile by: nn # ปักครั้งเดียว บอกหมุด4รูปแบบ
#---------------------------------------------------------------------------------------------------------------------------#
#----------------------------ปักหมุดเฟก BY: NN-------------------------------------------------------------------#                                      
                elif msg.text in ["เชคหมุด"]:
                    a = linux.getGroupIdsJoined()
                    ret_ = " 📍รายชื่อกลุ่มที่ปักหมุด📍"
                    num = 1
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            group = linux.getGroup(manusia)
                            ret_ += "\n {}. {} \n🌸จำนวน {} คน".format(str(num), str(group.name), str(len(group.members)))
                            num=(num+1)					
                    linux.sendMessage(to, str(ret_))
#----------------------------------------------------------------------------#
                elif msg.text in ["ปักหมุด"]:
                    apalo["bc"][receiver] = True
                    linux.sendMessage(receiver,"📍ปักหมุดกลุ่มนี้เรียบร้อย📍")
                   
                elif msg.text in ["ลบหมุด"]:
                    try:
                        del apalo["bc"][receiver]
                        linux.sendMessage(receiver,"📍ลบหมุดออกเรียบร้อย📍")
                    except:
                        linux.sendMessage(receiver," 📍ไม่พบหมุดในกลุ่ม📍 ")
#----------------------[บอกหมุด 4 รูปแบบ]------------------------------------------------------#                 
                elif "ประกาศหมุด " in msg.text.lower():
                    bctxt = msg.text.replace("ประกาศหมุด ", "")
                    a = linux.getGroupIdsJoined()
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            linux.sendMessage(manusia,(bctxt))
                            time.sleep(1)
                    linux.sendMessage(receiver,"📍ประกาศหมุดเรียบร้อย📍")  
               
                elif "บอกหมุด2: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด2: ", "")
                    a = linux.getGroupIdsJoined()
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            linux.sendMessage(manusia,(bctxt))
                            time.sleep(1)
                    linux.sendMessage(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")
             
                elif "บอกหมุด3: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด3: ", "")
                    a = linux.getGroupIdsJoined()
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            linux.sendMessage(manusia,(bctxt))
                            time.sleep(1)
                    linux.sendMessage(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")
             
                elif "บอกหมุด4: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด4: ", "")
                    a = linux.getGroupIdsJoined()
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            linux.sendMessage(manusia,(bctxt))
                            time.sleep(1)
                    linux.sendMessage(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")  
#---------------------------------------------------------------------------------------------------------------------------#
                elif msg.text.startswith("ตั้งรูป1: "):
                    text = msg.text.replace("ตั้งรูป1: ","")                    
                    usa["usa"] = text
                    linux.sendMessage(to, "🔻ลิ้งรูปประกาศ1🔻\n{}".format(str(usa["usa"])))
                    
                elif msg.text.startswith("ตั้งรูป2: "):
                    text = msg.text.replace("ตั้งรูป2: ","")
                    usa["usa1"] = text
                    linux.sendMessage(to, "🔻ลิ้งรูปประกาศ2🔻\n{}".format(str(usa["usa1"])))
                    
                elif msg.text.startswith("ตั้งรูป3: "):
                    text = msg.text.replace("ตั้งรูป3: ","")
                    usa["usa2"] = text
                    linux.sendMessage(to, "🔻ลิ้งรูปประกาศ3🔻\n{}".format(str(usa["usa2"])))
                    
                elif msg.text.startswith("ตั้งขาย1: "):
                    text = msg.text.replace("ตั้งขาย1: ","")                    
                    usa["us"] = text
                    linux.sendMessage(to, "🔻ข้อความประกาศ1🔻\n{}".format(str(usa["us"])))
                    
                elif msg.text.startswith("ตั้งขาย2: "):
                    text = msg.text.replace("ตั้งขาย2: ","")
                    usa["us1"] = text
                    linux.sendMessage(to, "🔻ข้อความประกาศ2🔻\n{}".format(str(usa["us1"])))
                    
                elif msg.text.startswith("ตั้งขาย3: "):
                    text = msg.text.replace("ตั้งขาย3: ","")
                    usa["us2"] = text
                    linux.sendMessage(to, "🔻ข้อความประกาศ3🔻\n{}".format(str(usa["us2"])))   
   
                elif msg.text.startswith("ลิ้งรูปประกาศ1 "):
                    text = msg.text.replace("ลิ้งรูปประกาศ1 ","")
                    bed["bed1"] = text
                    linux.sendMessage(to, "🔻ลิ้งรูปประกาศออโต้1🔻 \n{}".format(str(bed["bed1"])))
                elif msg.text.startswith("ลิ้งรูปประกาศ2 "):
                    text = msg.text.replace("ลิ้งรูปประกาศ2 ","")                    
                    bed["bed2"] = text
                    linux.sendMessage(to, "🔻ลิ้งรูปประกาศออโต้2🔻 \n{}".format(str(bed["bed2"])))
                elif msg.text.startswith("ลิ้งรูปประกาศ3 "):
                    text = msg.text.replace("ลิ้งรูปประกาศ3 ","")                    
                    bed["bed3"] = text
                    linux.sendMessage(to, "🔻ลิ้งรูปประกาศออโต้3🔻 \n{}".format(str(bed["bed3"])))                    
                
                elif msg.text.startswith("ตั้งประกาศ1 "):
                    text = msg.text.replace("ตั้งประกาศ1 ","")
                    bed["tetx"] = text
                    linux.sendMessage(to, "🔻ข้อความประกาศออโต้1🔻 \n{}".format(str(bed["tetx"])))
                elif msg.text.startswith("ตั้งประกาศ2 "):
                    text = msg.text.replace("ตั้งประกาศ2 ","")
                    bed["tetx2"] = text
                    linux.sendMessage(to, "🔻ข้อความประกาศออโต้2🔻 \n{}".format(str(bed["tetx2"])))
                elif msg.text.startswith("ตั้งประกาศ3 "):
                    text = msg.text.replace("ตั้งประกาศ3 ","")
                    bed["tetx3"] = text
                    linux.sendMessage(to, "🔻ข้อความประกาศออโต้3🔻 \n{}".format(str(bed["tetx3"])))
 
                elif text.lower() == 'เปิดประกาศ':
                    bed["bed"] = True
                    linux.sendMessage(to, "ประกาศออโต้จะเริ่มทำงานอีก1ชั่วโมง ✓") 
                    
                elif text.lower() == 'ปิดประกาศ':
                    bed["bed"] = False
                    linux.sendMessage(to, "ประกาศออโต้จะปิดทำงานอีก1ชั่วโมง ❎") 
                    
                elif msg.text.startswith("ลิ้งติดต่อ "):
                    text = msg.text.replace("ลิ้งติดต่อ ","")
                    uu["uuu"] = text
                    linux.sendMessage(to, "🔻ลิ้งผู้ติดต่อ🔻\n{}".format(str(uu["uuu"])))

                elif msg.text.startswith("ตั้งเวลา "):
                    text = msg.text.replace("ตั้งเวลา ","")                    
                    bed["TIME"] = text
                    linux.sendMessage(to, "🔻เวลาประกาศออโต้🔻\nตั้งประกาศทุกๆ {} วินาที".format(str(bed["TIME"])))
  
                elif msg.text.startswith("ตั้งสีขอบ "):
                    text = msg.text.replace("ตั้งสีขอบ ","")                    
                    uck["uck1"] = text
                    linux.sendMessage(to, "🔻เปลี่ยนสีกรอบเชล🔻\n{}".format(str(uck["uck1"])))
                    
                elif msg.text.startswith("ตั้งสีme "):
                    text = msg.text.replace("ตั้งสีme ","")
                    uck["uck2"] = text
                    linux.sendMessage(to, "🔻เปลี่ยนสีหัวข้อ🔻\n{}".format(str(uck["uck2"])))
                    
                elif msg.text.startswith("ตั้งสีอักษร "):
                    text = msg.text.replace("ตั้งสีอักษร ","")
                    uck["uck3"] = text
                    linux.sendMessage(to, "🔻เปลี่ยนสีอักษร🔻\n{}".format(str(uck["uck3"])))                 
#---------------------------------------------------------------------------------------------------------------------------#
#==============โหมดคณิตศาร==============
                elif text.lower() == 'เครื่องคิดเลข':
                    linux.sendMessage(to, "วิธีการใช้งาน\nสูตรคูณแม่ /mtpt [ ตัวเลข ]\nคูณ /mtp [ ตัวเลข ] [ ตัวเลข ]\nหาร /divide [ ตัวเลข ] [ ตัวเลข ]\nบวก /plus [ ตัวเลข ] [ ตัวเลข ]\nลบ /minus [ ตัวเลข ] [ ตัวเลข ]")
                elif text.startswith("/mtpt"):
                            separate = text.split(" ")
                            try:
                                m = int(text.replace(separate[0] + " ",""))
                                txt = "สูตรคูณแม่ " + str(m) + "\n──────────────"
                                for i in range(12):
	                                x = i+1
	                                txt+="\n" + str(m) + " * " + str(x) + " = " + str(m * x)
                                linux.sendMessage(msg.to, (txt))
                            except:
                                linux.sendMessage(msg.to, ("😍"))
                if text.startswith("/mtp"):
                            separate = text.split(" ")
                            try:
                                t1 = int(text.split(" ")[1])
                                t2 = int(text.split(" ")[2])
                                txt = str(t1) + " * " + str(t2) + "\n──────────────"
                                txt+="\n" + str(t1 * t2)
                                linux.sendMessage(to, str(txt))
                            except:
                                linux.sendMessage(to, "วิธีการใช้งาน:\n/mtp [ ตัวเลข ] [ ตัวเลข ]")
       
                if text.startswith("/divide"):
                            separate = text.split(" ")
                            try:
                                t1 = int(text.split(" ")[1])
                                t2 = int(text.split(" ")[2])
                                txt = str(t1) + " / " + str(t2) + "\n──────────────"
                                txt+="\n" + str(t1 / t2)
                                linux.sendMessage(to, str(txt))
                            except:
                                linux.sendMessage(to, "วิธีการใช้งาน:\n/divide [ ตัวเลข ] [ ตัวเลข ]")
                if text.startswith("/plus"):
                            separate = text.split(" ")
                            try:
                                t1 = int(text.split(" ")[1])
                                t2 = int(text.split(" ")[2])
                                txt = str(t1) + " + " + str(t2) + "\n──────────────"
                                txt+="\n" + str(t1 + t2)
                                linux.sendMessage(to, str(txt))
                            except:
                                linux.sendMessage(to, "วิธีการใช้งาน:\n/plus [ ตัวเลข ] [ ตัวเลข ]")
           
                if text.startswith("/minus"):
                            separate = text.split(" ")
                            try:
                                t1 = int(text.split(" ")[1])
                                t2 = int(text.split(" ")[2])
                                txt = str(t1) + " - " + str(t2) + "\n──────────────"
                                txt+="\n" + str(t1 - t2)
                                linux.sendMessage(to, str(txt))
                            except:
                                linux.sendMessage(to, "วิธีการใช้งาน:\n/minus [ ตัวเลข ] [ ตัวเลข ]")                           
#=====================================================================                
                if text.lower() == "เปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = True
                      linux.sendMessage(to,"🌸 เปิดบล็อคเรียบร้อย 🌸")
                  else:
                      linux.sendMessage(to,"🌸 บล็อคเปิดเรียบร้อย 🌸")
                if text.lower() == "ปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = False
                      linux.sendMessage(to,"🌸 ปิดบล็อคเรียบร้อย 🌸")
                  else:
                      linux.sendMessage(to,"🌸 บล็อคปิดเรียบร้อย 🌸")
                if text.lower() == "เปิดแทค":
                    tagadd["tags"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดแทคเรียบร้อย 🌸")
                if text.lower() == "ปิดแทค":
                    tagadd["tags"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดแทคเรียบร้อย 🌸")
                if text.lower() == "เปิดกันรัน":
                    sets["autoCancel"]["on"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดกันรันเรียบร้อย 🌸")
                if text.lower() == "ปิดกันรัน":
                    sets["autoCancel"]["on"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดกันรันเรียบร้อย 🌸")
                if text.lower() == "เปิดแอด":
                    settings["autoAdd"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดแอดเรียบร้อย 🌸")
                if text.lower() == "ปิดแอด":
                    settings["autoAdd"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดแอดเรียบร้อย 🌸")
                if text.lower() == "ปิดไลค์":
                   settings["autolike"] = False
                   linux.unsendMessage(msg_id)
                   linux.sendMessage(to, "🌸 ปิดไลค์แล้ว 🌸")
                if text.lower() == "เปิดไลค์":
                   settings["autolike"] = True
                   linux.unsendMessage(msg_id)
                   linux.sendMessage(to, "🌸 เปิดไลค์แล้ว 🌸")                    
#                if text.lower() == "เปิดไลค์":
#                    settings["autolike"] = True
#                    linux.unsendMessage(msg_id)
#                    linux.sendMessage(to, "?? เปิดไลค์เรียบร้อย 🦋")
#                if text.lower() == "ปิดไลค์":
#                    settings["autolike"] = False
#                    linux.unsendMessage(msg_id)
#                    linux.sendMessage(to, "🦋 ปิดไลค์เรียบร้อย 🦋")
            #    if text.lower() == "เปิดแทค2":
            #        tagadd["tagss"] = True
            #        linux.sendMessage(to, "เปิดระบบเรียบร้อยแล้ว")
            #    if text.lower() == "ปิดแทค2":
            #        tagadd["tagss"] = False
            #        linux.sendMessage(to, "ปิดระบบเรียบร้อยแล้ว")
                if text.lower() == "ปิดคอมเม้น":
                    settings["com"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดคอมเม้นเรียบร้อย 🌸")
                if text.lower() == "เปิดคอมเม้น":
                    settings["com"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดคอมเม้นเรียบร้อย 🌸")
#                if text.lower() == "เปิดคอมเม้น":
#                    settings["com"] = True
#                    linux.unsendMessage(msg_id)
#                    linux.sendMessage(to, "🦋 เปิดคอมเม้นเรียบร้อย 🦋")
#                if text.lower() == "ปิดคอมเม้น":
#                    settings["com"] = False
#                    linux.unsendMessage(msg_id)
#                    linux.sendMessage(to, "🦋 ปิดคอมเม้นเรียบร้อย 🦋")
            #    if text.lower() == "เปิดต้อนรับ":
            #        settings["Welcome"] = True
            #        linux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "🦋 เปิดต้อนรับเรียบร้อย 🦋")
            #    if text.lower() == "ปิดต้อนรับ":
            #        settings["Welcome"] = False
            #        linux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "🦋 ปิดต้อนรับเรียบร้อย 🦋")
            #    if text.lower() == "เปิดต้อนรับ2":
            #        settings["Wc"] = True
            #        linux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "?? เปิดต้อนรับ2เรียบร้อย 🦋")
            #    if text.lower() == "ปิดต้อนรับ2":
            #        settings["Wc"] = False
            #        linux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "🦋 ปิดต้อนรับ2เรียบร้อย ??")
            #    if text.lower() == "เปิดคนออก":
            #        settings["Leave"] = True
            #        linux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "🦋 เปิดคนออกเรียบร้อย 🦋")
            #    if text.lower() == "ปิดคนออก":
            #        settings["Leave"] = False
            #        linux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "🦋 ปิดคนออกเรียบร้อย 🦋")
                if text.lower() == "เปิดยกเลิก":
                    settings["unsendMessage"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดยกเลิกเรียบร้อย 🌸")
                if text.lower() == "ปิดยกเลิก":
                    settings["unsendMessage"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดยกเลิกเรียบร้อย 🌸")
                if text.lower() == "เปิดติ๊กapi":
                    settings["Sticker"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดติ๊กapiเรียบร้อย 🌸")
                if text.lower() == "ปิดติ๊กapi":
                    settings["Sticker"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดติ๊กapiเรียบร้อย 🌸")                  
                if text.lower() == "เปิดโค้ดติ้ก":
                    sets["Sticker"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดโค๊ดติ๊กเรียบร้อย 🌸")
                if text.lower() == "ปิดโค้ดติ้ก":
                    sets["Sticker"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดโค๊ดติ๊กเรียบร้อย 🌸")
                if text.lower() == "เปิดแทค2":
                    sets["tagsticker"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดแทค2เรียบร้อย 🌸")
                if text.lower() == "ปิดแทค2":
                    sets["tagsticker"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดแทค2เรียบร้อย 🌸")
            #    if text.lower() == "เปิดติ๊กคนออก":
            #        settings["lv"] = True
            #        mlinux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "🦋 เปิดติ๊กคนออกเรียบร้อย 🦋")
            #    if text.lower() == "ปิดติ๊กคนออก":
            #        settings["lv"] = False
            #        linux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "🦋 ปิดติ๊กคนออกเรียบร้อย 🦋")
            #    if text.lower() == "เปิดติ๊กคนเข้า":
            #        settings["wcsti2"] = True
            #        linux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "🦋 เปิดติ๊กคนเข้าเรียบร้อย 🦋")
            #    if text.lower() == "ปิดติ๊กคนเข้า":
            #        settings["wcsti2"] = False
            #        linux.unsendMessage(msg_id)
            #        linux.sendMessage(to, "🦋 ปิดติ๊กคนเข้าเรียบร้อย 🦋")
                if text.lower() == "เปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดมุดลิ้งเรียบร้อย 🌸")
                if text.lower() == "ปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดมุดลิ้งเรียบร้อย 🌸")
                if text.lower() == "เปิดติ๊กใหญ่":
                    sets["sti2"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดติ๊กใหญ่เรียบร้อย 🌸")
                if text.lower() == "ปิดติ๊กใหญ่":
                    sets["sti2"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดติ๊กใหญ่เรียบร้อย 🌸")
                if text.lower() == "เปิดออกแชทรวม":
                    sets["leaveRoom"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดออกแชทรวม 🌸")
                if text.lower() == "ปิดออกแชทรวม":
                    sets["leaveRoom"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดออกแชทรวม 🌸")
                if text.lower() == "เปิดกันสแปม":
                    spamc["spamcall"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดกันสแปมแชทเรียบร้อย 🌸")
                if text.lower() == "ปิดกันสแปม":
                    spamc["spamcall"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดกันสแปมแชทเรียบร้อย 🌸") 
                elif text.lower() == 'เปิดอ่าน':
                    reads["autoRead"] = True
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 เปิดอ่านข้อความอัตโนมัติ 🌸")
                elif text.lower() == 'ปิดอ่าน':
                    reads["autoRead"] = False
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ปิดอ่านข้อความอัตโนมัติ 🌸")
                    
                elif cmd == "เปิดเข้า":
                	if msg._from in admin:
                          if settings['autoJoin'] == True:
                          	msgs="🌸 เข้ากลุ่มอัตโนมัติเปิดอยู่แล้ว 🌸"
                          else:
                          	settings['autoJoin']=True
                          	msgs="🌸 เปิดเข้ากลุ่มอัตโนมัติเรียบร้อย 🌸"
                          linux.sendMessage(msg.to, msgs)
                    
                elif cmd == "ปิดเข้า":
                    if settings['autoJoin'] == False:
                        msgs=" 「 Auto Join 」\nAuto Join already set to DISABLED♪"
                    else:
                        msgs=" 「 Auto Join 」\nAuto Join has been set to DISABLED♪"
                        settings['autoJoin']=False
                    linux.sendMessage(msg.to, msgs)                    
#                                
                elif msg.text.lower().startswith("กันเตะ "):
                    text = removeCmd("กันเตะ", text)
                    spl = text.replace('prokick ', text)
                    if spl == 'เปิด':
                        if msg.to in protectkick:
                             msgs = "เปิดระบบกันเตะเรียบร้อย"
                        else:
                             protectkick.append(msg.to)
                             ginfo = linux.getGroup(msg.to)
                             msgs = "เปิดระบบกันเตะเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                        linux.sendMessage(to, "「 โหมดป้องกันเตะ 」\n" + msgs)
                    elif spl == 'ปิด':
                          if msg.to in protectkick:
                               protectkick.remove(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "ปิดระบบกันเตะเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                          else:
                               msgs = "ปิดระบบกันเตะเรียบร้อย"
                          linux.sendMessage(to, "「 โหมดป้องกันเตะ 」\n" + msgs)
                elif msg.text.lower().startswith("กันเชิญ "):
                    text = removeCmd("กันเชิญ", text)
                    spl = text.replace('proinv ', text)
                    if spl == 'เปิด':
                        if msg.to in protectinvite:
                             msgs = "เปิดระบบกันเชิญคนเรียบร้อย"
                        else:
                             protectinvite.append(msg.to)
                             ginfo = linux.getGroup(msg.to)
                             msgs = "เปิดระบบกันเชิญคนเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                        linux.sendMessage(to, "「 โหมดป้องกันเชิญ 」\n" + msgs)
                    elif spl == 'ปิด':
                          if msg.to in protectinvite:
                               protectinvite.remove(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "ปิดระบบเชิญคนเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                          else:
                               msgs = "ปิดระบบเชิญคนเรียบร้อย"
                          linux.sendMessage(to, "「 โหมดป้องกันเชิญ 」\n" + msgs) 
                elif msg.text.lower().startswith("กันยก "):
                    text = removeCmd("กันยก", text)
                    spl = text.replace('procan ', text)
                    if spl == 'เปิด':
                        if msg.to in protectcancel:
                             msgs = "เปิดระบบกันยกเชิญเรียบร้อย"
                        else:
                             protectcancel.append(msg.to)
                             ginfo = linux.getGroup(msg.to)
                             msgs = "เปิดระบบกันยกเชิญเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                        linux.sendMessage(to, "「 โหมดป้องกันยกเชิญ 」\n" + msgs)
                    elif spl == 'ปิด':
                          if msg.to in protectcancel:
                               protectinvite.remove(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "ปิดระบบกันยกเชิญเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                          else:
                               msgs = "ปิดระบบกันยกเชิญเรียบร้อย"
                          linux.sendMessage(to, "「 โหมดป้องกันยกเชิญ 」\n" + msgs)                                    
                elif msg.text.lower().startswith("กันเข้า "):
                    text = removeCmd("กันเข้า", text)
                    spl = text.replace('กันเข้า ', text)
                    if spl == 'เปิด':
                        if msg.to in protectjoin:
                             msgs = "เปิดระบบกันคนเข้าเรียบร้อย"
                        else:
                             protectjoin.append(msg.to)
                             ginfo = linux.getGroup(msg.to)
                             msgs = "เปิดระบบกันคนเข้าเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                        linux.sendMessage(to, "「 โหมดป้องกันคนเข้า 」\n" + msgs)
                    elif spl == 'ปิด':
                          if msg.to in protectjoin:
                               protectjoin.remove(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "เปิดระบบกันคนเข้าเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                          else:
                               msgs = "เปิดระบบกันคนเข้าเรียบร้อย"
                          linux.sendMessage(msg.to, "「 โหมดป้องกันตนเข้า 」\n" + msgs)                            
                elif msg.text.lower().startswith("กันลิ้ง "):
                    text = removeCmd("กันลิ้ง", text)
                    spl = text.replace('proqr ', text)
                    if spl == 'เปิด':
                        if msg.to in protectqr:
                             msgs = "เปิดระบบป้องกันลิ้งกลุ่ม"
                        else:
                             protectqr.append(msg.to)
                             ginfo = linux.getGroup(msg.to)
                             msgs = "เปิดระบบป้องกันลิ้งกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                        linux.sendMessage(to, "「 โหมดป้องกันลิ้ง 」\n" + msgs)
                    elif spl == 'ปิด':
                          if msg.to in protectqr:
                               protectqr.remove(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "ปิดระบบป้องกันลิ้ง\nกลุ่ม : " +str(ginfo.name)
                          else:
                               msgs = "ปิดระบบป้องกันลิ้ง"
                          linux.sendMessage(to, "「 โหมดกันลิ้ง 」\n" + msgs)    
#                                  
                elif msg.text.lower().startswith("ป้องกัน "):
                    text = removeCmd("ป้องกัน", text)
                    spl = text.replace('ป้องกัน  ', text)
                    if spl == 'เปิด':
                        if msg.to in protectqr:
                             msgs = ""
                        else:
                             protectqr.append(msg.to)
                        if msg.to in protectkick:
                            msgs = ""
                        else:
                            protectkick.append(msg.to)
                        if msg.to in protectinvite:
                             msgs = ""
                        else:
                            protectinvite.append(msg.to)           
                        if msg.to in protectcancel:
                             msgs = ""
                        else:
                            protectcancel.append(msg.to)
                            ginfo = linux.getGroup(msg.to)
                            msgs = "เปิดระบบป้องทั้งหมดเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                            ginfo = linux.getGroup(msg.to)
                            msgs = "เปิดระบบป้องกันทั้งหมดเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                        linux.sendMessage(to, "「 โหมดป้องกันกลุ่ม 」\n" + msgs)
                    elif spl == 'ปิด':
                          if msg.to in protectqr:
                               protectqr.remove(msg.to)
                          else:
                               msgs = ""
                          if msg.to in protectkick:
                               protectkick.remove(msg.to)
                          else:
                               msgs = ""
                          if msg.to in protectinvite:
                               protectinvite.remove(msg.to)
                          else:
                               msgs = ""                                                                  
                          if msg.to in protectcancel:
                               protectcancel.remove(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "ปิดระบบป้องกันกลุ่มทั้งหมด\nกลุ่ม : " +str(ginfo.name)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "ปิดระบบป้องกันกลุ่มทั้งหมด\nกลุ่ม: " +str(ginfo.name)
                          linux.sendMessage(to, "「 โหมดป้องกันกลุ่ม 」\n" + msgs)
                          
                elif cmd == "เชคป้องกัน":
                        ma = ""
                        mb = ""
                        md = ""
                        me = ""
                        mc = ""
                        a = 0
                        b = 0
                        d = 0
                        e = 0
                        c = 0
                        gid = protectqr
                        for group in gid:
                            a = a + 1
                            end = '\n'
                            ma += str(a) + ". " +linux.getGroup(group).name + "\n"
                        gid = protectkick
                        for group in gid:
                            b = b + 1
                            end = '\n'
                            mb += str(b) + ". " +linux.getGroup(group).name + "\n"
                        gid = protectjoin
                        for group in gid:
                            d = d + 1
                            end = '\n'
                            md += str(d) + ". " +linux.getGroup(group).name + "\n"
                        gid = protectinvite
                        for group in gid:
                            e = e + 1
                            end = '\n'
                            me += str(e) + ". " +linux.getGroup(group).name + "\n"
                        gid = protectcancel
                        for group in gid:
                            c = c + 1
                            end = '\n'
                            mc += str(e) + ". " +linux.getGroup(group).name + "\n"                                  
                        linux.sendMessage(to,"• รายชื่อกลุ่มที่ได้รับการป้องกัน •\n\n- ป้องกันลิ้งค์ :\n"+ma+"\n- ป้องกันคนเตะ :\n"+mb+"\n- ป้องกันคนเข้า :\n"+md+"\n- ป้องกันคนเชิน :\n"+mc+"\n- ป้องกันคนยกเชิน :\n"+mc+"\nจำนวน「%s」กลุ่ม" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectinvite)+len(protectcancel))))
#==============================================================================#                
                elif msg.text.lower().startswith("เลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimics["target"][target] = True
                            linux.sendMessage(to,"🌸 เพิ่มเลียนแบบเรียบร้อย 🌸")
                            break
                        except:
                            linux.sendMessage(to,"🌸 เพิ่มเลียนแบบผิดพลาด 🌸")
                            break
                elif msg.text.lower().startswith("ลบเลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimics["target"][target]
                            linux.sendMessage(to,"🌸 ลบจากรายการเลียนเรียบร้อย 🌸")
                            break
                        except:
                            linux.sendMessage(to,"🌸 ขออภัยไม่สามารถลบได้🌸")
                            break
                elif text.lower() == 'ลิสเลียนแบบ':
                    if mimics["target"] == {}:
                        linux.sendMessage(msg.to,"🌸 ไม่พบรายการเลียนแบบ 🌸")
                    else:
                        mc = "╔══[ จำนวนคนที่เลียนแบบ ]"
                        for mi_d in mimics["target"]:
                            mc += "\n╠ "+linux.getContact(mi_d).displayName
                        linux.sendMessage(msg.to,mc + "\n╚══[ Finish ]")     
#                  
                elif msg.text in ["เปิด:แอบ"]:
                    try:
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        linux.sendMessage(to, "💥เปิดระบบจับคนแอบ💥\n\n💥วันที่💥: "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n💥เวลา💥 [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                        del cctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    linux.sendMessage(msg.to,"เปิดระบบแสกนคนอ่านอัตโนมัติ")

                elif msg.text == "ปิด:แอบ":
                  if msg.to in RfuCctv['point']:
                      tz = pytz.timezone("Asia/Jakarta")
                      timeNow = datetime.now(tz=tz)
                      RfuCctv['cyduk'][msg.to]=False
                      linux.sendMessage(to, "💥ปิดระบบจับคนแอบ💥\n\n💥วันที่💥 : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n💥เวลา💥 [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                  else:
                      linux.sendMessage(to, "Sudak tidak aktif")
                      
#                if msg.text.lower() == "เริ่มนับ":
#                  group = linux.getGroup(msg.to)
#                  groupMemberMids = [i.mid for i in group.members if i.mid in admin]
#                  b=  "พิมว่า ปิดจับอ่าน เพื่อดูสมาชิกที่อ่านข้อความ (｀・ω・´)"
#                  if linuxMID in groupMemberMids:
#                      anuchai(to, b)
#                  else:
#                      anuchai(to,b)
#                  try:
#                      del read['readPoint'][msg.to]
#                      del read['readMember'][msg.to]
#                  except:
#                      pass
#                  read['readPoint'][msg.to] = True
#                  read['readMember'][msg.to] = {}
#                  read['ROM'][msg.to] = {}
                  
#                if msg.text.lower() == "เลิกนับ" or text.lower() == "#reader":
#                  group = linux.getGroup(msg.to)
#                  groupMemberMids = [i.mid for i in group.members if i.mid in admin]
#                  if msg.to in read['readPoint']:
#                      if read["ROM"][msg.to] == {}:
#                          ed = "\nNone"
#                          lread = "None"
#                      else:
#                          ed = ""
#                          for i in read["readMember"][msg.to]:
#                              ed += "\n- " + linux.getContact(i).displayName
#                          lr = read["ROM"][msg.to]
#                          lread = "- " + linux.getContact(lr).displayName
#
#                      b="รายชื่อสมาชิกที่อ่านทั้งหมด\n\nสมาชิกที่อ่าน" + ed + "\n\nสมาชิกที่อ่านล่าสุด\n"+lread+"\n\nพิมพ์ เริ่มนับ เพื่อตั้งคนนับอ่านใหม่ (｀・ω・´)"
#
#                      if linuxMID in groupMemberMids:
#                          anuchai(to, b)
#                      else:
#                         anuchai(to,b)
#                  else:
#                      b="คุณยังไม่ได้ตั้งนับอ่าน พิมพ์ เริ่มนับ เพื่อตั้งจุดอ่าน (｀・ω・´)"
#                      if linuxMID in groupMemberMids:
#                          anuchai(to, b)
#                      else:
#                         anuchai(to,b)
                if msg.text.lower().startswith("ใคร "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    linux.sendContact(msg.to,str(getx))
            #    if msg.text.lower().startswith("/exec "):
            #        delcmd = msg.text.split(" ")
            #        getx = msg.text.replace(delcmd[0] + " ","")
            #        data = data="{}".format(getx)
            #        sendTemplate(to, data)                         
#----------------------------------------------------------------------------#                    
                if text.lower() == "h1":
                    contact = linux.getContact(sender)
                    cover = linux.getProfileCoverURL(linux.profile.mid)
                    pp = linux.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = linux.getProfile().displayName
                    status = linux.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={'type':'flex','altText':"🌸help Vip🌸",'contents':{"type":"bubble","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"『Ẫµŧø ฿øŧĹįח€』","weight":"bold","color":"#CC0000","align":"center"}]},"body":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"เที่ยว「 บินJs 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=เที่ยว"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"/ลาก่อน「 ยกเชิญ&บิน 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=/ลาก่อน"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"/หาย「 บินธรรมดา 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=/หาย"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"@@「 บินJs 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=@@"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ลงดำ「 ยัดดำทั้งกลุ่ม 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=ลงดำ"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ประกาศเตะดำ「 ไม่บัค 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=ประกาศ:kKb"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ติดต่อข้อมูลอื่นๆ","uri":"http://line.me/ti/p/~anan789anan"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"ต้องการคำสั่งอะไรสามารกดที่ปุ่มได้เลย","color":"#CC0000","align":"center"}]},"styles":{"header":{"backgroundColor":"#000000","separator":True,"separatorColor":"#000000"},"hero":{"separator":True,"separatorColor":"#000000"},"footer":{"backgroundColor":"#000000","separator":True,"separatorColor":s},"body":{"separator":True,"separatorColor":s,"backgroundColor":a}}}}
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#                    
                if text.lower() == "h2":
                    contact = linux.getContact(sender)
                    cover = linux.getProfileCoverURL(linux.profile.mid)
                    pp = linux.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = linux.getProfile().displayName
                    status = linux.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={'type':'flex','altText':"🌸ระบบปุ่ม🌸",'contents':{"type":"bubble","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"•คำสั่งพิเศษ ระบบคลิก•","weight":"bold","color":"#CC0000","align":"center"}]},"body":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"kickjs「 คำสั่งพิเศษ 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=kickjs"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ระบบเตะ「 คำสั่งเตะ 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=ระบบเตะ"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ระบบป้องกัน「 ป้องกันกลุ่ม 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=ระบบป้องกัน"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"คำสั่งแบน「 โหมด ขาว/ดำ 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=blacklist"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ตั้งค่า เปิด/ปิด「 ตั้งค่าส่วนตัว 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=ตั้งค่าเรา"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"spam「 คำสั่งสแปม 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=spam"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ประกาศ「 คำสั่งประกาศ 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=ประกาศ"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ลูกเล่น「 เกมหรรษา 」","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=ลูกเล่น"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"คำสั่งหมุด","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=หมุด"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"เชคสติ้กเกอร์","uri":"line://app/1602687308-GXq4Vvk9?type=text&text=sticker"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"ต้องการคำสั่งอะไรสามารกดที่ปุ่มได้เลย","color":"#CC0000","align":"center"}]},"styles":{"header":{"backgroundColor":"#000000","separator":True,"separatorColor":"#000000"},"hero":{"separator":True,"separatorColor":"#000000"},"footer":{"backgroundColor":"#000000","separator":True,"separatorColor":s},"body":{"separator":True,"separatorColor":s,"backgroundColor":a}}}}
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#
#==============================================================================#
#===========Protection============#
                elif 'in ' in msg.text:
                   if msg._from in admin:
                      spl = msg.text.replace('in ','')
                      if spl == 'on':
                          if msg.to in welcome:
                               msgs = "ข้อความต้อนรับเปิดใช้งานอยุ่"
                          else:
                               welcome.append(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "ข้อความต้อนรับเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                          linux.sendMessage(to, "「 เปิดใช้งานสำเร็จ 」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in welcome:
                                 welcome.remove(msg.to)
                                 ginfo = linux.getGroup(msg.to)
                                 msgs = "ข้อความต้อนรับเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                            else:
                                 msgs = "ข้อความต้อนรับปิดใช้งานอยุ่"
                            linux.sendMessage(to, "「 ปิดใช้งานเรียบร้อย 」\n" + msgs)                                                                                       
#===========Protection============#
                elif 'out ' in msg.text:
                   if msg._from in admin:
                      spl = msg.text.replace('out ','')
                      if spl == 'on':
                          if msg.to in welcomeout:
                               msgs = "ข้อความคนออกเปิดใช้งานอยุ่"
                          else:
                               welcomeout.append(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "ข้อความคนออกเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                          linux.sendMessage(to, "「 เปิดใช้งานสำเร็จ 」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in welcomeout:
                                 welcomeout.remove(msg.to)
                                 ginfo = linux.getGroup(msg.to)
                                 msgs = "ข้อความคนออกเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                            else:
                                 msgs = "ข้อความคนออกปิดใช้งานอยุ่"
                            linux.sendMessage(to, "「 ปิดใช้งานเรียบร้อย 」\n" + msgs)                    
#===========Protection============#
                elif 'in1 ' in msg.text:
                      spl = msg.text.replace('in1 ','')
                      if spl == 'on':
                          if msg.to in welcomeb:
                               msgs = "ข้อความต้อนรับเปิดใช้งานอยุ่"
                          else:
                               welcomeb.append(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "ข้อความต้อนรับเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                          linux.sendMessage(to, "「 เปิดใช้งานสำเร็จ 」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in welcomeb:
                                 welcomeb.remove(msg.to)
                                 ginfo = linux.getGroup(msg.to)
                                 msgs = "ข้อความต้อนรับเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                            else:
                                 msgs = "ข้อความต้อนรับปิดใช้งานอยุ่"
                            linux.sendMessage(to, "「 ปิดใช้งานเรียบร้อย 」\n" + msgs)                  
#===========Protection============#
                elif 'st2 ' in msg.text:
                      spl = msg.text.replace('st2 ','')
                      if spl == 'on':
                          if msg.to in welcomes:
                               msgs = "สติกเกอร์คนออกเปิดใช้งานอยุ่"
                          else:
                               welcomes.append(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "สติกเกอร์คนออกเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                          linux.sendMessage(to, "「 เปิดใช้งานสำเร็จ 」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in welcomes:
                                 welcomes.remove(msg.to)
                                 ginfo = linux.getGroup(msg.to)
                                 msgs = "สติกเกอร์คนออกเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                            else:
                                 msgs = "สติกเกอร์คนออกปิดใช้งานอยุ่"
                            linux.sendMessage(to, "「 ปิดใช้งานเรียบร้อย 」\n" + msgs)
 #===========Protection============#
                elif 'st1 ' in msg.text:
                   if msg._from in admin:
                      spl = msg.text.replace('st1 ','')
                      if spl == 'on':
                          if msg.to in welcomet:
                               msgs = "สติกเกอร์คนเข้าเปิดใช้งานอยุ่"
                          else:
                               welcomet.append(msg.to)
                               ginfo = linux.getGroup(msg.to)
                               msgs = "สติกเกอร์คนเข้าเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                          linux.sendMessage(to, "「 เปิดใช้งานสำเร็จ 」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in welcomet:
                                 welcomet.remove(msg.to)
                                 ginfo = linux.getGroup(msg.to)
                                 msgs = "สติกเกอร์คนเข้าเฉพาะกลุ่ม\nกลุ่ม : " +str(ginfo.name)
                            else:
                                 msgs = "สติกเกอร์คนเข้าปิดใช้งานอยุ่"
                            linux.sendMessage(to, "「 ปิดใช้งานเรียบร้อย 」\n" + msgs)
#----------------------------------------------------------------------------#
                elif msg.text.lower().startswith("ประกาศ3 "):
                            txt = removeCmd("ประกาศ3", text)
                            s = "#000000"
                            a = "#ffffff"
                            groups = linux.getGroupIdsJoined()
                            contact = linux.getContact(linuxMID)
                            pp = linux.getProfile().pictureStatus
                            profile = "https://profile.line-scdn.net/" + str(pp)
                            for group in groups:
                                sa = "{}".format(str(txt))
                                data = {"type": "flex","altText": str(sa),"contents": {"type": "bubble",'styles': {"body": {"backgroundColor":str(a)}},"hero": {"type":"image","url":"https://sv1.picz.in.th/images/2020/02/24/xsEsA8.jpg","size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": str(sa),"wrap": True,"color":str(s),"align": "center","gravity": "center","size": "md"},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#FF0066","action": {"type": "uri","label": "•สนใจติดต่อ•","uri": "line://ti/p/~"+str(linux.getProfile().userid)}}]}}}
                                sendTemplate(group, data)
                                time.sleep(5)
                            linux.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))
#----------------------------------------------------------------------------#                                            
                elif msg.text.lower().startswith("ประกาศแชท: "):
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    friends = linux.friends
                    for friend in friends:
                        linux.sendMessage(friend, "「 ข้อความอัตโนมัติ ประกาศแชท 」\n{}".format(str(txt)))
                    linux.sendMessage(to, "ส่งข้อความถึงเพื่อน {} คน".format(str(len(friends))))
                     
                elif msg.text.lower().startswith("ประกาศ2 "):
                            text_ = removeCmd("ประกาศ2", text)
                            groups = linux.getGroupIdsJoined()
                            path = sets["listpict"]
                            for group in groups:
                              #  linux.generateReplyMessage(msg.id)
                              #  linux.sendReplyImage(msg.id, group, path)
                                linux.sendMessage(group, "「 ประกาศ 」\n\n{}".format(str(text_)))
                               # linux.generateReplyMessage(msg.id)
                                linux.sendImage(group, str(path))
                            linux.sendMessage(to, "ส่งคำประกาศเสร็จแล้ว จำนวน {} กลุ่ม".format(str(len(groups))))
                elif msg.text.lower().startswith("ประกาศ: "):
                            txt = removeCmd("ประกาศ:", text)
                            groups = linux.getGroupIdsJoined()
                            for group in groups:
                                linux.sendMessage(group, "{}".format(str(txt)))
                                time.sleep(1)
                            linux.sendMessage(to, "ส่งข้อความ ประกาศ ทั้งหมด {} กลุ่ม".format(str(len(groups))))
                elif msg.text.lower().startswith("ประกาศ:"):
                            txt = removeCmd("ประกาศ:", text)
                            groups = linux.getGroupIdsJoined()
                            for group in groups:
                                linux.sendMessage(group, "{}".format(str(txt)))
                                time.sleep(1)
                            linux.sendMessage(to, "ประกาศเตะดำ ทั้งหมด {} กลุ่ม".format(str(len(groups))))                            
                elif msg.text.lower().startswith("//ประกาศ "):
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split("/")
                            kw = get[0]
                            ans = get[1]
                            groups = linux.getGroupIdsJoined()
                            for group in groups:
                                sa = "「 ประกาศ 」\n\n{}".format(str(kw))
                                data = {
                                    "type": "flex",
                                    "altText": "มาอ่านเอาสิ",
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                   "type": "text",
                                                   "text": sa,
                                                   "wrap": True,
                                                   "align": "center",
                                                   "gravity": "center",
                                                   "size": "md"
                                               },
                                               {  
                                                   "type":"text",
                                                   "text":" "
                                               },
                                               {
                                                   "type":"button",
                                                   "style":"primary",
                                                   "color":"#FF0066",
                                                   "action": {
                                                       "type": "uri",
                                                       "label": "• แอด •",
                                                       "uri": "line://ti/p/~{}".format(ans),
                                                   }
                                               }
                                           ]
                                        }
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(10)
                            linux.sendMessage(to, "ส่งคำประกาศจำนวน {} กลุ่ม".format(str(len(groups))))
                elif msg.text.lower().startswith("ประกาศ1 "):
                            txt = removeCmd("ประกาศ1", text)
                            groups = linux.getGroupIdsJoined()
                            url = 'https://nekos.life/api/v2/img/ngif'
                            text1 = requests.get(url).text
                            image = json.loads(text1)['url']
                            for group in groups:
                                sa = " ประกาศ \n\n{}".format(str(txt))
                                data = {
                                    "type":"flex",
"altText":"「 ขออนุญาติประกาศ 」",
"contents":{
"type":"bubble",
"body":{
"type":"box",
"layout":"vertical",
"backgroundColor":"#7efff5",
"contents":[
{
"type":"box",
"layout":"vertical",
"margin":"xl",
"contents":[
{
"type":"text",
"size":"md",
"color":"#111111",
"align":"center",
"gravity":"center",
"wrap":True,
"text": sa
},
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
"size":"full",
"aspectMode":"cover"
}
],
"width":"40px",
"height":"40px",
"cornerRadius":"100px",
"borderColor":"#a29bfe",
"borderWidth":"2px"
},
{
"type":"text",
"text":"            สนใจติดต่อ",
"align":"start",
"gravity":"center",
"color":"#111111",
"size":"sm",
"action": {
"uri": "line://ti/p/~"+str(linux.getProfile().userid),
"type": "uri",
},
"margin":"xl",
"weight":"bold"
}
],
"margin":"xxl"
}
]
}
],"borderWidth":"3px",
"borderColor":"#a29bfe",
"cornerRadius":"xl"
}
}
}
                                sendTemplate(group, data)
                                time.sleep(5)
                            linux.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))
#==============================================================================#
                elif text.lower() == "ส่งรูป":                        
                          if msg._from in admin:                                 
                                groups = linux.getGroupIdsJoined()
                                for ajang in groups:
                                    time.sleep(1)
                                    data = {
                                "type": "flex",
                                "altText": "BOTLINE LINUX",
                                "contents": {
                                    "type": "bubble",
                                    "size": "giga", 
                                    "hero": {
                                         "type":"image",
                                         "url": "https://sv1.picz.in.th/images/2020/02/13/xwI35P.jpg",
#                                         "url": "https://sv1.picz.in.th/images/2020/01/31/RmGMWk.jpg",
                                         "size":"full",
                                         "aspectRatio": "6:9", 
                                         "action": {
                                             "type": "uri",
                                             "uri": "line://ti/p/~"+str(linux.getProfile().userid),
#                                             "uri": "line://ti/p/~anan789anan"
                                           #"
                                         }
                                    },
                                }
                            }                                                         
                          sendTemplate(to, data)
#                          time.sleep(1)                        
#==============================================================================#                           
                elif msg.text.lower().startswith("ประกาศ "):
                    delcmd = msg.text.split(" ")
                    get = msg.text.replace(delcmd[0] + " ", "")
                    kw = get[0]
                    ans = get[1]
                    text = "{}".format(get)
                    groups = linux.getGroupIdsJoined()
                    for group in groups:
                        sa = "{}".format(str(text))
                        data = {
"type":"flex",
"altText":" มีคนกล่าวถึงคุณ ",
"contents":{
"type":"bubble",
"body":{
"type":"box",
"layout":"vertical",
"contents":[
{
"type": "text",
"text": " 🌸ขออนุญาติประกาศ🌸",
"color":str(uck["uck2"]),
"gravity": "center",
"align":"center",
"wrap": True,
"size": "sm"
},
{
"type": "text",
"text": sa,
"color": str(uck['uck3']),
"gravity": "center",
"align":"center",
"wrap": True,
"size": "md"
},
{
"type":"box",
"layout":"vertical",
"margin":"lg",
"contents":[
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
"size":"full",
"aspectMode":"cover"
}
],
"width":"40px",
"height":"40px",
"cornerRadius":"100px",
"borderColor":str(uck['uck1']),
"borderWidth":"2px"
},
{
"type":"text",
"text":"           🌸ติดต่อ🌸",
"color":str(uck["uck2"]),
"align":"start",
"gravity":"center",
"size":"sm",
"action": {
"uri": "line://ti/p/~"+str(linux.getProfile().userid),
#"uri": str(uu['uuu']),
"type": "uri"
},
"margin":"xl",
"weight":"bold"
}
]
}
],
"spacing": "xl",
"paddingAll": "20px",
"paddingTop": "10px",
"paddingBottom": "10px",
"paddingStart": "20px",
"paddingEnd": "20px",
"paddingAll": "3px",
"borderColor": str(uck['uck1']),
"cornerRadius": "20px",
"flex": 1,
"borderWidth": "1px"
}
],
"paddingAll": "3px",
"backgroundColor": "#000000",
"borderWidth":"2px",
"borderColor":str(uck['uck1']),
"cornerRadius":"xl"
}
}
}
                        sendTemplate(group, data)
                        time.sleep(5)
                    linux.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups)))) 
#----------------------------------------------------------------------------------------------------                            
                elif msg.text.lower().startswith("ส่งประกาศ"):
                    delcmd = msg.text.split(" ")
                    get = msg.text.replace(delcmd[0] + " ", "")
                    kw = get[0]
                    ans = get[1]
                    text = "{}".format(get)
                    groups = linux.getGroupIdsJoined()
                    for group in groups:
                        sa = "{}".format(str(text))
                        data = {
                                        "type": "flex",
                                        "altText": "มีคนกล่าวถึงคุณ",
                                        "contents":{   "type": "bubble",
  "size":"giga",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type":"box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": " ",
            "size": "sm",
            "weight": "bold",
             "align": "center",
            "wrap": True,
            "color": "#FFFF00"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor":"#000000"
    },
    "footer": {
      "backgroundColor": "#3300FF"
    },
    "header": {
      "backgroundColor": "#0000FF"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "🌸 ติดต่อข้อมูล 🌸",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "action": {
          "type": "uri",
#          "uri": "line://ti/p/~"+str(linux.getProfile().userid),
          "uri": str(uu['uuu'])
        },
        "align": "center"
      }
    ]
  },
  "hero": {
    "aspectMode": "cover",
    "aspectRatio": "1:1",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
    "size": "full",
    "align": "center",   "action": {
          "type": "uri",
          "uri": str(uu['uuu'])
       } }}}
                        sendTemplate(group, data)
                        time.sleep(5)
                    linux.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))                     
#----------------------------------------------------------------------------------------------------                                      

                elif msg.text.lower().startswith("/ประกาศ "):
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split("/")
                            kw = get[0]
                            ans = get[1]
                            contact = linux.getContact(sender)
                            groups = linux.getGroupIdsJoined()
                            for group in groups:
                                sa = "{}".format(str(kw))
                                data = {
                                    "type":"flex",
"altText":"「 ประกาศ 」",
"contents":{
"type":"bubble",
"body":{
"type":"box",
"layout":"vertical",
"backgroundColor":"#7efff5",
"contents":[
{
"type":"text",
"text":"「 ประกาศ 」",
"align":"center"
},
{
"type":"box",
"layout":"vertical",
"margin":"lg",
"contents":[
{
"type":"text",
"size":"sm",
"wrap":True,
"text": sa
},
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),
"size":"full",
"aspectMode":"cover"
}
],
"width":"40px",
"height":"40px",
"cornerRadius":"100px",
"borderColor":"#a29bfe",
"borderWidth":"2px"
},
{
"type":"text",
"text":" 『Ẫµŧø ฿øŧĹįח€』",
"align":"start",
"gravity":"center",
"size":"sm",
"action": {
"uri": "line://ti/p/~{}".format(ans),
"type": "uri",
},
"margin":"xl",
"weight":"bold"
}
],
"margin":"xxl"
}
]
}
],"borderWidth":"3px",
"borderColor":"#a29bfe",
"cornerRadius":"xl"
}
}
}
                                sendTemplate(group, data)
                                time.sleep(5)
                            linux.sendMessage(to, "ส่งคำประกาศจำนวน {} กลุ่ม".format(str(len(groups))))

#==============================================================================#
                if text.lower() == 'ส่งรูป1':
                    groups = linux.getGroupIdsJoined()
                    for group in groups:
                          data={
"type":"flex",
"altText":"มีคนกล่าวถึงคุณ",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": str(usa['usa']),
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"gravity": "top"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "vertical",
"contents": [
{
"text": str(usa['us']),
"size": "sm",
"align": "center",
"color": str(uck['uck3']),
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"spacing": "lg"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "filler"
},
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "filler"
},
{
"type": "text",
"text": " 🌸สนใจติดต่อ🌸 ",
"color": str(uck["uck2"]),
"flex": 0,
"offsetTop": "-2px",
"weight": "bold"
},
{
"type": "filler"
}
],
"spacing": "sm",
"action": {
"type": "uri",
"label": "action",
"uri": "line://ti/p/~"+str(linux.getProfile().userid),
#"uri": str(uu['uuu'])
}
},
{
"type": "filler"
}
],
"borderWidth": "1px",
"cornerRadius": "4px",
"spacing": "sm",
"borderColor": str(uck['uck1']),
"margin": "xxl",
"height": "40px"
}
],
"position": "absolute",
"offsetBottom": "0px",
"offsetStart": "0px",
"offsetEnd": "0px",
"paddingAll": "20px",
"paddingTop": "18px",
"cornerRadius": "20px",
"borderColor": "#ff0000"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": " ",
"size": "lg",
"color": "#FF0000",
"weight": "bold"
}
],
"position": "absolute",
"offsetTop": "18px",
"offsetStart": "18px"
}
],
"paddingAll": "0px",
"borderWidth":"2px",
"borderColor":str(uck['uck1']),
"cornerRadius":"xl"
}
}
]
}
}
#                          sendTemplate(groups​,data)
                          sendTemplate(group, data)
                          time.sleep(5)
                    linux.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups)))) 
#==============================================================================#
                if text.lower() == 'ประกาศเฟก':
                    groups = linux.getGroupIdsJoined()
                    for group in groups:
                          data = {
"type":"flex",
"altText":"มีของมาขายจ้า",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": str(usa['usa']),
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"gravity": "top"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "vertical",
"contents": [
{
"text": str(usa['us']),
"size": "sm",
"align": "center",
"color": str(uck['uck3']),
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"spacing": "lg"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "filler"
},
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "filler"
},
{
"type": "text",
"text": " 🌸สนใจติดต่อ🌸 ",
"color": str(uck["uck2"]),
"flex": 0,
"offsetTop": "-2px",
"weight": "bold"
},
{
"type": "filler"
}
],
"spacing": "sm",
"action": {
"type": "uri",
"label": "action",
"uri": str(uu['uuu'])
}
},
{
"type": "filler"
}
],
"borderWidth": "1px",
"cornerRadius": "4px",
"spacing": "sm",
"borderColor": str(uck['uck1']),
"margin": "xxl",
"height": "40px"
}
],
"position": "absolute",
"offsetBottom": "0px",
"offsetStart": "0px",
"offsetEnd": "0px",
"paddingAll": "20px",
"paddingTop": "18px",
"cornerRadius": "20px",
"borderColor": "#ff0000"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": " ",
"size": "lg",
"color": "#FF0000",
"weight": "bold"
}
],
"position": "absolute",
"offsetTop": "18px",
"offsetStart": "18px"
}
],
"paddingAll": "0px",
"borderWidth":"2px",
"borderColor":str(uck['uck1']),
"cornerRadius":"xl"
}
},
{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": str(usa['usa1']),
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"gravity": "top"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "vertical",
"contents": [
{
"text": str(usa['us1']),
"size": "sm",
"align": "center",
"color": str(uck['uck3']),
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"spacing": "lg"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "filler"
},
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "filler"
},
{
"type": "text",
"text": " 🌸สนใจติดต่อ🌸 ",
"color": str(uck["uck2"]),
"flex": 0,
"offsetTop": "-2px",
"weight": "bold"
},
{
"type": "filler"
}
],
"spacing": "sm",
"action": {
"type": "uri",
"label": "action",
"uri": str(uu['uuu'])
}
},
{
"type": "filler"
}
],
"borderWidth": "1px",
"cornerRadius": "4px",
"spacing": "sm",
"borderColor": str(uck['uck1']),
"margin": "xxl",
"height": "40px"
}
],
"position": "absolute",
"offsetBottom": "0px",
"offsetStart": "0px",
"offsetEnd": "0px",
"paddingAll": "20px",
"paddingTop": "18px",
"cornerRadius": "20px",
"borderColor": "#ff0000"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": " ",
"size": "lg",
"color": "#FF0000",
"weight": "bold"
}
],
"position": "absolute",
"offsetTop": "18px",
"offsetStart": "18px"
}
],
"paddingAll": "0px",
"borderWidth":"2px",
"borderColor":str(uck['uck1']),
"cornerRadius":"xl"
}
},
{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": str(usa['usa2']),
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"gravity": "top"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "vertical",
"contents": [
{
"text": str(usa['us2']),
"size": "sm",
"align": "center",
"color": str(uck['uck3']),
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"spacing": "lg"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "filler"
},
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "filler"
},
{
"type": "text",
"text": " 🌸สนใจติดต่อ🌸 ",
"color": str(uck["uck2"]),
"flex": 0,
"offsetTop": "-2px",
"weight": "bold"
},
{
"type": "filler"
}
],
"spacing": "sm",
"action": {
"type": "uri",
"label": "action",
"uri": str(uu['uuu'])
}
},
{
"type": "filler"
}
],
"borderWidth": "1px",
"cornerRadius": "4px",
"spacing": "sm",
"borderColor": str(uck['uck1']),
"margin": "xxl",
"height": "40px"
}
],
"position": "absolute",
"offsetBottom": "0px",
"offsetStart": "0px",
"offsetEnd": "0px",
"paddingAll": "20px",
"paddingTop": "18px",
"cornerRadius": "20px",
"borderColor": "#ff0000"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": " ",
"size": "lg",
"color": "#FF0000",
"weight": "bold"
}
],
"position": "absolute",
"offsetTop": "18px",
"offsetStart": "18px"
}
],
"paddingAll": "0px",
"borderWidth":"2px",
"borderColor":str(uck['uck1']),
"cornerRadius":"xl"
}
}
]
}
}         
                          sendTemplate(group, data)
                          time.sleep(5)
                    linux.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))           
#==============================================================================#

#==============================================================================#
                elif text.lower() == "ลบแชท":
                            try:
                                linux.removeAllMessages(op.param2)
                                linux.unsendMessage(msg_id)
                                linux.sendMessage(to, "🌸 ลบประวัตแชทเรียบร้อย 🌸")
                            except:
                                pass
                                print ("ลบแชท")
                elif text.lower() == "/แทค":
                        group = linux.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(linux.getProfile().mid)
                        linux.datamention(to,'แทคทุกคน',nama)
                elif text.lower() == ".แทค" or text.lower() == "tagall":
                    if msg._from in linuxMID:
                        group = linux.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, jml = [], [], [], [], [], [], [], [], [], len(nama)
                        if jml <= 20:
                          mentionMembers(msg.to, nama)
                        if jml > 20 and jml < 40:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, len(nama)):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                        if jml > 40 and jml < 60:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, len(nama)):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                        if jml > 60 and jml < 80:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, len(nama)):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                        if jml > 80 and jml < 100:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for m in range (80, len(nama)):
                              nm5 += [nama[m]]
                          mentionMembers(msg.to, nm5)
                        if jml > 100 and jml < 120:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, len(nama)):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                        if jml > 120 and jml < 140:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for v in range (120, len(nama)):
                              nm7 += [nama[v]]
                          mentionMembers(msg.to, nm7)
                        if jml > 140 and jml < 160:
                          for i in range (0, 19):
                               nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for r in range (140, len(nama)):
                              nm8 += [nama[r]]
                          mentionMembers(msg.to, nm8)
                        if jml > 160 and jml < 180:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for z in range (140, 159):
                              nm8 += [nama[z]]
                          mentionMembers(msg.to, nm8)
                          for f in range (160, len(nama)):
                              nm9 += [nama[f]]
                          mentionMembers(msg.to, nm9)
#==============================================================================#
                elif msg.text.lower().startswith("/เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=ee1289,70&chf=bg,s,ff99cc"
                    linux.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("ดึง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                       linux.findAndAddContactsByMid(ls)
                                       linux.inviteIntoGroup(to, [ls])
                                    except:
                                       linux.unsendMessage(msg_id)
                                       linux.sendMessage(to, "🌸 จำกัด ! 🌸")
#==============================================================================#
                elif msg.text.lower().startswith("เขียน "):
                    contact = linux.getContact(linuxMID)	
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = textnya
                    data = {
                        "type": "flex",
                        "altText": "เขียน",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {"backgroundColor":"#000000"},
                            },
                            "hero": {
                                "type":"image",
                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                "size": "full",
                                "aspectRatio": "1:1",
                                "aspectMode": "fit"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": urlnya,
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "xxl"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)                                       
                elif msg.text.lower().startswith("สะกดจิต"):
                  if msg.toType == 2:
                    data = text.replace("สะกดจิต ","")
                    yud = data.split(' ')
                    yud = yud[0].replace(' ','_')
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            linux.unsendMessage(msg_id)
                            linux.sendMessage(to, yud,contentMetadata={"MSG_SENDER_NAME": str(linux.getContact(ls).displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/%s" % linux.getContact(ls).pictureStatus})
                elif msg.text.lower().startswith("youtube"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyCxNem5XpY70Wi21g1VAWs36jLbPzjTJzc".format(str(search)))
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
                                                "backgroundColor": "#000000"
                                            },
                                            "body": {
                                               "backgroundColor": "#000000",
                                               "separator": True,
                                               "separatorColor": "#00FFFF"
                                            },
                                            "footer": {
                                                "backgroundColor": "#000000",
                                                "separator": True,
                                               "separatorColor": "#00FFFF"
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
                                                    "color": "#FFFFFF",
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
                                                "uri": "line://nv/profilePopup/mid=u97d99f2b0574c393b1d8af252398e05c"
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
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
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
                                                "color": "#00FFFF"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#00FFFF",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#00FFFF",
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
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#000000",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
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
#----------------------------------------------------------------------------------------------------                                    
                elif msg.text.lower().startswith("ยูทูป"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyCxNem5XpY70Wi21g1VAWs36jLbPzjTJzc".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
            }
          }
        ],
        "borderColor": "#00FFFF",
        "borderWidth": "1px"
      },
      {
        "type": "text",
        "text": "YouTube",
        "weight": "bold",
        "size": "xl",
        "wrap": True,
        "align": "center",
        "color": "#ffffff"
      },
      {
        "type": "separator",
        "color": "#00FFFF"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "%s" % music['snippet']['title'],
                "wrap": True,
                "color": "#Ffffff",
                "size": "xs",
                "flex": 5,
                "align": "center",
                "weight": "regular",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://app/1623679774-k9nBDB6b?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                }
              }
            ]
          },
          {
            "type": "separator",
            "color": "#00FFFF"
          },
          {
            "type": "text",
            "text": "0",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "มองหาพ่อมุงหรอ",
              "uri": "http://line.me/ti/p/~anan789anan"
            },
            "style": "secondary",
            "color": "#00FFFF"
          }
        ]
      }
    ],
    "spacing": "sm",
    "paddingAll": "13px",
    "backgroundColor": "#000000",
    "borderWidth": "2px",
    "borderColor": "#00FFFF",
    "cornerRadius": "10px"
  }
}
)
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
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
#----------------------------------------------------------------------------------------------------                                    
                elif msg.text.lower().startswith("image "):
                	sep = text.split(" ")
                	txt = text.replace(sep[0] + " ","")
                	url = requests.get("https://rest.farzain.com/api/gambarg.php?id={}&apikey=VBbUElsjMS84rXUO7wRlIwjFm".format(txt))
                	data = url.json()
                	linux.sendReplyImageWithURL(to, data["url"])
                elif msg.text.lower().startswith("เพลสโต "):
                                query = removeCmd("เพลสโต", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = linux.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ผู้สร้างกลุ่มนี้ลบชี"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(linux.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม👉 : {}".format(gTicket)
                    ret_ += "\n╚══『『มองหาพ่อมุงหรอ』』"
                    data = {
                        "type": "flex",
                        "altText": "กลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                            #        {
                            #            "type": "image",
                            #            "url": path, 
                            #            "size": "xl"
                            #        },
                                    {
                                        "type": "text",
                                        "text": ret_,
                                        "color": "#00F5FF",
                                        "wrap": True,
                                        "size": "md",
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                    linux.sendImageWithURL(to, path)                                       
                elif msg.text.lower().startswith("ขอรูป "):
                                query = removeCmd("ขอรูป", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.boteater.co/googleimg?search={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
#                elif msg.text.lower().startswith('/ยกเลิก '):
#                            linux.unsendMessage(msg.id)
#                            j = int(msg.text.split(' ')[1])
#                            a = [linux.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
#                            if len(msg.text.split(' ')) == 2:
#                                h = wait['Unsend'][msg.to]['B']
#                                n = len(wait['Unsend'][msg.to]['B'])
#                                for b in h[:j]:
#                                    try:
#                                        linux.unsendMessage(b)
#                                        wait['Unsend'][msg.to]['B'].remove(b)
#                                    except:pass
#                                t = len(wait['Unsend'][msg.to]['B'])
#                            if len(msg.text.split(' ')) >= 3:h = [linux.unsendMessage(linux.sendMessage(to,linux.adityasplittext(msg.text,'s')).id) for b in a]
                elif msg.text.lower().startswith("ยก"):
                   args = msg.text.lower().replace("ยก","")
                   mes = 0
                   try:
                       mes = int(args[1])
                   except:
                       mes = 100
                       M = linux.getRecentMessagesV2(to, 100)
                       MId = []
                       for ind,i in enumerate(M):
                           if ind == 0:
                               pass
                           else:
                               if i._from == linux.profile.mid:
                                   MId.append(i.id)
                                   if len(MId) == mes:
                                       break
                       def unsMes(id):
                           linux.unsendMessage(id)
                       for i in MId:
                           thread1 = threading.Thread(target=unsMes, args=(i,))
                           thread1.start()
                           thread1.join()
#                       linux.sendMessage(to, ' 「 กำลังยกเลิก 」\nยกเลิกทั้งหมด {} ข้อความ'.format(len(MId))) 
                       linux.unsendMessage(msg_id)        
                elif msg.text.lower().startswith("เพิ่มเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = linux.getContact(ls)
                                    linux.findAndAddContactsByMid(ls)
                                linux.generateReplyMessage(msg.id)
                                linux.sendReplyMessage(msg.id, to, "Success add " + str(contact.displayName) + " to Friendlist")
#                elif msg.text.lower().startswith("แปลไทย "):
#                	if msg._from in admin or msg._from in [linuxMID]:
#                	    sep = text.split(" ")
#                	    isi = text.replace(sep[0] + " ","")
#                	    translator = Translator()
#                	    hasil = translator.translate(isi, dest='th')
#                	    A = hasil.text
#                	    teambotmaxText(msg.to, A)
                elif msg.text.lower().startswith("แอด "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = linux.getContact(ls)
                                    linux.findAndAddContactsByMid(ls)
                                linux.generateReplyMessage(msg.id)
                                linux.sendReplyMessage(msg.id, to, "ทำการแอดเพื่อนเรียบร้อย " + str(contact.displayName) + " to Friendlist")                                
                elif msg.text.lower().startswith("ลบเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = linux.getContact(ls)
                                    n = len(linux.getAllContactIds())
                                    try:
                                        linux.deleteContact(ls)
                                    except:pass
                                    t = len(linux.getAllContactIds())
                                    linux.generateReplyMessage(msg.id)
                                    linux.sendReplyMessage(msg.id, to, "Type: Friendlist\n • Detail: Delete friend\n • Status: Succes..\n • Before: %s Friendlist\n • After: %s Friendlist"%(n,t))
                elif msg.text.lower().startswith("บล็อค "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = linux.getContact(ls)
                                    linux.blockContact(ls)
                                linux.generateReplyMessage(msg.id)
                                linux.sendReplyMessage(msg.id, to, "Success add " + str(contact.displayName) + " to Blocklist")
                elif msg.text.lower().startswith("ไอดีไลน์ "):
                            a = removeCmd("ไอดีไลน์", text)
                            b = linux.findContactsByUserid(a)
                            line = b.mid
                            linux.sendMessage(msg.to,"line://ti/p/~" + a)
                            linux.sendContact(to, line)                                                                                           
                            linux.sendMessage(to,str(hasil))
                elif msg.text.lower().startswith("stag "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = linux.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = linux.getContact(receiver)
                                RhyN_(to, contact.mid)
#                        
                elif "/ลบรัน2" == msg.text.lower():
                        ginvited = linux.getGroupIdsInvited()
                        if ginvited != [] and ginvited != None:
                           for gid in ginvited:
                                time.sleep(0.65)
                                linux.rejectGroupInvitation(gid)
                                ronum = (ronum + 1)
                                print("RejectGroupInvitation",ronum)
                        linux.sendMessage(to, "AutorejectGroupInvitation {} Group".format(str(len(ginvited))))
                                                        
                elif "/ลบรัน" in msg.text.lower():
                    spl = re.split("/ลบรัน",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = linux.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        data = {"type": "text","text": "{}".format(str(txt)),"sentBy": {"label": "{}".format(linux.getContact(linuxMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ufdd706a81ff7557b83592e3b134c6e61"}}
                        sendTemplate(to, data)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                linux.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    linux.sendMessage(gr,spl[1])
                                time.sleep(0.65)  
                                linux.leaveGroup(gr)
                            except:
                                pass
                        sis = "สำเร็จแล้ว (｀・ω・´)"
                        data = {"type": "text","text": "{}".format(str(sis)),"sentBy": {"label": "{}".format(linux.getContact(linuxMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ufdd706a81ff7557b83592e3b134c6e61"}}
                        sendTemplate(to, data)
                elif text.lower() == 'ลบรัน':
                                gid = linux.getGroupIdsInvited()  
                                k = len(gid)//10     
                                num = 1                     
                                for i in range(k+1):
                                   for j in gid[i*20 : (i+1)*20]: 
                                       time.sleep(0.65)                                  	
                                       linux.acceptGroupInvitation(j)
                                       linux.leaveGroup(j)
                                       print(j)
                                linux.unsendMessage(msg_id)
                                linux.sendMessage(to, "🌸 ลบรันเรียบร้อย 🌸")
#=====================================================================
#                              \\ COMMAND SPAM //
#=====================================================================
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               linux.sendMessage(msg.to, teks)
                        else:
                           linux.sendMessage(to,"Out of Range!")
                elif cmd.startswith('Spam 1 '):
                    try:
                        msg.text = linux.mycmd(msg.text,wait)
                        j = int(msg.text.split(' ')[2])
                        a = [linux.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                        h = [linux.sendMessage(to,b) for b in a];linux.sendMessage(to, '「 สแปม 」\nสแปมข้อความจำนวน {} ข้อความ'.format(j))
                    except:pass
                elif cmd.startswith('Spam 2 '):
                    if msg.toType == 0:
                        msg.text = linux.mycmd(msg.text,wait)
                        j = int(msg.text.split(' ')[2])
                        a = [linux.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                        b = [linux.giftmessage(to) for b in a];linux.sendMessage(to, '「 สแปม 」\nทำการแจกของขวัญ {} ชิ้น♪'.format(j))
                    else:
                        j = int(msg.text.split(' ')[2])
                        a = [linux.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                        if 'MENTION' in msg.contentMetadata.keys()!=None:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            nama = [key1]
                            b = [linux.giftmessage(key1) for b in a];linux.sendMention(to, '「 สแปม 」\n@!ทำการแจกของขวัญ {} ของขวัญ♪'.format(j),'',[key1])
#
                elif text.lower() == '/เชคยก':
                    mtext = "🔻ข้อความยกเลิก🔻"
                    for m in [i for i in linux.talk.getRecentMessagesV2(msg.to, 10) if "UNSENT" in i.contentMetadata]:
                        mtext += "\n\nมุงยกเลิกทมาย\n "+str(linux.getContact(m._from).displayName)+"\nข้อความยกเลิก\n "+str(m.text)
                        linux.sendMessage(msg.to, str(mtext))
                        
                elif "เชคยก" in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(text)
                    teks = msg.text.replace("เชคยก"+str(text)+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt == "unsend":
                        if jmlh <= 5000:
                           mtext = "🔻ข้อความที่ยกเลิก🔻\n"
                           for m in [i for i in linux.talk.getRecentMessagesV2(msg.to, jmlh) if "UNSENT" in i.contentMetadata]:
                               mtext += "\n\n🔻ข้อความของคนนี้🔻\n "+str(linux.getContact(m._from).displayName)+"\n🔻ข้อความยกเลิก🔻\n"+str(m.text)
                           linux.sendMessage(msg.to, str(mtext))                        

                elif cmd.startswith('spam 1 '):
                    try:
                        msg.text = linux.mycmd(msg.text,wait)
                        j = int(msg.text.split(' ')[2])
                        a = [linux.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                        h = [linux.sendMessage(to,b) for b in a];linux.sendMessage(to, '「 สแปม 」\nสแปมข้อความจำนวน {} ข้อความ'.format(j))
                    except:pass
                elif cmd.startswith('spam 3 '):
                    if msg.toType == 0:
                        msg.text = linux.mycmd(msg.text,wait)
                        j = int(msg.text.split(' ')[2])
                        a = [linux.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                        b = [linux.giftmessage(to) for b in a];linux.sendMessage(to, '「 สแปม 」\nทำการแจกของขวัญ {} ชิ้น♪'.format(j))
                    else:
                        j = int(msg.text.split(' ')[2])
                        a = [linux.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                        if 'MENTION' in msg.contentMetadata.keys()!=None:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            nama = [key1]
                            b = [linux.giftmessage(key1) for b in a];linux.sendMention(to, '「 สแปม 」\n@!ทำการแจกของขวัญ {} ของขวัญ♪'.format(j),'',[key1])                            
                elif msg.text.lower().startswith("ของขวัญ "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = linux.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:                  
#                                linux.sendMessage(to, "🎁•รับทางแชทสต.นะ•🎁".format(str(jml)))
                                linux.sendMessage(receiver, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
#                                linux.sendMessage(to, "ไปดู ส.ต ด้วย".format(str(jml)))
                            else:
                                pass
                elif msg.text in ["เชคบล็อค"]: 
                    blockedlist = linux.getBlockedContactIds()
                    kontak = linux.getContacts(blockedlist)
                    num=1
                    msgs="═══ไม่มีรายการบัญชีที่ถูกบล็อค═══"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═══รายการบัญชีที่ถูกบล็อค════\n\nTotal Blocked : %i" % len(kontak)
                    linux.sendMessage(receiver, msgs)                                                         
                elif cmd == "เชครัน":
                    groups = linux.getGroupIdsInvited()
                    ret_ = "「 รายการกลุ่มที่รอการอนุมัติ 」\n"
                    no = 1
                    for gid in groups:
                        group = linux.getGroup(gid)
                        ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                        no = (no+1)
                    ret_ += "\n\nทั้งหมด {} รอดำเนินการ".format(str(len(groups)))
                    ret_ += "\n\nการใช้ : ปฏิเสธ [จำนวน]"
                    linux.generateReplyMessage(msg.id)
                    linux.sendMessage(msg.id, to, str(ret_))
#                    linux.sendReplyMessage(msg.id, to, str(ret_))
                elif cmd == "เปิดลิ้ง":
                    if msg.toType == 2:
                        group = linux.getGroup(to)
                        group.preventedJoinByTicket = False
                        linux.updateGroup(group)
                        gurl = linux.reissueGroupTicket(to)
                        linux.unsendMessage(msg_id)
                        linux.sendMessage(to, "🌸 เปิดลิ้งเรียบร้อย 🌸")
                elif cmd == "ปิดลิ้ง":
                    if msg.toType == 2:
                        group = linux.getGroup(to)
                        group.preventedJoinByTicket = True
                        linux.updateGroup(group)
                        linux.unsendMessage(msg_id)
                        linux.sendMessage(to, "🌸 ปิดลิ้งเรียบร้อย 🌸")
                elif cmd == "ลิ้ง":
                    if msg._from in admin:
                        if msg.toType == 2:
                           x = linux.getGroup(msg.to)
                           if x.preventedJoinByTicket == True:
                              x.preventedJoinByTicket = False
                              linux.updateGroup(x)
                           gurl = linux.reissueGroupTicket(msg.to)
                           linux.sendMessage(msg.to, "Gruop "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
#--------------------------------------------------------------------------------------------------------------
                elif msg.text in ["/ไวรัส"]:
                    linux.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    linux.sendMessage(msg.to, "ไ.ว.รั.ส.ด.อ.จั.ง.คุริๆอะจึ๋งๆ~4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังค่ะ")
                    linux.sendMessage(msg.to, "💗.ไ.ว.รั.ส.ด.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    linux.sendMessage(msg.to, "ไ.ว.รั.ส.ด.อ.จั.ง.น่.า.รั๊.ก.ไ.ล.น์.เ.ขี.ย.ว.~.☆. 🤗.🕸.💙.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.1.๑.i0s.")
                    linux.sendMessage(msg.to, "ไ.ว.รั.ส.ด.อ.จั.ง.คุริๆอะจึ๋งๆ~4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังค่ะ")
                    linux.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟรุ้งมุ้งมิ้ง~☆😍💜💛💚💙💗💖.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.ฟรุ้งฟริ้ง by.เอจัง~☆🤗")
                    linux.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    linux.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    linux.sendMessage(msg.to, "💗.ไ.ว.รั.ส.ด.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    linux.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.ด.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    linux.sendMessage(msg.to, "🌸•••••••••❂🌸✯🌸❂••••••••••🌸\n   💖💖 HELLO KITTY 💖💖\n🌸•••••••••❂🌸✯🌸❂••••••••••🌸")                     
#-------------------------------------------------------------------------------------------------------------
                elif msg.text.lower().startswith("คำห้ามพิม "):
                    wban = msg.text.lower().split()[1:]
                    wban = " ".join(wban)
                    wbanlist.append(wban)
                    linux.sendMessage(to,"%s พิมคำนี้อาจมีปลิวนะ."%wban)
                elif msg.text.lower().startswith("ลบคำห้ามพิม "):
                    wunban = msg.text.lower().split()[1:]
                    wunban = " ".join(wunban)
                    if wunban in wbanlist:
                        wbanlist.remove(wunban)
                        linux.sendMessage(to,"%s ล้างออกจากคำสั่งห้ามพิมแล้ว."%wunban)
                    else:
                        linux.sendMessage(to,"%s is not blacklisted."%wunban)
                elif msg.text.lower() == 'เช็คคำห้ามพิม':
                    tst = "คำห้ามพิม:\n"
                    if len(wbanlist) > 0:
                        for word in wbanlist:
                            tst += "- %s \n"%word
                        linux.sendMessage(msg.to,tst)
                    else:
                        linux.sendMessage(msg.to,"คำที่ห้ามพิมทั้งหมด") 

                elif text.lower() == 'คนสร้างกลุ่ม' or text.lower() == "แอด":
                    group = linux.getGroup(to)
                  #  maxg = "u51f2d901e6ae79ea2649062da18176df"
                  #  contact = linux.getContact(maxg)
                    GS = group.creator
                  #  n = contact.displayName
                    name = GS.displayName
                    pp = GS.pictureStatus
                    data = {
                        "type": "flex",
                        "altText": "linux Bots",
                        "contents": {
                            "type": "bubble",
                           # "hero": {
                               # "type":"text",
                              #  "text": "By : {}".format(contact.displayName),
                             #   "size":"md",
                            #    "align": "center",       
                           #     "weight":"bold",
                          #      "color":"#000000"
                          #  },
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
                    linux.sendContact(to, GS.mid)
                #    data = {
                #        "type": "flex",
                #        "altText": "linux Bots",
                #        "contents": {
                #            "type": "bubble",
                #            "hero": {
                #                "type":"image",
                #                "url": "https://profile.line-scdn.net/" + str(pp),
                #                "size":"sm",
                #                "action": {
                #                    "type": "uri",
                #                    "uri": "line://ti/p/~xj6gbn222"
                #                }
                #            },
                #        }
                #    }
                #    sendTemplate(to, data)
                elif msg.text.lower().startswith("ตั้งรูป ") and sender == linuxMID:
                            load()
                            name = removeCmd("ตั้งรูป", text)
                            name = name.lower()
                            if name not in images:
                                settings["addImage"]["status"] = True
                                settings["addImage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                linux.sendMessage(to, "Type: Picture\n • Detail: Add picture\n • Statud: Send pict...")
                            else:
                                linux.sendMessage(to, "Type: Picture\n • Detail: Add picture\n • Status: Failed, Picture already in list...")
                elif msg.text.lower().startswith("ลบรูป ") and sender == linuxMID:
                            load()
                            name = removeCmd("ลบรูป", text)
                            name = name.lower()
                            if name in images:
                                linux.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                linux.sendMessage(to, "Type: Picture\n • Detail: Delete list picture\n • Status: Succes delete Picture {}".format(str(name.lower())))
                            else:
                                linux.sendMessage(to, "Type: Picture\n • Detail: Delete list picture\n • Status: Failed, Picture not in list...")
                if text.lower() == "ตั้งรูป":
                    sets["pict"] = True
                    linux.sendMessage(to,"Send Pict...")
                if text.lower() == "เชครูป":
                    path = sets["listpict"]
                 #   linux.generateReplyMessage(msg.id)
                    linux.sendImage(to, path)                                
#=====================================================================
            elif msg.contentType == 1:
                if wait["changePictureProfile"] == True:
                    path = linux.downloadObjectMsg(msg_id)
                    wait["changePictureProfile"] = False
                    linux.updateProfilePicture(path)
                    linux.sendMessage(to, "🌸อัพเดทโปรไฟล์เรียบร้อย🌸")
            elif msg.contentType == 1:
                if wait["changeProfileCover"] == True:
                    path = linux.downloadObjectMsg(msg_id)
                    wait["changeProfileCover"] = False
                    linux.updateProfileCover(path)
                    linux.sendMessage(to, "🌸อัพเดทรูปปกเรียบร้อย🌸")                     

#=====================================================================
                elif text.lower()== "ตั้งติ๊กคนแทค":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "tag"
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                elif msg.text.lower() == "ลบติ๊กคนแทค":
                    sets["messageSticker"]["listSticker"]["tag"] = None
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ลบสติกเกอรคนแทคแล้ว 🌸")
                elif msg.text.lower()== "ตั้งติ๊กคนเข้า":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "wc"
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                elif msg.text.lower() == "ลบติ๊กคนเข้า":
                    sets["messageSticker"]["listSticker"]["wc"] = None
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                    linux.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว")
                elif msg.text.lower()== "ตั้งติ๊กคนออก":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "lv"
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                elif msg.text.lower() == "ลบติ๊กคนออก":
                    sets["messageSticker"]["listSticker"]["lv"] = None
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ลบสติกเกอรคนออกแล้ว 🌸")
                elif msg.text.lower()== "ตั้งติ๊กคนแอด":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "add"
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                elif msg.text.lower() == "ลบติ๊กคนแอด":
                    sets["messageSticker"]["listSticker"]["add"] = None
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ลบสติกเกอรคนแอดแล้ว 🌸")
                elif msg.text.lower() == "ตั้งติ๊กมุดลิ้ง":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "join2"
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ส่งสติกเกอรที่จะใช่ลงมา 🌸")
                elif msg.text.lower() == "ลบติ๊กมุดลิ้ง":
                    sets["messageSticker"]["listSticker"]["join2"] = None
                    linux.unsendMessage(msg_id)
                    linux.sendMessage(to, "🌸 ลบสติกเกอรแล้ว 🌸")
#=====================================================================
            elif msg.contentType == 1:
                if sets["pict"] == True:
                    path = linux.downloadObjectMsg(msg_id)
                    sets["pict"] = False
                    sets["listpict"] = str(path)
                #    f = codecs.open("image.json","w","utf-8")
                #    json.dump(path, f, sort_keys=True, indent=4, ensure_ascii=False)
#                    linux.sendMessage(to, "Done.....")
           #     if msg.toType == 2:
            #        if to in sets["pictGroup"]:
             #           path = linux.downloadObjectMsg(msg_id)
              #          sets["pictGroup"].remove(to)
                      #  line.updateGroupPicture(to, path)
              #          linux.sendMessage(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว")
            #    elif msg.contentType == 1:
            #        if settings["addImage"]["status"] == True and sender == linuxMID:
            #            path = linux.downloadObjectMsg(msg_id)
            #            images[settings["addImage"]["name"]] = str(path)
            #            f = codecs.open("image.json","w","utf-8")
            #            json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
            #            linux.sendMessage(to, "picture {} in list".format(str(settings["addImage"]["name"])))
            #            settings["addImage"]["status"] = False
            #            settings["addImage"]["name"] = ""
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != linux.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            #    elif msg.contentType == 1:
            #        if sets["pict"] == True:
             #           path = linux.downloadObjectMsg(msg.id)
                      #  sets["image"]["name"] = str(path)
               #         sets["pict"] = False
               #         linux.sendMessage(to, "Done..")
                    #    sets["pict"] == False
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            linux.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            linux.sendMessage(to, str(ret_))
                        except Exception as error:
                            linux.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in linuxMID:
                            try:
                                linux.kickoutFromGroup(msg.to,[sender])
                                linux.sendMessage("บอกแล้อย่าพิมไม่เชื่อจุกไปสิ55555")
                            except Exception as e:
                                print(e)
                    for image in images:
                        if msg.text.lower() == image:
                            linux.generateReplyMessage(msg.id)
                            linux.sendReplyImage(msg.id, to, images[image])
                    if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = linux.findGroupByTicket(ticket_id)
                                linux.acceptGroupInvitationByTicket(group.id,ticket_id)
                                linux.sendMessage(to, "🌸มุดเข้ากลุ่ม🌸\n👉 %s 👈อัตโนมัติ\n🌸ผ่านการแชร์ด้วยลิงค์🌸" % str(group.name))
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            linux.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        linux.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
            elif msg.contentType == 7:
                if sets["Sticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    linux.sendMessage(to, str(ret_))               
#========================================================================
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != linux.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#                    
                elif msg.text in ["แจกฟรี"]:
                            pesannya = {
                                "type": "template",
                                "altText": "🌸แจกฟรี🌸",
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://sv1.picz.in.th/images/2020/03/01/xX225y.jpg",
                                    "action": {
                                        "type": "uri",
                                        "uri": "http://line.me/ti/p/~anan789anan",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            sendTemplate(to,pesannya)                                   
            elif msg.contentType == 7: # Content type is sticker
                if sets['sti2']:
                    linux.unsendMessage(msg.id)
                    if 'STKOPT' in msg.contentMetadata:
                        contact = linux.getContact(linuxMID)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        linux.unsendMessage(msg.id)
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = linux.getContact(linuxMID)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        linux.unsendMessage(msg.id)
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != linux.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "/บอท":
                    linux.sendMessage(to," 🌸กูยังอยู่ดีไม่ต้องเรียกบ่อย🌸")
                    return
                if text.lower() == "///เชคเฟก":
                    linux.sendMessage(to, "『『มองหาพ่อมุงหรอ』』 ")
                    return
                if text.lower() == ".":
                    linux.sendMessage(to, "มองหาพ่อมุงหรอ『』")                    
                    return
#                if text.lower() == "/แทค":
#                	group = linux.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(linux.getProfile().mid)
#                	linux.datamention(to,'แทคทุกคน',nama)
#                if text.lower() == "/คำสั่ง":
#                    linux.sendMessage(msg.to, "🇹🇭❂➣/แทค =『แทคสมาชิกทั้งหมด』\n\n🇹🇭❂➣เปิด:แอบ =『เปิดดูคนอ่าน』\n\n🇹🇭❂➣ปิด:แอบ =『ปิดดูคนอ่าน』\n\n🇹🇭❂➣/บอท =『เชคบอท』")

#========================================================================
            elif msg.contentType == 7: # Content type is sticker
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = linux.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = linux.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
             #   elif msg.contentType == 7:
                if msg.toType == 0 and sender != linuxMID: to = sender
                else: to = receiver
            #    elif msg.contentType == 7:
            #        if "/ti/g/" in msg.text.lower():
            #            if sets["autoJoinTicket"] == True:
            #                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
            #                links = link_re.findall(text)
            #                n_links = []
            #                for l in links:
            #                    if l not in n_links:
            #                        n_links.append(l)
            #                for ticket_id in n_links:
            #                    group = linux.findGroupByTicket(ticket_id)
            #                    linux.acceptGroupInvitationByTicket(group.id,ticket_id)
                                #
             #                   linux.sendMessage(to, "เข้าไปสิงในห้องชื่อ %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 0 and sender not in linuxMID and msg.toType == 2:
#                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:     
                         if tagadd["tags"] == True:
                             me = linux.getContact(sender)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in linuxMID:
                                          cover = linux.getProfileCoverURL(sender)
                                          pp = me.pictureStatus
                                          profile = "https://profile.line-scdn.net/" + str(pp)
                                          name = me.displayName
                                          status = "\nสเตตัส\n" + me.statusMessage
                                          pk = str(tagadd["tag"])
                                          tz = pytz.timezone("Asia/Jakarta")
                                          timeNow = datetime.now(tz=tz)
                                          van2 = "🆃🅸🅼🅴:"+ datetime.strftime(timeNow,'%H:%M:%S')                                 	
                                          data={
"type":"flex",
"altText":"🌸Autotags🌸",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"text": van2,
"size": "xs",
"margin": "none",
"color": str(uck['uck2']),
"wrap": True,
"weight": "regular",
"type": "text"
}
]
},
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": profile,
"size": "full",
"position": "relative",
"margin": "none",
"align": "end",
"gravity": "top",
"aspectMode": "cover"
}
],
"cornerRadius": "100px",
"width": "72px",
"height": "72px",
"margin": "xxl",
"spacing": "xxl",
"position": "relative",
"borderColor": str(uck['uck1']),
"borderWidth": "1px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "text",
"text": "Ẫµŧø ฿øŧĹįח€",
"size": "sm",
"color": "#FFFFFF"
}
],
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🅰🆄🆃🅾 🅱🅾🆃🅻🅸🅽🅴",
"size": "sm",
"color": str(uck['uck2']),
},
{
"type": "text",
"text": name,
"size": "sm",
"color": str(uck['uck2']),
},
{
"text": pk,
"size": "sm",
"margin": "none",
"color": str(uck['uck2']),
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"spacing": "sm",
"margin": "md"
}
]
}
],
"spacing": "xl",
"paddingAll": "20px",
"paddingTop": "10px",
"paddingBottom": "10px",
"paddingStart": "20px",
"paddingEnd": "20px",
"borderColor": str(uck['uck1']),
"paddingAll": "3px",
"borderColor": str(uck['uck4']),
"cornerRadius": "20px",
"flex": 1,
"borderWidth": "1px"
}
],
"paddingAll": "3px",
"backgroundColor": "#000000",
"borderWidth":"2px",
"borderColor":str(uck['uck1']),
"cornerRadius":"xl"
}
}
]
}
}
                                          sendTemplate(to, data)
                if msg.contentType == 0 and sender not in linuxMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if tagadd["tagss"] == True:
                            contact = linux.getContact(sender)
                            cover = linux.getProfileCoverURL(sender)
                            names = contact.displayName
                            status = contact.statusMessage
                            pp = contact.pictureStatus
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if linuxMID in mention["M"]:
                                     data = {
                                         "type": "flex",
                                         "altText": "tagall",
                                         "contents": {
                                             "type": "bubble",
                                             'styles': {
                                                 "body": {
                                                     "backgroundColor": '#000033'
                                                 },
                                             },
                                             "hero": {
                                                 "type":"image",
                                                 "url": cover,
                                                 "size":"full",
                                                 "aspectRatio":"20:13",
                                                 "aspectMode":"cover"
                                             },
                                             "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
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
                                                         "text":"{}".format(names),
                                                         "size":"xl",
                                                         "weight":"bold",
                                                         "color":"#FFFF00",
                                                         "align":"center"
                                                     },
                                                     {
                                                         "type": "text",
                                                         "text": status,
                                                         "wrap": True,
                                                         "align": "center",
                                                         "gravity": "center",
                                                         "color": "#FFFF00",
                                                         "size": "md"
                                                     },
                                                 ]
                                             }
                                         }
                                     }
                                     sendTemplate(to, data)
                if msg.contentType == 0 and sender not in linuxMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if linuxMID in mention["M"]:
                                    #  contact = linux.getContact(linuxMID)
                                   #   a = contact.displayName
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = linux.getContact(linuxMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = linux.getContact(linuxMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
#==============================================================================#
        if op.type == 19:
            if linuxMID in op.param3:
                LnBots["blacklist"][op.param2] = True
                banned()
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
               if mc["wr"][str(msg.text)]:
                   linux.sendMessage(msg.to,mc["wr"][str(msg.text)])
            except:
              pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != linux.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if msg.text.lower().startswith("แปรงคท "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    linux.sendContact(msg.to,str(getx))
            #    if msg.text.lower().startswith("/exec "):
            #        delcmd = msg.text.split(" ")
            #        getx = msg.text.replace(delcmd[0] + " ","")
            #        data = data="{}".format(getx)
            #        sendTemplate(to, data)
                if msg.text.startswith("ตั้งapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        mc["wr"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                        linux.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: "+ str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("ล้างapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del mc["wr"][getx]
                        linux.sendMessage(msg.to, "คำ " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "เชคapi":
                    lisk = "[ คำตอบโต้ทั้งหมด ]\n"
                    for i in mc["wr"]:
                        lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(mc["wr"][i])+"\n"
                    lisk+="\nวิธีล้างapi >\\<\nล้างapi ตามด้วยคำที่จะล้าง"
                    data = {"type": "text","text": "{}".format(lisk),"sentBy": {"label": "Botline By 『Ẫµŧø ฿øŧĹįח€』", "iconUrl": "https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ue6245127d69b7edfc88835ec0d535cd6"}}
                    sendTemplate(to,data)
#==============================================================================#
#==============================================================================#
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != linux.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            linux.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
                        
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != linux.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if reads["autoRead"] == True:
                    linux.sendChatChecked(to, msg_id)				
                if sender in mimics["target"] and mimics["status"] == True and mimics["target"][sender] == True:
                    text = msg.text
                    if text is not None:   
                        for x in linux.getGroupIdsJoined():
                            try: linux.sendMessage(x, text)
                            except: pass
                        
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != linuxMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
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
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = linux.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = linux.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = linux.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = linux.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
        if op.type in [26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                  to = receiver
               elif msg.toType == 2:
                  to = receiver
               if msg.contentType == 0:
                  if text is None:
                     return
                  else:
                    if receiver in temp_flood:
                      if temp_flood[receiver]["expire"] == True:
                        if msg.text == "/open":
                           temp_flood[receiver]["expire"] = False
                           temp_flood[receiver]["time"] = time.time()
                           linux.sendMessage(to,"Bot Actived")
                        return
                      elif time.time() - temp_flood[receiver]["time"] <= 5:
                         temp_flood[receiver]["flood"] += 1
                         if temp_flood[receiver]["flood"] >= 400:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
#                            linux.unsendMessage(msg_id)
                            a = "💥คุณฝลัดข้อความมากเกินไป💥"
                            sendTemplate(to,{"type":"flex","altText":"{}".format(a),"contents":{"type":"bubble","styles":{"footer":{"backgroundColor":"#000000"}},"footer":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","url":"https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"size":"md"},{"type":"text","text":"{}".format(a),"color":"#0099FF","gravity":"center","align":"center","wrap":True,"size":"md"},{"type":"icon","url":"https://obs.line-scdn.net/{}".format(linux.getContact(linuxMID).pictureStatus),"size":"md"}]}]}}})
                            linux.kickoutFromGroup(msg.to,[sender])
                      else:
                       temp_flood[receiver]["flood"] = 0
                      temp_flood[receiver]["time"] = time.time()
                    else:
                      temp_flood[receiver] = {
                       "time": time.time(),
                       "flood": 0,
                       "expire": False
}                                                         
#=====================================================================

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = linux.getContact(op.param2).displayName
                        contact = linux.getContact(op.param2).picturePath
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=['จ๊ะเอ๋','รู้นะว่าแอบอยู่','เล่นซ่อนแอบกันเหรอ','คิดว่าเป็นนินจารึไง','ว่าไง','อ่านอย่างเดียวเลยนะ','ออกมาคุยหน่อย','ออกมาเดี๋ยวนี้']
                            warnanya1 = random.choice(pref)
#                            linux.sendMention(op.param1, "@!","",[op.param2])
                            data = {
                                         "type": "flex",
                                         "altText": "แอบ",
                                         "contents": {
                                             "type": "bubble",
                                             'styles': {
                                                 "body": {
                                                     "backgroundColor": '#000000'
                                                 },
                                             },
                                             "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
                                                     {
                                                         "type": "image",
                                                         "url": "https://obs.line-scdn.net/{}".format(linux.getContact(op.param2).pictureStatus),
                                                         "size": "full"
                                                     },
                                                     {
                                                          "type":"text",
                                                          "text":" "
                                                     },
                                                     {
                                                         "type":"text",
                                                         "text": "{}".format(linux.getContact(op.param2).displayName),
                                                         "size":"xl",
                                                         "weight":"bold",
                                                         "color":"#FFFFFF",
                                                         "align":"center"
                                                     },
                                                     {
                                                         "type": "text",
                                                         "text": str(random.choice(pref)) ,
                                                         "wrap": True,
                                                         "align": "center",
                                                         "gravity": "center",
                                                         "color": "#FFFFFF",
                                                         "size": "md"
                                                     },
                                                 ]
                                             }
                                         }
                                     }
                            sendTemplate(op.param1, data)                            
#                            linux.sendMessage(op.param1, str(random.choice(pref)) + Name)
#                            linux.sendContact(op.param1, op.param2)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = linux.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	linux.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass                            
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = linux.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                linux.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    linux.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        linux.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            linux.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                linux.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    linux.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        linux.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")                    
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            NOTIFIED_READ_MESSAGE(op)      
    except Exception as error:
        traceback.print_exc()
        
#==============================================================================#
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
#


def nameUpdate():
    while True:
        try:
            if bed["bed"] == True:
                time.sleep(3600)
                gid = linux.getGroupIdsJoined()
                for i in gid:
                    be = bed["bed1"]
                    be = bed["bed2"]
                    be = bed["bed3"]
                    linux.sendImageWithURL(i,"{}".format(str(str(bed["bed1"]))))
                    linux.sendImageWithURL(i,"{}".format(str(str(bed["bed2"]))))
                    linux.sendImageWithURL(i,"{}".format(str(str(bed["bed3"]))))
                    linux.sendMessage(i,"{}".format(str(str(bed["tetx"]))))
                    linux.sendMessage(i,"{}".format(str(str(bed["tetx2"]))))
                    linux.sendMessage(i,"{}".format(str(str(bed["tetx3"]))))
                linux.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(gid))))
                break
        except Exception as e:
            print (e)
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()   
#==============================================================================#

def run():
    while True:
        try:
            ops = linuxPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(linuxBot(op))
                   linuxPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()
