import lxml
import scrapy
import re
from lxml import etree


class WikiScraping(scrapy.Spider):
    name = "inf_program"

    start_urls = ["https://en.wikipedia.org/wiki/Clustal#ClustalW",
                  "https://en.wikipedia.org/wiki/MAFFT"
                  ]

    def parse(self, response):
        tr = response.xpath('//table[@class="infobox vevent"]//tr')
        y = "vida"

        vida = "developer"
        for x in range(len(tr)):

            teste = tr[x].extract()
            ', '.join(teste)
            resultado = re.search(vida, teste)
            #resultado = compara(teste, vida)
            if resultado.group(0) == "developer":
                print(resultado.group(0))
            #print(teste)
            # yield dict(info=tr[x].extract())

            #if compara(teste, "developer") == "developer":
               # print(teste)

            # limpar = tr[x].extract()
            # teste = response.xpath('//table[@class="infobox vevent"]//tr//th//text()')[x].extract()
            # print(teste)
            # if response.xpath('//table[@class="infobox vevent"]//tr//th//text()')[x].extract() == 'Developer(s)':
            # yield dict(developer=response.xpath('//table[@class="infobox vevent"]//tr//th.//td//text()')[x].extract())
            # if response.xpath('//table[@class="infobox vevent"]//tr//th//text()')[x].extract() == 'Stable release':
            # yield dict(stable_release=tr[x].extract())
            # if response.xpath('//table[@class="infobox vevent"]//tr//th//text()')[x].extract() == 'Written in':
            # yield dict(written_in=tr[x].extract())

            # yield dict(info=limpar[x].extract())
            # yield dict(info=tr[x].extract())
            # if (limpar.xpath)
            # document = lxml.html.document_fromstring(limpar)
            # print(raw_text = document.text_content())


def compara(lista, palavra):

    for n in range(len(lista)):
        comparar = lista[n]
        resultado = re.search(palavra, comparar)
        if resultado:
            return resultado.group(0)
            """ for x in tr:    
    
                    # print(x.extract())
                     yield dict(info=response.xpath('//table[@class="infobox vevent"]//tr[1]//text()').extract())
                     #yield dict(info=x.extract())
                     
                     
            """
