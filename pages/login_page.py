from pages.base_page import BasePage
from pages.locators import login_page_locators as loc


class LogInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def should_be_login_url(self):
        return self.driver.current_url

    def should_be_login_form_is_displayed(self):
        return self.find_element(loc.log_in_form).is_displayed()

    def should_be_register_forms_is_displayed(self):
        return self.find_element(loc.reg_form).is_displayed()
