# -*- coding:utf-8 -*-
import os
import commands
import re
import django
import _mysql
(status, output) = commands.getstatusoutput("cp ~/Library/Application\ Support/Google/Chrome/Default/History ~/GoogleHistory | sqlite3 ~/GoogleHistory && echo 'select * from urls;' | sqlite3 ~/GoogleHistory > temp.txt && rm ~/GoogleHistory")
history=file("temp.txt",'r')
content=history.read()
result=re.findall('http://(.+?)/',content,re.S)

#去除相邻且相同的网址
'''num=len(result)-1
while num>=1:
    if result[num-1]==result[num]:
        result.pop(num)
    num-=1
'''
print django.VERSION
newlist=[]
for item in result:
    if result.count(item)<10 and  result.count(item)>0:
        tempnum=str(result.count(item))
        tempnum='000'+tempnum
    elif result.count(item)>9 and  result.count(item)<100:
        tempnum=str(result.count(item))
        tempnum='00'+tempnum
    elif result.count(item)>99 and  result.count(item)<1000:
        tempnum=str(result.count(item))
        tempnum='0'+tempnum
    elif result.count(item)>999 and  result.count(item)<10000:
        tempnum=str(result.count(item))
    newlist.append(tempnum+"  "+item)

nnewlist=list(set(newlist))
nnewlist.sort()
nnewlist.reverse()
print nnewlist
writefile=open('Chrome浏览网页次数排序.txt','w+')

for h in nnewlist:
    writefile.write('%s %s' %(h,os.linesep))

print "Done!"