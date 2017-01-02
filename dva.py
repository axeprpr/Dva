#!/usr/bin/env python
#encoding=utf-8
import time
import setting
from BaiduYuyin import Record
from BaiduYuyin import Play
from BaiduYuyin import Identify
from Tuling import Tuling

if __name__ == '__main__':

#调试代码
    #Record.record()
    #Play.play("hello")
    #print Tuling.response("你好")
    #print Identify.identify()


    Record.record()
    info = Identify.identify()
    #print 'axe: '.decode('utf-8') + info
    response = Tuling.response(info)
    print 'dva: '.decode('utf-8') + response
    Play.play(response)
