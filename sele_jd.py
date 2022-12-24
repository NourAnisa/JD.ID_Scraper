from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

url = 'https://www.jd.id/search?keywords=jilbab'

# options = Options()
# options.add_argument("--headless")
browser = webdriver.Chrome("chromedriver.exe")
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')


data = []
table = soup.find_all('div', {"class": "p-info"})
for x, div in enumerate(table):
    title = div.find("div", class_="p-name").text
    harga = div.find("div", class_="p-price-zj").text
    obj = {
        "name": title,
        "price": harga,
    }
    data.append(obj)

print(data)
