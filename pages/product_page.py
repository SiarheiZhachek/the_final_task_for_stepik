from pages.base_page import BasePage
from pages.locators import product_page_locators as loc


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_product_page(self):
        self.driver.get(
            'http://selenium1py.pythonanywhere.com/'
            'catalogue/the-shellcoders-handbook_209/?promo=newYear'
        )

    def add_to_cart_button_is_displayed(self):
        return self.find_element(loc.add_to_cart_button)

    def product_title(self):
        return self.find_element(loc.product_name).text

    def product_price(self):
        return self.find_element(loc.product_price).text

    def add_to_cart_button_click(self):
        return self.find_element(loc.add_to_cart_button).click()

    def alert_check(self):
        return self.solve_quiz_and_get_code()

    def message_with_the_cost_of_the_cart_is_displayed(self):
        return self.find_element(loc.message_cart).is_displayed()

    def product_addition_messages_is_displayed(self):
        return self.find_elements(loc.massage_add_product)[0].is_displayed()

    def check_title_add_to_cart(self):
        return self.find_elements(loc.information_by_add)[0].text

    def check_price_add_to_cart(self):
        return self.find_elements(loc.information_by_add)[2].text