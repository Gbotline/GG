# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re

class Config(object):
    LINE_HOST_DOMAIN            = 'https://legy-jp-addr.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://legy-jp-addr.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://legy-jp-addr.line.naver.jp/mh'

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_TYPE    = "DESKTOPMAC"
    APP_VER     = '6.5.2'
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'BotBasX'
    SYSTEM_VER  = '10.15.1'
    IP_ADDR     = '1.1.1.1'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self):
        self.APP_NAME = 'DESKTOPMAC\t6.5.2\tMAC\t10.15.1'
        self.USER_AGENT = 'Line/%s' % self.APP_VER
