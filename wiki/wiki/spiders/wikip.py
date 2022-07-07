from http.client import ResponseNotReady
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class WikipSpider(CrawlSpider):
    name = 'wikip'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Kevin_Bacon']

    rules = [Rule(LinkExtractor(allow = r'wiki/((?!:).)*$'), callback = 'parse_info', follow = True)]

    def parse(self, response):
        return  {   
                    'title': response.xpath('//h1/text()').get(),
                    'url': response.url,
                    'lastupdated': response.xpath('/html/body/footer/ul[1]/li[1]/text()').get()

                }
