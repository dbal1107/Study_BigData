# 할리스 카페 매장 정보 크롤링
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def getHollysStoreInfo(result):
    for page in range(1, 53+1):
        # 디버깅 
        hollys_url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}'
        # print(hollys_url)
        html = urllib.request.urlopen(hollys_url)
        soup = BeautifulSoup(html, 'html.parser') # html 전부 불러오기. ()는 생성 .은
        tbody = soup.find('tbody')

        # tr개수 파악
        for store in tbody.find_all('tr') : # < > 전부찾기
            if len(store) <= 3 : # 값이 3보다 작으면 문제가 있다. -> break
                break 
            store_td = store.find_all('td')
            
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string

            result.append([store_name]+[store_sido]+[store_address]+[store_phone])
        
    # result
    print('완료!!')

def main():
    result = []
    print('할리스매장 크롤링 >>> ')
    getHollysStoreInfo(result)

    # 판다스 데이터프레임 생성
    columns = ['store','sido-gu','address','phone']
    hollys_df = pd.DataFrame(result, columns = columns)

    '''
     csv 저장
     ./ 상대경로
     C:/ 절대경로
    '''
    hollys_df.to_csv('C:/localRepository/StudyBigData/day03./hollys_shop_info2.csv',index=True, encoding='utf-8') # True 해야 인덱스나옴
    print('저장완료!')

    del result[:]

if __name__ == '__main__' : # 네임이 메인이면 네임실행
    main()
