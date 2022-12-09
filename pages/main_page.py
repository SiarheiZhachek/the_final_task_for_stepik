from pages.base_page import BasePage
from pages.locators import main_page_locators as loc


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_site(self):
        self.driver.get('http://selenium1py.pythonanywhere.com/')

    def go_to_login_page(self):
        login_button = self.find_element(loc.login_link)
        return login_button.click()

    # def should_be_login_link(self):
    #     self.find_element(LocMP.login_link)

    def login_link_is_displayed(self):
        return self.find_element(loc.login_link).is_displayed()
