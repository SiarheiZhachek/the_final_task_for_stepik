from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def test_1(driver):
    driver.get('http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear')
    title_1 = driver.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    print(title_1.text)
    price_1 = driver.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    print(price_1.text)

