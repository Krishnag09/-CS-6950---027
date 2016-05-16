from lxml import html
from bs4 import BeautifulSoup
import requests
import math
import csv
from requests import get
from selenium import webdriver
import socks
import socket
import string
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import datetime
from datetime import datetime
from datetime import timedelta
now = datetime.now()
print now
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

chrome_options = Options()
PROXY = "162.245.62.166:1000" 
chrome_path= "/Users/krishna/Downloads/chromedriver"
chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
top_countries_list= ""
#driver = webdriver.Chrome(chrome_path,chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_path)
with open('Most_funded_Security_USA.csv','a') as csvfile:
     fieldnames= ['ID','url','status','name','short-description','proj_description','proj_location','proj_creator','proj_milestones', 'proj_creatorinfo','creator-history','project_rewards','no-of-updates','allrewards','noofrewards','updates','proj_backers','new_backers','existing_backers','proj_raised','proj_goal','proj_goaldate','proj_startdate','comment-count','all-comments','top-cities','top-countries']
     writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
     writer.writeheader()

#days_left1= driver.find_element_by_css_selector('#stats > div > div:nth-child(4) > div > div > span').text
#days_left= driver.find_element_by_css_selector('div.col.col-12.stat-item').text
#print days_left1   
driver.implicitly_wait(3)
url='https://www.kickstarter.com'
#pagelink='https://www.kickstarter.com/discover/advanced?state=successful&term=security&category_id=16&sort=magic&seed=2415916&page=1' #working
pagelink='https://www.kickstarter.com/discover/advanced?term=security&category_id=16&woe_id=23424977&sort=most_funded&seed=2432592&page=1' #working
page_first = requests.get(pagelink)
tree = html.fromstring(page_first.content)
projectcountdiv=tree.xpath('//*[@id="projects"]/div/h3/b')[0].text
project_count=int(projectcountdiv.split()[0])
print project_count
project_index_pages= float(project_count)/20 
project_index_pages1= int(math.ceil(project_index_pages))
def truncate_string(mystring, numberofwords):
    return ' '.join(mystring.split()[:numberofwords])
for x in range (1, project_index_pages1+1):
    print x
    #page_master_index=requests.get('https://www.kickstarter.com/discover/advanced?term=security&category_id=16&sort=end_date&seed=2430946&page='+ str(x))
    page_master_index=driver.get('https://www.kickstarter.com/discover/advanced?term=security&category_id=16&woe_id=23424977&sort=most_funded&seed=2432592&page='+ str(x))
    #projectlink= driver.find_elements_by_css_selector('#projects_list > div:nth-child(1) > li:nth-child(1) > div > div.project-thumbnail > a')
    projectlink= driver.find_elements_by_css_selector('div.project-profile-title')

    links=[]
    i=0
    for linkx in projectlink:
        #print linkx.text
    	link1=linkx.find_element_by_css_selector('a').get_attribute('href')
        link1= link1.split('?', 1)[0]
        print link1
    	links.append(link1)
    for link in links:
        i=i+1
        print i
        #print link
        project_desc_link= link+'/description'
        #creator_bio_page= link+ '/creator_bio'
        driver.get(project_desc_link)
        #driver.implicitly_wait(2)
        #location= driver.find_element_by_css_selector('#content-wrap > section > div.container-flex.px2 > div:nth-child(2) > div.col.col-8.py4 > div > div.h5.mb3 > div > a:nth-child(1)').text  #works for all except the sucessful
        location_cat= driver.find_element_by_css_selector('div.NS_projects__category_location').text #works for all typpes
        split_cat_loc= location_cat.split()
        location= split_cat_loc[0]+ split_cat_loc[1]

        project_community= link+ '/community'

        driver.get(project_community)
        name= driver.find_element_by_css_selector('div.NS_project_profile__title').text
        #name= " "
        with open('location_data.csv','a') as csvfile:
             fieldnames= ['Name','Url','location','top-cities','top-city-country','top_cities_data','top-countries','top_countries_data']
             writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
             writer.writerow({'Name':name,'Url': link,'location':location})
        try:
            
            top_places= driver.find_elements_by_css_selector('div.primary-text.js-location-primary-text')
            top_places_len= len(top_places)
            top_places_data= driver.find_elements_by_css_selector('div.tertiary-text.js-location-tertiary-text')
            top_cities_countries= driver.find_elements_by_css_selector('div.secondary-text.js-location-secondary-text')
            for x in xrange(10):
                try:
                    #print top_places[x].text
                    #print top_places_data[x].text
                    y= x+10
                    if y <= top_places_len-1:
                        print top_places[x].text
                        print top_places[y].text
                        with open('location_data.csv','a') as csvfile:
                            fieldnames= ['Name','Url','location','top-cities','top-city-country','top_cities_data','top-countries','top_countries_data']
                            writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
                            writer.writerow({'top-cities':top_places[x].text, 'top-city-country':top_cities_countries[x].text,'top_cities_data':top_places_data[x].text,'top-countries': top_places[y].text,'top_countries_data':top_places_data[y].text})
                    else:
                        with open('location_data.csv','a') as csvfile:
                            fieldnames= ['Name','Url','location','top-cities','top-city-country','top_cities_data','top-countries','top_countries_data']
                            writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
                            writer.writerow({'top-cities':top_places[x].text, 'top-city-country':top_cities_countries[x].text,'top_cities_data':top_places_data[x].text})
                        

                except NoSuchElementException:
                    print "hello"



        except NoSuchElementException:

            print "hello"




