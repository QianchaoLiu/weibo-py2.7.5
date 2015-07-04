# encoding: UTF-8
_author__ = 'liuqianchao'
import jieba
import re
import sys
import os
import gensim
import jieba.analyse
model = gensim.models.Word2Vec.load("wiki.zh.text.model")
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
reload(sys)
sys.setdefaultencoding('gbk')
f=open('neg.txt')
text=f.read().encode('utf-8')

myItems = re.findall('</ID>(.*?)<Product>',text,re.S)     #获取到学分
i=0
#while i<len(len(myItems)):
file_path = os.path.join(BASE_DIR, 'weibo-py2.7.5') #获取当前文件夹内的Test_Data文件
while i<len(myItems):
    #f=open(file_path+'/Neg/%d.txt'%i,'w+')
    #f.write(myItems[i])
    for x, w in jieba.analyse.textrank(myItems[i], withWeight=True):
        print('%s %s' % (x, w))
    i+=1
