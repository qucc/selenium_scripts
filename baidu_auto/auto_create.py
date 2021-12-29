from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import time
def log(message):
   print(message)
   driver.execute_script(f"console.log('{message}')")



with open('event.txt') as f:
   names_list = [l for l in (line.strip() for line in f) if l]
print(len(names_list))


s = Service('C:\\Users\\Hp\\Downloads\\chromedriver_win32\\chromedriver.exe')
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=s,options=chrome_options)     
wait = WebDriverWait(driver, 10)
driver.get('https://mtj.baidu.com/web/home/event?appId=3215820')


i = 0
while i < len(names_list):
    actionName = names_list[i]
    log(f'process{actionName}' )
    time.sleep(6)

    create_button = wait.until( EC.presence_of_element_located((By.ID, "add-event-toggle-btn")))
    log('create_button ' + str(create_button))
    time.sleep(1)
    ActionChains(driver).move_to_element(create_button).perform()
    create_button.click()

    event_name = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[2]/div/form/div[1]/input")))
    log('event_name ' + str(event_name))
    time.sleep(1)
    ActionChains(driver).move_to_element(event_name).perform()
    event_name.send_keys(actionName)
    time.sleep(1)
    #ctui-text-input/div/input
    event_input = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[2]/div/form/div[2]/input")))
    ActionChains(driver).move_to_element(event_input).double_click().send_keys(actionName).perform()

   
    eventzero_input = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[2]/div/form/a")))
    ActionChains(driver).move_to_element(eventzero_input).click().perform()

    i = i + 1

    

