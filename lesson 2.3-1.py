import math,time,os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/alert_accept.html")
        # Ваш код, который заполняет обязательные поля
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        confirm = browser.switch_to.alert
        confirm.accept()
        first = browser.find_element_by_id("input_value").text
        second = browser.find_element_by_id("answer")
        second.send_keys(calc(first))

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Ваш код, который заполняет обязательные поля

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла