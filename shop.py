import time #Задание 4
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
shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a")
shop.click()
time.sleep(3)
book = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/a[1]/h3")
book.click()
time.sleep(3)
header = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/h1")
header_text = header.text
assert "HTML5 Forms" in header_text #Конец задания 4

import time #Задание 5
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
shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a")
shop.click()
time.sleep(3)
html_cat = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/aside/div[3]/ul/li[2]/a")
html_cat.click()
time.sleep(3)
element = driver.find_element_by_class_name("product_cat-html")
count = len(driver.find_elements_by_class_name("product_cat-html"))
if count == 3:
    print("Three cards") #Конец задания 5

import time #Задание 6
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a")
shop.click()
time.sleep(5)
from selenium.webdriver.support.select import Select
default_sorting = driver.find_element_by_css_selector("#content > form > select > option:nth-child(1)")
default_sorting_select = default_sorting.get_attribute("selected")
if default_sorting_select is not None:
    print("Correct")
else:
    print("Error.")
selector = driver.find_element_by_tag_name("select")
select=Select(selector)
select.select_by_value("price-desc")
time.sleep(3)
selector = driver.find_element_by_tag_name("select")
price_desc = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/form/select/option[6]")
price_desc_select = price_desc.get_attribute("selected")
if price_desc_select is not None:
    print("Correct")
else:
    print("Error") #Конец задания 6

#Задание 7
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a")
shop.click()
time.sleep(3)
book = driver.find_element_by_css_selector("#content > ul > li.post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img")
book.click()
old_price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/p/del/span")
old_price_text = old_price.text
assert "600" in old_price_text
new_price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/p/ins/span")
new_price_text = new_price.text
assert "450" in new_price_text
driver.implicitly_wait(20)
picture = driver.find_element_by_css_selector("#product-169 > div.images > a > img")
picture.click()
time.sleep(3)
close_btn = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div[2]/div[3]/a")
close_btn.click() #Конец задания 7

import time #Задание 8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
#my_acc = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
#my_acc.click()
#time.sleep(2)
#username = driver.find_element_by_id("username")
#username.send_keys("testuser@mail.ru")
#time.sleep(1)
#password = driver.find_element_by_id("password")
#password.send_keys("Nbnfys12&")
#login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")
#login.click()
#time.sleep(3)
shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a")
shop.click()
time.sleep(3)
add_to_basket = driver.find_element_by_css_selector("#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
add_to_basket.click()
menucart = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a")
menucart_text = menucart.text
assert "1 item" in menucart_text
assert "180" in menucart_text
menucart.click()
#С ожиданиями, если честно, запутался и не очень понял, как их выполнять...
#Конец задания 8