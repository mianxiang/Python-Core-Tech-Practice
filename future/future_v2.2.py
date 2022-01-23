from asyncio import futures
import requests
import time
import threading
import concurrent.futures

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_one, sites)


def main():
    sites = ['http://www.xinhuanet.com/',
    'https://english.news.cn/home.htm',
    'http://jp.news.cn/index.htm',
    'http://german.news.cn/index.htm',
    'http://french.news.cn/index.htm',
    'http://kr.news.cn/index.htm',
    'http://arabic.news.cn/index.htm',
    'http://spanish.news.cn/index.htm']

    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()