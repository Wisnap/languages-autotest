import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_foreign_button_on_page(browser):
    browser.get(link)
    element = browser.find_element_by_class_name("btn-add-to-basket")
    #time.sleep(30)
    assert element.is_displayed(), "No button on page!"
    # line at the end
