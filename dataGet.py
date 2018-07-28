# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 下午8:33
# @Author  : Xieli Ruan
# @Site    : 
# @File    : dataGet.py
# @Software: PyCharm

from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup


movies=[
    {
        'name': '',
        'date': ''

    }
]



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
    movieUrls = soup.find_all('div',{'id':'ranks-list'})
    # for movieUrl in movieUrls:
    #     url=movieUrl.find_all('ul',class_='row')
    #     print(url.get('data-com'))

    movieNames=soup.find_all('p',class_='first-line')
    movieDates = soup.find_all('p',class_='second-line')

    # for name in movieNames:
    #     print(movieNames.__len__())
    #     print(name.get_text())
    # for date in movieDates:
    #     print(date.get_text())
    for url in movieUrls:
        print(url.get('data-com'))

def main():
    url = 'http://piaofang.maoyan.com/rankings/year?year=2017&limit=100&tab=2'
    html = get_one_page(url)
    parse_one_page(html)


if __name__ == '__main__':
    main()