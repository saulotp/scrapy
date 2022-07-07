import scrapy


class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        return {
                'title': response.css('.titleColumn a::text').getall(),
                'year': response.css('.secondaryInfo::text').getall(),
                'rating': response.css('strong::text').getall()
        }
        
