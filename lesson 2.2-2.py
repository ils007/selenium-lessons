import math,time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/execute_script.html")
        x = browser.find_element_by_id("input_value")
        x = int(x.text)
        y = math.log(abs(12*math.sin(x)))
        browser.execute_script("arguments[0].scrollIntoView(true);",browser.find_element_by_id("answer"))
        browser.find_element_by_id("answer").send_keys(str(y))
        browser.execute_script("arguments[0].scrollIntoView(true);", browser.find_element_by_css_selector("button.btn"))
        checkbox = browser.find_element_by_id("robotCheckbox")
        checkbox.click()
        checkbox = browser.find_element_by_id("robotsRule")
        checkbox.click()
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