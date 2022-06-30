from distutils.filelist import findall
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome(executable_path=r"C:/Users/mikat/Desktop/python/webscraping/chromedriver.exe")

headers = ["name", "distance", "mass", "radius"]
new_planets_data = []
def scrape_more_data():
    try:
        page =requests.get(START_URL)
        soup = BeautifulSoup(browser.page_source, "html.parser")

        temp_list = []
        startable =soup.find_all("table")
        for tr_tag in startable.find_all("tr"):
            td_tags = tr_tag.find_all("td")
          
            for td_tag in td_tags:
                try: 
                    temp_list.append(td_tag.find_all("a", attrs={"class": "new"})[0].contents[0])
                except:
                    temp_list.append("")
                    
        new_planets_data.append(temp_list)

    except:
        time.sleep(1)
        scrape_more_data()

#Calling method

for index, data in enumerate(new_planets_data):
    scrape_more_data(data[5])
    print(f"scraping at hyperlink {index+1} is completed.")

print(new_planets_data[0:10])
final_planet_data = []

for index, data in enumerate(new_planets_data):
    new_planet_data_element = new_planets_data[index]
    new_planet_data_element = [elem.replace("\n", "") for elem in new_planet_data_element]
    new_planet_data_element = new_planet_data_element[:7]
    final_planet_data.append(data + new_planet_data_element)

with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_planet_data)
