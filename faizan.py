from selenium import webdriver
from selenium.webdriver.common.by import By

#  we can use also through this .....>     search_box = find_by(how=By.xpath, "")

driver = webdriver.Chrome(executable_path="chromedriver.exe")

# open title of website
driver.get("https://www.goibibo.com/hotels/")
driver.maximize_window()

driver.find_element_by_xpath("(//*[contains(@class, 'dwebCommonstyles_SmallSectionHeader-sc-112ty3f-7 SearchBlockUIstyles_CheckInDateWrapDiv-sc-fity7j-14 hAEfdZ kSflmU')])[2]").click()