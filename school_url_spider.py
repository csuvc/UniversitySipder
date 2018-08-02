#/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup

url = 'http://www.hao123.com/edu'
headers = {
    'Host': 'www.hao123.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Referer': 'http://www.hao123.com/exam/wangzhi',
}
area_url_list = []   # 存放获取到的地区学校url
urls_file = '/opt/url.txt' # 第一次抓取完的url

def get_area_school_url(url,headers):

    '''获得地区学校的url地址'''

    try:
        response = requests.get(url=url,headers=headers)
        soup = BeautifulSoup(response.text,"lxml")
    except requests.exceptions.RequestException:
        pass

    else:
        print soup.title.string
        div = soup.select("[href^='http://www.hao123.com/eduhtm']")

        for tag in div[1:-2]:
            area_url = tag.get('href')
        #print "[+]" + area_url  # 地区学校的url
            area_url_list.append(area_url)

def get_school_url(headers):

    '''获取学校的url地址'''

    for school_url in area_url_list:
        try:
            response = requests.get(url=school_url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            div = soup.select("a[href^=http://]")
        except requests.exceptions.RequestException:
            pass
        else:
            for tag in div[60:-5]:
                if 'baidu' in tag:
                    pass
                else:
                    target_url = str(tag.get('href'))
                    #print target_url
                    with open('/opt/url.txt','at') as f:
                        f.write(target_url+'\n')

def file_handle(urls_file,target_urls_file):

    '''处理掉不需要的 url并保存到target_url.txt中'''

    with open(urls_file,'rt') as f2:
        for line in f2:
            line = line.strip('\n')
            #print line
            if 'baidu' in line:
                pass
            else:
                print line
                with open(target_urls_file,'at') as f3:
                    f3.write(line+'\n')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print '[-] Usage: ' + str(sys.argv[0]) + ' -o outputfile'
        print 'Error: argument -o/--output is required'
    else:
        targets_file = sys.argv[2]
        get_area_school_url(url,headers)
        get_school_url(headers)
        file_handle(urls_file,targets_file)