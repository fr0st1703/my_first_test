import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.tutorialsninja.com/demo/')

search = driver.find_element(By.XPATH, '//*[@id="search"]/input')
search.clear()
search.send_keys('iphone')
search.send_keys(Keys.RETURN)

basket_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
basket_button.click()
time.sleep(4)

basket_menu_btn = driver.find_element(By.XPATH, '//*[@id="cart"]/button')
basket_menu_btn.click()

link_in_basket = driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[1]')
link_in_basket.click()

assert 'product 11' in driver.page_source

driver.close()
driver.quit()





