from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.get("https://www.meesho.com/men-watches/pl/3k7")
driver.implicitly_wait(10)

html = driver.page_source

driver.quit()

soup = BeautifulSoup(html, 'html.parser')

product_boxes = soup.find_all('div', class_="sc-dkrFOg ProductList__GridCol-sc-8lnc8o-0 cokuZA eCJiSA")
names = []
prices = []
ratings = []
for box in product_boxes:
    name_tag = box.find('div', class_="NewProductCardstyled__ProductHeaderWrapper-sc-6y2tys-30 gspQJ")
    name = name_tag.text if name_tag else "N/A"
    names.append(name)
    price_tag = box.find('h5', class_="sc-eDvSVe dwCrSh")
    price = price_tag.text if price_tag else "N/A"
    prices.append(price)
    rating_tag = box.find('span', class_="sc-eDvSVe laVOtN")
    rating = rating_tag.text if rating_tag else "N/A"
    ratings.append(rating)
data = {
    'Name': names,
    'Price': prices,
    'Rating': ratings
}
df = pd.DataFrame(data)
df.to_csv('meesho_men_watches.csv', index=False)

print("Data has been successfully scraped and saved to 'meesho_men_watches.csv'.")
