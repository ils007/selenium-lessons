import math,time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/selects2.html")
        x = browser.find_element_by_id("num1")
        x = int(x.text)
        y = browser.find_element_by_id("num2")
        y = int(y.text)
        browser.find_element_by_id("dropdown").click()
        browser.find_element_by_css_selector(f"[value='{x+y}'").click()
        # Ваш код, который заполняет обязательные поля

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла