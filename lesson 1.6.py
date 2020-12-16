import math,time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/find_xpath_form"

if __name__ == '__main__':

    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(link)
        # link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
        # link.click()

        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id("country")
        input4.send_keys("Russia")
        button = browser.find_element_by_xpath("//button[contains(text(), 'Submit')]")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

# не забываем оставить пустую строку в конце файла