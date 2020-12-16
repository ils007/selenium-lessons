import math,time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/find_link_text"

if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements_by_tag_name ("input")
        for element in elements:
            element.send_keys("Мой ответ")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()



    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла