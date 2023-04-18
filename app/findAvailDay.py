from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from .env import NAME, TLNO, EMAIL

def findAvailDay():
    print("findAvailDay start!")
    # availDays = [9, 10, 11, 12]
    availDays = []
    availDays = getWeb()
    print(f'findAvailDay end: {availDays}')
    return availDays


def getWeb():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # 포켓몬카페예약 페이지 접속
    browser.get("https://reserve.pokemon-cafe.jp/reserve/agree")

    # 동의창에서 동의 체크 후 버튼 클릭
    agree_checkbox = browser.find_element(By.XPATH, '//*[@id="forms-agree"]/div/label')
    agree_btn = browser.find_element(By.XPATH, '//*[@id="forms-agree"]/div/div/input')
    agree_checkbox.click()
    agree_btn.click()
    browser.implicitly_wait(2)

    selectbox = Select(browser.find_element(By.XPATH, '//*[@id="guest"]'))
    selectbox.select_by_value('1')
    browser.implicitly_wait(2)

    weekList = ['1','2','3','4','5']
    dayList = ['1','2','3','4','5','6','7']
    availDayList = []
    xList = []
    yList = []

    for x in weekList:
        for y in dayList:
            xpathNow  = f'//*[@id="step2-form"]/div[2]/div[2]/div[2]/div[2]/div/div[{x}]/div/li[{y}]'
            dayXY = browser.find_element(By.XPATH, xpathNow)
            if 'Full' not in dayXY.text:
                availDayList.append(dayXY.text[0:2])
                xList.append(x)
                yList.append(y)
    

    # if len(availDayList) > 0:
    #     print("예약 시도 시작!!!!!", availDayList)
    #     reserveDayXpath  = f'//*[@id="step2-form"]/div[2]/div[2]/div[2]/div[2]/div/div[{xList[0]}]/div/li[{yList[0]}]'
    #     reserveDay = browser.find_element(By.XPATH, reserveDayXpath)
    #     reserveDay.click()
    #     nextStep_btn = browser.find_element(By.XPATH, '//*[@id="submit_button"]')
    #     nextStep_btn.click()
    #     browser.implicitly_wait(2)

    #     timeXList = ['1', '2', '3']
    #     timeYList = ['1', '2', '3', '4']
    #     for a in timeXList:
    #         for b in timeYList:
    #             print(a, b)
    #             xpathTime  = f'//*[@id="time_table"]/tbody/tr[{a}]/td[{b}]/div/div'
    #             timeXY = browser.find_element(By.XPATH, xpathTime)
    #             print(timeXY.text)
    #             if 'Available' in timeXY.text:
    #                 reserveLink = browser.find_element(By.XPATH, f'//*[@id="time_table"]/tbody/tr[{a}]/td[{b}]/div/a')
    #                 reserveLink.click()
    #                 break
    #             continue
    #     browser.implicitly_wait(2)

    #     btn2 = browser.find_element(By.XPATH, '//*[@id="seat-stock-form"]/div/div/button')
    #     browser.implicitly_wait(1)

    #     name_input = browser.find_element(By.XPATH, '//*[@id="name"]')
    #     name_input.send_keys(NAME)
    #     nameConfirm_input = browser.find_element(By.XPATH, '//*[@id="name_kana"]')
    #     nameConfirm_input.send_keys(NAME)
    #     tlno_input = browser.find_element(By.XPATH, '//*[@id="phone_number"]')
    #     tlno_input.send_keys(TLNO)
    #     email_input = browser.find_element(By.XPATH, '//*[@id="phone_number"]')
    #     email_input.send_keys(EMAIL)

    #     submit_btn = browser.find_element(By.XPATH, '//*[@id="submit_button"]')
    #     submit_btn.click()
    #     browser.implicitly_wait(1)

    #     notBuy_btn = browser.find_element(By.XPATH, '//*[@id="step4-form"]/div[12]/a[1]')
    #     notBuy_btn.click()

    #     confirmReserve_btn = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/form/div/div/button')
    #     confirmReserve_btn.click()
        
    # 브라우저를 닫습니다.
    browser.quit()
    return availDayList