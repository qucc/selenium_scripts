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
driver.get('https://analytics.google.com/analytics/web/#/a215517535p297278339/admin/streams/table/3108122653')
#time.sleep(8)
card = wait.until( EC.presence_of_element_located((By.XPATH, '//web-stream-details/div/div/additional-settings/div/mat-card/mat-card-content/slat[2]')))
#card = driver.find_element(By.XPATH,'//web-stream-details/div/div/additional-settings/div/mat-card/mat-card-content/slat[2]')
log('card ' + str(card))


card.click()

ogtframe = wait.until( EC.presence_of_element_located((By.CSS_SELECTOR ,'.ogt-iframe')))
log('ogtframe ' + str(ogtframe))

driver.switch_to.frame(ogtframe)

create_event_button = wait.until( EC.presence_of_element_located((By.CSS_SELECTOR, '.blg-card')))
log('create_event_button ' + str(create_event_button))
create_event_button.click()

#//table/tbody/tr[2]
#/html/body/div/div[4]/activity-list-slider/div/div[2]/div/div[2]/activity-list/unordered-list/div/table/tbody/tr[2]/td[1]
i = 0
while i < len(names_list):
    actionName = names_list[i]
    log(f'process{actionName}' )
    time.sleep(6)

    create_button = wait.until( EC.presence_of_element_located((By.XPATH, "//*[@data-ng-click='ctrl.openCreateActivity()']")))
    log('create_button ' + str(create_button))
    time.sleep(1)
    ActionChains(driver).move_to_element(create_button).perform()
    create_button.click()

    event_name = wait.until( EC.presence_of_element_located((By.XPATH, "//*[@data-ng-model='ctrl.value']")))
    log('event_name ' + str(event_name))
    time.sleep(1)
    ActionChains(driver).move_to_element(event_name).perform()
    event_name.send_keys(actionName)
    time.sleep(1)
    #ctui-text-input/div/input
    event_input = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[6]/activity-editor-slider/div/div[2]/div/activity-editor/form/veditor/div/veditor-section/div/div[1]/div[3]/vt-instance/vt-params/vt-group[1]/div/div/vt-params/vt-simple-table/div/div[1]/div[2]/div[1]/div[1]/ctui-text-input/div/input")))
    ActionChains(driver).move_to_element(event_input).double_click().send_keys("button_click").perform()

    eventzero_input = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div/div[6]/activity-editor-slider/div/div[2]/div/activity-editor/form/veditor/div/veditor-section/div/div[1]/div[3]/vt-instance/vt-params/vt-group[1]/div/div/vt-params/vt-simple-table/div/div[1]/div[2]/div[3]/div[1]/ctui-text-input/div/input")))
    ActionChains(driver).move_to_element(eventzero_input).double_click().send_keys("0").perform()
   
    eventzero_input = wait.until( EC.presence_of_element_located((By.XPATH, "/html/body/div/div[6]/activity-editor-slider/div/div[2]/div/activity-editor/div/div/button[1]")))
    ActionChains(driver).move_to_element(eventzero_input).click().perform()

    i = i + 1

    

