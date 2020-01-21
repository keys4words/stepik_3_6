import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
time.sleep(30)

def test_product_page_contains_add_to_cart_button(browser):
    browser.get(link)
    button_text = (browser.find_element_by_css_selector("button.btn-add-to-basket")).text
    assert len(button_text) > 0, '-------!!! no button Add to cart on the page !!!--------'