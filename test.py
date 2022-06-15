from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class Test_class_name(unittest.TestCase):
    def test_name(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]').send_keys('Ivan')
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]').send_keys('Petrov')
        input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]').send_keys('Ivan@gmail.com')
        input4 = browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control first"]').send_keys('+128657263026')
        input5 = browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control second"]').send_keys('New-York')
        button = browser.find_element(By.XPATH, '//button[@type="submit"]')
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "FAILED")

    def test_name2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]').send_keys('Ivan')
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]').send_keys('Petrov')
        input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]').send_keys('Ivan@gmail.com')
        input4 = browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control first"]').send_keys('+128657263026')
        input5 = browser.find_element(By.XPATH, '//div[@class="second_block"]//input[@class="form-control second"]').send_keys('New-York')
        button = browser.find_element(By.XPATH, '//button[@type="submit"]')
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "FAILED")

if __name__ == "__main__":
    unittest.main()
