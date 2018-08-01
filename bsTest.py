# -*- coding: utf-8 -*-
# @Time    : 2018/7/26 下午8:06
# @Author  : Xieli Ruan
# @Site    : 
# @File    : bsTest.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
from bs4 import  BeautifulSoup

import re

'''
soup=BeautifulSoup(html,'lxml')   #创建一个对象
soup.title                       #打印标签中的所有内容
soup.title.text                  #打印标签中的文本内容   ==soup.title.string
soup.p.attrs                     #以字典的形式将标签中的属性输出
soup.p.attrs['href']              #获得标签中的属性值   ==soup.p.attrs.get('href')  ==soup.p.get('href')==soup.p['href']
soup.find_all('a')                 #查找所有的a标签并且将所有的a标签存储在列表中，可以遍历列表输出
soup.find('a')                     #只查找第一个a标签，只是一个
soup.find_all(['a','b'])            #查找所有的a和b标签，并且存储在列表中

soup.find_all('p',class_='title')     #查找属性是title的p    ==all_p=soup.find_all('p',{'class':'title'})

soup.find_all('p',class_=['title','main'])      #查找同时具备两个属性的p

get_text()                                     #获取文本内容


soup.find_all('div').find_all('a')                #在所有的div中查找a标签
等同于   all_div=soup.find_all('div')
         all_a=all_div.find_all('a')


soup.find_all('a',limit=2)                        #limit=2是限制的作用，用来限制返回的a标签最多两个
soup.find_all(text=".....")                         #查找所有文本内容是。。。。的标签


#在css中进行查找的方法
soup.select('p')                                  #查找所有的p标签   ==soup.find_all('p')

soup.select(".title")                            #通过类名进行查找

soup.select('#link1')                             #通过id名进行查找

all_p=soup.select('p[class="title"]')                    #属性进行查找

all_p[0].get_text()                              #获取文本内容









'''

html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<div>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</div>
"""


soup=BeautifulSoup(html,'lxml')   #创建一个对象
'''
print soup.prettify()   #格式化的输出
print soup.title  #输出标签中的全部内容
print soup.p
print soup.body

print soup.title.text
print soup.p.attrs
print soup.p.get('text')
print soup.p.attrs.get('name')
print soup.title.string


all_a=soup.find_all('a')
for i in all_a:
    print i.get("href")


a=soup.find('a')
print a.get('href')

all_a_p=soup.find_all(['a','p'])
for i in all_a_p:
    print i
all_p=soup.find_all('p',class_=['title','story'])
print all_p


all_p=soup.find_all('p',{'class':'title'})

all_div=soup.find('div')
print all_div
all_a=all_div.find_all('a')
for i in all_a:


all_a=soup.find_all('a',limit=4)
for i in all_a:



all_p=soup.select('p')
for i in all_p:
    print i

all=soup.select(".title")
print al
get_text()

all_p=soup.select('p[class="title"]')
print all_p
print all_p[0].get_text()
'''

# all_p=soup.find('p')
# print all_p.string()


def convert(s):
    return ''.join([r'\u', s.strip('&#x;')]).decode('unicode_escape')

ss='&#xf745;'
ss = unicode(ss, 'gbk') # convert gbk-encoded byte-string ss to unicode string

print re.sub(r'&#x....;', lambda match: convert(match.group()), ss)
