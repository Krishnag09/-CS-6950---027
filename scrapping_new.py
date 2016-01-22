from lxml import html
import requests
import math
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#binary = FirefoxBinary('path/to/binary')
#driver = webdriver.Firefox(firefox_binary=binary)


url='https://www.kickstarter.com'
page_first = requests.get('https://www.kickstarter.com/discover/advanced?state=successful&term=security&category_id=16&sort=magic&seed=2415916&page=1')
tree = html.fromstring(page_first.content)
projectcountdiv=tree.xpath('//*[@id="projects"]/div/h3/b')[0].text
project_count=int(projectcountdiv.split()[0])
project_index_pages= float(project_count)/20 
project_index_pages1= int(math.ceil(project_index_pages))
for x in range (1, project_index_pages1+1):
    page_master_index=requests.get('https://www.kickstarter.com/discover/advanced?state=successful&term=security&category_id=16&sort=magic&seed=2415916&page='+ str(x))
    tree1=html.fromstring(page_master_index.content)
    projectlink= tree1.xpath('//*[@id="projects_list"]/li/div/div/div/a/@href')
    for link in projectlink:
        link= url + link
        #print link
        projectpage= requests.get(link)
        projecttree = html.fromstring(projectpage.content)
        backers= projecttree.xpath('//*[@id="content-wrap"]/section/div/div/div/div/div/div/b')[0].text
        print backers
        raisedmoney= projecttree.xpath('//*[@id="content-wrap"]/section/div/div/div/div/div/div/span')[0].text
        print raisedmoney
        project_name= projecttree.xpath('//*[@id="content-wrap"]/section/div/div/h2/span/a')[0].text
        print project_name
        goal_date= projecttree.xpath('//*[@id="content-wrap"]/div/section/div/div/div/div/div/div/div[1]/time')[0].text
        print goal_date
        start_date= projecttree.xpath('//*[@id="content-wrap"]/div/section/div/div/div/div/div/div/div/time')[0].text
        print start_date

        #project_desc= projecttree.xpath('//*[@id="projects_list"]/li/div/div/p/text()')
        link_strip=link[:-14]
        projectpage1= requests.get(link_strip)
        projecttree1= html.fromstring(projectpage1.content)
        #project_desc= projecttree1.xpath('//*[@id="content-wrap"]/section/div/div/div/div/div/div/div/span/span')[0].text
        project_desc= projecttree.xpath('//*[@id="projects_show"]/div/div/div/ul/li/div/div/p')
        link_decs=link_strip+'/description'
        print link_strip
        print project_desc
        driver =webdriver.Firefox()
        driver.get(link_decs)
        tree = lxml.html.fromstring(driver.page_source)
        
        #project_desc= tree.xpath('//*[@id="content-wrap"]/section/div/div/div/div/div/div/div/span/span')[0].text

        #project_desc_link= requests.get('https://www.kickstarter.com/projects/xolutronic/passfort-your-digital-life-secure/description')
        #project_desc_tree=html.fromstring(project_desc_link.content)
        print project_desc
        #project_desc= project_desc_tree.xpath('//*[@id="content-wrap"]/div/section/div/div/div/div/div/div/h1/text()')
        #project_desc= project_desc_tree.xpath('//*[@id="content-wrap"]/div/section/div/div/div/div/div/div/h1')[0].text
        #project_desc= project_desc_tree.xpath('///*[@id="content-wrap"]/div/section/div/div/div/div/div/div/h1')
        #location= project_desc_tree.xpath('//*[@id="content-wrap"]/div/section/div/div/div/div/div/div/div/div/div/a/')[0].text
        

  

        
