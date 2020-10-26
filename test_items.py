import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_see_correct_language(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_css_selector("#login_link")