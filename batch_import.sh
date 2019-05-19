#!/bin/sh

scrapy crawl import_ufc_repository -o 01-BU.json -a url=http://www.repositorio.ufc.br/handle/riufc/2/browse					# BU
scrapy crawl import_ufc_repository -o 02-CCA.json -a url=http://www.repositorio.ufc.br/handle/riufc/41/browse				# CCA
scrapy crawl import_ufc_repository -o 03-CC.json -a url=http://www.repositorio.ufc.br/handle/riufc/58/browse				# CC
scrapy crawl import_ufc_repository -o 04-CRATEUS.json -a url=http://www.repositorio.ufc.br/handle/riufc/16297/browse		# Crateus
scrapy crawl import_ufc_repository -o 05-CH.json -a url=http://www.repositorio.ufc.br/handle/riufc/232/browse				# CH
scrapy crawl import_ufc_repository -o 06-QUIXADA.json -a url=http://www.repositorio.ufc.br/handle/riufc/533/browse			# Quixada
scrapy crawl import_ufc_repository -o 07-RUSSAS.json -a url=http://www.repositorio.ufc.br/handle/riufc/13973/browse			# Russas
scrapy crawl import_ufc_repository -o 08-SOBRAL.json -a url=http://www.repositorio.ufc.br/handle/riufc/472/browse			# Sobral
scrapy crawl import_ufc_repository -o 09-CT.json -a url=http://www.repositorio.ufc.br/handle/riufc/419/browse				# CT
scrapy crawl import_ufc_repository -o 10-EU.json -a url=http://www.repositorio.ufc.br/handle/riufc/22988/browse				# EU
scrapy crawl import_ufc_repository -o 11-FACED.json -a url=http://www.repositorio.ufc.br/handle/riufc/349/browse			# FACED
scrapy crawl import_ufc_repository -o 12-FADIR.json -a url=http://www.repositorio.ufc.br/handle/riufc/112/browse			# FADIR
scrapy crawl import_ufc_repository -o 13-FAMED.json -a url=http://www.repositorio.ufc.br/handle/riufc/389/browse			# FAMED
scrapy crawl import_ufc_repository -o 14-FEAAC.json -a url=http://www.repositorio.ufc.br/handle/riufc/137/browse			# FEAAC
scrapy crawl import_ufc_repository -o 15-FFOE.json -a url=http://www.repositorio.ufc.br/handle/riufc/179/browse				# FFOE
scrapy crawl import_ufc_repository -o 16-ICA.json -a url=http://www.repositorio.ufc.br/handle/riufc/622/browse				# ICA
scrapy crawl import_ufc_repository -o 17-LABOMAR.json -a url=http://www.repositorio.ufc.br/handle/riufc/10/browse			# LABOMAR
scrapy crawl import_ufc_repository -o 18-MEMUFC.json -a url=http://www.repositorio.ufc.br/handle/riufc/23970/browse			# Memorial UFC
scrapy crawl import_ufc_repository -o 19-PREX.json -a url=http://www.repositorio.ufc.br/handle/riufc/13179/browse			# PREX
scrapy crawl import_ufc_repository -o 20-PROGEP.json -a url=http://www.repositorio.ufc.br/handle/riufc/962/browse			# PROGEP
scrapy crawl import_ufc_repository -o 21-PROGRAD.json -a url=http://www.repositorio.ufc.br/handle/riufc/20641/browse		# PROGRAD
scrapy crawl import_ufc_repository -o 22-PRPPG.json -a url=http://www.repositorio.ufc.br/handle/riufc/923/browse			# PRPPG
scrapy crawl import_ufc_repository -o 23-TCCESP.json -a url=http://www.repositorio.ufc.br/handle/riufc/28762/browse			# TCC Especializacao
scrapy crawl import_ufc_repository -o 24-TCC.json -a url=http://www.repositorio.ufc.br/handle/riufc/21982/browse			# TCC Graduacao
scrapy crawl import_ufc_repository -o 25-IEFES.json -a url=http://www.repositorio.ufc.br/handle/riufc/40619/browse			# IEFES