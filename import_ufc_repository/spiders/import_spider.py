import scrapy
import re

# Inspired by tutorial at https://docs.scrapy.org/en/latest/intro/tutorial.html

class ImportUfcRepositorySpider(scrapy.Spider):
	name = 'import_ufc_repository'
	domain = 'http://www.repositorio.ufc.br'

	def start_requests(self):
		url = getattr(self, 'url', None)
		yield scrapy.Request(url = url, callback=self.parse)

	# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
	def cleanhtml(self, raw_html):
		cleanr = re.compile('<.*?>')
		cleantext = re.sub(cleanr, '', raw_html)
		return cleantext

	def parse(self, response):
		# follow links to document pages
		for href in response.xpath('//td[@headers="t2"]/strong/a'):
			yield response.follow(href, self.parse_document)

		# follow pagination link
		for href in response.xpath('//a[@class="pull-right"]'):
			yield response.follow(href, self.parse)	

	def parse_document(self, response):
		table = response.xpath('//table[@class="table itemDisplayTable"]')
		rows = table.xpath('.//tr')
		output = {}
		for row in rows:
			# get row's label
			raw_label = row.xpath('.//td[@class="metadataFieldLabel"]/text()').extract()
			label = raw_label[0].split(':', 1)[0]		# remove punctation		

			# get row's value
			raw_value = row.xpath('.//td[@class="metadataFieldValue"]').extract_first()
			raw_value = raw_value.replace('<br>',';')	# properly set separators
			raw_value = raw_value.encode('utf-8')
			value = self.cleanhtml(raw_value)

			# store data at the output dict :)
			output[label] = value

		# get pdf download panel
		panel_div = response.xpath('//div[@class="panel panel-info"]')
		href = panel_div.xpath('.//a/@href').extract_first()

		if href is not None:
			output['href'] = self.domain + href
		else:
			output['href'] = ''
			self.logger.warning('There is no pdf available at {}'.format(response.url))

		yield output