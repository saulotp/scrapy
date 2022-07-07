from matplotlib.cbook import report_memory
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['www.zapimoveis.com.br']
    start_urls = ['https://www.zapimoveis.com.br/imovel/venda-apartamento-2-quartos-mobiliado-baln-jd-praia-grande-mongagua-sp-68m2-id-2568882003/']
    rules = [Rule(LinkExtractor(), callback = 'parse_info', follow = True)]
    
    def parse(self, response):
        return {
                'name': response.css('.heading-large__bold strong::text').get(),
                'value': response.css('.text-regular__bolder strong::text').get(),
                'address': response.css('.link--icon-right .link::text').get(),
                'condominium value':response.css('.condominium .price__value::text').get(),
                'iptu price': response.css('.iptu .price__value::text').get(),
                'square meters': response.css('.js-areas span::text').get(),
                'bedrooms': response.css('.js-bedrooms span::text').get(),
                'garage': response.css('.js-parking-spaces span::text').get(),
                'bathrooms': response.css('.js-bathrooms span::text').get(),
                'features': response.css('.amenities__list-item::text').getall(),
               }



#https://www.zapimoveis.com.br/venda/?transacao=Venda&tipo=Im%C3%B3vel%20usado'