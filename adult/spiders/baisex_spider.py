from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from adult.items import AdultItem 

class BaiSexSpider(BaseSpider):
	#baisex ip
	baisex_url = "http://173.245.71.203/" 

	name = "baisex"
	allowed_domains = ["173.245.71.203"]
	start_urls = [
			"http://173.245.71.203/forum-109-1.html"
		]
	#const xpath string
	title_xpath = "//form[@id=\'moderate\']/table/tbody[position()>9]//th/a[1]/text()"
	link_xpath = "//form[@id=\'moderate\']/table/tbody[position()>9]//th/a[1]/@href"
	date_xpath = "//form[@id=\'moderate\']/table/tbody[position()>9]//td[2]/em/span/text()"
 	

	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select(self.title_xpath).extract()
		links = hxs.select(self.link_xpath).extract()
		dates = hxs.select(self.date_xpath).extract()
		#items = []
		for title,link,date in zip(titles,links,dates):
			item = AdultItem()
			item['title'] = title
			item['link'] = self.baisex_url+link
			item['date'] = date
			yield item
			#items.append(item)
		#return items
		#pass

