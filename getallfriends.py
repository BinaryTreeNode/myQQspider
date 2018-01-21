#coding:utf-8
import requests
import time
import os
from urllib import parse

def get_friends_url(username, g_tk):
        url='https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/right/get_entryuinlist.cgi?'
        params = {"uin": username,
              "fupdate": 1,
              "action": 1,
              "g_tk": g_tk}
        url = url + parse.urlencode(params)
        return url

def get_friends_num(req, headers):
    t=True
    offset=0
    url=get_friends_url()
    while(t):
        url_=url+'&offset='+str(offset)
        page=req.get(url=url_,headers=headers)
        if "\"uinlist\":[]" in page.text:
            t=False
        else:

            if not os.path.exists("./friends/"):
                os.mkdir("friends/")
            with open('./friends/'+str(offset)+'.json','w',encoding='utf-8') as w:
                w.write(page.text)
            offset += 50