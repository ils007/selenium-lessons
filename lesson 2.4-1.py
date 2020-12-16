import math,time,os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/explicit_wait2.html")
        button = browser.find_element_by_css_selector("button.btn")

        WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.ID, "price"),'$100')
        )
        button.click()
        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_id("input_value").text
        second = browser.find_element_by_id("answer")
        second.send_keys(calc(first))

        # Отправляем заполненную форму
        button = browser.find_element_by_id("solve")
        button.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла