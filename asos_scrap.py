from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.asos.com/us/men/")
driver.maximize_window()
time.sleep(5)

xpath = '/html/body/div[2]/div/div[2]/header/div[3]/div/div[2]/div[2]/nav/div/div/button[3]'
time.sleep(5)

new_elements = driver.find_elements(By.XPATH, xpath)
a = []
b = []

if new_elements:
    new_elements[0].click()
    time.sleep(5)
    view_all = driver.find_element(By.PARTIAL_LINK_TEXT, 'Top Rated Clothing')
    view_all.click()
    time.sleep(5)

    while True:
        try:
            load_button = driver.find_element(By.CLASS_NAME, 'loadButton_wWQ3F')
            if load_button:
                load_button.click()
                time.sleep(2)
        except NoSuchElementException:
            break

    product_names = driver.find_elements(By.CLASS_NAME, 'productDescription_sryaw')
    prices = driver.find_elements(By.CLASS_NAME, 'container_s8SSI')

    for product_name, price in zip(product_names, prices):
        print(product_name.text)
        a.append(product_name.text)
        print(price.text)
        b.append(price.text)


    df = pd.DataFrame({'Product Name': a, 'Price': b})


    df.to_excel('product_names.xlsx', index=False)
else:
    print("No elements found matching the specified XPath")
