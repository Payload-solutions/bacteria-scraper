
# import unittest
# from pyunitreport import HTMLTestRunner
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By


# class HomePageTests(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
#         driver = self.driver
#         driver.get("http://demo-store.seleniumacademy.com/")
#         driver.maximize_window()
#         driver.implicitly_wait(30)
    
    
#     def test_search_tee(self):
#         driver = self.driver
#         search_field = driver.find_element_by_name('q')
#         search_field.clear()
        
#         search_field.send_keys('tee')
#         search_field.submit()
    
#     # def test_search_salt_shaker(self):
#     #     driver = self.driver
#     #     search_field = driver.find_element_by_name('q')
#     #     search_field.clear()
        
#     #     search_field.send_keys('salt shaker')
#     #     search_field.submit()
        
#     #     products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/a')
        
#     #     self.assertEqual(1, len(products))
        
    
#     def tearDown(self):
#         self.driver.quit()
    
    
#     # those test, are used to search for some element
#     # in the search fild, and comprove if it exists
    
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")
  

	def test_search_tee(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		search_field.clear() #limpia el campo de búsqueda en caso de que haya algún texto. 
		
		search_field.send_keys('tee') #simulamos la escritura del teclado para poner "tee"
		search_field.submit() #envía los datos ('tee') para que la página muestre los resultados de "tee"
		
	def test_search_salt_shaker(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		
		search_field.send_keys('salt shaker') #escribimos 'salt shaker' en la barra de búsqueda
		search_field.submit() #envíamos la petición

		#hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida.
		products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')

		#vamos a preguntar si la cantidad de resultados es igual a 1
		self.assertEqual(1, len(products))
		
	def tearDown(self):
		self.driver.quit()
    
    
    
    
#     # def test_search_field(self):
#     #     self.assertTrue(self.is_element_present(By.NAME, 'q'))
    
#     # def test_language_option(self):
#     #     self.assertTrue(self.is_element_present(By.ID, 'select-language'))
        
#     # def is_element_present(self, how, what):
#     #     try:
#     #         self.driver.find_element(by=how, value=what)
#     #     except NoSuchElementException as e:
#     #         return False
#     #     return True

