# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 下午8:33
# @Author  : Xieli Ruan
# @Site    : 
# @File    : dataGet.py
# @Software: PyCharm

from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    movie = soup.find_all(class_='col1')
    for a in movie:
        print(a.find_all(class_='first-line'))
        print(a.find_all('p',class_='second-line'))

def main():
    url = 'http://piaofang.maoyan.com/rankings/year?year=2017&limit=100&tab=2'
    html = get_one_page(url)
    parse_one_page(html)

'''
def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    html = soup.find_all(class_='infolist-row')
    for a in html:
        print(a.find_all('a')[0])

def main():
    url = 'https://www.0951job.com/jobs/jobs-list.php'
    html = get_one_page(url)
    parse_one_page(html)
'''
if __name__ == '__main__':
    main()