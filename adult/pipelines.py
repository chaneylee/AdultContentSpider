# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sqlite3

class AdultPipeline(object):
	#when the spider is open,then open the datebase
	def open_spider(self,spider):
		#self.con=sqlite3.connect("G:/baisex.db")
		self.con=sqlite3.connect("baisex.db")
		self.cur=self.con.cursor()
	
	def process_item(self, item, spider):
		self.cur.execute("insert into movie values(?,?,?,?)",
				(None,item['title'],item['link'],item['date'])
				)
        	return item
	
	#when the spider is finished,commit the transaction and close the datebase connection
	def close_spider(self,spider):
		self.con.commit()
		self.con.close()

