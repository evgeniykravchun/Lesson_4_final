import time #Задание 2
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_acc = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
my_acc.click()
time.sleep(2)
email = driver.find_element_by_id("reg_email")
email.send_keys("testuser@mail.ru")
time.sleep(1)
password = driver.find_element_by_id("reg_password")
password.send_keys("Nbnfys12&")
register = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]")
register.click()
time.sleep(3) #Конец задания 2

import time #Задание 3
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_acc = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
my_acc.click()
time.sleep(2)
username = driver.find_element_by_id("username")
username.send_keys("testuser@mail.ru")
time.sleep(1)
password = driver.find_element_by_id("password")
password.send_keys("Nbnfys12&")
login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")
login.click()
time.sleep(3)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logout = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/nav/ul/li[6]/a")
if logout.is_displayed():
    print("Element found") #Конец задания 3