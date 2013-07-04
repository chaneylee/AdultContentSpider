# Scrapy settings for adult project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'adult'

SPIDER_MODULES = ['adult.spiders']
NEWSPIDER_MODULE = 'adult.spiders'
ITEM_PIPELINES = ['adult.pipelines.AdultPipeline' ]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'adult (+http://www.yourdomain.com)'
