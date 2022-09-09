import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_path_driver = "L:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_path_driver))
driver.get("https://www.olx.in")

location_drop = driver.find_element(By.CSS_SELECTOR, ".rui-1rYgw")
location_drop.click()

current_loc = driver.find_element(By.CSS_SELECTOR, "._1nWq6")
current_loc.click()

search = driver.find_element(By.CSS_SELECTOR, ".rui-1Azjs input")
search.send_keys("Apple Macbook Pro 13 inch")
search.send_keys(Keys.ENTER)

time.sleep(3)

list_of_links = driver.find_elements(By.CSS_SELECTOR, ".EIR5N a")
list_of_price = driver.find_elements(By.CSS_SELECTOR, ".EIR5N ._89yzn")
list_of_names = driver.find_elements(By.CSS_SELECTOR, ".EIR5N ._2tW1I")

all_data = [(name.text, price.text, link.get_attribute("href")) for name, price, link in
            zip(list_of_names, list_of_price, list_of_links)]

for data in all_data:
    if int(data[1].lstrip("₹ ").replace(",", "")) <= 40000:
        driver.get("https://forms.gle/mGvFRvNdVW9VuYrS9")
        name_path = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/'
                                        'div/div/div[2]/div/div[1]/div/div[1]/input')
        price_path = driver.find_element(By.XPATH,
                                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                         '/div/div[1]/div/div[1]/input')
        address_path = driver.find_element(By.TAG_NAME, "textarea")
        submit = driver.find_element(By.CSS_SELECTOR, ".l4V7wb")
        name_path.send_keys(data[0])
        price_path.send_keys(data[1])
        address_path.send_keys(data[2])
        submit.click()

driver.quit()
