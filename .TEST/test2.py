#!/usr/bin/env python
#encoding=utf-8
import urllib
import json
import PyBaiduYuyin as pby

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

if __name__ == '__main__':
    key = 'cd2767a03612491b89e40b2f07d0a9d3'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='  
    while True:
        info = raw_input('axe: ')
        request = api + info
        response = getHtml(request)
        dic_json = json.loads(response)
        print 'dva: '.decode('utf-8') + dic_json['text']
        tts = pby.TTS(app_key='Oguw8LNsBK16QTsylkHgiUxu',secret_key='e396a1424d6ddbe72e935a3e96c35593',per=1)
        a = dic_json['text']
        tts.say(a.encode("UTF-8"))
