import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_foreign_button_on_page(browser):
    browser.get(link)
    #time.sleep(30)
    assert browser.find_element_by_class_name("btn-add-to-basket"), "No button on page!"
    # line at the end
