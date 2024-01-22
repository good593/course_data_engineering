#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys  
# site-packages path 추가
sys.path.append( '/home/ubuntu/.local/lib/python3.8/site-packages')

import requests
from bs4 import BeautifulSoup as bs 
 
import pandas as pd 
from hdfs import InsecureClient


def do_crawling(url):
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "referer": "https://www.google.com/"
    }
    response = requests.get(url, headers=header)
    response.raise_for_status()

    return response

def get_titles(response):
    soup = bs(response.text, "html.parser")
    html_titles = soup.find_all('a', class_='title')

    return [ title.text for title in html_titles ]


def main(guest_ip, review_url, localpath, hdfspath):

    # 크롤링
    response = do_crawling(review_url)

    # 데이터 추출 
    review_titles = get_titles(response)

    # 데이터 저장 
    with open(localpath, "w",  encoding='utf8') as file:
        file.writelines(review_titles)

    # hadoop에 데이터 저장
    hdfs_ip = "http://{guest_ip}:50070".format(guest_ip=guest_ip)
    client_hdfs = InsecureClient(hdfs_ip, user='ubuntu')
    client_hdfs.upload(hdfspath, localpath)


###############################
# 크롤링 실행함수
###############################
if __name__ == "__main__":
    # master ip 주소
    guest_ip = '10.0.2.15'
    # 크로링할 리듀 url 주소  
    review_url = "https://www.imdb.com/title/tt0111161/reviews/?ref_=tt_ov_rt"
    # 하둡 저장될 주소
    hdfspath = '/crawling/input/review_titles.txt'
    # 리눅스에 저장될 주소
    localpath = '/home/ubuntu/src/data/review_titles.txt'

    main(guest_ip, review_url, localpath, hdfspath)



