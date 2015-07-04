# -*- coding:utf-8 -*-

__author__ = 'liuqianchao'
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

import jieba
f=open('/Users/liuqianchao/PycharmProjects/weibo-py2.7.5/test.txt')
file=f.read()
print '开始分词'
seg_list =jieba.cut(file, cut_all=False)

print '分词结束'
newf=" ".join(seg_list)

wt=open('newtest.text','w')
wt.write(newf)