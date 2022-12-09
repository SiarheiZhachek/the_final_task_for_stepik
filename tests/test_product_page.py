import allure
from pages.product_page import ProductPage


@allure.feature('Product page')
@allure.story('Add to cart')
def test_add_to_cart_button_is_displayed(driver):
    with allure.step('Open site'):
        product_page = ProductPage(driver)
        product_page.open_product_page()
    with allure.step('Add to cart button is displayed'):
        assert product_page.add_to_cart_button_is_displayed()


@allure.feature('Product page')
@allure.story('Add to cart')
def test_messages_that_the_product_has_been_added_is_displayed(driver):
    with allure.step('Open site'):
        product_page = ProductPage(driver)
        product_page.open_product_page()
    with allure.step('Click button: Add to cart'):
        product_page.add_to_cart_button_click()
    with allure.step('Check alert'):
        product_page.alert_check()
    with allure.step('Check message'):
        assert product_page.product_addition_messages_is_displayed()


@allure.feature('Product page')
@allure.story('Add to cart')
def test_message_with_the_cost_of_the_cart_is_displayed(driver):
    with allure.step('Open site'):
        product_page = ProductPage(driver)
        product_page.open_product_page()
    with allure.step('Click button: Add to cart'):
        product_page.add_to_cart_button_click()
    with allure.step('Check alert'):
        product_page.alert_check()
    with allure.step('Check message'):
        assert product_page.message_with_the_cost_of_the_cart_is_displayed()


@allure.feature('Product page')
@allure.story('Add to cart')
def test_the_product_was_added_with_the_name_correctly(driver):
    with allure.step('Open site'):
        product_page = ProductPage(driver)
        product_page.open_product_page()
        title_book = product_page.product_title()
    with allure.step('Click button: Add to cart'):
        product_page.add_to_cart_button_click()
    with allure.step('Check alert'):
        product_page.alert_check()
    with allure.step('Check message'):
        assert title_book == product_page.product_title()


@allure.feature('Product page')
@allure.story('Add to cart')
def test_the_price_of_the_added_product_corresponds(driver):
    with allure.step('Open site'):
        product_page = ProductPage(driver)
        product_page.open_product_page()
        price_book = product_page.product_price()
    with allure.step('Click button: Add to cart'):
        product_page.add_to_cart_button_click()
    with allure.step('Check alert'):
        product_page.alert_check()
    with allure.step('Check message'):
        assert price_book == product_page.product_price()
