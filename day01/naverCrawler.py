import os
import sys
import urllib.request
import urllib.parse
import datetime
import time
import json
from webbrowser import get
from xml.etree.ElementPath import _SelectorContext

client_id = 'hW71n2RhmLvagg_eekUQ'
client_secret = 'y9qxXxDaS0'


# url 접속 요청 후 응답 리턴 함수
def getRequestUrl(url):
    req = urllib.request.Request(url) # url 보내고 req 객체 만듬
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200: #200 ok 40X error, 50X Server error
            print(f'[{datetime.datetime.now()}] Url Request success')
            return res.read().decode('utf-8')
    except Exception as e: #제로디비젼 에러 파일에러 제외
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None #get request url 에 대한 함수 정의

# 핵심함수, 네이버 API 검색
def getNaverSearch(node, srcText, start, display): #고정할 값 패스
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'
    text = urllib.parse.quote(srcText) # 파싱
    params = f'?query={text}&start={start}&display={display}' #srcText -> 인코딩필요

    url = base + node + params

    resDecode = getRequestUrl(url) #예외처리

    if resDecode == None :
        return None
    else:
        return json.loads(resDecode) #네이버에서 json으로 보냄

#
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    originallink = post['originallink']
    link = post['link']

    pubDate = datetime.datetime.strptime(post['pubDate'],'%a, %d %b %Y %H:%M:%S +0900')
    pubDate = pubDate.strftime('%Y-%m-%d %H:%M:%S') #2022-08-02 15:56:34

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description,
                       'originallink':originallink, 'link':link, 'pubDate':pubDate})

# 실행 최초 함수 (그전에 get post data 만들기)
def main():
    node = 'news'
    srcText = input('검색어를 입력하세요 : ')
    cnt = 0
    jsonResult =[]

    jsonRes = getNaverSearch(node, srcText, 1, 50)
    # print(jsonRes)
    total = jsonRes['total'] # 검색된 뉴스 개수

    while ((jsonRes != None) and (jsonRes['display'] != 0)):
        for post in jsonRes['items'] :
            cnt += 1
            getPostData(post, jsonResult, cnt)

        start = jsonRes['start'] + jsonRes['display'] # 1+50 50설정시 이후부터 2번째 페이지
        jsonRes = getNaverSearch(node, srcText, start, 50) 
    
    print(f'전체 검색 : {total} 건')

    # file output
    with open(f'./{srcText}_naver_{node}.json', mode='w', encoding='utf8') as outfile : # ./ 내위치
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii=False)
                    # 50개씩 한번에 저장,   들여쓰기 4,     시간순정렬,      ascii 말고 utf8로 저장
        outfile.write(jsonFile)
    
    print(f'가져온 데이터 : {cnt} 건')
    print(f'{srcText}_naver_{node}.json SAVED')


if __name__ == '__main__':
    main()