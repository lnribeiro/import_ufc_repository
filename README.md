# import_ufc_repository

This repository provides a Scrapy spider that crawls the [Repositório Institucional da Universidade Federal do Ceará](http://www.repositorio.ufc.br/).

The crawler is fed with a repository link, e.g. "CH - Centro de Humanidades [http://www.repositorio.ufc.br/handle/riufc/232](http://www.repositorio.ufc.br/handle/riufc/232)" and then it scraps every listed document and also follows the pagination links.

## Usage

To start scraping a repository:

```
scrapy crawl import_ufc_repository -a url=REPOSITORY_URL_HERE
```

The shell script ``batch_import.sh`` imports all repositories as JSON files. To run it:

```
sh batch_import.sh
```

## Scrapy Settings

To avoid being blocked by the repository server, we have set the number of concurrent requests and the download delay to one in ``import_ufc_repository/settings.py``. Larger values may give 503 and timeout errors. For more information, please read Scrapy's documentation on [Avoiding getting banned](https://docs.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned).

## Dependencies

This tool depends on [Scrapy](https://scrapy.org/). It can be easily installed with pip:

```
pip install scrapy
```


