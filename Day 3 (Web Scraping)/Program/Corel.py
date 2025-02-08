"""Kb Corel Scrapper"""

#Importing Required Libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
# from webdriver_manager.chrome import ChromeDriverManager

#Setting Up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome()

#Opening the Web Page
#chrome instance
driver.get("https://kb.corel.com/en/125936")
time.sleep(1)

#Extracting Table Data
tables = driver.find_element(By.XPATH, "//table")
all_table_rows = tables.find_elements(By.XPATH, ".//tr")

#Storing Table Data
list_of_rows = []
 
for each_row in all_table_rows:
    list_of_data = []
    all_data = each_row.find_elements(By.XPATH, ".//td")
    for data in all_data:
        list_of_data.append(data.text)
        print(list_of_data)
    list_of_rows.append(list_of_data)
print(list_of_rows)
 
#Converting Data into a CSV File
df = pd.DataFrame(list_of_rows[1:], columns = list_of_rows[0])
df.to_csv("korel.csv", index = False)
print(df)
