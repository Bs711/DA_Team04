#Perform a “get” request on the given website	[LAB 10b]X
# Display an “OK same as 200” return status

import requests
url ="http://172.18.58.238/hr2/"
get = requests.get(url)
print(get)
print("status code is: " + str(get.status_code))
if get.status_code == 200:
    print("Return Status is: OK")
elif get.status_code == 404:
    print("Not Found")
else:
    print("Error")

#header modifier--------------
                            #|
h = requests.head(url)     #<-
print("Header:")#header req
print("_______________________________________________________________________")
for x in h.headers:
    print("\t",x,":",h.headers[x])
    print("_______________________________________________________________________")

#modifing the user agent to mobile
headers ={
    'User-Agent':'Mobile'
}
#Test it on an external site
url2 = 'http://172.18.58.238/headers.php'
rh = requests.get(url2,headers=headers)
print(rh.text)

# 4i

import webbrowser
import scrapy
from scrapy.crawler import CrawlerProcess

testurls = ['http://172.18.58.238/hr2/']  # ---->need to change when submit


class NewSpider(scrapy.Spider):
    name = 'new_spider'
    start_urls = testurls

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }


# 4iii - FEED_URI and FEED_FORMAT to output results in JSON


#process = CrawlerProcess({
    #'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    #'FEED_FORMAT': 'json',
    #'FEED_URI': ''
#})


#process.crawl(NewSpider,)
#process.start()


# 4ii - Display reference web pages

#for url in testurls:
   # webbrowser.open_new_tab(url)


