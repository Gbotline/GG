from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
#from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
#======================================================================================
botStart = time.time()
#==============================================================================#
try:
    with open('token.txt','r') as tokens:
        token = tokens.read()
    print(str(token))
except Exception as e:
    maxgie = LINE(token)
maxgie = LINE(token)
maxgie.log("Auth Token : " + str(maxgie.authToken))
maxgie.log("Timeline Token : " + str(maxgie.tl.channelAccessToken))

waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#==============================================================================#
maxgieMID = maxgie.profile.mid
maxgieProfile = maxgie.getProfile()
maxgieSettings = maxgie.getSettings()
#==============================================================================#
maxgiePoll = OEPoll(maxgie)
maxgieMID = maxgie.getProfile().mid
admin = [maxgieMID]
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']
mc = {"wr":{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
msg_dict = {}
temp_flood = {}

#==============================================================================#
did = {"join": True,}
kcn = {"autojoin": True,"Members":5,}
sets = {
    "l":True, 
      "c":True, 
      "cm":"Auto Like By.??????????????????????????????????????????????????????????\nline://ti/p/~boy-5566",  
    "winvite": False,
    "wblacklist": False,
    "tagsticker": False,
    "Sticker": False,
    "autoJoin": False,
    "autoCancel": True,
    "autoJoinTicket": False,
   "changePictureProfile": False, 
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
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "????????????????????????????????? \n- ????????????????????? ???????????????????????????????????????????????????",
    "add": "????????????????????????????????????????????????????????????????????? ????\n?????????????????????????????????. >_<",
    "wctext": "????????????????????????????????????????????????????????????????????????????????? ????",
    "lv": "????????????????????? >< ???????????????????????????????????????????????? >_<",
    "b": "?????????????????????????????????????????????????????????????????? Self Bot By. ?????????????????????????????????????????????????????????? ??????????????????????????????????????????????????????????????????????????????????????? >_<",
    "c":"Auto Like By. ??????????????????????????????????????????????????????????",
    "m": "?????????????????????????????? ??????????????????????????????????????????????????? >_<",
}
apalo = {
    "winvite": False,
    "wblacklist": False,
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#333333","t": "#6600CC"}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
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
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}    
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hoho = {
    "savefile": False,
    "namefile": "",
}

user1 = maxgieMID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = maxgie.getProfile() 
backup = maxgie.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = maxgieProfile.displayName
settings["myProfile"]["statusMessage"] = maxgieProfile.statusMessage
settings["myProfile"]["pictureStatus"] = maxgieProfile.pictureStatus
cont = maxgie.getContact(maxgieMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = maxgie.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = maxgieProfile.statusMessage
ProfileMe["pictureStatus"] = maxgieProfile.pictureStatus
coverId = maxgie.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("max.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Max2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        maxgie.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = maxgie.getContact(mid)
    if contact.videoProfile == None:
        maxgie.cloneContactProfile(mid)
    else:
        profile = maxgie.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = maxgie.getProfileDetail(mid)['result']['objectId']
    maxgie.updateProfileCoverById(coverId)
def backupProfile():
    profile = maxgie.getContact(maxgieMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = maxgie.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = maxgie.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        maxgie.updateProfileAttribute(8, profile.pictureStatus)
        maxgie.updateProfile(profile)
    else:
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    maxgie.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        maxgie.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = maxgie.getGroup(msg.to).name
    sd = maxgie.waktunjir()
    maxgie.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = maxgie.getContact(to)
        profile = maxgie.profile
        profileName = maxgie.profile
        profileStatus = maxgie.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        maxgie.updateProfile(profileName)
        maxgie.updateProfile(profileStatus)
        profile.pictureStatus = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if maxgie.getProfileCoverId(to) is not None:
            maxgie.updateProfileCoverById(maxgie.getProfileCoverId(to))
        maxgie.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return maxgie.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        maxgie.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
        
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
        nama = "{}".format(maxgie.getContact(maxgieMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus)
        ticket = "https://line.me/ti/p/~topzalove123"
        maxgie.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def ggggg(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    return '%02d ?????????\n?????????????????????????????????\n%02d ?????????????????????\n?????????????????????????????????\n%02d ????????????\n?????????????????????????????????\n' %(days ,hours, mins)
    
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@"
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
    maxgie.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(maxgie.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + maxgie.getContact("ube3faf73d9f1d8388b472b576328ec21").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = maxgie.genOBSParams({'oid': maxgieMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = maxgie.server.postContent('{}/talk/vp/upload.nhn'.format(str(maxgie.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        maxgie.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.liff.issueLiffView(view)
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
    token = maxgie.liff.issueLiffView(view)
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
    maxgie.log("[ ??????????????????????????? ] " + str(text))
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
        maxgie.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = maxgie.getGroup(to)
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
        maxgie.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d ???????????????" % (months)
    if weeks != 0: text += " %02d ?????????????????????" % (weeks)
    if days != 0: text += " %02d ?????????" % (days)
    if hours !=  0: text +=  " %02d ?????????????????????" % (hours)
    if mins != 0: text += " %02d ????????????" % (mins)
    if secs != 0: text += " %02d ??????????????????" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def restartBot():
    print ("RESETBOT..")
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
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': maxgie.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + maxgie.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            maxgie.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
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
def duc1(to, duc1):
    data={
"type": "flex",
"altText": duc1,
"contents": {
"type": "bubble",
"styles": {
"footer": {"backgroundColor": "#FF9933"},
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
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"size": "md"
},
{
"type": "text",
"text": duc1,
"color":"#8B0000",
"gravity": "center",
"align":"center",
"wrap": True,
"size": "md"
},
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"size": "md"
},
]
}
]
}
}
}
    sendTemplate(to, data)
#=====================================================================
#=====================================================================
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
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
async def maxgieBot(op):
    try:
        if settings["restartPoint"] != None:
            maxgie.sendMessage(settings["restartPoint"], '???????????????????????????????????????????????????????????? ><')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
             # if op.param2 in admin:
                 # return
              maxgie.findAndAddContactsByMid(op.param1)
              maxgie.sendMessage(op.param1,"{}".format(tagadd["add"]))
              msgSticker = sets["messageSticker"]["listSticker"]["add"]
              if msgSticker != None:
                  sid = msgSticker["STKID"]
                  spkg = msgSticker["STKPKGID"]
                  sver = msgSticker["STKVER"]
                  sendSticker(op.param1, sver, spkg, sid)
              print ("[ 5 ] AUTO ADD")
        if op.type == 5:
            if settings["autoblock"] == True:
              #if op.param2 in admin:
                 # return
              maxgie.sendMessage(op.param1,tagadd["b"])
          #    msgSticker = sets["messageSticker"]["listSticker"]["block"]
          #    if msgSticker != None:
          #        sid = msgSticker["STKID"]
          #        spkg = msgSticker["STKPKGID"]
          #        sver = msgSticker["STKVER"]
          #        sendSticker(op.param1, sver, spkg, sid)
                    #maxgie.sendMessage(op.param1,tagaad["b"])
              maxgie.blockContact(op.param1)
              print ("[ 5 ] AUTO BLOCK")
        if op.type == 13:
         if kcn["autojoin"] == True:
             G = maxgie.getCompactGroup(op.param1)
             if len(G.members) <= kcn["Members"]:
                 maxgie.acceptGroupInvitation(op.param1)
                 maxgie.leaveGroup(op.param1)               	
             else:
                 maxgie.acceptGroupInvitation(op.param1)
                 
        if op.type == 13:
            if maxgieMID in op.param3:
                if did["join"] == True:
                    friend = maxgie.getAllContactIds()
                    kontak = maxgie.getContacts(friend)
                    for ids in kontak:
                      The = ids.mid
                      if op.param2 not in The:
                          try:
                             maxgie.acceptGroupInvitation(op.param1)
                             ginfo = maxgie.getGroup(op.param1)
                          except:
                             maxgie.acceptGroupInvitation(op.param1)
                             ginfo = maxgie.getGroup(op.param1)
                             maxgie.sendMessage(op.param1,"BYE BYE~~")
                             maxgie.leaveGroup(op.param1)
        if op.type == 13:
            if maxgieMID in op.param3:
                G = maxgie.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            maxgie.acceptGroupInvitation(op.param1)
                        else:
                            maxgie.leaveGroup(op.param1)
                    else:
                        maxgie.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        maxgie.acceptGroupInvitation(op.param1)
                        maxgie.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in apalo["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    maxgie.acceptGroupInvitation(op.param1, matched_list)
                    maxgie.leaveGroup(op.param1, matched_list)
                    print ("[ 17 ] LEAVE GROUP")
        if op.type == 15:
          if settings["Leave"] == True:
            if op.param2 in admin:
                return
            ginfo = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            name = contact.displayName
            pp = contact.pictureStatus
            s = name + " " + tagadd["lv"]
            data = {
                "type": "flex",
                "altText": "????????????????????????????????????",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#FF9933'
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
                                "color": "#8B0000",
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
                "altText": "????????????????????????????????????",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~boy-5566"
                     #      
                     #   "
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 15:
          if settings["lv"] == True:
              ginfo = maxgie.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["lv"]
              if msg != None:
                  contact = maxgie.getContact(maxgieMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ???????????????????????????????????????','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Welcome"] == True:
            if op.param2 in admin:
                return
            g = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            gname = g.name
            name = contact.displayName
            pp = contact.pictureStatus
            s = "??? Group Welcome ???\n"
            s += "\n??? ??????????????????????????? : {}".format(gname)
            s += "\n??? ????????????????????????????????????????????? : {}\n\n".format(name)
            s += tagadd["wctext"]
            data = {
                "type": "flex",
                "altText": "???????????????????????????????????????",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#FF9933'
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
                                "color": "#8B0000",
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
                "altText": "???????????????????????????????????????",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~boy-5566"
                           #"
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            cover = maxgie.getProfileCoverURL(op.param2)
            names = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            data = {
                "type": "flex",
                "altText": "???????????????????????????????????????",
                "contents": {
                    "type": "bubble",
                    'styles': {
                        "body": {
                            "backgroundColor": '#FF9933'
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
                                 "color":"#8B0000",
                                 "align":"center"
                             },
                             {
                                 "type": "text",
                                 "text": status,
                                 "wrap": True,
                                 "align": "center",
                                 "gravity": "center",
                                 "color": "#8B0000",
                                 "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["wcsti2"] == True:
              ginfo = maxgie.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["wc"]
              if msg != None:
                  contact = maxgie.getContact(maxgieMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ???????????????????????????????????????','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
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
               # if msg.toType == 0 and sender != maxgieMID: to = sender
               # else: to = receiver
               # if msg.toType == 0 and settings["replays"] and sender != maxgieMID:
                   # contact = maxgie.getContact(sender)
                    #if contact.attributes != 32 and "[ auto reply ]" not in text.lower():
                     #   msgSticker = sets["messageSticker"]["listSticker"]["replay"]
                     #   if msgSticker != None:
                     #       sid = msgSticker["STKID"]
                     #       spkg = msgSticker["STKPKGID"]
                     #       sver = msgSticker["STKVER"]
                     #       sendSticker(to, sver, spkg, sid)
                     #   if "@!" in settings["reply"]:
                     #       msg_ = settings["reply"].split("@!")
                     #       sendMention(to, sender, "??? ?????????????????????????????? ???\n" + msg_[0], msg_[1])
                     #   maxgie.sendMessage(to, "??? ?????????????????????????????? ???\n", settings["reply"])
                     
        if op.type == 24:
            if settings["autoLeave"] == True:
                maxgie.leaveRoom(op.param1)                      
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if apalo["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = maxgie.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 maxgie.sendMessage(msg.to,"-> " + _name + " ?????????????????????????????????????????????")
                                 break
                             elif invite in apalo["blacklist"]:
                                 maxgie.sendMessage(msg.to,"??????????????????, " + _name + " ?????????????????????????????????????????????????????????????????????????????????")
                                 maxgie.sendMessage(msg.to,"???????????????????????????!,??????????????????,?????????" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     maxgie.findAndAddContactsByMid(target)
                                     maxgie.inviteIntoGroup(msg.to,[target])
                                     maxgie.sendMessage(msg.to,"???????????? :" + _name + "???????????????????????????")
                                     apalo["winvite"] = False
                                     break
                                 except:
                                     try:
                                         maxgie.findAndAddContactsByMid(invite)
                                         maxgie.inviteIntoGroup(op.param1,[invite])
                                         apalo["winvite"] = False
                                     except:
                                         maxgie.sendMessage(msg.to,"??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
                                         apalo["winvite"] = False
                                         break
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
                        if msg._from not in [maxgieMID]:
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
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg._from not in maxgieMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        maxgie.sendMention(to, "???????????????????????????????????????????????????????????? @! :)","",[msg._from])
                        maxgie.kickoutFromGroup(msg.to, [msg._from])
                if msg.contentType == 13:
                  if apalo["Talkwblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          maxgie.sendMessage(msg.to,"Sudah Ada")
                          apalo["Talkwblacklist"] = False
                      else:
                          apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
                          apalo["Talkwblacklist"] = False
                          maxgie.unsendMessage(msg_id)
                          duc1(to, "??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
                  if apalo["Talkdblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
                          maxgie.unsendMessage(msg_id)
                          duc1(to, "?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
                          apalo["Talkdblacklist"] = False
                      else:
                          apalo["Talkdblacklist"] = False
                          maxgie.sendMessage(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
        if op.type in [25,26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        try:
                            if sets["l"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                duc1(to,"???????????????????????????????????????????????????????????")
                                if purl[1] not in wait['postId']:
                                    maxgie.likePost(purl[0], purl[1], random.choice([1001]))
                                if sets["c"] == True:
                                    maxgie.createComment(purl[0], purl[1], sets["cm"])
                                    wait['postId'].append(purl[1])
                                else:
                                    pass
                        except Exception as e:
                                if sets["l"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    duc1(to,"???????????????????????????????????????????????????????????")
                                    if purl[1] not in wait['postId']:
                                        maxgie.likePost(msg._from, purl[1], random.choice([1001]))
                                    if sets["c"] == True:
                                        maxgie.createComment(msg._from, purl[1], sets["cm"])
                                        wait['postId'].append(purl[1])
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
                    if sender != maxgie.profile.mid:
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
                if text.lower() == "??????????????????":
                    sa="????????????????????? ????????????????????????????????? >\\<"
                    sa+="\n- ?????????????????? ?????????????????????/????????????????????????"
                    sa+="\n???????????????????????? >\\<"
                    sa+="\n- ?????????????????? ??????????????????/nonbysignal"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": " ??????????????????????????????????????????????????????????", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~boy-5566"}}
                    sendTemplate(to,data)
                if text.lower() == "????????????api":
                    sa = "????????????????????? api >\\<"
                    sa += "\n- ????????????api ??????????????????????????????;;?????????????????????"
                    sa += "\n???????????????????????? >\\<"
                    sa += "\n- ????????????api ?????????;;?????????????????????"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "?????????????????????????????????????????????????????????? ", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~boy-5566"}}
                    sendTemplate(to,data)
                if text.lower() == "stag":
                    sa = "????????????????????? stag >\\<"
                    sa += "\n- stag [???????????????????????????????????????] @user"
                    sa += "\n???????????????????????? >\\<"
                    sa += "\n- stag 1 @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "??????????????????????????????????????????????????????????", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~boy-5566"}}
                    sendTemplate(to,data)
                if text.lower() == "????????????":
                    sa = "????????????????????? ???????????? >\\<"
                    sa += "\n- ????????????????????? [?????????????????????] @user"
                    sa += "\n???????????????????????? >\\<"
                    sa += "\n- ???????????? ?????????????????? @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "?????????????????????????????????????????????????????????? ", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~boy-5566"}}
                    sendTemplate(to,data)
                if text.lower() == "??????????????????" or text.lower() == "set":
                    sas = "??? Settings ???"
                    if settings["autoAdd"] == True: sa = "\n??? ???????????????????????? ( ???????????? )"
                    else:sa = "\n??? ???????????????????????? ( ????????? )"
                    if settings["autoblock"] == True: sa += "\n??? ?????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ?????????????????????????????? ( ????????? )"
                    if settings["autoCancel"]["on"] == True: sa +="\n??? ????????????????????????????????????????????????????????????????????????: " + str(settings["autoCancel"]["members"])
                    else:sa += "\n??? ????????????????????????????????????????????? ( ????????? )"
                    if kcn["autojoin"] == True: sa += "\n??? ?????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ?????????????????????????????? ( ????????? )"    
                    if tagadd["tags"] == True: sa += "\n??? ???????????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ???????????????????????????????????? ( ????????? )"
                    if tagadd["tagss"] == True: sa += "\n??? ????????????????????????????????????2 ( ???????????? )"
                    else:sa += "\n??? ????????????????????????????????????2 ( ????????? )"
                    if sets["tagsticker"] == True: sa += "\n??? ??????????????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ??????????????????????????????????????? ( ????????? )"
                    if settings["autolike"] == True: sa += "\n??? ??????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ??????????????????????????? ( ????????? )"
                    if settings["com"] == True: sa += "\n??? ?????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ?????????????????????????????? ( ????????? )"
                    if settings["Welcome"] == True: sa += "\n??? ?????????????????????????????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ?????????????????????????????????????????????????????? ( ????????? )"
                    if settings["Wc"] == True: sa += "\n??? ??????????????????????????????????????????????????????2 ( ???????????? )"
                    else:sa += "\n??? ??????????????????????????????????????????????????????2 ( ????????? )"
                    if settings["wcsti2"] == True: sa += "\n??? ????????????????????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ????????????????????????????????????????????? ( ????????? )"
                    if settings["Leave"] == True: sa += "\n??? ?????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ?????????????????????????????? ( ????????? )"
                    if settings["lv"] == True: sa += "\n??? ?????????????????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ?????????????????????????????????????????? ( ????????? )"
                    if settings["unsendMessage"] == True: sa += "\n??? ??????????????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ??????????????????????????????????????? ( ????????? )"
                    if settings["Sticker"] == True: sa += "\n??? ????????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ????????????????????????????????? ( ????????? )"
                    if sets["Sticker"] == True: sa += "\n??? ??????????????????????????????????????????????????? ( ???????????? )"
                    else:sa += "\n??? ??????????????????????????????????????????????????? ( ????????? )"
                    
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#FF9933'
                                },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
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
                                        "text": sas,
                                        "color": "#8B0000",
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#8B0000",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'clearban' or text.lower() == "??????????????????":
                      apalo["Talkblacklist"] = []
                      duc1(to, "??????????????????????????")
                
                elif text.lower() == "????????????":
                    if msg._from in maxgieMID:
                        if apalo["Talkblacklist"] == []:
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "?????????????????????????.?????????????????????????")
                        else:
                            for bl in apalo["Talkblacklist"]:
                                maxgie.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif text.lower() == "???????????????":
                    if msg.toType == 2:
                        groupMemberMids = [contact.mid for contact in maxgie.getGroup(to).members]
                        matched_list = []
                        for mid in apalo["Talkblacklist"]:
                            matched_list += [x for x in groupMemberMids if x == mid]
                        if matched_list == []:
                            duc1(to, "??????????????????????????????????????")
                        else:
                            for mids in matched_list:
                                try:
                                    maxgie.kickoutFromGroup(to, [mids])
                                except:pass
                
                elif "Kick " in msg.text:
                    Ri0 = text.replace("kick ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = maxgie.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    maxgie.kickoutFromGroup(to,[target])
                                except:
                                    pass                              

                elif ".?????????????????????" in msg.text:
                  if msg._from in admin:
                   if msg.toType == 2:
                      print("ok")
                      _name = msg.text.replace(".?????????????????????","")
                      gs = maxgie.getGroup(msg.to)
                      gs = maxgie.getGroup(msg.to)
                      gs = maxgie.getGroup(msg.to)
                      targets = []
                      for g in gs.members:
                         if _name in g.displayName:
                             targets.append(g.mid)
                      if targets == []:
                         maxgie.sendText(msg.to,"Tidak Ditemukan.")
                      else:
                          for target in targets:
#                           if not target in admin and Bots:
                              try:
                                  klist=[maxgie]
                                  kicker=random.choice(klist)
                                  kicker.kickoutFromGroup(msg.to,[target])
                                  print (msg.to,[g.mid])
                              except Exception as e:
                                  break

                elif "????????????????????? " in msg.text:
                    Ri0 = text.replace("????????????????????? ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = maxgie.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    maxgie.kickoutFromGroup(to,[target])
                                    maxgie.findAndAddContactsByMid(target)
                                    maxgie.inviteIntoGroup(to,[target])
                                except:
                                    pass
                
                elif "????????? " in msg.text:
                        vkick0 = msg.text.replace("????????? ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = maxgie.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    maxgie.kickoutFromGroup(msg.to,[target])
                                    maxgie.findAndAddContactsByMid(target)
                                    maxgie.inviteIntoGroup(msg.to,[target])
                                    maxgie.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass            
                elif msg.text.lower().startswith("??????me "):
                            text_ = removeCmd("??????me", text)
                            try:
                                temp["t"] = text_
                                maxgie.sendMessage(to,"??? ?????????????????? ???\n????????? : " + text_)
                            except:
                                maxgie.sendMessage(to,"?????????????????????????????????")
                elif msg.text.lower().startswith("????????????????????? "):
                            text_ = removeCmd("?????????????????????", text)
                            try:
                                temp["te"] = text_
                                maxgie.sendMessage(to,"??? ?????????????????? ???\n????????? : " + text_)
                            except:
                                maxgie.sendMessage(to,"?????????????????????????????????")
                elif msg.text.lower() == "??????????????????":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="**?????????????????????????????????1**\n????????????????????????????????????????????? me\n?????????'??????????????????me #333333'\n**?????????????????????????????????2**\n????????????????????????????????????????????? tag\n?????????'??????????????????????????? #333333'"
                            maxgie.sendImageWithURL(to,c)
                            maxgie.sendImageWithURL(to,p)
                            maxgie.sendMessage(to,m)
                elif msg.text.lower().startswith("??????????????????????????? "):
                            text_ = removeCmd("???????????????????????????", text)
                            try:
                                tagadd["b"] = text_
                                maxgie.sendMessage(to,"??? ?????????????????????????????????????????????????????? ???\n????????? : " + text_)
                            except:
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "????????????????????????????????????????????")
                elif text.lower().startswith("???????????????????????????????????? "):
                            text_ = removeCmd("????????????????????????????????????", text)
                            try:
                                settings["autoCancel"]["members"] = text_
                                maxgie.sendMessage(to,"??? ?????????????????????????????????????????? ???\n??????????????? : " + text_)
                            except:
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "????????????????????????????????????????????")
                if text.lower() == "??????":
                  if msg._from in admin:
                      apalo["Talkwblacklist"] = True
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "???????????????????????????????...????")
                if text.lower() == "?????????":
                  if msg._from in admin:
                      apalo["Talkdblacklist"] = True
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "???????????????????????????????...????")
                elif msg.text.lower().startswith("????????????????????? "):
                      text_ = removeCmd("?????????????????????", text)
                      try:
                          tagadd["tag"] = text_
                          sa = "??? ??????????????????????????? ???\n????????? : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "?????????????????????????????????????????????????????????? ", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ube3faf73d9f1d8388b472b576328ec21"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("?????????????????????????????? "):
                      text_ = removeCmd("??????????????????????????????", text)
                      try:
                          settings["reply"] = text_
                          sa = "??? ??????????????????????????? ???\n????????? : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "??????????????????????????????????????????????????????????", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ube3faf73d9f1d8388b472b576328ec21"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("????????????????????????????????? "):
                      text_ = removeCmd("?????????????????????????????????", text)
                      try:
                          tagadd["wctext"] = text_
                          sa = "??? ????????????????????????????????? ???\n????????? : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": " ??????????????????????????????????????????????????????????", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ube3faf73d9f1d8388b472b576328ec21"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("??????????????????????????? "):
                            text_ = removeCmd("???????????????????????????", text)
                            try:
                                tagadd["lv"] = text_
                                maxgie.sendMessage(to,"??? ??????????????????????????? ???\n????????? : " + text_)
                            except:
                                maxgie.sendMessage(to,"?????????????????????????????????")
                elif msg.text.lower().startswith("????????????????????? "):
                      text_ = removeCmd("?????????????????????", text)
                      try:
                          tagadd["add"] = text_
                          sa = "??? ????????????????????? ???\n????????? : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "??????????????????????????????????????????????????????????", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ube3faf73d9f1d8388b472b576328ec21"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("????????????????????????????????? "):
                      text_ = removeCmd("?????????????????????????????????", text)
                      try:
                          settings["commet"] = text_
                          sa = "??? ????????????????????????????????? ???\n????????? : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "??????????????????????????????????????????????????????????", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ube3faf73d9f1d8388b472b576328ec21"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("????????? "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    for x in range(jml):
                        name = maxgie.getContact(to)
                        RhyN_(to, name.mid)                          
                elif msg.text.lower() == "?????????":
                  if msg.toType == 0:
                     sendMention(to, to, "?????????????????????????????????????????????????????????????????????????????????????????\n", "\n?????????????????????????????????????????????????????????????????????????????????????????")
                  elif msg.toType == 2:
                     group = maxgie.getGroup(to)
                     contact = [mem.mid for mem in group.members]
                     mentionMembers(to, contact)       
                if text.lower() == "?????????":
                    add = tagadd["add"]
                    tag = tagadd["tag"]
                    like = settings["commet"]
                    wc = tagadd["wctext"]
                    lv = tagadd["lv"]
                    c = settings["autoCancel"]["members"]
                    b = tagadd["b"]
                    Re = settings["reply"]
                    maxgie.generateReplyMessage(msg.id)
                    maxgie.sendMessags(id, to, "?????????????????????????????? :\n"+str(add)+"\n\n?????????????????????????????? :\n"+str(tag)+"\n\n????????????????????????????????? :\n"+str(like)+"\n\n?????????????????????????????????????????? :\n"+str(wc)+"\n\n???????????????????????????????????? :\n"+str(lv)+"\n\n??????????????????????????????????????? :\n"+str(c)+" ???????????????\n\n???????????????????????????????????? :\n"+str(b)+"\n\n??????????????????????????????????????? :\n"+str(Re))
                if text.lower() == "/??????????????????" or text.lower() == "/help":
                    sas = "???? Help Message ????\n"
                    sa = "??? ??????\n"
                    sa += "??? ?????????????????????\n"
                    sa += "??? ?????????????????????\n"
                    sa += "??? ??????????????????\n"
                    sa += "??? ??????????????????\n"
                    sa += "??? ????????????????????????????????????\n"
                    sa += "??? ???????????????\n"
                    sa += "??????????????????????????????????????????\n"
                    sa += "??? ??????????????????\n"
                    sa += "??? ?????????\n"
                    sa += "??? ???????????????\n"
                    sa += "??? ?????????\n"
                    sa += "??? ??????????????????\n"
                    sa += "??? /???????????????\n"
                    sa += "??? ???????????? @user\n"
                    sa += "??? ????????????????????????\n"
                    sa += "??????????????????????????????????????????\n"
                    sa += "??? ????????????????????? [?????????'?????????????????????'?????????????????????????????????]\n"
                    sa += "??? ????????????api [??????????????????????????????????????????]\n"
                    sa += "??? ????????????api [???????????????????????????]\n"
                    sa += "??? ?????????api\n"
                    sa += "??? stag [?????????'stag'?????????????????????????????????]\n"
                    sa += "??? ?????????????????? [MID]\n"
                    sa += "??? ??????????????? [?????????????????????]\n"
                    sa += "??? image [text(??????????????????????????????)]\n"
                    sa += "??? ????????? [?????????????????????(?????????????????????)]\n"
                    sa += "??? ?????????????????? [?????????????????????]\n"
                    sa += "??? ?????????????????????????????????????????? [???????????????????????????]\n"
                    sa += "??? ?????????????????? [?????????'??????????????????'?????????????????????????????????]\n"
                    sa += "??? ?????? [?????????????????????????????????????????????????????????]\n"
                    sa += "??????????????????????????????????????????\n"
                    sa += "??? ?????? ???????????????.\n"
                    sa += "??? ????????? ???????????????.\n"
                    sa += "??? ?????? @user\n"
                    sa += "??? ???????????? @user\n"
                    sa += "??? ???????????????\n"
                    sa += "??? ????????????\n"
                    sa += "??? ??????????????????\n"
                    sa += "??????????????????????????????????????????\n"
                    sa += "??? ????????????????????????????????? [?????????????????????]\n"
                    sa += "??? ??????????????????????????? [?????????????????????]\n"
                    sa += "??? ????????????????????? [?????????????????????]\n"
                    sa += "??? ????????????????????? [?????????????????????]\n"
                    sa += "??? ????????????????????????????????? [?????????????????????]\n"
                    sa += "??????????????????????????????????????????\n"
                    sa += "??? ?????????????????????/??????????????????\n"
                    sa += "??? ?????????????????????2/??????????????????2\n"
                    sa += "??? ?????????????????????3/??????????????????3\n"
                    sa += "??? ????????????????????????/?????????????????????\n"
                    sa += "??? ?????????????????????????????????/??????????????????????????????\n"
                    sa += "??? ???????????????????????????/????????????????????????\n"
                    sa += "??? ?????????????????????/??????????????????\n"
                    sa += "??? ??????????????????????????????/???????????????????????????\n"
                    sa += "??? ?????????????????????????????????/??????????????????????????????\n"
                    sa += "??? ?????????????????????????????????2/??????????????????????????????2\n"
                    sa += "??? ???????????????????????????/????????????????????????\n"
                    sa += "??? ??????????????????????????????/???????????????????????????\n"
                    sa += "??? ????????????????????????????????????/?????????????????????????????????\n"
                    sa += "??? ????????????????????????????????????/?????????????????????????????????"
                    helps = "{}".format(str(sa))
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#EE1289'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": sas,
                                        "size":"xl",
                                        "weight":"bold",
                                        "color":"#00F5FF",
                                        "align":"center"
                                    },
                                    {
                                        "type":"text",
                                        "text": " "
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#000000",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type":"button",
                                        "style":"primary",
                                        "color":"#",
                                        "action": {
                                            "type":"uri",
                                            "label":"????????????????????????",
                                            "uri":"line://ti/p/~boy-5566"
                                        },
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "help" or text.lower() == "??????????????????":
                            s = "#8B0000"
                            sa = "?????? me & ????????? & ?????????2\n"
                            sa += "?????? /me\n"
                            sa += "?????? ??????\n"
                            sa += "?????? ?????????????????????\n"
                            sa += "?????? ?????????????????????\n"
                            sa += "?????? ??????????????????\n"
                            sa += "?????? ??????????????????\n"
                            sa += "?????? ????????????????????????????????????\n"
                            sa += "?????? ???????????????\n"
                            sa += "?????? ??????????????????\n"
                            sa += "?????? ???????????????\n"
                            sa += "?????? ????????? & ?????????1 & ?????????2\n"
                            sa += "?????? /???????????????\n"
                            sa += "?????? ??????????????????\n"
                            sa += "?????? ?????????\n"
                            sa += "?????? ?????????\n"     
                            sa += "?????? ???????????? & sp\n"       
                            sa += "?????? ??????????????????"    
                            ss = "?????? ?????????\n"
                            ss += "?????? ????????? [???????????????] (??????) \n"
                            ss += "?????? ?????????\n"
                            ss += "?????? ????????? ???[????????????] @user\n"
                            ss += "?????? ???????????? @user\n"
                            ss += "?????? ????????????????????????\n"
                            ss += "?????? ????????????api [??????????????????????????????????????????]\n"
                            ss += "?????? ????????????api [???????????????????????????]\n"
                            ss += "?????? ?????????api\n"
                            ss += "?????? stag [?????????'stag'?????????????????????????????????]\n"
                            ss += "?????? ?????????????????? [MID]\n"
                            ss += "?????? ??????????????? [?????????????????????]\n"
                            ss += "?????? image [text(??????????????????????????????)]\n"
                            ss += "?????? ????????? [?????????????????????(?????????????????????)]\n"
                            ss += "?????? ?????????????????? [?????????????????????]\n"
                            ss += "?????? ?????????????????????????????????????????? [???????????????????????????]\n"
                            ss += "?????? ?????????????????? [?????????'??????????????????'?????????????????????????????????]\n"
                            ss += "?????? ?????????????????? [?????????????????????????????????????????????????????????]"
                            sd = "?????? ?????? ???????????????.\n"
                            sd += "?????? ????????? ???????????????.\n"
                            sd += "?????? ?????? @user\n"
                            sd += "?????? ???????????? @user\n"
                            sd += "?????? ???????????????\n"    
                            sd += "?????? ???????????????\n"
                            sd += "?????? ????????????\n"
                            sd += "?????? ??????????????????\n"
                            sd += "?????? kick @user\n"    
                            sd += "?????? ????????????????????????????????? [?????????????????????]\n"
                            sd += "?????? ??????????????????????????? [?????????????????????]\n"
                            sd += "?????? ????????????????????? [?????????????????????]\n"
                            sd += "?????? ????????????????????? [?????????????????????]\n"
                            sd += "?????? ?????????????????????????????? [?????????????????????]\n"    
                            sd += "?????? ????????????????????????????????? [?????????????????????]\n"
                            sd += "?????? ???????????????????????????????????? [???????????????]\n"
                            sd += "?????? ????????????????????????????????? [?????????????????????]\n"
                            sd += "?????? ??????????????????????????? [?????????????????????]"
                            se = "?????? ?????????????????????/??????????????????\n"
                            se += "?????? ?????????????????????2/??????????????????2\n"
                            se += "?????? ?????????????????????3/??????????????????3\n"
                            se += "?????? ????????????????????????/?????????????????????\n"
                            se += "?????? ?????????????????????????????????/??????????????????????????????\n"
                            se += "?????? ???????????????????????????/????????????????????????\n"
                            se += "?????? ?????????????????????/??????????????????\n"
                            se += "?????? ?????????????????????/??????????????????\n"    
                            se += "?????? ??????????????????????????????/???????????????????????????\n"
                            se += "?????? ?????????????????????????????????/??????????????????????????????\n"    
                            se += "?????? ?????????????????????????????????/??????????????????????????????\n"
                            se += "?????? ?????????????????????????????????2/??????????????????????????????2\n"
                            se += "?????? ???????????????????????????/????????????????????????\n"
                            se += "?????? ??????????????????????????????/???????????????????????????\n"
                            se += "?????? ??????????????????????????????????????????/???????????????????????????????????????\n"
                            se += "?????? ???????????????????????????????????????/????????????????????????????????????\n"
                            se += "?????? ????????????????????????????????????/?????????????????????????????????\n"
                            se += "?????? ????????????????????????/?????????????????????\n"
                            sti = "?????? ?????????????????????????????????/??????????????????????????????\n"
                            sti += "?????? ???????????????????????????????????????\n"
                            sti += "?????? ?????????????????????????????????\n"
                            sti += "?????? ???????????????????????????????????????\n"
                            sti += "?????? ?????????????????????????????????\n"
                            sti += "?????? ??????????????????????????????????????????\n"
                            sti += "?????? ????????????????????????????????????\n"
                            sti += "?????? ???????????????????????????????????????\n"
                            sti += "?????? ?????????????????????????????????\n"
                            sti += "?????? ??????????????? [?????????????????????]\n"
                            sti += "?????? ???????????????????????? [idline]\n"
                            sti += "?????? ????????? @user\n"
                            sti += "?????? ??????????????? @user\n"
                            sti += "?????? ????????????????????????????????? @user\n"
                            sti += "?????? ???????????????????????? @user\n"
                            sti += "?????? ?????? @user\n"
                            sti += "?????? Spam on [???????????????] [?????????????????????]\n"
                            sti += "?????? /????????? [???????????????]"
                            stz = "?????? ???????????????????????????\n"
                            stz += "?????? ????????????????????? [?????????????????????]\n"
                            stz += "?????? ?????????????????? [??????????????????]\n"
                            stz += "?????? ??????????????????\n"
                            stz += "?????? ?????????????????????????????????\n"
                            stz += "?????? ???????????????????????????\n"
                            stz += "?????? ????????????????????????\n"
                            stz += "?????? ???????????????????????????\n"
                            stz += "?????? ????????????\n"
                            stz += "?????? ????????????????????????\n"
                            stz += "?????? ?????????????????????\n"
                            stz += "?????? ????????????????????? [???????????????] @user\n"
                            stz += "?????? /???????????????\n"
                            stz += "?????? .?????????????????????\n"
                            stz += "\n"
                            stz += "\n"
                            stz += "\n"
                            stz += "\n"  
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#FF9933"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                               "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "??? ??????????????????????????????????????? ???",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sa,
                                                "color": s, 
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
                                                 "color":"#1C1C1C",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"??????????????????????????????????????????????????????????",
                                                     "uri":"line://ti/p/~boy-5566"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FF9933"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "??? ????????????????????????????????? ???",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": ss, 
                                                "color": s,
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
                                                 "color":"#1C1C1C",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"??????????????????????????????????????????????????????????",
                                                     "uri":"line://ti/p/~boy-5566"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FF9933"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "??? ??????????????????????????????/????????? ???",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sd, 
                                                "color": s,
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
                                                 "color":"#1C1C1C",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"??????????????????????????????????????????????????????????",
                                                     "uri":"line://ti/p/~boy-5566"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FF9933"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "??? ???????????????????????????????????????/??????????????? ???",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
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
                                                "text": se, 
                                                "color": s,
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
                                          #      "text": "????????????????????? ?????????????????????????????????????????????????????????????????? >_<",
                                          #      "color": "#B5B5B5",
                                          #      "size": "xs"
                                          #  },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#1C1C1C",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"??????????????????????????????????????????????????????????",
                                                     "uri":"line://ti/p/~boy-5566"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FF9933"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "??? ???????????????????????????????????? ???",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sti, 
                                                "color": s,
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
                                                 "color":"#1C1C1C",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"??????????????????????????????????????????????????????????",
                                                     "uri":"line://ti/p/~boy-5566"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#FF9933"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "??? ???????????????????????????????????? ???",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": stz, 
                                                "color": s,
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
                                                 "color":"#1C1C1C",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"??????????????????????????????????????????????????????????",
                                                     "uri":"line://ti/p/~boy-5566"
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
#=====================================================================
                elif cmd.startswith("/????????? "):
                  #          if msg._from in "u51f2d901e6ae79ea2649062da18176df":
                               number = removeCmd("/?????????", text)
                               if len(number) > 0:
                                   if number.isdigit():
                                       number = int(number)
                                       if number > 1000000:                                             
                                           maxgie.sendMessage(to,"invalid >_< ! Max: 1000000.")
                                       else:
                                           for i in range(0,number):
                                               maxgie.sendMessage(to,str(number))
                                               number -= 1
                                               time.sleep(0.005)
                                   else:
                                      maxgie.sendMessage(to,"Please specify a valid number.")
                elif msg.text.lower().startswith("???????????? "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = maxgie.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = maxgie.getContact(she);ClonerV2(she)
                                    sendMention(to, contact.mid, "=??????????? ?????????????????????????????????????????????", "?????????????????????????????? >_<");maxgie.sendContact(to, str(BackupProfile.mid));maxgie.sendContact(to, str(contact.mid))
                elif text.lower() == "????????????????????????":
                            try:
                                maxgiestatus = maxgie.getProfile()
                                maxgieName = maxgie.getProfile()
                                maxgieName.statusMessage = ProfileMe["statusMessage"]
                                maxgieName.pictureStatus = str(ProfileMe["pictureStatus"])
                                maxgie.updateProfile(maxgiestatus)
                                maxgieName.displayName = ProfileMe["NameMe"]
                                maxgie.updateProfile(maxgieName)
                                path = maxgie.downloadFileURL(ProfileMe["PictureMe"])
                                maxgie.updateProfilePicture(path)
                                coverId = ProfileMe["coverId"]
                                maxgie.updateProfileCoverById(coverId)
                                BackupProfile = maxgie.getContact(sender)
                                sendMention(to, BackupProfile.mid, "=??????????? ??????????????????????????????????????????????????????????????????", ">_<");maxgie.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "?????????????????????????????????????????????????????????????????")
                elif msg.text.lower().startswith("."):
                    text = msg.text.lower().replace("."," ")
                    maxgie.unsendMessage(msg_id)                                       
                    duc1(msg.to,text)
                if text.lower() == "??????":
                    maxgie.generateReplyMessage(msg.id) 
                    maxgie.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': maxgieMID}, contentType=13)
                if text.lower() == "mid" or text.lower() == "?????????????????????":
                    maxgie.generateReplyMessage(msg.id)
                    maxgie.sendReplyMessage(msg.id, to,maxgieMID)
                elif text.lower() == "myname" or text.lower() == "?????????????????????":
                            h = maxgie.getContact(maxgieMID)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyMessage(msg.id, to, "??? ?????????????????????????????? ???\n"+str(h.displayName))
                elif text.lower() == "mybio" or text.lower() == "??????????????????":
                            h = maxgie.getContact(maxgieMID)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyMessage(msg.id, to, "??? ??????????????????????????? ???\n"+str(h.statusMessage))
                elif text.lower() == "mypicture" or text.lower() == "??????????????????":
                            h = maxgie.getContact(maxgieMID)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                elif text.lower() == "myvideo" or text.lower() == "????????????????????????????????????":
                            h = maxgie.getContact(maxgieMID)
                            if h.videoProfile == None:
                            	return maxgie.sendMessage(to, "??????????????????????????????????????????????????????????????? >_<")
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                elif text.lower() == "mycover" or text.lower() == "???????????????":
                            h = maxgie.getContact(maxgieMID)
                            cu = maxgie.getProfileCoverURL(maxgieMID)
                            image = str(cu)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                elif msg.text in ["?????????"]:
                        apalo["winvite"] = True
                        maxgie.unsendMessage(msg_id)
                        duc1(to, "???????????????????????????????????????????????????????..????")                        
                            
                elif "????????????????????? " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.displayName = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Update to :\n" + string)
                        print ("Update Name")

                elif "?????????????????? " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.statusMessage = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Succes Update :\n" + string)
                        print ("Update Bio Succes")
                        
                elif text.lower() == "??????????????????":
                    sets["changePictureProfile"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????????????????????????????????????????????????????..????")
                elif text.lower() == '?????????????????????':
                    did["join"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????? (????????????) ??????????????????????")
                elif text.lower() == '??????????????????':
                    did["join"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????? (?????????) ??????????????????????") 
                if text.lower() == "?????????1":
                    cover = maxgie.getProfileCoverURL(maxgie.profile.mid)
                    pp = maxgie.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = maxgie.getProfile().displayName
                    status = maxgie.getProfile().statusMessage     
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    eltime = time.time() - mulai
                    van = ggggg(eltime)
                    van2 = "\n\n????????????????????? :"+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n?????????????????????????????????\n???????????????:"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n\n"      
                    data={
"type":"flex",
"altText":"Weclome",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#FF9933", "separator": True, "separatorColor": "#FF9933"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "??? ????????? ???",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#8B0000",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#8B0000"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#8B0000"
},
{
"contents": [
{
"text": "????????????????????????????????????????????????",
"size": "md",
"align": "center",
"color": "#8B0000",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#8B0000"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#8B0000",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " ??? ???????????????????????? : \n ??? ??????????????????????????????????????????????????????????",
"size": "xs",
"margin": "none",
"color": "#8B0000",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#8B0000",
"height": "sm",
"action": {
"type": "uri",
"label": "???????????????????????????",
"uri": "https://line.me/ti/p/~boy-5566",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#8B0000",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "??????????????????????????????????????????",
"uri": "https://line.me/ti/p/~boy-5566",
}
}
]
}
},
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#FF9933", "separator": True, "separatorColor": "#FF9933"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "??? ?????????????????? ???",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#8B0000",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#8B0000"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#8B0000"
},
{
"contents": [
{
"text": "?????????????????????????????????????????????????????????",
"size": "md",
"align": "center",
"color": "#8B0000",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#8B0000"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van2,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#8B0000",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " ??? ???????????????????????? : \n ??? ??????????????????????????????????????????????????????????",
"size": "xs",
"margin": "none",
"color": "#8B0000",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#8B0000",
"height": "sm",
"action": {
"type": "uri",
"label": "???????????????????????????",
"uri": "https://line.me/ti/p/~boy-5566",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#8B0000",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "??????????????????????????????????????????",
"uri": "https://line.me/ti/p/~boy-5566",
}
}
]
}
}
]
}
}                    
                    sendTemplate(to, data)   
                if text.lower() == "?????????2" or text.lower() == "runtime":
                    contact = maxgie.getContact(sender)
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)   
                    a = "??????????????????"+ datetime.strftime(timeNow,'%d-%m-%Y')+"????????????????????"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n"
                    run = "??? ????????????????????? ???\n"
                    run += runtime
                    data = {
                            "type": "flex",
                            "altText": "{}".format(run),
                            "contents": {
                            "styles": {
                              "body": {
                                "backgroundColor": "#FF9933"
                              },
                              "footer": {
                                "backgroundColor": "#FF9933"
                              }
                            },
                            "type": "bubble",
                            "body": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                      "type": "image"
                                    },
                                    {
                                      "type": "separator",
                                      "color": "#8B0000"
                                    },
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                      "type": "image"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "horizontal"
                                },
                                {
                                  "type": "separator",
                                  "color": "#8B0000"
                                },
                                {
                                  "contents": [
                                    {
                                      "text": "?????????????????????????????????????????????",
                                      "size": "lg",
                                      "align": "center",
                                      "color": "#8B0000",
                                      "wrap": True,
                                      "weight": "bold",
                                      "type": "text"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "vertical"
                                },
                                {
                                  "type": "separator",
                                  "color": "#8B0000"
                                },
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "{}".format(run),
                                          "size": "lg",
                                          "align": "center",
                                          "margin": "none",
                                          "color": "#8B0000",
                                          "wrap": True,
                                          "weight": "regular",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    },
                                  ],
                                  "type": "box",
                                  "layout": "vertical"
                                }
                              ],
                              "type": "box",
                              "spacing": "md",
                              "layout": "vertical"
                            },
                            "footer": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "??????????????????????????????????????????????????????????",
                                          "size": "xl",
                                          "action": {
                                            "uri": "line://ti/p/~boy-5566",
                                            "type": "uri",
                                            "label": "Add Maker"
                                          },
                                          "margin": "xl",
                                          "align": "center",
                                          "color": "#8B0000",
                                          "weight": "bold",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    }
                                  ],
                                  "type": "box",
                                  "layout": "horizontal"
                                }
                              ],
                              "type": "box",
                              "layout": "vertical"
                            }
                        }
                    }
                    sendTemplate(to, data)      
                if text.lower() == "me":
                    cover = maxgie.getProfileCoverURL(maxgie.profile.mid)
                    pp = maxgie.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = maxgie.getProfile().displayName
                    status = maxgie.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText":"{} sendFlex".format(name),"contents":{"type":"bubble",'styles': {"body":{"backgroundColor":a}},"hero":{"type":"image","url":cover,"size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":" "},{"type":"image","url":profile,"size":"lg"},{"type":"text","text":" "},{"type":"text","text":name,"size":"xl","weight":"bold","color":s,"align":"center"},{"type":"text","text":" "},{"type":"text","text":status,"align":"center","size":"xs","color":s,"wrap":True},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#FF9933","action":{"type":"uri","label":"??????????????????????????????????????????????????????????","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://i.pinimg.com/originals/63/c4/12/63c412c55c99b6e0742bebaf53dd40d6.jpg"}}]}}}
                    sendTemplate(to, data)
                elif text.lower() == "?????????2":
                            s = temp["te"]
                            a = temp["t"]
                            contact = maxgie.getContact(maxgieMID)
                            cover = maxgie.getProfileCoverURL(maxgieMID)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
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
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "weight": "bold",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1
                                            },
                                            {
                                                "type": "text",
                                                "text": " ?????????????????????????????? ",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                       ]
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
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "??????????????????????????????????????????????????????????",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~boy-5566"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(cover),
                                        "size": "full",
                                        "aspectRatio":"20:13",
                                        "aspectMode":"cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.mid),
                                                "align": "center",
                                                "color": s,
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": "??????????????????????????????????????? ",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                        ]
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
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "??????????????????????????????????????????????????????????",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~boy-5566"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "??????????????????????????????",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "color": s,
                                                "size": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "align": "center",
                                                "color": a,
                                                "size": "sm",
                                            },
                                            {
                                                "type": "text",
                                                "text": "???????????????????????????????????? ",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.statusMessage),
                                                "align": "center",
                                                "color": s,
                                                "wrap": True,
                                                "size": "md"
                                           },
                                        ]
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
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "??????????????????????????????????????????????????????????",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~boy-5566"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(contact.displayName),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                if text.lower() == "?????????":
                    contact = maxgie.getContact(sender)
                    sendTemplate(to,{"type":"flex","altText": "??????????????????????????????????????????????????????????","contents":{"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#333333","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://img.live/images/2019/02/10/1549778907829.jpg"},"type":"text","text":"??????????????????????????????????????????????????????????","align":"center","weight":"bold"},{"type":"separator","color":"#FF9933"},{"color":"#FF9933","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://ti/p/~boy-5566"},"type":"text","text":"????????????????????????","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#8B0000"},"body":{"backgroundColor":"#FF9933"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#FF9933"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/02/21/c5f4e567380d0f1e31acb822d0b5cfd2819c8e3b_00.jpg"},{"type":"separator","color":"#FF9933"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/21/d1566d9832bd42f14ec4d2538f74ab76.jpg"},{"type":"separator","color":"#FF9933"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/10/1549778907829.jpg"},{"type":"separator","color":"#FF9933"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/10/1549778907829.jpg"},{"type":"separator","color":"#FF9933"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF9933"},{"type":"box","contents":[{"type":"separator","color":"#FF9933"},{"color":"#FF9933","size":"md","wrap":True,"type":"text","text":" ??????????????????????????????????????????????????????????","weight":"bold"},{"type":"separator","color":"#FF9933"},{"color":"#FF9933","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#FF9933"},{"color":"#FF9933","size":"xs","wrap":True,"type":"text","text":"Status Profile:","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":"#FF9933"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"full","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}})            
                elif text.lower() == "/runtime" or text.lower() == "/?????????":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "????????????????????? \n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=ube3faf73d9f1d8388b472b576328ec21"
                        } 
                    }
                    sendTemplate(to, data)                            
                elif text.lower() == "/runtime" or text.lower() == "/?????????":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "??? ????????????????????? ???\n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=ube3faf73d9f1d8388b472b576328ec21"
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "?????????" or text.lower() == "runtime":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "??? ????????????????????? ???\n"
                    run += runtime
                    data = {
                        "type": "flex",
                        "altText": "{}".format(run),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#FF9933'
                                 },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                              #  {
                                              #  "type": "image",
                                                #"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                               # "size": "full"
                                             #  },
                                    {
                                        "type": "text",
                                        "text": "{}".format(run),
                                        "wrap": True,
                                        "color": "#8B0000",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "???????????????" or text.lower() == "reset":
                    gifnya = ["https://i.pinimg.com/originals/2e/d7/37/2ed737ba301b048afdb355fd9d1c2e86.gif"]
                    data = {
                        "type": "template",
                        "altText": "??????????????????????????????...",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~boy-5566"
                                     }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, data)
                    restartBot()
                    time.sleep(1)
                    ga = "?????????????????????????????? (?????????????)"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(ga)),
                        "sentBy": {
                             "label": "?????????????????????????????????...",
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://ti/p/~boy-5566"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "Sp" or text.lower() == "????????????":                       
                    contact = maxgie.getContact(sender)
                    start = time.time()
                    maxgie.sendMessage(to, "?????????????????????????????????????????????")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = " ????????????????????? \n????????????????????????????????????????? ??????\n ???????? Took : %.3fms ??????\n????????????????????????????????????????????: %.10f ??????" % (took,elapsed_time)
                    LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                    LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"                            
                    data = {
                        "type": "flex",
                                "altText": "{}".format(a),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#FF9933'
                                            },
                                            "footer": {
                                                "backgroundColor": '#1C1C1C'
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
                                                                "color": "#8B0000",
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
                                                    "label": "??????????????????????????????????????????????????????????",
                                                    "uri": "line://ti/p/~boy-5566"
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
                elif "?????????" in msg.text.lower():
                   if msg.toType == 2:
                      sep = msg.text.split(" ")
                      resp = msg.text.replace(sep[0] + " ","")
                      num = int(resp)
                      try:
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "??????????????????????????????????????????????...????") 
                      except:
                         pass
                      for var in range(num):
                            group = maxgie.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            maxgie.acquireGroupCallRoute(msg.to)
                            maxgie.inviteIntoGroupCall(msg.to, contactIds=members)
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "???????????????????????????????????????????????")

                elif msg.text.startswith("?????????"):
                    dan = text.split(" ")
                    num = int(dan[1])
                    ret_ = "?????????[ ??????????????????????????????????????? ]"
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
                                group = maxgie.getGroup(to)
                                members = [ls]
                                maxgie.acquireGroupCallRoute(to)
                                maxgie.inviteIntoGroupCall(to, contactIds=members)
                            ret_ += "\n???> @!"
                        ret_ += "\n?????????????????????????????????"
                        maxgie.sendPhu(to, ret_, lists)   
                                        
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               maxgie.sendMessage(msg.to, teks)
                        else:
                           maxgie.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            maxgie.sendMessage(msg.to, tulisan)
                elif text.lower() == '??????????????????' or text.lower() == "about":
                    try:
                        arr = []
                        owner = "ube3faf73d9f1d8388b472b576328ec21"
                        creator = maxgie.getContact(owner)
                        contact = maxgie.getContact(maxgieMID)
                        grouplist = maxgie.getGroupIdsJoined()
                        contactlist = maxgie.getAllContactIds()
                        blockedlist = maxgie.getBlockedContactIds()
                        IdsInvit = maxgie.getGroupIdsInvited()
                        times = time.time() - Start
                        runtime = timeChange(times)
                        ret_ = "??????????????? About Your ???"
                        ret_ += "\n??? ???????????? : {}".format(contact.displayName)
                        ret_ += "\n??? ??????????????? : {}".format(str(len(grouplist)))
                        ret_ += "\n??? ?????????????????? : {}".format(str(len(contactlist)))
                        ret_ += "\n??? ??????????????? : {}".format(str(len(blockedlist)))
                        ret_ += "\n??? ???????????????????????? : {}".format(str(len(IdsInvit)))
                        ret_ += "\n???????????????????????????????????????"
                        ret_ += "\n??? ?????????????????????????????? :"
                        ret_ += "\n??? {}".format(str(runtime))
                        ret_ += "\n???????????????????????????????????????"
                        ret_ += "\n??? ???????????????????????? : {}".format(str(creator.displayName))
                        ret_ += "\n??????????????? ?????????????????????????????????????????????????????????? ???"
                        feds = "{}".format(str(ret_))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret_)),
                            "sentBy": {
                                 "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                                 "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                 "linkUrl": "line://ti/p/~boy-5566"
                            }
                        }
                        sendTemplate(to, data)
                        maxgie.sendContact(msg.to, creator.mid)
                    except Exception as e:
                        maxgie.sendMessage(msg.to, str(e))
                elif text.lower() == "?????????????????????":
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
                                                "uri": "line://ti/p/~boy-5566"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "?????????" or text.lower() == "????????????":
                            gifnya = ['https://thumbs.gfycat.com/KlutzyUglyGelding-small.gif']
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
                                                "uri": "line://ti/p/~boy-5566"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif cmd == "random":
                            gifnya = ['https://thumbs.gfycat.com/AngelicCloudyJaeger-size_restricted.gif','https://thumbs.gfycat.com/AgedZealousBlackfootedferret-size_restricted.gif','https://thumbs.gfycat.com/FondHastyChinesecrocodilelizard-size_restricted.gif','https://thumbs.gfycat.com/LividCrazyDipper-size_restricted.gif','https://thumbs.gfycat.com/LoathsomeDevotedGossamerwingedbutterfly-size_restricted.gif','https://thumbs.gfycat.com/SamePhysicalHarrierhawk-size_restricted.gif','https://thumbs.gfycat.com/ColorlessPinkLangur-size_restricted.gif','https://thumbs.gfycat.com/ThoseBitesizedBrahmanbull-size_restricted.gif','https://thumbs.gfycat.com/FakeSlowBengaltiger-size_restricted.gif','https://thumbs.gfycat.com/TanSpitefulChupacabra-size_restricted.gif']
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
                                                "uri": "line://ti/p/~boy-5566"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                            
                elif msg.text.lower().startswith("??????????????????????????????????????????"):
                            link = removeCmd("??????????????????????????????????????????", text)
                            contact = maxgie.getContact(sender)
                            maxgie.sendMessage(to, "Type: Profile\n ??? Detail: Change video url\n ??? Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = maxgie.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            changeVideoAndPictureProfile(pict, vids)
                            maxgie.sendMessage(to, "Type: Profile\n ??? Detail: Change video url\n ??? Status: Succes")
                            os.remove("TeamAnuBot.mp4")
#=====================================================================

#=====================================================================
                elif msg.text.lower().startswith("?????? "):
                   if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = maxgie.getContact(ls)
                            mi_d = contact.mid
                            maxgie.sendContact(msg.to, mi_d)
                            
                elif text.lower() == "?????????":
                    duc1(to, "??????... 10.0%")
                    duc1(to, "????????????... 25.0%")
                    duc1(to, "??????????????????... 50.0%")
                    duc1(to, "????????????????????????... 75.0%")
                    duc1(to, "?????????????????????????????????..100.0%")

                elif msg.text in ["?????????"]:
                    duc1(to,"??? ?????????????????????????????????????????????????????????????")
                    duc1(to,"??:::??? 1 ???:::????")
                    duc1(to,"????:::??? 5 ???:::????")
                    duc1(to,"????:::??? 10 ???:::????")
                    duc1(to,"???????????????????????????????????????????????????" +datetime.today().strftime('%H:%M:%S')+ "???") 
#=====================================================================
                elif msg.text.lower().startswith("???????????????????????????: "):
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    friends = maxgie.friends
                    for friend in friends:
                        maxgie.sendMessage(friend, "??????????????????????????????????????????????????? ??????????????????????????????\n{}".format(str(txt)))
                    duc1(to, "????????????????????????????????????????????????????????? {} ??????".format(str(len(friends))))
#=============================================================================           
                elif msg.text.lower().startswith("?????? "):
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
                                        apalo["Talkblacklist"][ls] = True
                                        maxgie.sendMessage(to, 'Add to TalkBan')
                                    except:
                                        pass
                elif msg.text.lower().startswith("???????????? "):
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
                                        del apalo["Talkblacklist"][ls]
                                        maxgie.sendMessage(to, 'Deleted from TalkBan')
                                    except:
                                        pass
                elif text.lower() == "???????????????":
                            if apalo["Talkblacklist"] == {}:
                              maxgie.unsendMessage(msg_id)
                              duc1(to, "?????????????????????????????????????????????????????")
                            else:
                              ma = ""
                              a = 0
                              for m_id in apalo["Talkblacklist"]:
                                  a = a + 1
                                  end = '\n'
                                  ma += str(a) + ". " +maxgie.getContact(m_id).displayName + "\n"
                              duc1(to,"?????????????????????????????????????????? :\n\n"+ma+"\n??????????????? %s ?????????????????????" %(str(len(apalo["Talkblacklist"]))))
#=====================================================================                
                if text.lower() == "???????????????????????????":
                  if msg._from in admin:
                      settings["autoblock"] = True
                      sa = "???????????????????????? (?????????????)"
                  else:
                      sa = "???????????????????????????????????? (?????????????)"
                  duc1(to, sa)
                if text.lower() == "????????????????????????":
                  if msg._from in admin:
                      settings["autoblock"] = False
                      duc1(to,"????????????????????? (?????????????)")
                  else:
                      duc1(to,"????????????????????????????????? (?????????????)")
                if text.lower() == "?????????????????????":
                    tagadd["tags"] = True
                    sa = "??????????????????????????? >_<"
                    duc1(to,str(sa))
                if text.lower() == "??????????????????":
                    tagadd["tags"] = False
                    sa = "????????????????????? >_<"
                    duc1(to,str(sa))
                if text.lower() == "??????????????????????????????":
                    settings["autoCancel"]["on"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                if text.lower() == "???????????????????????????":
                    settings["autoCancel"]["on"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????????????????????????????????????????????")
                if text.lower() == "?????????????????????????????????":
                  if msg._from in maxgieMID:
                      kcn["autojoin"] = True
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "????????????????????????? (????????????) ??????????????????????")
                  else:
                      maxgie.sendMessage(msg.to,"??? Status Autoleave ???\n??????????????????????????????????????????????????????????????????????????????????????????")
                if text.lower() == "??????????????????????????????":
                  if msg._from in maxgieMID:
                      kcn["autojoin"] = False
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "????????????????????????? (?????????) ??????????????????????")
                  else:
                      maxgie.sendMessage(msg.to,"??? Status Autoleave ???\n??????????????????????????????????????????????????????????????????????????????????????????") 
                if text.lower() == "?????????????????????":
                    settings["autoAdd"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "????????????????????????????????????????????????????????")
                if text.lower() == "??????????????????":
                    settings["autoAdd"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????")
                if text.lower() == "?????????????????????":
                   sets["l"] = False
                   maxgie.unsendMessage(msg_id)
                   duc1(to, "?????????????????????????????????????????")
                if text.lower() == "????????????????????????":
                   sets["l"] = True
                   maxgie.unsendMessage(msg_id)
                   duc1(to, "????????????????????????????????????????????")
                if text.lower() == "?????????????????????2":
                    tagadd["tagss"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????2???????????????????????????????")
                if text.lower() == "??????????????????2":
                    tagadd["tagss"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????2???????????????????????????????")
                if text.lower() == "?????????????????????????????????":
                    settings["com"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "????????????????????????????????????????????????????????????????????")
                if text.lower() == "??????????????????????????????":
                    settings["com"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                if text.lower() == "?????????????????????????????????":
                    settings["Welcome"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "????????????????????????????????????????????????????????????????????")
                if text.lower() == "??????????????????????????????":
                    settings["Welcome"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                if text.lower() == "?????????????????????????????????2":
                    settings["Wc"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????2???????????????????????????????")
                if text.lower() == "??????????????????????????????2":
                    settings["Wc"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????????????????2???????????????????????????????")
                if text.lower() == "???????????????????????????":
                    settings["Leave"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????????????????????????????????????????????")
                if text.lower() == "????????????????????????":
                    settings["Leave"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "???????????????????????????????????????????????????????????")
                if text.lower() == "??????????????????????????????":
                    settings["unsendMessage"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                if text.lower() == "???????????????????????????":
                    settings["unsendMessage"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????????????????????????????????????????????")
                if text.lower() == "????????????????????????????????????":
                    settings["Sticker"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "???????????????????????????????????????????????????????????????????????")
                if text.lower() == "?????????????????????????????????":
                    settings["Sticker"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "????????????????????????????????????????????????????????????????????")
                if text.lower() == "????????????????????????????????????":
                    sets["Sticker"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "???????????????????????????????????????????????????????????????????????")
                if text.lower() == "?????????????????????????????????":
                    sets["Sticker"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "????????????????????????????????????????????????????????????????????")
                if text.lower() == "?????????????????????3":
                    sets["tagsticker"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????3???????????????????????????????")
                if text.lower() == "??????????????????3":
                    sets["tagsticker"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????3???????????????????????????????")
                if text.lower() == "???????????????????????????????????????":
                    settings["lv"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????????????????????????????????????????????????????????")
                if text.lower() == "????????????????????????????????????":
                    settings["lv"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "???????????????????????????????????????????????????????????????????????")
                if text.lower() == "??????????????????????????????????????????":
                    settings["wcsti2"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????????????????")
                if text.lower() == "???????????????????????????????????????":
                    settings["wcsti2"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????????????????????????????????????????????????????????")
                if text.lower() == "?????????????????????????????????":
                    sets["autoJoinTicket"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "????????????????????????????????????????????????????????????????????")
                if text.lower() == "??????????????????????????????":
                    sets["autoJoinTicket"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
#==============================================================================#
                elif msg.text in ["????????????????????????"]:
                    try:
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        maxgie.sendMessage(to, "????????????????????????????????????????????????????????\n\n??????????????????????????: "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n???????????????????? [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                        del cctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    maxgie.sendMessage(msg.to,"?????????????????????????????????????????????????????????????????????????????????")

                elif msg.text == "?????????????????????":
                  if msg.to in RfuCctv['point']:
                      tz = pytz.timezone("Asia/Jakarta")
                      timeNow = datetime.now(tz=tz)
                      RfuCctv['cyduk'][msg.to]=False
                      maxgie.sendMessage(to, "?????????????????????????????????????????????????????\n\n???????????????????????? : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n???????????????????? [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                  else:
                      maxgie.sendMessage(to, "Sudak tidak aktif")                    
#==============================================================================#
                elif text.lower() == 'speed':start = time.time();maxgie.sendMessage("ubd86e8c77559b1493f0ad64b1dba2d6c", "??????????????????????????????????????????????????????????");elapsed_time = time.time() - start;duc1(to, "Speed : %s second"%str(round(elapsed_time,4)))
                
                elif msg.text.lower().startswith("?????????????????? "):
                            txt = removeCmd("??????????????????", text)
                            groups = maxgie.getGroupIdsJoined()
                            url = 'https://nekos.life/api/v2/img/ngif'
                            text1 = requests.get(url).text
                            image = json.loads(text1)['url']
                            for group in groups:
                                sa = " ?????????????????? \n\n{}".format(str(txt))
                                data = {
"type":"flex",
"altText":"???????????????????????????",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FF9933"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FF9933"},
"footer": {"backgroundColor": "#0033FF", "separator": True, "separatorColor": "#FF9933"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "????????????????????????????????????? ????",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#8B0000",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"type": "image"
},
{
"type": "separator",
"color": "#000000"
},
{
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
},
{
"contents": [
{
"text": sa,
"size": "md",
"align": "center",
"color": "#8B0000",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#8B0000"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": sa,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#000000",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"type": "icon",
"size": "md"
},
{
"text": " ??? ???????????????????????? : \n ??? ??????????????????????????????????????????????????????????",
"size": "xs",
"margin": "none",
"color": "#8B0000",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#8B0000",
"height": "sm",
"action": {
"type": "uri",
"label": "??????????????????????????????????????????????????????????",
"uri": "https://line.me/ti/p/~boy-5566",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#8B0000",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "??????????????????????????????????????????",
"uri": "https://line.me/ti/p/~boy-5566",
}
}
]
}
}
]
}
}
                                sendTemplate(group, data)
                                time.sleep(1)
                            maxgie.sendMessage(to, "????????????????????????????????????????????????  {} ???????????????".format(str(len(groups))))
                elif msg.text.lower().startswith("//??????????????????"):
                            contact = maxgie.getContact(sender) 
                            groups = maxgie.getGroupIdsJoined()
                            for group in groups:
                                dataProfile = [ 
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FF0033'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "???{???????????????????????????????}???",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#FF0033"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/03/28/1553773108509.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~nonbysignal"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/F6FBB34A-3B96-41A7-944D-E17454BC6F25.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/1553451636487.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "self bot python3",
                                                  "color": "#FF0033",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "???????????? 100 ?????????/???????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "?????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "???????????? 200 ?????????",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "???????????????????????????????????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "??????????????????????????????",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~nonbysignal",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                       }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FF0033'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "???{???????????????????????????????}???",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#FF0033"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/03/28/1553773108509.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~nonbysignal"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/D88BDCD7-3CFC-4BD9-BE86-210B7A22CD3C.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/1553451634501.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "??????????????????????????? ?????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "????????????????????????????????????????????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "???????????????????????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "????????????????????????????????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "????????????????????????????????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "??????????????????????????????",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~nonbysignal",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FF0033'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "???{???????????????????????????????}???",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#FF0033"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/03/28/1553773108509.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~nonbysignal"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/2832_20180721151831.png",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://i.dlpng.com/static/png/75778_thumb.png",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "?????????????????????/?????????/?????????/??????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "???????????????????????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "??????????????????????????????????????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "????????????????????????????????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "???????????????????????????????????????????????????",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "??????????????????????????????",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~nonbysignal",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                ]
                                data = {
                                    "type": "flex",
                                    "altText": "??????????????????????????????",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(1)
                            maxgie.sendMessage(to, "????????????????????????????????????????????????  {} ???????????????".format(str(len(groups))))
#==============================================================================#
                elif text.lower() == "?????????":
                        group = maxgie.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(maxgie.getProfile().mid)
                        maxgie.datamention(to,'????????????????????????',nama)
                elif text.lower() == "/?????????" or text.lower() == "tagall":
                    if msg._from in maxgieMID:
                        group = maxgie.getGroup(msg.to)
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
                elif msg.text.lower().startswith("???????????????1 "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya ="http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya +"&chts=ff3333,70&chf=bg,s,ff3333"
                    maxgie.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("??????????????? "):
                    sep = text.split(" ")
                    textnya = text.replace(sep[0] + " ", "")
                    text = "{}".format(textnya)
                    contact = maxgie.getContact(maxgieMID)
                    data = {
                        "type": "flex",
                        "altText": "??????????????????",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#1C1C1C'
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
                                        "color":"#8B0000",
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
                elif msg.text.lower().startswith("????????? "):
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
                                       maxgie.findAndAddContactsByMid(ls)
                                       maxgie.inviteIntoGroup(to, [ls])
                                    except:
                                       duc1(to, "Limited !")
                elif msg.text.lower().startswith("????????????"):
                  if msg.toType == 2:
                    data = text.replace("???????????? ","")
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
                            maxgie.unsendMessage(msg_id)
                            maxgie.sendMessage(to, yud,contentMetadata={"MSG_SENDER_NAME": str(maxgie.getContact(ls).displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/%s" % maxgie.getContact(ls).pictureStatus})
                elif text.startswith("??????????????? "):
                   a = maxgie.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+maxgie.adityasplittext(text,'s')+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                   if a["items"] != []:
                       no = 0
                       ret_ = []
                       for music in a["items"]:
                           no += 1
                           ret_.append({"type": "bubble","styles": {"header": {"backgroundColor": "#0033FF", "separator": True, "separatorColor": "#FFFFFF"},"body": {"backgroundColor": "#0033FF", "separator": True, "separatorColor": "#FFFFFF"},"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},},"header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Youtube","weight": "bold","color": "#FFFFFF","size": "sm"}]},"hero": {"type": "image","url": 'https://i.ytimg.com/vi/{}/maxresdefault.jpg'.format(music['id']['videoId']),"size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "??????????????????","color": "#FFFFFF","size": "sm","flex": 1},{"type": "text","text": "{}".format(music['snippet']['title']),"color": "#FFFFFF","wrap": True,"size": "sm","flex": 5}]}]}]},"footer": {"type": "box","layout": "horizontal","spacing": "sm","contents": [{"type": "button","flex": 2,"style": "primary","color": "#EE1289","height": "sm","action": {"type": "uri","label": "????MP4????","uri": "{}??????????????????%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},{"type": "button","flex": 2,"style": "primary","color": "#EE1289","height": "sm","action": {"type": "uri","label": "????MP3????","uri": "{}???????????????%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},],}})
                       k = len(ret_)//10
                       for aa in range(k+1):
                           data = {"messages": [{"type": "flex","altText": "???????????????","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                           maxgie.sendMessage(to,data)
                   else:
                      maxgie.sendMessage(to,"Type: Search Youtube Video\nStatus: "+str(self.adityasplittext(msg.text,'s'))+" not found")
                
                elif msg.text.lower().startswith("image "):
                                query = removeCmd("image", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("?????????????????? "):
                                query = removeCmd("??????????????????", text)
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
                elif msg.text.lower().startswith("????????? "):
                                query = removeCmd("?????????", text)
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
                                        
                 #=====================================================================

                elif msg.text.lower().startswith("??????????????????"):
                                if msg._from in maxgieMID:                                
                                    if msg.toType == 2:
                                        group = maxgie.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//20
                                        maxgie.sendMessage(msg.to,"[ ?????????????????????????????? ??????????????? {} ??????] \n???????????????????????????...".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*20 : (i+1)*20]:
                                                time.sleep(random.uniform(0.5,0.4))
                                                maxgie.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            maxgie.sendMessage(receiver,"????????????????????????????????????????????????????????????? 20 ??????\n ???.????????????????????????????????????????????????????????????? ")
                                            time.sleep(random.uniform(15,10))
                                        maxgie.sendMessage(receiver,"[ ?????????????????????????????? ??????????????? {} ?????? ???????????????????????????????????????????]".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        maxgie.sendMessage(receiver, None, contentMetadata={"STKID": "52002735","STKPKGID": "11537","STKVER": "1" }, contentType=7)
                                        gname = line.getGroup(receiver).name
                                        maxgie.sendMessage(Notify,"[ ?????????????????????????????? >> "+gname+"  <<] \n ??????????????? {} ?????? ???????????????????????????????????????????\n????????????????????????????????????????????????????????????????".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        maxgie.leaveGroup(receiver)
                                								
                                    maxgie.sendMessage(receiver,"[??????????????????????????????????????? ??????????????????????]")
                                    maxgie.sendMessage(receiver, None, contentMetadata={"STKID": "52114123","STKPKGID": "11539","STKVER": "1" }, contentType=7)
                                    maxgie.leaveGroup(receiver)
                #=====================================================================              
                elif msg.text.lower().startswith("?????????????????? "):
                   args = msg.text.lower().replace("?????????????????? ","")
                   mes = 0
                   try:
                       mes = int(args[1])
                   except:
                       mes = 100
                       M = maxgie.getRecentMessagesV2(to, 100)
                       MId = []
                       for ind,i in enumerate(M):
                           if ind == 0:
                               pass
                           else:
                               if i._from == maxgie.profile.mid:
                                   MId.append(i.id)
                                   if len(MId) == mes:
                                       break
                       def unsMes(id):
                           maxgie.unsendMessage(id)
                       for i in MId:
                           thread1 = threading.Thread(target=unsMes, args=(i,))
                           thread1.start()
                           thread1.join()
                       duc1(to, ' ??? ????????????????????????????????? ???\n??????????????????????????????????????? {} ?????????????????????'.format(len(MId))) 
                       maxgie.unsendMessage(msg_id) 
#----------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text.lower().startswith("????????????????????? "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
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
#                                maxgie.sendMessage(to, "????????????????????????????????????????.?????????????".format(str(jml)))
                                maxgie.sendMessage(receiver, "???.???.??????.???.??????.???.?????????.???.???.??????.???.~.???????.???.???.???.???.???.???.??????.???.??????.???.???.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.b.y.???.???.??????.???.~.???.????.????.????.")
#                                maxgie.sendMessage(to, "???????????? ???.??? ????????????".format(str(jml)))
                elif msg.text in ["/???????????????"]:
                    maxgie.sendMessage(msg.to, "???.???.??????.???.??????.???.?????????.???.???.??????.???.~.???????.???.???.???.???.???.???.??????.???.??????.???.???.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.???.K.1.t.t.y.b.y.???.???.??????.???.~.???.????.????.????.")
                    maxgie.sendMessage(msg.to, "???.???.??????.???.???.???.??????.???.????????????????????????????????????~???????.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q???.Q4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.????????????????????????")
                    maxgie.sendMessage(msg.to, "????.???.???.??????.???.???.???.??????.???.????.??? .???.???.???.???.???.???.??????.??????.&???.???.??????.???.??????.???.??????.???.~.????.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4???.???.??????.???.???.?????????.???.?????????.???.?????????.???.b.y.???.???.??????.???.~.???.????.????.????")
                    maxgie.sendMessage(msg.to, "????????????????????????????????????????????????????????????????????????????????????~???????????????????????????????.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.???.4.?????????????????????????????? by.???????????????~???????")
                    maxgie.sendMessage(msg.to, "????.???.???.??????.???.???.???.??????.???.????.??? .???.???.???.???.???.???.??????.??????.&???.???.??????.???.??????.???.??????.???.~.????.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4???.???.??????.???.???.?????????.???.?????????.???.?????????.???.b.y.???.???.??????.???.~.???.????.????.????")
                    maxgie.sendMessage(msg.to, "????.???.???.??????.???.???.???.??????.???.????.??? .???.???.???.???.???.???.??????.??????.&???.???.??????.???.??????.???.??????.???.~.????.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4???.???.??????.???.???.?????????.???.?????????.???.?????????.???.b.y.???.???.??????.???.~.???.????.????.????")
                    maxgie.sendMessage(msg.to, "????.???.???.??????.???.???.???.??????.???.????.??? .???.???.???.???.???.???.??????.???.??????.???.???.??????.???.????.????.????1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.???.?????????.???.???.?????????.???.?????????.???.?????????.???.b.y.???.???.??????.???.~.???.????.????.????.")
                    maxgie.sendMessage(msg.to, "???.???.??????.???.???.???.??????.???.????????????????????????????????????~???????.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q???.Q4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.Q.4.???.????????????????????????")
                    maxgie.sendMessage(msg.to, "????????????????????????????????????????????????\n  ???????????? ????????????????????????????????????????????????????????? ????????????\n????????????????????????????????????????????")                                                             
#=====================================================================                                       
                
                
                elif msg.text.lower().startswith("????????????????????????????????? "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.findAndAddContactsByMid(ls)
                                maxgie.generateReplyMessage(msg.id)
                                duc1(id, to, "Success add " + str(contact.displayName) + " to Friendlist")
                elif msg.text.lower().startswith("???????????????????????? "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    n = len(maxgie.getAllContactIds())
                                    try:
                                        maxgie.deleteContact(ls)
                                    except:pass
                                    t = len(maxgie.getAllContactIds())
                                    maxgie.generateReplyMessage(msg.id)
                                    duc1(id, to, "Type: Friendlist\n ??? Detail: Delete friend\n ??? Status: Succes..\n ??? Before: %s Friendlist\n ??? After: %s Friendlist"%(n,t))
                elif msg.text.lower().startswith("??????????????? "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.blockContact(ls)
                                maxgie.generateReplyMessage(msg.id)
                                duc1(id, to, "Success add " + str(contact.displayName) + " to Blocklist")
                elif msg.text.lower().startswith("???????????????????????? "):
                            a = removeCmd("????????????????????????", text)
                            b = maxgie.findContactsByUserid(a)
                            line = b.mid
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "line://ti/p/~" + a)
                            maxgie.sendContact(to, line)                                                                                           
                            maxgie.sendMessage(to,str(hasil))
                elif msg.text.lower().startswith("stag "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
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
                                contact = maxgie.getContact(receiver)
                                RhyN_(to, contact.mid)
                elif "/???????????????" in msg.text.lower():
                    spl = re.split("/???????????????",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = maxgie.getGroupIdsInvited()
                        txt = "???????????????????????????????????????????????????????????????????????? "+str(len(ag))+" ???????????????"
                        if spl[1] != "":
                            txt = txt + " ????????????????????????????????? \""+spl[1]+"\""
                        txt = txt + "\n??????????????????????????????????????????.."
                        data = {"type": "text","text": "{}".format(str(txt)),"sentBy": {"label": "{}".format(maxgie.getContact(maxgieMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ube3faf73d9f1d8388b472b576328ec21"}}
                        sendTemplate(to, data)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                maxgie.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    maxgie.sendMessage(gr,spl[1])
                                time.sleep(random.uniform(0.65,0.6))    
                                maxgie.leaveGroup(gr)
                            except:
                                pass
                        sis = "?????????????????????????????? (?????????????)"
                        data = {"type": "text","text": "{}".format(str(sis)),"sentBy": {"label": "{}".format(maxgie.getContact(maxgieMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ube3faf73d9f1d8388b472b576328ec21"}}
                        sendTemplate(to, data)
            
#=====================================================================
#==============================================================================#
                elif text.lower() == '????????????????????????????????????' or text.lower() == "?????????":
                    group = maxgie.getGroup(to)
                    cg = group.creator
                    c = cg.mid
                    name = cg.displayName
                    pp = cg.pictureStatus
                 #   profile = "https://profile.line-scdn.net/" + str(pp)
                    data = {
                        "type": "flex",
                        "altText": "????????????????????????",
                        "contents": {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": "??????????????????????????????????????????????????????????",
                                        "size":"md",
                                       # "weight":"bold",
                                        "color":"#FF3333",
                                        "align":"center"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://profile.line-scdn.net/" + str(pp),
                                        "size": "xl"
                                    },
                                    {
                                        "type":"text",
                                        "text":" "
                                    },
                                    {
                                       "type":"text",
                                       "text": name,
                                       "color":"#FF3333",
                                       "align":"center",
                                       "size":"xl",
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                    maxgie.sendContact(to, c)
                elif text.lower() == '???????????????????????????':
                    gid = maxgie.getGroup(to)
                  #  
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "{ Group ID }\n" + gid.id)
                    maxgie.sendMessage(to, maxgie.getGroup(to).name, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+maxgie.getGroup(to).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~', 'type': 'mt', 'subText': "??????????????????????????????????????????????????????????", 'a-installUrl': 'https://line.me/ti/p/~', 'a-installUrl': ' https://line.me/ti/p/~', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~', 'i-linkUri': 'https://line.me/ti/p/~', 'id': 'mt000000000a6b79f9', 'text': '??????????????????????????????????????????????????????????', 'linkUri': 'https://line.me/ti/p/~'}, contentType=19)
                elif text.lower() == '????????????????????????':
                    group = maxgie.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    maxgie.sendImageWithURL(to, path)
                elif text.lower() == '???????????????????????????':
                    gid = maxgie.getGroup(to)
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????????? -> \n" + gid.name) 
                elif text.lower() == '????????????':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = maxgie.reissueGroupTicket(to)
                            maxgie.sendMessage(to, "???????????????????????????????????? : "+group.name+"\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == '????????????????????????':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == False:
                           maxgie.unsendMessage(msg_id)
                           duc1(to, "???????????????????????????????????????????????????????????")
                        else:
                            group.preventedJoinByTicket = False
                            maxgie.updateGroup(group)
                            maxgie.sendMessage(to, "???????????????????????????????????????????????????")
                elif text.lower() == '?????????????????????':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == True:
                           maxgie.unsendMessage(msg_id)
                           duc1(to, "????????????????????????????????????????????????????????")
                        else:
                            group.preventedJoinByTicket = True
                            maxgie.updateGroup(group)
                            maxgie.sendMessage(to, "????????????????????????????????????????????????")
                elif text.lower() == '?????????????????????????????????':
                    group = maxgie.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "????????????????????????????????????????????????????????????"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "?????????"
                        gTicket = "?????????????????????????????????????????????????????????"
                    else:
                        gQr = "????????????"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(maxgie.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "?????????[ ??????????????????????????????????????????????????? ]"
                    ret_ += "\n??? ???????????????????????????????????? : {}".format(str(group.name))
                    ret_ += "\n??? ???????????????????????????????????? : {}".format(group.id)
                    ret_ += "\n??? ??????????????????????????????????????? : {}".format(str(gCreator))
                    ret_ += "\n??? ????????????????????????????????? : {}".format(str(len(group.members)))
                    ret_ += "\n??? ??????????????????????????????????????? : {}".format(gPending)
                    ret_ += "\n??? ???????????????????????????????????? : {}".format(gQr)
                    ret_ += "\n??? ??????????????????????????????? : {}".format(gTicket)
                    ret_ += "\n?????????????????????????????????????????????????????????????????????????"
                    data = {
                        "type": "flex",
                        "altText": "???????????????",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#FF9933'
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
                                        "color": "#8B0000",
                                        "wrap": True,
                                        "size": "md",
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                    maxgie.sendImageWithURL(to, path)
                elif text.lower() == '????????????????????????':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        ret_ = "?????????????????????????????????????????????????????????????????????\n"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n\n??????????????? {} ??????".format(str(len(group.members)))
                        data = {
                            "type": "flex",
                            "altText": "???????????????",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                        "backgroundColor": '#3300CC'
                                    },
                                },
                                   "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
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
                                            "text": ret_,
                                            "color": "#000000",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                elif text.lower() == '????????????????????????????????????':
                        groups = maxgie.groups
                        ret_ = "????????????????????????????????????????????????????????? :\n"
                        no = 0 + 1
                        for gid in groups:
                            group = maxgie.getGroup(gid)
                            ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n\n??????????????? {} ???????????????".format(str(len(groups)))
                        data = {
                            "type": "flex",
                            "altText": "Group list",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                         "backgroundColor": '#3300CC'
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type":"text",
                                            "text": ret_,
                                            "color": "#000000",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                elif "????????????????????? " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.displayName = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Update to :\n" + string)
                        print ("Update Name")

                elif "?????????????????? " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.statusMessage = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Succes Update :\n" + string)
                        print ("Update Bio Succes")
                        
                elif text.lower() == "???????????????????????????":
                    sets["changePictureProfile"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??????????????????????????????????????????????????????????????????????????????????????")
                elif text.lower() == "?????????????????????????????????":
                    if msg.toType == 2:
                        if to not in sets["changeGroupPicture"]:
                            sets["changeGroupPicture"].append(to)
                        maxgie.unsendMessage(msg_id)
                        duc1(to, "??????????????????????????????????????????????????????????????????????????????????????")
            
                elif text.lower() == '??????????????????':
                    contactlist = maxgie.getAllContactIds()
                    kontak = maxgie.getContacts(contactlist)
                    num=1
                    msgs="????????????????????????????????????????????????????????????????????????"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n????????????????????????????????????????????????????????????????????????\n\n??????????????????????????????????????? : %i" % len(kontak)
                    maxgie.sendMessage(msg.to, msgs)
            #      if msg.toType == 2:                
#
             #              ginfo = line.getGroup(receiver)
             #              try:
             #                  gcmid = ginfo.creator.mid
             #              except:
             #                  gcmid = "Error"
             #              if settings["lang"] == "JP":
             #                  line.inviteIntoGroup(receiver,[gcmid])
             #                  line.sendMessage(receiver, "????????????????????????????????????????????????")
             #              else:
             #                  line.inviteIntoGroup(receiver,[gcmid])
             #                  line.sendMessage(receiver, "?????????????????????????????????????????????????????????????????????")
                                
#====================================================================
                elif msg.text.lower()== "???????????????????????????????????????":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "tag"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                elif msg.text.lower() == "?????????????????????????????????":
                    sets["messageSticker"]["listSticker"]["tag"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                elif msg.text.lower()== "??????????????????????????????????????????":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "wc"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                elif msg.text.lower() == "????????????????????????????????????":
                    sets["messageSticker"]["listSticker"]["wc"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "????????????????????????????????????????????????????????????????????")
                elif msg.text.lower()== "???????????????????????????????????????":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "lv"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                elif msg.text.lower() == "?????????????????????????????????":
                    sets["messageSticker"]["listSticker"]["lv"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                elif msg.text.lower()== "???????????????????????????????????????":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "add"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                elif msg.text.lower() == "?????????????????????????????????":
                    sets["messageSticker"]["listSticker"]["add"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????")
                elif msg.text.lower() == "?????????????????????????????????????????????":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "join2"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "?????????????????????????????????????????????????????????????????????????????")
                elif msg.text.lower() == "???????????????????????????????????????":
                    sets["messageSticker"]["listSticker"]["join2"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "???????????????????????????????????????????????????????????")
                    
#=====================================================================
            elif msg.contentType == 1:
                if sets["changePictureProfile"] == True:
                    path = maxgie.downloadObjectMsg(msg_id)
                    sets["changePictureProfile"] = False
                    maxgie.updateProfilePicture(path)
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "????????????????????????????????????????????????????????????????????")
                    
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "??? Check Sticker ???\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            maxgie.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            maxgie.sendMessage(to, str(ret_))
                        except Exception as error:
                            maxgie.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in maxgieMID:
                            try:
                                maxgie.kickoutFromGroup(msg.to,[sender])
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "???????????????????????????????????????????????????????????????????????????????????")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = maxgie.findGroupByTicket(ticket_id)
                                maxgie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                maxgie.sendMessage(group.id,str(tagadd["m"]))
                            #    msgSticker = sets["messageSticker"]["listSticker"]["join2"]
                            #    if msgSticker != None:
                            #        sid = msgSticker["STKID"]
                            #        spkg = msgSticker["STKPKGID"]
                            #        sver = msgSticker["STKVER"]
                            #        sendSticker(group.id, str(sver), str(spkg), str(sid))
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "???????????????????????????????????????????????????? %s ??????????????????????????? 555????" % str(group.name))
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            maxgie.sendMessage(to, "Success Sticker " + name + " Done...")
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        maxgie.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
            elif msg.contentType == 7:
                if sets["Sticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "?????????[ Sticker Info ]"
                    ret_ += "\n??? STICKER ID : {}".format(stk_id)
                    ret_ += "\n??? STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n??? STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n??? STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n?????????[ Finish ]"
                    maxgie.sendMessage(to, str(ret_))
#=====================================================================
        if op.type == 22:
            if did["join"] == True:
                maxgie.leaveRoom(op.param1)              
        if op.type == 24:
            if did["join"] == True:
                maxgie.leaveRoom(op.param1)
#========================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
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
                if text.lower() == ".":
                    duc1(to, "[Admin]\n??????????????????????????????????????????????????????????") 
#========================================================================
            elif msg.contentType == 7: # Content type is sticker
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ???????????????????????????????????????','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ???????????????????????????????????????','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
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
                if msg.toType == 0 and sender != maxgieMID: to = sender
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
            #                    group = maxgie.findGroupByTicket(ticket_id)
            #                    maxgie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                #
             #                   maxgie.sendMessage(to, "????????????????????????????????????????????????????????? %s ???? ???????????????????????????????????????" % str(group.name))
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if tagadd["tags"] == True:
                             me = maxgie.getContact(sender)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in maxgieMID:
                                          cover = maxgie.getProfileCoverURL(sender)
                                          pp = me.pictureStatus
                                          profile = "https://profile.line-scdn.net/" + str(pp)
                                          name = me.displayName
                                          status = "\n??????????????????\n" + me.statusMessage
                                          pk = str(tagadd["tag"])
                                          tz = pytz.timezone("Asia/Jakarta")
                                          timeNow = datetime.now(tz=tz)
                                          van2 = "???????????????:"+ datetime.strftime(timeNow,'%H:%M:%S')                                 	
                                          data = {
"type":"flex",
"altText": pk, 
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#3300CC"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#3300CC"}
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#8B0000"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#8B0000"
},
{
"contents": [
{
"text": name,
"size": "sm",
"align": "center",
"color": "#8B0000",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": pk, 
"align": "center",
"size": "sm",
"weight": "bold",
"color": "#8B0000",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"text": " ?????? ????????????????????? :"+van2 +" \n ?????? ??????????????????????????????????????????????????????????",
"size": "xs",
"margin": "none",
"color": "#8B0000",
"wrap": True,
"weight": "regular",
"type": "text"
}
]
}
}
]
}
}                                          
                                          sendTemplate(to, data)                        
        if op.type == 26:
            print ("[Self Bot ?????????????????????????????????????????????????????????? ] ")
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
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                    #  contact = maxgie.getContact(maxgieMID)
                                   #   a = contact.displayName
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' ???????????????????????????????????????','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'???????????????????????????????????????','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
#==============================================================================#
        if op.type == 19:
            if maxgieMID in op.param3:
                apalo["Talkblacklist"][op.param2] = True
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
               if mc["wr"][str(msg.text)]:
                   maxgie.sendMessage(msg.to,mc["wr"][str(msg.text)])
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
                    if sender != maxgie.profile.mid:
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
                if msg.text.lower().startswith("?????????????????? "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    maxgie.sendContact(msg.to,str(getx))
                if msg.text.startswith("????????????api "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        mc["wr"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                        maxgie.sendMessage(msg.to,"??????????????????????????????: " + str(kw) + "\n?????????????????????: "+ str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("????????????api "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del mc["wr"][getx]
                        maxgie.sendMessage(msg.to, "?????? " + str(getx) + " ????????????????????????")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "?????????api":
                    lisk = "[ ????????????????????????????????????????????? ]\n"
                    for i in mc["wr"]:
                        lisk+="\n??????????????????????????????: "+str(i)+"\n??????????????????: "+str(mc["wr"][i])+"\n"
                    lisk+="\n????????????????????????api >\\<\n????????????api ??????????????????????????????????????????????????????"
                    data = {"type": "text","text": "{}".format(lisk),"sentBy": {"label": "list API", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~boy-5566"}}
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
                if sender != maxgie.profile.mid:
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
                            maxgie.sendMessage(to, "Success Added " + name)
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
                if msg.toType == 0 and sender != maxgieMID: to = sender
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
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
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
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = maxgie.getContact(msg_dict[msg_id]["from"])
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
                                maxgie.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    maxgie.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        maxgie.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            maxgie.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                maxgie.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    maxgie.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        maxgie.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")
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
                           maxgie.sendMessage(to,"Bot Actived")
                        return
                      elif time.time() - temp_flood[receiver]["time"] <= 5:
                         temp_flood[receiver]["flood"] += 1
                         if temp_flood[receiver]["flood"] >= 200:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "??????????????????????????????????????????????????????????200?????????????????????????????????????????????????????????????")
                            maxgie.leaveGroup(to)
                      else:
                       temp_flood[receiver]["flood"] = 0
                      temp_flood[receiver]["time"] = time.time()
                    else:
                      temp_flood[receiver] = {
                       "time": time.time(),
                       "flood": 0,
                       "expire": False
}
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = maxgie.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n????" + Name
                            pref=['????????????????????????????????????']
                            maxgie.sendMessage(op.param1, str(random.choice(pref))+' '+Name)
                            maxgie.sendContact(op.param1, op.param2)
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
                        Name = maxgie.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n??? " + Name + "\n??????????????????????????????????????????????????????"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	maxgie.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                                        
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            NOTIFIED_READ_MESSAGE(op)
    except Exception as error:
        logError(error)

#==============================================================================#
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        try:
            ops = maxgiePoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(maxgieBot(op))
                   maxgiePoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()
