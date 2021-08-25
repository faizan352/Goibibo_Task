import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#  we can use also through this .....>     search_box = find_by(how=By.xpath, "")

driver = webdriver.Chrome(executable_path="chromedriver.exe")

# open title of website
driver.get("https://www.goibibo.com/hotels/")
driver.maximize_window()

time.sleep(2)
# click on country radio button
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/section/div[1]'
                             '/div/div[1]/div[1]/input').click()


time.sleep(2)
# click on date selection option for check-in and check-out
driver.find_element_by_xpath("//*[@id='root']/div[2]/div/section/div[1]"
                             "/div/div[3]/div/div[1]/div/h4").click()


time.sleep(2)
# check-in date
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]/div[3]"
    "/div/div[1]/div[2]/section/div/div[1]/div[2]/div/ul["
    "2]/li[37]/span").click()


time.sleep(2)
# checkout-date
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]/div[3]"
    "/div/div[1]/div[2]/section/div/div[2]/div[2]/div/ul["
    "2]/li[3]/span").click()


time.sleep(2)
# Total night count
print(driver.find_element_by_xpath("//*[@id='root']/div[2]/div/section[1]"
                                   "/div[1]/div/div[3]/div/div[3]").text)


time.sleep(2)
# click room selection
driver.find_element_by_xpath("//*[@id='root']/div[2]/div/section[1]"
                             "/div[1]/div/div[4]/div/input").click()


time.sleep(2)
# Room
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
    "/div[4]/div/div/div/div[1]/div/span[2]").click()


time.sleep(2)
# Adult
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]"
    "/div[2]/div[4]/div/div/div/div[2]/div/span[2]").click()


time.sleep(2)
# child
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]"
    "/div[1]/div[2]/div[4]/div/div/div/div[3]/div/span[2]").click()

driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
    "/div[4]/div/div/div/div[3]/div/span[2]").click()


time.sleep(2)
# child dropdown enable
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
    "/div[4]/div/div/div/div[4]/div").click()
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
    "/div[4]/div/div/div/div[4]/ul/li[3]").click()


time.sleep(2)
# select age
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
    "/div[4]/div/div/div/div[5]/div").click()
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
    "/div[4]/div/div/div/div[5]/ul/li[3]").click()


print("Two child de")
time.sleep(2)


# click done Button
driver.find_element_by_xpath(
    "//*[@id='root']/div[2]/div/section[1]/div[1]/div[2]"
    "/div[4]/div/div/div/div[6]/button").click()


time.sleep(5)
# click on dropdown city
driver.find_element_by_xpath("//*[@id='root']/div[2]/div/section[1]"
                             "/div[1]/div/div[2]/div/div").click()


time.sleep(2)
# select city
driver.find_element_by_xpath("//p[text()='Mumbai']").click()

time.sleep(3)
driver.close()
