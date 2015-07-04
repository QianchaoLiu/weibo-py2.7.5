# -*- coding: UTF-8 -*-
__author__ = 'liuqianchao'



import urllib2
import re
import time
import weibo

APP_KEY = '797443775'
APP_SECRET = '00bde1cb190286a234009713e5b9ddf3'
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'

#NET
url='http://www.163.com/'
#NET


SLEEP_TIME_LONG=60

def run():
    client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)
    auth_url = client.get_authorize_url()
    #print "auth_url : " + auth_url
   # code = raw_input("input the retured code : ")
   # r = client.request_access_token(code)



    #NET
    '''response=urllib2.urlopen(url)
    html=response.read().decode('gbk')
    mygoal=re.findall(' <li class="hx"><a href="http://news.163.com/">(.*?)</a>',html,re.S)
    for item in mygoal:
           item[0].encode('gbk')
    #NET'''





    client.set_access_token('2.00GnDhNC04Yzxr78374d51ceNB2t3D', '1394996399')

    NUM=1
    while NUM<=1:

        content=weibocontent()

        client.statuses.update.post(status=content)
        print 'Sent successfully for the %d times. and the content is: '% NUM +content
        #time.sleep(SLEEP_TIME_LONG)
        NUM+=1



def weibocontent():
    #NET

    response=urllib2.urlopen(url)
    html=response.read().decode('gbk')
    #mygoal=re.findall(' <li class="hx"><a href="http://news.163.com/">(.*?)</a>',html,re.S)
    mygoal=re.findall(' <li class="hx"><a href="http://news.163.com/special/mhkjsl_live/">(.*?)</a>',html,re.S)

    for item in mygoal:
        item[0].encode('gbk')

    content=time.strftime('%Y-%m-%d %H:%M:%S')+' #TODAY TOP NEWS FROM NETEASE#:'+''+item

    #content='RANGE(-1,-7)>>>'+str(range(-1,-7,-1))
    #' #TODAY TOP NEWS FROM NETEASE#:'+''
    return content
if __name__ == "__main__":
    run()
#{'access_token': u'2.00GnDhNC04Yzxr5befff706c0RXUuN', 'expires': 1391799600, 'expires_in': 1391799600, 'uid': u'2034620712'}