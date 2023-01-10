from flask import Flask,request
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage



def high_speed_rail(start_use,arrival_use,data_use,time_use):
    PATH="D:/PYTHONE/new/chromedriver_win32/chromedriver.exe" #chromedriver檔案存放位置
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=PATH)

    url = "https://www.thsrc.com.tw/"
    driver.get(url)
    driver.find_element(by=By.CLASS_NAME,value="swal2-confirm.swal2-styled").click()

    ticket_use = "單程"
    #輸入值
    start_find = driver.find_element(by=By.ID,value="select_location01").send_keys(start_use) #上車
    arrival_find = driver.find_element(by=By.ID,value="select_location02").send_keys(arrival_use) #下車
    ticket_find =  driver.find_element(by=By.ID,value="typesofticket").send_keys(ticket_use) #單程/去回程
    #data_find =  driver.find_element_by_id("Departdate03").send_keys(data_use) # 去程日期
    data_find = driver.execute_script(f"document.getElementById('Departdate01').value='{data_use}'")
    #timd_find = driver.find_element_by_id("outWardTime").send_keys(time_use) #去程時刻
    timd_find = driver.execute_script(f"document.getElementById('outWardTime').value='{time_use}'")
    time.sleep(5)
    driver.find_element(by=By.ID,value="start-search").click()

    time.sleep(5)

    photo_use = driver.find_element_by_class_name("ticket-tb-scroll-end")
    action = ActionChains(driver)
    action.move_to_element(photo_use).perform()
    time.sleep(6)
    driver.get_screenshot_as_file("new.png")

    #以下為時間
    '''
    tr = driver.find_elements(by=By.CLASS_NAME,value="tr-tbody")
    for i in tr:
        print(i.text)
    '''
    time.sleep(2)
    driver.close()

high_speed_rail("台中","彰化","2022.11.16","14:30")