#coding=UTF-8
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from adult.items import AdultItem 

class BaiSexSpider(BaseSpider):
	#baisex ip
	baisex_url = "http://173.245.71.203/"
	
	pages = (
			{'channel':'亚洲BT无码',
		  	'relative_url_prifix':'forum-109-',
	          	'total_pages':531,
			'ToBeCrawled':False
			 	},
			{'channel':'亚洲BT有码',
		  	'relative_url_prifix':'forum-108-',
	          	'total_pages':417,
			'ToBeCrawled':False
			 	},
			{'channel':'迅雷下载 | HTTP Download',
		  	'relative_url_prifix':'forum-66-',
	          	'total_pages':212,
			'ToBeCrawled':False
			 	},
			{'channel':'HD 高清成人影视',
		  	'relative_url_prifix':'forum-107-',
	          	'total_pages':145,
			'ToBeCrawled':False
			 	},
			{'channel':'手机成人影片3GP MP4等',
		  	'relative_url_prifix':'forum-69-',
	          	'total_pages':213,
			'ToBeCrawled':False
			 	},
			{'channel':'电驴 | Emule',
		  	'relative_url_prifix':'forum-67-',
	          	'total_pages':287,
			'ToBeCrawled':False
			 	},
			{'channel':'亚洲无码',
		  	'relative_url_prifix':'forum-60-',
	          	'total_pages':673,
			'ToBeCrawled':False
			 	},
			{'channel':'亚洲有码',
		  	'relative_url_prifix':'forum-61-',
	          	'total_pages':407,
			'ToBeCrawled':False
			 	},
			{'channel':'三级SM综合片',
		  	'relative_url_prifix':'forum-111-',
	          	'total_pages':245,
			'ToBeCrawled':False
			 	},
			{'channel':'高清专区',
		  	'relative_url_prifix':'forum-182-',
	          	'total_pages':44,
			'ToBeCrawled':False
			 	},
			{'channel':'网盘下载 | Network Disk',
		  	'relative_url_prifix':'forum-68-',
	          	'total_pages':928,
			'ToBeCrawled':False
			 	},
			)

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
	
	##Emule 
	##movie section relative page url prifix
	#relative_url_prifix = "forum-67-"
	##total number of the section
	#total_pages = 287 

	##mosaic 2 
	##movie section relative page url prifix
	#relative_url_prifix = "forum-61-"
	##total number of the section
	#total_pages = 407 
	
	##no mosaic 2 
	##movie section relative page url prifix
	#relative_url_prifix = "forum-60-"
	##total number of the section
	#total_pages = 673 
	
	##X-rated  
	##movie section relative page url prifix
	#relative_url_prifix = "forum-111-"
	##total number of the section
	#total_pages = 245  

	##HD 2  
	##movie section relative page url prifix
	#relative_url_prifix = "forum-182-"
	##total number of the section
	#total_pages = 44  
	
	#Network Disk  
	#movie section relative page url prifix
	relative_url_prifix = "forum-68-"
	#total number of the section
	total_pages = 928

	#test one page
	#total_pages = 1  
	
	name = "baisex"
	allowed_domains = ["173.245.71.203"]
	start_urls = []
	
	#xpath string
	#title_xpath = "//form[@id=\'moderate\']/table/tbody[position()>9]//th/a[1]/text()"
	#link_xpath = "//form[@id=\'moderate\']/table/tbody[position()>9]//th/a[1]/@href"
	#date_xpath = "//form[@id=\'moderate\']/table/tbody[position()>9]//td[2]/em/span/text()"
 	
	#xpath string
	title_xpath = "//form[@id=\'moderate\']/table/tbody//th/a[1]/text()"
	link_xpath = "//form[@id=\'moderate\']/table/tbody//th/a[1]/@href"
	date_xpath = "//form[@id=\'moderate\']/table/tbody//td[2]/em/span/text()"
	channel_xpath = "//h1[@class=\'xs2\']/a[1]/text()"
 	
	def __init__(self):
		self.__create_urls()


	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select(self.title_xpath).extract()
		links = hxs.select(self.link_xpath).extract()
		dates = hxs.select(self.date_xpath).extract()
		channel = hxs.select(self.channel_xpath).extract()
		item = AdultItem()
		item['channel'] = channel[0]
		for title,link,date in zip(titles,links,dates):
			item['title'] = title
			item['link'] = self.baisex_url+link
			item['date'] = date
			yield item
	

	#create the urls need to be extracted
	def __create_urls(self):
		start_page = 1 
		while start_page <= self.total_pages:
			self.start_urls.append(self.baisex_url+self.relative_url_prifix+str(start_page)+".html")
			start_page += 1
	
