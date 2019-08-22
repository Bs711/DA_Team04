# Display an “OK same as 200” return status
import requests
url ="http://172.18.58.238/hr2/"
get = requests.get(url)
print(get)
print("status code is: " + str(get.status_code)) #checking of the return status to see if it is correct.
if get.status_code == 200:
    print("Return Status is: OK")
elif get.status_code == 404:
    print("Not Found")
else:
    print("Error")



#Display the header
#header modifier--------------
                            #|
h = requests.head(url)     #<-
print("Header:")
print("_______________________________________________________________________")
for x in h.headers:
    print("\t",x,":",h.headers[x])
    print("_______________________________________________________________________")



#modifing the user agent to mobile
headers ={
    'User-Agent':'Mobile'
}
url2 = 'http://172.18.58.238/headers.php'
rh = requests.get(url2,headers=headers)# sends a request to the url using the new header. #to change the user agent
print(rh.text)



#to delete the unnecessary information that is not required.
import scrapy
from scrapy.crawler import CrawlerProcess
import logging
logging.disable(50)



#global makes the website useable anywhere in the script
global website
website = 'http://172.18.58.238/hr2/'



#to scrape the website
class NewSpider(scrapy.Spider):
    name = "new_spider" #name
    start_urls = [website] #website you are scraping from



#this is to extract the images from the Website and store in results.json
    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield{
                'image Link':x.xpath(newsel).extract_first()
            }



#this is to check the next page for images and scrap them out
        Page_selector = '.next a ::attr(href)'
        NextPage = response.css(Page_selector).extract_first()
        if NextPage:
            yield scrapy.Request(response.urljoin(NextPage),callback=self.parse)



process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'results.json'})
process.crawl(NewSpider)  # Selecting spider class
process.start()  #



#to read the results.json file and display it when run
with open('results.json', 'rt') as filehandle:
    lines = filehandle.readlines()[3:17]
for line in lines:
    print(website + line.replace('{"image Link": "' , "").replace('"}' , "").replace("," , ""))#the replace function is used to remove the unwanted words



#To Display the Website
testurls = ['http://172.18.58.238/hr2/']
import webbrowser
for url in testurls:
    webbrowser.open_new_tab(website)



# unittesting on the OK response and the User-Agent
import unittest
class testMyProgram(unittest.TestCase):
    def test_response_200_check(self):
        self.assertEqual(get.status_code, 200)

    def test_modification_header_check(self):
        result=headers
        self.assertEqual(result,({'User-Agent':'Mobile'}))
unittest.main()