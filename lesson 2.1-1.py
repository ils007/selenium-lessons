import math,time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/get_attribute.html")
        x_element = browser.find_element_by_id("treasure")
        x = x_element.get_attribute("valuex")
        y = calc(x)
        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_id("answer")
        first.send_keys(y)
        checkbox = browser.find_element_by_id("robotCheckbox")
        checkbox.click()
        checkbox = browser.find_element_by_id("robotsRule")
        checkbox.click()
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла