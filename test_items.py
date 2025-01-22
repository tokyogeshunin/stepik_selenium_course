import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_btn_add_to_card_exist(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)
    time.sleep(30)

    try:
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except NoSuchElementException:
        assert False, "There is no add to card button on the page"
