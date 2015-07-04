# -*- coding:utf-8 -*-

__author__ = 'liuqianchao'
import os
import sys
import re
import ConfigParser
import webbrowser
import json
import time
import urllib
import urllib2
#import requests
import cookielib
import hashlib
import binascii
#import rsa
import base64
import jieba
reload(sys)
sys.setdefaultencoding( "utf-8" )


import weibo
APP_KEY = '797443775'
APP_SECRET = '00bde1cb190286a234009713e5b9ddf3'
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'
def run():
    client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)
    auth_url = client.get_authorize_url()
    print "auth_url : " + auth_url
    code = raw_input("input the retured code : ")
    r = client.request_access_token(code)
    print r
    #r={'access_token': u'2.00Twg9rB04Yzxr78c8a6f55fvlrsVC', 'expires': 1592568897, 'expires_in': 1592568897, 'uid': u'1706116897'}
    client.set_access_token(r['access_token'], r['expires_in'])
    while True:
        list=[]
        key_word_list=[]
        print 'Ready!'
        g = client.statuses.user_timeline.get(screen_name='逾别情',feature=1)
        for page_num in range(10):
            comment=client.comments.show.get(id='3855865943806558',count=200,page=page_num+1)
            for item in comment.comments:
                i=(str(item.text).encode('utf-8'))

                key_word_list.append(jieba.analyse.textrank(i))
                list.append(i)
        print len(list)
        print list
        #list存储已经爬下来的评论:
        #对评论进行分词
        #使用rank方式所有评论的提取关键词，把关键词存入一个list中

        print '-------------------------'
        count_expression=0
        l='adaf'

        #计算表情的数目
        #for item in list:
        #    print item
        #    if '[' in item:
        #        count_expression+=1
        #print count_expression
        for item in key_word_list:
            print item
        break
        '''
        print "Ready! Do you want to send a new weibo?(y/n)"
        choice = raw_input()
        if choice == 'y' or choice == 'Y':
            content = raw_input('input the your new weibo content : ')
            if content:
                client.statuses.update.post(status=content)
                print "Send succesfully!"
                break
            else:
                print "Error! Empty content!"
        if choice == 'n' or choice == 'N':
            break

        '''
if __name__ == "__main__":
    run()
