import pytest as pytest
from selenium import webdriver
import unittest
import HtmlTestRunner


class Test_Grid(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.maximize_window()

    def test_homepagetitle(self):
        self.driver.get('https://www.goibibo.com/hotels/')

        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section/div[1]'
                                          '/div/div[1]/div[1]/input').click()

        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]/div[1]/div/div[3]'
                                          '/div/div[1]/div/div').click()
        # check-in date
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]/div[1]/div[2]'
                                          '/div[3]/div/div[1]/div[2]/section/div/div[1]/div[2]'
                                          '/div/ul[2]/li[37]/span').click()
        # checkout-date
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]/div[1]/div[2]'
                                          '/div[3]/div/div[1]/div[2]/section/div/div[2]/div[2]'
                                          '/div/ul[2]/li[6]/span').click()

        # Total night count
         #self.print(driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]/div[1]'
                                          #'/div/div[3]/div/div[3]').text)

        # click on room selection
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]/div[1]/div/'
                                          'div[4]/span').click()

        # Room
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]/div[1]/div[2]'
                                          '/div[4]/div/div/div/div[1]/div/span[2]').click()

        # Adult
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section[1]'
                                          '/div[1]/div[2]/div[4]/div/div/div/div[2]'
                                          '/div/span[2]').click()

        # Children
        self.driver.find_element_by_xpath("//*[@id='root']/div[2]/div/section[1]"
                                          "/div[1]/div[2]/div[4]/div/div/div/div[3]"
                                          "/div/span[2]").click()

        self.driver.find_element_by_xpath(
            "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
            "/div[4]/div/div/div/div[3]/div/span[2]").click()

        # click on dropdown city
        self.driver.find_element_by_xpath("//*[@id='root']/div[2]/div/section[1]"
                                          "/div[1]/div/div[2]/div/div").click()

        # select city
        self.driver.find_element_by_xpath("//p[text()='Mumbai']").click()

        # child dropdown enable
        self.driver.find_element_by_xpath(
            "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
            "/div[4]/div/div/div/div[4]/div").click()
        self.driver.find_element_by_xpath(
            "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
            "/div[4]/div/div/div/div[4]/ul/li[3]").click()

        # select age
        self.driver.find_element_by_xpath(
            "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
            "/div[4]/div/div/div/div[5]/div").click()
        self.driver.find_element_by_xpath(
            "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
            "/div[4]/div/div/div/div[5]/ul/li[3]").click()

        print("Two child de")

        # click done Button
        self.driver.find_element_by_xpath(
            "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
            "/div[4]/div/div/div/div[6]/button").click()

        # click on dropdown city
        self.driver.find_element_by_xpath("//*[@id='root']/div[2]/div/section[1]"
                                          "/div[1]/div/div[2]/div/div").click()

        # select city
        self.driver.find_element_by_xpath("//p[text()='Mumbai']").click()

        self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/ANSARI/'
                                                                  'PycharmProjects/TestGrid/reports'))

