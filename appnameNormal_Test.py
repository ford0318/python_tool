import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test1.testt import AES_test
import time
import random
import string

driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe") #開啟Chrome
driver.get("http://127.0.0.1:8000/")

wait = WebDriverWait(driver, 1)
elemLogName = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="username"]')))
elemLogName.send_keys("rkms")
elemPwd = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="password"]')))
elemPwd.send_keys("2Password!")

accountname = "testaccount1"
beginstr="-----BEGIN CERTIFICATE-----"
endstr="-----END CERTIFICATE-----"
centerstr="asdfghjkl"
senstivecontent = beginstr+centerstr+endstr
hostname="127.0.0.1"
testkey="TestPPK"


def find_elem(elem_xpath):
    return wait.until(EC.presence_of_element_located((By.XPATH, elem_xpath)))


with open('randnormalletter.txt','r') as f:
    # 讀取一般字元應用程式名稱測試
    for line in f.readlines():
        try:
            # 系統管理 //*[@id="side-menu"]/li[4]/a
            elem_sysmange = find_elem('//*[@id="side-menu"]/li[4]/a')
            elem_sysmange.click()


            # 應用程式 //*[@id="side-menu"]/li[4]/ul/li[3]/a
            elem_app = find_elem('//*[@id="side-menu"]/li[4]/ul/li[3]/a')
            elem_app.click()
            

            # 新增    //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/center/button[1]
            elem_create = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/center/button[1]')
            elem_create.click()

            # 輸入應用程式名稱   //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[1]/div/input
            elem_input_appname = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[1]/div/input')
            elem_input_appname.send_keys(line)

            # 輸入帳號   //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[3]/div/input
            elem_input_account = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[3]/div/input')
            elem_input_account.send_keys(accountname)

            # 輸入機敏   //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[5]/div/textarea
            elem_input_sensitive = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[5]/div/textarea')
            elem_input_sensitive.send_keys(senstivecontent)

            # 輸入server ip/host name   //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[7]/div/input
            elem_input_host = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[7]/div/input')
            elem_input_host.send_keys(hostname)
            
            # 輸入金鑰名稱  //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[9]/div/input
            elem_input_key = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[9]/div/input')
            elem_input_key.send_keys(testkey)

            # 確定     //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[11]/div/button[2]
            elem_submit = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[11]/div/button[2]')
            elem_submit.click()


            #input radios //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div/table/tbody/tr[15]/td[1]/input
            elem_radio = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div/table/tbody/tr[15]/td[1]/input')
            elem_radio.click()


            #進入只有機敏可以輸入
            # 修改    //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/center/button[2]
            elem_update =find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/center/button[2]')
            elem_update.click()

            # 輸入機敏   //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[5]/div/textarea
            elem_input_sensitive = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[5]/div/textarea')
            elem_input_sensitive.send_keys(senstivecontent)
            
            # 確定
            elem_submit = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div[11]/div/button[2]')
            elem_submit.click()


            #input radios //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div/table/tbody/tr[15]/td[1]/input
            elem_radio = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/div/table/tbody/tr[15]/td[1]/input')
            elem_radio.click()

            # 刪除    //*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/center/button[3]
            elem_delete = find_elem('//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/form/center/button[3]')
            elem_delete.click()

        except:
            with open("ApplicationNormal_Error.txt","a") as f:
                error_line = f'Some error has happended! {line}'+'\n'
                f.write(error_line)
                

driver.close()