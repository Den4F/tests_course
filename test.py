from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_window = browser.window_handles[0]
    button = browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    z = browser.find_element(By.ID, 'answer').send_keys(y)
    click_submit = browser.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

