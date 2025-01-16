import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link2)

    # required_fields = browser.find_elements(By.CSS_SELECTOR, "[required]")
    #
    # for field in required_fields:
    #     field.send_keys("value")

    try:
        last_name = browser.find_element(
            By.CSS_SELECTOR,
            "div.first_block input.form-control.second"
        )
        last_name.send_keys("Petrov")
    except NoSuchElementException as err:
        print("NoSuchElementException had occur")
        raise err

    first_name = browser.find_element(
        By.CSS_SELECTOR,
        "div.first_block input.form-control.first"
    )
    first_name.send_keys("Andrey")

    email = browser.find_element(
        By.CSS_SELECTOR,
        "div.first_block input.form-control.third"
    )
    email.send_keys("andrew2124@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
