import math,time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_css_selector(".first_block .first")
        first.send_keys("Имя")
        second = browser.find_element_by_css_selector(".first_block .second")
        second.send_keys("Имя")
        third = browser.find_element_by_css_selector(".first_block .third")
        third.send_keys("Имя")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text




    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла