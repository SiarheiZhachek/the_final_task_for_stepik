import math
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *args):
        element, value = args[0]
        return self.driver.find_element(element,  value)

    def find_elements(self, *args):
        element, value = args[0]
        return self.driver.find_elements(element,  value)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x_num = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x_num))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            print(answer)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
