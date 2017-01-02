#!/usr/bin/env python
#encoding=utf-8

import os
import time
import json
import urllib, urllib2
import sys

#TULING_GLOBAL
TULING_KEY = 'cd2767a03612491b89e40b2f07d0a9d3'
TULING_API = 'http://www.tuling123.com/openapi/api?key=' + TULING_KEY + '&info='

#BAIDU_GLOBAL
BAIDU_APP_ID='9152340'
BAIDU_APP_KEY='Oguw8LNsBK16QTsylkHgiUxu'
BAIDU_SECRET_KEY='e396a1424d6ddbe72e935a3e96c35593'
BAIDU_CUID = 'C02S19SUFVH3' #mac序列号

#BAIDU_RECORD
CHUNK = 1024
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 5

#BAIDU_PLAY
PLAY_API = 'http://tsn.baidu.com/text2audio?tex='
LAN = 'zh'
CTP = '1'
PER = '4'

#BAIDU_IDENTIFY
SRV_URL = 'http://vop.baidu.com/server_api?cuid=' + BAIDU_CUID + '&token='

#BAIDU_TOKEN
TOKEN_PATH = './Temp/speech.token'
LOG_PATH = './Temp/log_spx.log'
AUTH_URL = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + BAIDU_APP_KEY + "&client_secret=" + BAIDU_SECRET_KEY;

def has_token():
    try:
        stat_info = os.stat(TOKEN_PATH)
    except OSError:
        return False
    if stat_info.st_size < 10: #invalid if too small
        return False
    db_ctime = stat_info.st_ctime
    create_date = time.strftime('%m', time.localtime(db_ctime))
    current_date = time.strftime('%m', time.localtime(time.time()))
    if current_date != create_date:
        return False
    else:
        return True

def get_token():
    if has_token():
        fp = open(TOKEN_PATH, 'r')
        token = fp.readline().rstrip('\n')
        fp.close()
        return token
    auth_url = AUTH_URL
    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    token = json.loads(json_data)['access_token']
    fp = open(TOKEN_PATH, 'w')
    fp.write(token)
    fp.close()
    return token




