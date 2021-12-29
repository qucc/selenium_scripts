from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import time
def log(message):
   print(message)
   driver.execute_script(f"console.log('{message}')")

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
while i < 100:
    i = i + 1
    log('process ' + str(i))
    time.sleep(5)
    record = wait.until( EC.presence_of_element_located((By.XPATH, "//table/tbody/tr[2]/td[1]")))
    log('record ' + str(record))
    ActionChains(driver).move_to_element(record).perform()
    # time.sleep(1)
    record.click()

    #ctui-bubble-icon-menu
    ctui = wait.until( EC.presence_of_element_located((By.XPATH, '//activity-editor/div/ctui-bubble-icon-menu')))
    log('ctui ' + str(ctui))
    time.sleep(1)
    ActionChains(driver).move_to_element(ctui).perform()
    ctui.click()

    #/html/body/div[2]/div/div[2]
    #ctui-bubble-icon-menu
    delete_button = wait.until( EC.presence_of_element_located((By.XPATH, "//*[@data-ng-click='ctrl.deleteActivity()']")))
    log('delete_button ' + str(delete_button))
    time.sleep(1)
    ActionChains(driver).move_to_element(delete_button).perform()
    delete_button.click()

    #/html/body/div[4]/div/div[3]/button[2]
    confirm_delete_button = wait.until( EC.presence_of_element_located((By.XPATH, "//*[@data-ng-click='ctrl.delete()']")))
    log('confirm_delete_button ' + str(confirm_delete_button))
    time.sleep(1)
    ActionChains(driver).move_to_element(confirm_delete_button).perform()
    confirm_delete_button.click()
