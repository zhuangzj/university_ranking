import scrapy
from scrapy.crawler import CrawlerProcess
from WebCrawler.Items import DegreeItem

class UniversitySpider(scrapy.Spider):
    name = 'uci'
    allowed_domains = ['grad.uci.edu']
    start_urls = [
        'http://www.grad.uci.edu',
    ]

    def parse(self, response):
        degree = DegreeItem()
        for panel in response.xpath('//div[@class="AccordionPanel"]'):
            degree['name'] = panel.xpath('./div[@class="AccordionPanelTab"]/a/text()').extract()
            degree['deadline'] = panel.xpath('./div[@class="AccordionPanelContent"]/div[@class="degreeBox1"]/text()').extract()
            print(degree['name'])
            print(degree['deadline'])

def main():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(UniversitySpider)
    process.start()  # the script will block here until the crawling is finished

if __name__ == "__main__": main()