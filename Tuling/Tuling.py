#!/usr/bin/env python
#encoding=utf-8
import urllib
import json
import sys
sys.path.append("..")
import setting

API = setting.TULING_API

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def response(info):
    request = API + info
    response = getHtml(request)
    dic_json = json.loads(response)
    return dic_json['text']
