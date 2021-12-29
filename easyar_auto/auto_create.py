from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

import time
def log(message):
   print(message)
   driver.execute_script(f"console.log('{message}')")



with open('event.txt') as f:
   names_list = [l for l in (line.strip() for line in f) if l]
print(len(names_list))

startIndex = 205
productName = "ANReye"
folderPath = "D:\\ANReye\\"
extensionList = ('jpg',  'png')

image_list = []
for currentFileName in os.listdir(folderPath):
      if currentFileName.endswith(extensionList):
            print(currentFileName)
            print(f"{folderPath}{currentFileName}")
            image_list.append(currentFileName)
      else:
            continue

print(len(image_list))

s = Service('C:\\Users\\Hp\\Downloads\\chromedriver_win32\\chromedriver.exe')
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=s,options=chrome_options)     
wait = WebDriverWait(driver, 10)
driver.get('https://portal.easyar.cn/crs/info/1/101/16495')
# k = PyKeyboard()
#k.tap_key(k.enter_key)

i = 0
while i < len(image_list):
    imageName = image_list[i]
    log(f'process{imageName}' )
    time.sleep(6)

    create_button = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/button")))
    log('create_button ' + str(create_button))
    time.sleep(1)
    ActionChains(driver).move_to_element(create_button).perform()
    create_button.click()

    product_name = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/input")))
    log('product_name ' + str(product_name))
    time.sleep(1)
    ActionChains(driver).move_to_element(product_name).perform()
    product_name.send_keys(f"{productName}_{i + startIndex}")

    update_file = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/span[2]/div/span/input")))
    log('update_file ' + str(update_file))
    time.sleep(1)
    driver.execute_script("arguments[0].style.display='block';",update_file)
    ActionChains(driver).move_to_element(update_file).perform()
    update_file.send_keys(f"{folderPath}{imageName}")


    product_width = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[4]/input")))
    log('product_width ' + str(product_width))
    time.sleep(1)
    ActionChains(driver).move_to_element(product_width).perform()
    product_width.send_keys('50')
   
    save_button = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[6]/button[1]")))
    ActionChains(driver).move_to_element(save_button).click().perform()
    
    try:
      time.sleep(5)
      confirm_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]")
      log('confirm_button ' + str(confirm_button))
      if not confirm_button is None:
         ActionChains(driver).move_to_element(confirm_button).click().perform()
    except:
        print("not found repeat")

    i = i + 1

    

