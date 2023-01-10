from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

print("請輸入上車站別、下車站別、單程(目前只提供查詢單程)、去程日期、去程時刻(每30分鐘為基準)") 
print("上車及下車站別選項為:南港、台北、板橋、桃園、新竹、苗栗、台中、彰化、雲林、嘉義、台南、左營")
#print("")
print("------------------------分割線------------------------")
print("請輸入上車站(Ex:台中):")
start_use = "台中"

print("請輸入下車站(Ex:彰化):")
arrival_use = "彰化"

#print("請輸入單程/去回程:")
ticket_use = "單程"

print("請輸入去程日期(Ex:2022.11.07):")
data_use = "2022.11.11"

print("請輸入去程時刻(Ex:20:30):")
time_use = "14:30"

#print("請輸入適用優惠(Ex:早鳥，若無則入1):")
#discount_use = input()

PATH="D:/PYTHONE/new/chromedriver_win32/chromedriver.exe" #chromedriver檔案存放位置
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)

url = "https://www.thsrc.com.tw/"
driver.get(url)
driver.find_element(by=By.CLASS_NAME,value="swal2-confirm.swal2-styled").click()

#輸入值
start_find = driver.find_element(by=By.ID,value="select_location01").send_keys(start_use) #上車
arrival_find = driver.find_element(by=By.ID,value="select_location02").send_keys(arrival_use) #下車
ticket_find =  driver.find_element(by=By.ID,value="typesofticket").send_keys(ticket_use) #單程/去回程
#data_find =  driver.find_element_by_id("Departdate03").send_keys(data_use) # 去程日期
data_find = driver.execute_script(f"document.getElementById('Departdate01').value='{data_use}'")
#timd_find = driver.find_element_by_id("outWardTime").send_keys(time_use) #去程時刻
timd_find = driver.execute_script(f"document.getElementById('outWardTime').value='{time_use}'")

driver.find_element(by=By.ID,value="start-search").click()
"""
soup = BeautifulSoup(driver.page_source, 'html.parser')
soup_use = soup.select("timeTableTrain_S,tr-td")
print(type(soup_use))
"""




time.sleep(2)
driver.close()