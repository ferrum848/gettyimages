import scrapy, os, shutil
from gettyimages.items import GettyimagesItem, ImgData
from scrapy.linkextractor import LinkExtractor
from scrapy.selector import Selector

class GettyimagesItem(scrapy.Spider):
	name = "gettyimages"
	start_urls = ['https://www.gettyimages.co.uk/photos/selfie?mediatype=photography&phrase=selfie&sort=mostpopular']
	
	def parse(self, response):
		images = ImgData()
		images['file_urls']=[] 

		EML_SELECTOR = 'div.gallery-container-columns a'
		#yield {'my_test': response.css(EML_SELECTOR).extract_first()}
		for i in response.css(EML_SELECTOR):
			#yield {'my_test': i.css('a ::attr(href)').extract_first()}
			link = i.css('a ::attr(src)').extract_first()
			if link:
				images['file_urls'].append(link)
		yield images

		if len(os.listdir('/work/gettyimages/output/full')) > 0:
			for name in os.listdir('/work/gettyimages/output/full'):
				temp = name.find('?')
				new_name = name[:temp]
				shutil.copy('/work/gettyimages/output/full/' + name, '/work/gettyimages/output/result/' + new_name + '.jpg')



		next_page = 'div.next a ::attr(href)'
		#yield {'next_page': response.css(next_page).extract_first()}
		if response.css(next_page).extract_first():
			page = 'https://www.gettyimages.co.uk' + response.css(next_page).extract_first()
			yield scrapy.Request(page, self.parse)




