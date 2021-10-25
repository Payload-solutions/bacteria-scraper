
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)
        
        
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")
        
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")
    
    def tearDown(self):
        self.driver.quit()
    
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
    
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
        
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


def main():
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='ecommerce-test'))



if __name__ == "__main__":
    # http://demo-store.seleniumacademy.com/
    main()