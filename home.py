import time #Задание 1
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")
selenium_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/ul/li/a[1]/h3")
selenium_btn.click()
time.sleep(3)
reviews = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[3]/ul/li[2]/a")
reviews.click()
time.sleep(2)
five_stars = driver.find_element_by_class_name("star-5")
five_stars.click()
time.sleep(2)
review_text = driver.find_element_by_id("comment")
review_text.send_keys("Nice book!")
time.sleep(1)
name = driver.find_element_by_id("author")
name.send_keys("TestUser")
time.sleep(1)
email = driver.find_element_by_id("email")
email.send_keys("test@mail.ru")
time.sleep(1)
submit = driver.find_element_by_id("submit")
submit.click() #Конец задания 1





import time
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
