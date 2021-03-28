from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")

webdriver=webdriver.Chrome(
    options=chrome_options
)
#Population
#Median Age
#Income
#Employees
#Property Value

webdriver.get('https://datausa.io/profile/geo/tampa-fl')
# https://www.macrotrends.net/cities/us/fl/clearwater/crime-rate-statistics#:~:text=The%20Florida%20City%20FL%20crime%20rate%20for%202017%20was%202275.89,a%2013.84%25%20increase%20from%202014.

soup=BeautifulSoup(webdriver.page_source, 'html.parser')

# print(soup.prettify())

stats = soup.find(class_ = 'profile-stats')

titles = stats.find_all(class_='stat-title')
values = stats.find_all(class_='stat-value')
subtitle = stats.find_all(class_='stat-subtitle')

datausa = {}

for idx, val in enumerate(titles):
    datausa[val.find('p').text] = [values[idx].find('p').text, subtitle[idx].find('p').text]

print(datausa)
