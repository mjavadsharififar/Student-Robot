#!/usr/bin/env python
# coding: utf-8

# # Student Robot

# You can give link of virtual classroom ti thes robot, and it would be present in the class!

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 


# In[2]:


url = 'https://vc.isu.ac.ir/ch/culture-sci-assn' #link of class
s = Service('C:/Users/MJavad/Desktop/chromedriver.exe') # The path to your driver

driver = webdriver.Chrome(service = s)
driver.get(url)
time.sleep(3)


# In[3]:


enter = driver.find_element(By.ID, value = 'btn_guest')
enter.click()
time.sleep(3)


# In[4]:


name = driver.find_element(By.XPATH, value = "//input[@class='full-width']")
name.click()
name.send_keys('محمدجواد شریفی فر') #name of student
confirm = driver.find_element(By.XPATH, value = "//button[@class='btn']")
confirm.click()


# In[5]:


box = driver.find_element(By.XPATH, value = "//div[@class='input box dont-break-out is-rtl']")
box.click()
time.sleep(3)
box.send_keys('سلام استاد') #say hello to teacher
send = driver.find_element(By.XPATH, value = "(//button[@class='btn btn-flat icon-button'])[last()]")
send.click()


# In[6]:


#rejecting speack requests
while True:
    a = WebDriverWait(driver, 5400).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn'][2]")))
    time.sleep(3)
    a.click()
    box.click()
    box.send_keys('ببخشید الان امکان صحبت ندارم') #we can make different terms and return them by random
    send = driver.find_element(By.XPATH, value = "(//button[@class='btn btn-flat icon-button'])[last()]")
    send.click()


# In[ ]:


driver.quit()


# In[ ]:




