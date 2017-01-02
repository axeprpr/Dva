#!/usr/bin/env python
#encoding=utf-8
import os
import time
import urllib, urllib2
import base64
import json
import subprocess
import sys

TOKEN_PATH = './speech.token'

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

## get access token by api key & secret key
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
        return False   #old beyond 1 day, need update
    else:
        return True

def get_token():
    if has_token():
        fp = open(TOKEN_PATH, 'r')
        token = fp.readline().rstrip('\n')
        fp.close()
        return token
    apiKey = "Oguw8LNsBK16QTsylkHgiUxu"
    secretKey = "e396a1424d6ddbe72e935a3e96c35593"

    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;

    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    token = json.loads(json_data)['access_token']
    fp = open(TOKEN_PATH, 'w')
    fp.write(token)
    fp.close()
    return token

def dump_res(buf):
    fp = open('log_spx.log', 'w')
    fp.write(buf)
    fp.close()


## post audio to server
# def use_cloud(token):
#     fp = open('test.spx', 'rb')
#     fp.seek(os.SEEK_END)
#     f_len = fp.tell()
#     audio_data = fp.read(f_len)

#     cuid = "acxxxxxx677" #my xiaomi phone MAC
#     srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
#     http_header = [
#         'Content-Type: audio/speex; rate=8000',
#         'Content-Length: %d' % f_len
#     ]

#     c = pycurl.Curl()
#     c.setopt(pycurl.URL, str(srv_url)) #curl doesn't support unicode
#     #c.setopt(c.RETURNTRANSFER, 1)
#     c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict
#     c.setopt(c.POST, 1)
#     c.setopt(c.CONNECTTIMEOUT, 30)
#     c.setopt(c.TIMEOUT, 30)
#     c.setopt(c.WRITEFUNCTION, dump_res)
#     c.setopt(c.POSTFIELDS, audio_data)
#     c.setopt(c.POSTFIELDSIZE, f_len)
#     c.perform() #pycurl.perform() has no return val

# if __name__ == "__main__":
#     token = get_token()
#     #use_cloud(token)

if __name__ == '__main__':
    token = get_token()
    key = 'cd2767a03612491b89e40b2f07d0a9d3'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    while True:
        if len(sys.argv)==2:
            info = sys.argv[1]
        else:
            info = raw_input('axe: ')
        request = api + info
        response = getHtml(request)
        dic_json = json.loads(response)
        print 'dva: '.decode('utf-8') + dic_json['text']
        a = dic_json['text']
        tex = a.encode("UTF-8")
        subprocess.call(["mpg123","http://tsn.baidu.com/text2audio?tex="+tex+"&lan=zh&cuid=C02S19SUFVH3&ctp=1&per=4&tok="+token])
        print "http://tsn.baidu.com/text2audio?tex="+tex+"&lan=zh&cuid=C02S19SUFVH3&ctp=1&per=4&tok="+token
