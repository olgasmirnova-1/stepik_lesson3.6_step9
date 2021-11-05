import pytest
import time


@pytest.mark.parametrize('language', ["es"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = len(browser.find_elements_by_css_selector("#add_to_basket_form > button"))        
        assert button > 0, 'Не нашел'    
