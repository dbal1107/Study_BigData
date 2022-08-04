# Selenium 사용 웹페이지 크롤링
# 패키지로드
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

def getCoffeeBeanStoreInfo(result):
    # chrome webdriver 객체 생성
    # wd = webdriver.Chrome('./day03/chromedriver.exe') # 경로조심
    # 열릴 때까지 delay 타임 줘야함
    # usb오류 해결
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    wd = webdriver.Chrome('./day03/chromedriver.exe', options=options)
    

    for i in range(1, 300):
        wd.get('https://www.coffeebeankorea.com/store/store.asp')
        time.sleep(1) # 1s 팝업표시 후 크롤링 안돼서 브라우저 닫히는것 방지
        
        try:
            wd.execute_script(f"storePop2('{i}')")
            time.sleep(0.5) # 1s 팝업표시 후 크롤링 안돼서 브라우저 닫히는것 방지
            html = wd.page_source
            soup = BeautifulSoup(html,'html.parser')
            store_name = soup.select('div.store_txt > h2')[0].string
            print(store_name)
            store_info = soup.select('table.store_table > tbody > tr > td')
            store_address_list = list(store_info[2])
            store_address = store_address_list[0].strip()
            store_contact=store_info[3].string
            result.append([store_name]+[store_address]+[store_contact])

        except Exception as e:
            print(e)
            continue

def main():
    result = []
    print('커피빈 매장 크롤링 >>> ')
    getCoffeeBeanStoreInfo(result)

    # 판다스 데이터프레임 생성
    columns = ['store','address','phone']
    coffeebean_df = pd.DataFrame(result, columns = columns)

    # '''
    #  csv 저장
    #  ./ 상대경로
    #  C:/ 절대경로
    # '''
    coffeebean_df.to_csv('C:/localRepository/StudyBigData/day03./coffeebean_shop_info2.csv',index=True, encoding='utf-8') # True 해야 인덱스나옴
    print('저장완료!')

    del result[:]

if __name__ == '__main__' : # 네임이 메인이면 네임실행
    main()