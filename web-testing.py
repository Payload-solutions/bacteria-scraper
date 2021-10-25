
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)
        
        
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")
    
    def tearDown(self):
        self.driver.quit()


def main():
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='ecommerce-test'))



if __name__ == "__main__":
    # http://demo-store.seleniumacademy.com/
    main()