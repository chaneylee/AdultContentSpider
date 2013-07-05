from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from adult.items import AdultItem 

class BaiSexSpider(BaseSpider):
	#baisex ip
	baisex_url = "http://173.245.71.203/"
	
	##movie section relative page url prifix
	##mosaic
	#relative_url_prifix = "forum-109-"
	##total number of the section
	#total_pages = 531 
	
	##no mosaic
	##movie section relative page url prifix
	#relative_url_prifix = "forum-108-"
	##total number of the section
	#total_pages = 417 
	
	##thunder
	##movie section relative page url prifix
	#relative_url_prifix = "forum-66-"
	##total number of the section
	#total_pages = 212 

	##HD
	##movie section relative page url prifix
	#relative_url_prifix = "forum-107-"
	##total number of the section
	#total_pages = 145 
	
	##Cell phone
	##movie section relative page url prifix
	#relative_url_prifix = "forum-69-"
	##total number of the section
	#total_pages = 213 
	
	#Emule 
	#movie section relative page url prifix
	relative_url_prifix = "forum-67-"
	#total number of the section
	total_pages = 287 



	name = "baisex"
	allowed_domains = ["173.245.71.203"]
	start_urls = []
	
	#start_urls = [
	#		"http://173.245.71.203/forum-109-1.html"
	#	]


	#xpath string
	#title_xpath = "//form[@id=\'moderate\']/table/tbody[position()>9]//th/a[1]/text()"
	#link_xpath = "//form[@id=\'moderate\']/table/tbody[position()>9]//th/a[1]/@href"
	#date_xpath = "//form[@id=\'moderate\']/table/tbody[position()>9]//td[2]/em/span/text()"
 	
	#xpath string
	title_xpath = "//form[@id=\'moderate\']/table/tbody//th/a[1]/text()"
	link_xpath = "//form[@id=\'moderate\']/table/tbody//th/a[1]/@href"
	date_xpath = "//form[@id=\'moderate\']/table/tbody//td[2]/em/span/text()"
 	
	#create the urls need to be extracted
	def __init__(self):
		page_num = 1 
		while page_num <= self.total_pages:
			self.start_urls.append(self.baisex_url+self.relative_url_prifix+str(page_num)+".html")
			page_num += 1
	

	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select(self.title_xpath).extract()
		links = hxs.select(self.link_xpath).extract()
		dates = hxs.select(self.date_xpath).extract()
		for title,link,date in zip(titles,links,dates):
			item = AdultItem()
			item['title'] = title
			item['link'] = self.baisex_url+link
			item['date'] = date
			yield item
	

		



