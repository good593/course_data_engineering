import requests
from bs4 import BeautifulSoup as bs 
 
import pandas as pd 
from hdfs import InsecureClient


def do_crawling(url, header):
    response = requests.get(url, headers=header)
    response.raise_for_status()
    return response

def get_movies(response):
    movies = []
    soup = bs(response.text, "html.parser")
    html_movies = soup.find_all('div', class_='wrap_cont')

    for _html in html_movies:
        _title = _html.find_all('a', class_='tit_main')
        if not len(_title):
            continue # 제목이 없는 경우에는 제외 

        _rate = _html.find_all('em', class_='rate')
        _lst = _html.find_all('dd', class_='cont')
        movies.append({
            'title' : _title[0].text # 제목
            , 'rate' : _rate[0].text if len(_rate) > 0 else '0.0' # 평점
            , 'reservation_rate' : _lst[0].text # 예매율
            , 'release_date' : _lst[1].text # 개봉일자
            , 'attendance_count' : _lst[2].text if len(_lst) > 2 else '0명'     # 누적관객수
        })

    return movies


def main(guest_ip):

    # 크롤링
    url = "https://search.daum.net/search?w=tot&DA=TMZ&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "referer": "https://www.google.com/"
    }
    response = do_crawling(url, header)

    # 데이터 추출 
    movies = get_movies(response)

    # 데이터 저장 
    df_movies = pd.DataFrame(movies)
    localpath = 'movies.parquet'
    df_movies.to_parquet(localpath, engine='pyarrow', index=False)

    # hadoop에 데이터 저장
    hdfs_ip = "http://{guest_ip}:50070".format(guest_ip=guest_ip)
    client_hdfs = InsecureClient(hdfs_ip, user='ubuntu')
    hdfspath = '/crawling/movies.parquet'
    client_hdfs.upload(hdfspath, localpath)

if __name__ == "__main__":
    guest_ip = '10.0.2.15' # master ip 주소!! 
    main(guest_ip)



