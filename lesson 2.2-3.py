import math,time,os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/file_input.html")
        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_name("firstname")
        first.send_keys("Имя")
        second = browser.find_element_by_name("lastname")
        second.send_keys("Имя")
        third = browser.find_element_by_name("email")
        third.send_keys("Имя")
        browser.find_element_by_id("file").send_keys(os.path.abspath('upload.txt'))



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