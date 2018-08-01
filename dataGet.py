# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 下午8:33
# @Author  : Xieli Ruan
# @Site    : 
# @File    : dataGet.py
# @Software: PyCharm

from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup
import json
import chardet

# develop.douban.com base uri
baseUri = 'https://api.douban.com'

moviesData=[
    {
        'name': '',
        'date': '',
        'director':'',
        'star1':'',
        'star2':'',
        'star3':'',
        'star4':'',


    }
]


detailUrls=[]
#标签：共11个，来自豆瓣
Labels=['剧情','喜剧','动作','爱情','科幻','悬疑','惊悚','恐怖','犯罪','同性',
        '音乐','歌舞','传记','历史','战争','西部','奇幻','冒险','灾难','武侠','情色']
# 单位：万元
boxOffices=[
    568254,267088,221345,174866,165206,155123,129912,118794,117990,115891,115301,112517,110949,104604,103780,77475,75611,74370,74050,73008,
    69653,69054,68611,62560,61010,60694,59030,57721,54938,53980,53473,52262,52110,47719,47427,46884,45932,43403,40952,40360,
    40185,40050,33990,31899,31385,31116,30416,29910,29517,29292,29184,27132,27022,26570,25162,24725,23710,23015,21886,21569,
    21393,21075,20248,20126,19842,19500,17555,17507,17392,17258,17053,16965,16072,15636,15237,14890,13979,13711,13576,13388,
    12614,12527,12425,12167,11369,10895,10883,10738,10602,10584,10371,10345,10296,10128,10010,9566,9176,8760,8143,7954,
    7866,7696,7648,7545,7484,7372,6951,6781,6685,6632,6535,6512,6485,6465,6370,6295,5938,5706,5622,5577,
    5446,5392,5064,5026,4778,4688,4476,4454,4369,4318,4298,4241,4199,4099,4072,4025,4020,3870,3740,3673,
    3317,3299,3261,3233,3169,3041,3040,3005,2946,2873,2750,2717,2616,2565,2555,2530,2519,2461,2430,2221,
    2144,2109,2023,1825,1783,1762,1762,1733,1717,1645,1625,1602,1591,1568,1510,1487,1473,1455,1412,1388,
    1369,1361,1355,1347,1294,1294,1287,1280,1277,1262,1251,1216,1210,1162,1151,1149,1137,1081,1033,1023,
    1015,1011,1006,982,982,963,940,937,905,903,890,882,872,847,840,818,798,796,793,777,
    770,769,766,754,710,710,704,681,651,610,593,592,570,554,548,547,509,502,496,491,
    487,484,473,470,467,458,451,447,435,430,393,391,387,384,377,377,376,375,374,370,
    369,367,354,335,334,329,325,315,314,308,307,306,292,291,291,268,266,257,251,244,
    243,240,236,234,233,228,227,227,226,226,222,215,214,214,206,206,203,200,199,198


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
    for movieUrl in movieUrls:
        urls=movieUrl.find_all('ul',class_='row')
        for url in urls:
            detailUrls.append(url.get('data-com')[13:-1])
            # print(url.get('data-xcom')[13:-1])

    movieNames=soup.find_all('p',class_='first-line')
    movieDates = soup.find_all('p',class_='second-line')

    # for name in movieNames:
    #     print(name.get_text())
    # for date in movieDates:
    #     print(date.get_text())
def parse_celebrity_detail(celebrityId):
    celebrityUri='/v2/movie/celebrity/{0}/works'.format(celebrityId)
    worksRes=get_one_page(baseUri+celebrityUri)
    rates=0
    for work in worksRes:
        rates+=work['subject']['rating']['average']
    rates/=len(worksRes)

def parse_movie_detail(movieName):
    # boxOffice
    uri='/v2/movie/search?q={0}'.format(movieName)
    moviesRes=json.loads(get_one_page(baseUri+uri))
    # print(moviesRes[0])
    print(moviesRes['count'])
    print(type(moviesRes['count']))
    print(type(moviesRes['subjects'][0]['original_title']))
    string_code = chardet.detect(moviesRes['subjects'][0]['original_title'])
    print(string_code)
    '''
    for i in range(moviesRes['count']):

        if((moviesRes['subjects'][i]['original_title']==(unicode(movieName)))):
            movies=moviesRes['subjects'][i]['casts']
            for movie in movies:
                print(movie)
                # celebrityName=movie['name']
                # celebrityId=movie['id']
                # parse_celebrity_detail(celebrityId)
                # celebrity={celebrityName,celebrityId}
            return movies
        else:
            return None


'''

    # Director
    # issuingCompany
    # stars
    # labels




def main():
    url = 'http://piaofang.maoyan.com'
    ranklist_url='/rankings/year?year=2017&limit=100&tab=2'

    # html = get_one_page(url+ranklist_url)
    # parse_one_page(html)
    parse_movie_detail('战狼2')

if __name__ == '__main__':
    main()