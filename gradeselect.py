__author__ = 'liuqianchao'
import urllib
import urllib2
import cookielib

import re
import string
class TJU_Spider:
    # 申明相关的属性
    def __init__(self):
        self.loginUrl = 'http://e.tju.edu.cn/Main/logon.do'   # 登录的url
        self.resultUrl = 'http://e.tju.edu.cn/Education/toModule.do?prefix=/Education&page=/stuslls.do?todo=result'
        # 显示grade的url
        self.cookieJar = cookielib.CookieJar()                                      # 初始化一个CookieJar来处理Cookie的信息
        self.weights = []   #存储权重，也就是学分
        self.points = []    #存储分数，也就是成绩
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))

    def tju_init(self):
        uid=raw_input('uid=')
        password=raw_input('password=')
        choice=raw_input('第几学期？')
        self.postdata=urllib.urlencode({'uid':uid,'password':password})
        # 初始化链接并且获取cookie
        myRequest = urllib2.Request(url = self.loginUrl,data = self.postdata)   # 自定义一个请求
                   # 访问登录页面，获取到必须的cookie的值

        result = self.opener.open(self.resultUrl)  # 访问成绩页面，获得成绩的数据
        self.deal_data(result.read().decode('gbk'))

        self.deal_data(result.read().decode('gbk'))
        self.calculate_date()

    # 将内容从页面代码中抠出来
    def deal_data(self,myPage):
        myItems = re.findall('',myPage,re.S)     #获取到学分
        for item in myItems:
            self.weights.append(item[0].encode('gbk'))
            print item

    def calculate_date(self):
        point = 0.0
        weight = 0.0
        for i in range(len(self.points)):
              if string.atof(self.points[i])>100:
                  self.points[i]=0.0
                  self.weights[i]=0.0
              else:
                weight += string.atof(self.weights[i])
                point += string.atof(self.points[i])*string.atof(self.weights[i])
        print '加权为：',point/weight
#调用
mySpider = TJU_Spider()
mySpider.tju_init()




