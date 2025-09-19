from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import csv

print(f"Начало {datetime.datetime.now()}")

url = 'https://www.divan.ru/category/divany/'
file_path = 'prices.csv'

options = Options()
options.page_load_strategy = "eager"
driver = webdriver.Chrome(options=options)

driver.get(url)

url_len = len(driver.current_url)

pageLinks = driver.find_elements(By.CLASS_NAME, "PaginationLink")
pages = []

for link in pageLinks:
    ref = link.get_attribute("href")
    if ref and ref != driver.current_url:
        if not ref in pages:
            pages.append(ref)

pages.insert(0, driver.current_url)

with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])

    for i in range(len(pages)):
        if i > 0:
            driver.get(pages[i])

        prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")

        cnt = 0

        for price in prices:
            if price.text:
                writer.writerow([int(price.text.replace(' ', ''))])
                cnt += 1

        print(f"стр. {pages[i][url_len:]}, кол. {cnt}, время {datetime.datetime.now()}")

driver.quit()

data = pd.read_csv(file_path)
prices = data['Price']

print(f"Средняя цена: {prices.mean()}")

plt.hist(prices, bins=10, edgecolor='black')

plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')

print(f"Конец {datetime.datetime.now()}")

plt.show()