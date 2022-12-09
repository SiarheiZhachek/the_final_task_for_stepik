import allure
from pages.main_page import MainPage


@allure.feature('Home page')
@allure.story('Open site')
def test_guest_can_go_to_login_page(driver):
    with allure.step('Open web site'):
        main_page = MainPage(driver)
        main_page.open_site()
    with allure.step('Login link is displayed'):
        assert main_page.login_link_is_displayed()
    with allure.step('Click login button'):
        main_page.go_to_login_page()
    assert driver.current_url == 'http://selenium1py.pythonanywhere.com/accounts/login/'
