import scrapy
import re

# Inspired by tutorial at https://docs.scrapy.org/en/latest/intro/tutorial.html



class ImportUfcRepositorySpider(scrapy.Spider):
	name = 'import_ufc_repository'
	domain = 'http://www.repositorio.ufc.br'
	start_urls = ['http://www.repositorio.ufc.br/handle/riufc/2/browse',		# BU
					'http://www.repositorio.ufc.br/handle/riufc/41/browse',		# CCA
					'http://www.repositorio.ufc.br/handle/riufc/58/browse',		# CC
					'http://www.repositorio.ufc.br/handle/riufc/16297/browse',	# Crateus
					'http://www.repositorio.ufc.br/handle/riufc/232/browse',	# CH
					'http://www.repositorio.ufc.br/handle/riufc/533/browse',	# Quixada
					'http://www.repositorio.ufc.br/handle/riufc/13973/browse',	# Russas
					'http://www.repositorio.ufc.br/handle/riufc/472/browse',	# Sobral
					'http://www.repositorio.ufc.br/handle/riufc/419/browse',	# CT
					'http://www.repositorio.ufc.br/handle/riufc/22988/browse',	# EU
					'http://www.repositorio.ufc.br/handle/riufc/349/browse',	# FACED
					'http://www.repositorio.ufc.br/handle/riufc/112/browse',	# FADIR
					'http://www.repositorio.ufc.br/handle/riufc/389/browse',	# FAMED
					'http://www.repositorio.ufc.br/handle/riufc/137/browse',	# FEAAC
					'http://www.repositorio.ufc.br/handle/riufc/179/browse',	# FFOE
					'http://www.repositorio.ufc.br/handle/riufc/622/browse',			# ICA
					'http://www.repositorio.ufc.br/handle/riufc/10/browse',			# LABOMAR
					'http://www.repositorio.ufc.br/handle/riufc/23970/browse',			# Memorial UFC
					'http://www.repositorio.ufc.br/handle/riufc/13179/browse',			# PREX
					'http://www.repositorio.ufc.br/handle/riufc/962/browse',	# PROGEP
					'http://www.repositorio.ufc.br/handle/riufc/20641/browse',	# PROGRAD
					'http://www.repositorio.ufc.br/handle/riufc/923/browse',	# PRPPG
					'http://www.repositorio.ufc.br/handle/riufc/28762/browse',	# TCC Especializacao
					'http://www.repositorio.ufc.br/handle/riufc/21982/browse'	# TCC Graduacao
					]

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
		output['href'] = self.domain + href

		yield output