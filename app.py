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
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage

app = Flask(__name__,static_folder='static/')

#config = configparser.ConfigParser()
#config.read("config.ini")

line_bot_api = LineBotApi('')
handler = WebhookHandler('')
line_bot_api.push_message('', TextSendMessage(text='目前僅能查詢高鐵時間'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'



ngrok_url = "https://0cec-106-107-170-226.ngrok.io/"
@handler.add(MessageEvent)
def handle_message(event):
    print(event.message.text)
    event.message.text = event.message.text.split()
    start_use =event.message.text[0]
    arrival_use =event.message.text[1]
    data_use =event.message.text[2]
    time_use = event.message.text[3]
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

    photo_use = driver.find_element(by=By.CLASS_NAME,value="ticket-tb-scroll-end")
    action = ActionChains(driver)
    action.move_to_element(photo_use).perform()
    time.sleep(5)
    driver.get_screenshot_as_file("static/new.png")

    time.sleep(2)
    driver.close()
    #if event.message.text == "高鐵":
    #    content = high_speed_rail()
        #SendImage = line_bot_api.get_message_content(event.message.id)
    line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url = ngrok_url + "/static/new.png", preview_image_url = ngrok_url + "/static/new.png"))
    #print("helloworld")


if __name__ == '__main__':
    app.run(port=5000,debug=True,host="0.0.0.0")