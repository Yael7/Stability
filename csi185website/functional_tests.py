# My computer history web site as an example

# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

        Nomadism leads toward the exchange and transformation of theological
        disciplinary and methodological borders. In seeking a balance between
        self-sustenance and self-edification, nomadic tribes transform their
        space-time relationship with the surrounding country into an ongoing
        search for meaning and a sense of home. 

        """

        self.browser.get('http://localhost:8000/index.html')

        # there is a page title defined by <title></title> on the home page
        # check it

        self.assertIn('Stability within Movement',self.browser.title)

        # You will have an image for your home page I am assuming.
        # Put the name of your image here in place of homebrew.png
        # In general this is how we check for images on a page.

        # The user sees an image of sun hitting the Washington Monument

        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('help.jpg',m.get_attribute('src'))

        a=self.browser.find_element_by_id('sun')
        a.click()

        self.assertIn('sun',self.browser.title)

        h=self.browser.find_element_by_tag_name('h1')
        m=self.browser.find_element_by_tag_name('img')

if __name__=="__main__":
        unittest.main(warnings="ignore")
