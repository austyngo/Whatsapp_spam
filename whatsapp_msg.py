from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys

#set to whatever text you want
text = open("shrek_script.txt").read().split()

#set to path of chromedriver in your computer
driver = webdriver.Chrome(r"C:\Users\austi\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

#set to exact name of the person you want to send to on whatsapp - may need double quotations
target = '"<Contact Name>"'

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
By.XPATH, x_arg)))
print (group_title)
print ("Wait a few seconds")
group_title.click()
message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

for word in text:
    message.send_keys(word)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()

driver.close()
