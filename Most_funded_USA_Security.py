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
        print linkx.text
    	link1=linkx.find_element_by_css_selector('a').get_attribute('href')
        link1= link1.split('?', 1)[0]
        print link1
    	links.append(link1)
    for link in links[9:]:
        print link
        project_desc_link= link+'/description'
        creator_bio_page= link+ '/creator_bio'
        project_community= link+ '/community'
        project_comments=  link+ '/comments'
        project_updates=   link+ '/updates'
        project_post= link+ '/posts'
        driver.get(project_desc_link)
        #driver.implicitly_wait(2)
        #project_name= driver.find_element_by_css_selector('h2.normal.mb1').text
        project_name= driver.find_element_by_css_selector('a.hero__link').text
        #toggle1= driver.find_elements_by_class_name("js-faq-question-toggle").click()
        f1= driver.find_elements_by_class_name("faq-answer")
        project_desc= driver.find_element_by_css_selector('div.full-description.js-full-description.responsive-media.formatted-lists').text
        #location= driver.find_element_by_css_selector('#content-wrap > section > div.container-flex.px2 > div:nth-child(2) > div.col.col-8.py4 > div > div.h5.mb3 > div > a:nth-child(1)').text  #works for all except the sucessful
        location_cat= driver.find_element_by_css_selector('div.NS_projects__category_location').text #works for all typpes
        print location_cat
        split_cat_loc= location_cat.split()
        location= split_cat_loc[0]+ split_cat_loc[1]
        #category= split_cat_loc[2]
        #backers= driver.find_element_by_css_selector('div#backers_count.num.h1.bold').text #works for all except the sucessful
        #backers_field= driver.find_element_by_xpath("//*[contains(text(), 'backers')]").text #could work for all
        backers_info= driver.find_element_by_css_selector('div.NS_projects__spotlight_stats').text
        backers= backers_info.split()
        noof_backers= backers[0]
        print noof_backers
        #backers=backers_field
        #print backers_field
        #backers_split= backers_field.split()
        #backers= backers_split[0]
        #raisedmoney= driver.find_element_by_css_selector('div#pledged.num.h1.bold.nowrap').text
        funding_period= driver.find_element_by_css_selector('div.NS_projects__funding_period').text
        funding_period_split= funding_period.split()
        #funding_period_test=funding_period_test.text
        #short_description= driver.find_element_by_css_selector('p.h3.mb3').text
        #short_description=driver.find_element_by_css_selector('h3.normal').text
        short_description= driver.find_element_by_css_selector('span.content.edit-profile-blurb.js-edit-profile-blurb').text
        print short_description
        #category= driver.find_element_by_css_selector('a.grey-dark.mr3.nowrap').text
        #category= driver.find_element_by_xpath('//*[@id="content-wrap"]/div[2]/section[1]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div/a[2]').text
        #rewards= driver.find_elements_by_css_selector('li.hover-group.js-reward-available.pledge--available.pledge-selectable-sidebar')
        rewards= driver.find_elements_by_css_selector('div.pledge__info')
        allrewards=""
        noofrewards= len(rewards)
        for reward in rewards:
            allrewards= allrewards+ "  " + reward.text
        raisedmoney= driver.find_element_by_css_selector('h3.mb1').text
        print raisedmoney
        goalmoney= driver.find_element_by_xpath("//*[contains(text(), 'pledged of')]").text
        status= "Sucessfully Over"
        #timeline= driver.find_elements_by_css_selector('time.js-adjust-time')
        #timeline= funding_period_test.find_elements_by_css_selector('time').get_attribute('js-adjust-time')
        #start_date= timeline[0].text
        start_date= funding_period_split[2]+ " " + funding_period_split[3]+ " " + funding_period_split[4]
        print start_date
        end_date= funding_period_split[6]+ " " + funding_period_split[7]+ " " +funding_period_split[8]
        print end_date
        funding_days1= funding_period_split[9]
        funding_days= funding_days1[1:4] 
        print funding_days
        #end_date= timeline[1].text
        driver.get(project_post)
        updates= driver.find_elements_by_css_selector('div.post')
        noof_updates= driver.find_element_by_xpath('//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[3]/span').text
        print noof_updates
        allupdates= ""
        for update in updates:
            allupdates= allupdates + update.text
        driver.get(creator_bio_page) # moving to founders page,need to test this
        driver.implicitly_wait(3)
        creator_name= driver.find_element_by_css_selector('h1.h2.normal.mb1').text
        creator_history= driver.find_element_by_css_selector('div.created-projects.py1.h5.mb2').text
        try:
        	more_info= driver.find_element_by_link_text('See full profile').click() # if the content is beyond the default bio page
        	detail_info= driver.find_element_by_css_selector('a.remote_modal_dialog').click()
        	driver.implicitly_wait(3)
        	#more_info= driver.find_element_by_css_selector('a.btn.btn--gray.btn--small').click()
        	creator_info= driver.find_element_by_css_selector('div#profile-bio-full').text
        except NoSuchElementException:
        	creator_info= driver.find_element_by_css_selector('div.col.col-7.col-post-1.pt2.pb6').text

        driver.get(project_community)  # getting the top countries & top cities by backers
        top_cities= ""
        top_countries= ""
        new_backers= 0
        existing_backers= 0

        try:
            top_cities= driver.find_element_by_css_selector('div.location-list.js-locations-cities').text
            top_countries= driver.find_element_by_css_selector('div.location-list.js-locations-countries').text
            top_cities= driver.find_element_by_css_selector('div.location-list.js-locations-cities').text
            top_countries= driver.find_element_by_css_selector('div.location-list.js-locations-countries').text
            backers_data1= driver.find_element_by_css_selector('div.new-backers').text
            new_backers= backers_data1.split()[2]
            backers_data2= driver.find_element_by_css_selector('div.existing-backers').text
            existing_backers= backers_data2.split()[2]

        except NoSuchElementException:
            print "hello"

        #backers_locations= driver.find_elements_by_class_name("js-location-primary-text")

        #else:
            #top_countries= "NA"
            #top_cities= "NA"
        driver.get(project_comments) # getting project comments
        comments= driver.find_elements_by_css_selector("div.comment-inner")
        #comment_count= driver.find_element_by_css_selector("span.count")
        comment_count= driver.find_element_by_xpath('//*[@id="content-wrap"]/div[2]/div/div/div/div[2]/a[4]/span').text
        #click_more_comments= Show older comments
        #comment_count= len(comments)
        print comment_count
        allcomments= ""
        for comment in comments:
            comment= comment.text
            allcomments= allcomments + comment

        with open('Most_funded_Security_USA_.0.csv','a') as csvfile:
             fieldnames= ['ID','url','status','name','short-description','proj_description','proj_location','proj_creator','proj_milestones', 'proj_creatorinfo','creator-history','project_rewards','no-of-updates','allrewards','noofrewards','updates','proj_backers','new_backers', 'existing_backers','proj_raised','proj_goal','proj_goaldate','proj_startdate','funding_period','comment-count','all-comments','top-cities','top-countries']
             writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
             #milestones= milestones.encode('utf-8')
             project_name= project_name.encode('utf-8')
             project_desc= project_desc.encode('utf-8')
             location= location.encode('utf-8')
             short_description= short_description.encode('utf-8')
             #category= category.encode('utf-8')
             #backers= backers.encode('utf-8')
             #raisedmoney= raisedmoney.encode('utf-8')
             goalmoney= goalmoney.encode('utf-8')
             allupdates= allupdates.encode('utf-8')
             allcomments= allcomments.encode('utf-8')
             link= link.encode('utf-8')
             project_desc= project_desc.decode().encode('utf-8')
             #noof_updates= noof_updates.encode('utf-8')
             allrewards= allrewards.encode('utf-8')
             #start_date= start_date.encode('utf-8')
             #end_date= end_date.encode('utf-8')
             #noof_updates= noof_updates.encode('utf-8')
             #funding_period= funding_period.encode('utf-8')
             creator_name= creator_name.encode('utf-8')
             creator_history= creator_history.encode('utf-8')
             creator_info= creator_info.encode('utf-8')
             top_cities= top_cities.encode('utf-8')
             top_countries= top_countries.encode('utf-8')
             #comment_count= comment_count.encode('utf-8')
             #allcomments= allcomments.encode('utf-8')
             ID= i+1
             print i
             #writer.writerow({'ID':ID,'url': link,'status':status,'name': project_name,'short-description':short_description,'proj_description': project_desc,'proj_location':location,'proj_creator':creator_name, 'proj_milestones':allupdates,'no-of-updates':noof_updates,'proj_creatorinfo':creator_info,'creator-history':creator_history,'allrewards':allrewards, 'noofrewards':noofrewards,'proj_backers': noof_backers,'new_backers':new_backers, 'existing_backers':existing_backers,'proj_raised': raisedmoney,'proj_goal': goalmoney,'comment-count' : comment_count,'all-comments':allcomments,'proj_goaldate': end_date,'proj_startdate': start_date,'funding_period':funding_days,'top-cities':top_cities,'top-countries':top_countries})
             i=i+1
             
 
            




