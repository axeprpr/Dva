#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json

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
        print '机器人: '.decode('utf-8') + dic_json['text'] 
