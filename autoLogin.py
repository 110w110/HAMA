from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def fname(driver,name,value):
    driver.find_element_by_name(name).clear()
    time.sleep(0.3)
    driver.find_element_by_name(name).send_keys(value)
def cname(driver,name):
    driver.find_element_by_name(name).click()
def ename(driver,name):
    driver.find_element_by_name(name).send_keys(Keys.ENTER)
def fpath(driver,path,value):
    driver.find_element_by_xpath(path).send_keys(value)
def cpath(driver,path):
    driver.find_element_by_xpath(path).click()

def login(driver):
    print("비밀번호 끝 두자리를 입력해주세요.")
    passwd = 'jinsu781'
    passwd = passwd + input()
    fname(driver,'USER_ID','jpjung')
    fname(driver,'PASSWD',passwd)
    ename(driver,'PASSWD')
    # driver.get('https://itss.hongik.ac.kr/GateWeb/index.aspx')
    print("확인 후 아무 키나 입력해주세요")
    a = input()
    driver.get('https://itss.hongik.ac.kr/GateWeb/index.aspx')
    time.sleep(1)
    cpath(driver,'/html/body/form/div[3]/div[1]/div/div[1]/ul/li[2]/ul/li/a')
    time.sleep(0.3)
    cpath(driver,'/html/body/form/div[3]/div[1]/div/div[1]/ul/li[2]/ul/li/ul/li/a')
    time.sleep(0.3)
    cpath(driver,'/html/body/form/div[3]/div[1]/div/div[1]/ul/li[2]/ul/li/ul/li/ul/li[2]/a')
    time.sleep(0.3)
    cpath(driver,'/html/body/form/div[3]/div[1]/div/div[1]/ul/li[2]/ul/li/ul/li/ul/li[2]/ul/li[2]/a')
    return driver
    # time.sleep(0.3)
    # cpath(driver,'/html/body/form/div[3]/div[1]/div/div[1]/ul/li[2]/ul/li/ul/li/ul/li[2]/ul/li[2]/ul/li[2]/span/a')
    # ename(driver,'PASSWD')

    # ename(driver,'PASSWD')
    # time.sleep(1)
    # alert = driver.switch_to_alert
    # alert.dismiss()
    # print(1)
    # 비밀번호 변경 필요 알림 제거용


    # if EC.alert_is_present():
    #     alert = driver.switch_to_alert
    #     alert.dismiss()
    #
    # try:
    #     WebDriverWait(webbrowser, 3).until(EC.alert_is_present())
    #     alert = driver.switch_to_alert
    #     alert.dismiss()
    # except:
    #     time.sleep(1)



    # return driver


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.hongik.ac.kr/login.do?Refer=https://ngw.hongik.ac.kr/login_hongik.aspx")
    login(driver)