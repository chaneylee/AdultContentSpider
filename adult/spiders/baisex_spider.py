#coding=UTF-8
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from adult.items import AdultItem 

class BaiSexSpider(BaseSpider):
	#baisex ip. The last splash is necessary
	baisex_url = "http://173.245.71.203/"
	avbbs_url ="http://69.46.86.131/"
	
	#homepage_url = baisex_url
	homepage_url = avbbs_url
	
	
	channels= (
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
			{'channel':'自拍偷拍视频',
		  	'relative_url_prifix':'forum-123-',
	          	'total_pages':137,
			'ToBeCrawled':False
			 	},
			{'channel':'亚洲在线视频',
		  	'relative_url_prifix':'forum-107-',
	          	'total_pages':132,
			'ToBeCrawled':False
			 	},
			{'channel':'国产三级视频',
		  	'relative_url_prifix':'forum-106-',
	          	'total_pages':31,
			'ToBeCrawled':False
			 	},
			{'channel':'另类SM视频',
		  	'relative_url_prifix':'forum-124-',
	          	'total_pages':117,
			'ToBeCrawled':True
			 	},
			)
	
	name = "baisex"
	allowed_domains = [homepage_url[7:-1]]
	start_urls = []
 	
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
			item['link'] = self.homepage_url+link
			item['date'] = date
			yield item
	
	#create the urls need to be extracted
	def __create_urls(self):
		for channel in self.channels:
			if channel['ToBeCrawled']:
				start_page = 1 
				while start_page <= channel['total_pages']:
					self.start_urls.append(self.homepage_url+channel['relative_url_prifix']+str(start_page)+".html")
					start_page += 1

	
