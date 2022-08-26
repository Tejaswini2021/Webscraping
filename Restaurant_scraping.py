import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# default path to file to store data
path_to_file = "C:/Users/TNALUBAL/Desktop/Reviews1.csv"

# default number of scraped pages
num_page = 3

# default tripadvisor website of restaurant
url = "https://www.tripadvisor.com/Restaurant_Review-g297628-d13356884-Reviews-One_Atria_Cafe-Bengaluru_Bangalore_District_Karnataka.html#REVIEWS"


# Import the webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)

for i in range(0, num_page):
    
    # expand the review 
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='taLnk ulBlueLinks']").click()

    container = driver.find_elements(By.XPATH,".//div[@class='review-container']")
 
    for j in range(len(container)):

       title = container[j].find_element(By.XPATH,".//span[@class='noQuotes']").text
       date = container[j].find_element(By.XPATH,".//span[contains(@class, 'ratingDate')]").get_attribute("title")
       rating = container[j].find_element(By.XPATH,".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
       review = container[j].find_element(By.XPATH,".//p[@class='partial_entry']").text.replace("\n", " ")
       
       print("title:" ,title)

       print("date",date)
       print("rating:" ,rating)
       print("review",review)



    # change the page
    driver.find_element(By.XPATH,'.//a[@class="nav next ui_button primary"]').click()

driver.close()
