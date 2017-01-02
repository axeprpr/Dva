#!/usr/bin/env python
#encoding=utf-8
import subprocess
import sys
sys.path.append("..")
import setting

TOKEN = setting.get_token()
CUID = setting.BAIDU_CUID
PLAY_API = setting.PLAY_API
LAN = setting.LAN
CTP = setting.CTP
PER = setting.PER

def play(text,token=TOKEN):
    text = text.encode("UTF-8")
    subprocess.call(["mpg123",
                     PLAY_API
                    +text
                    +"&lan="+LAN
                    +"&cuid="+CUID
                    +"+&ctp="+CTP
                    +"&per="+PER
                    +"&tok="+token
                    ])
