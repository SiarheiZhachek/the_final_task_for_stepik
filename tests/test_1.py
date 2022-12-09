from selenium.webdriver.common.by import By
from time import sleep


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    driver.get(link)
    login_link = driver.find_element(By.CSS_SELECTOR, "#login_link")
    sleep(3)
    login_link.click()

