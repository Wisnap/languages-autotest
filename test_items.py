import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_see_correct_espanol_language(browser):
    browser.get(link)
    #time.sleep(30)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    value = button.text
    assert value in "Añadir al carrito", "Incorrect text in button!"
