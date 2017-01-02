#!/usr/bin/env python
#encoding=utf-8
import pyaudio
import wave
import urllib, urllib2, pycurl
import base64
import json
import sys
import StringIO
sys.path.append("..")
import setting

TOKEN = setting.get_token()

def identify():
    fp = wave.open('Temp/output.wav', 'rb')
    nf = fp.getnframes()
    print fp.getparams()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    srv_url = setting.SRV_URL + setting.get_token()
    http_header = [
        'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % f_len
    ]
    b = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url))
    c.setopt(c.HTTPHEADER, http_header)
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, b.write)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform()
    response = ''.join(json.loads(b.getvalue())['result']).encode("UTF-8")
    return response