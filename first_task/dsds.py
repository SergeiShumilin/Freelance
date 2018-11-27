from selenium import webdriver
from selenium.webdriver.support import ui

url = "https://chrome.google.com/webstore/detail/emoji-keyboard-by-emojion/ipdjnhgkpapgippgcgkfcbpdpcgifncb?hl=en"

driver = webdriver.Chrome()
wait = ui.WebDriverWait(driver, 10)
driver.get(url)
wait.until(lambda driver: driver.find_element_by_xpath('//div[.="Reviews"]')).click()
wait.until(lambda driver: driver.find_element_by_xpath('//a[.="Next »"]')).click()
#driver.quit()