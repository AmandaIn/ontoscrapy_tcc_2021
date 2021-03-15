import scrapy
import re


class WikiScraping(scrapy.Spider):
    name = "inf_program"

    start_urls = ["https://en.wikipedia.org/wiki/Clustal#ClustalW",
                  "https://en.wikipedia.org/wiki/MAFFT",
                  "https://en.wikipedia.org/wiki/MUSCLE_(alignment_software)",
                  "https://en.wikipedia.org/wiki/JAligner"
                  ]

    def parse(self, response):
        #--------salvar o nome e a descrição do programa-------
        yield dict(name_program=response.xpath('//title//text()').extract_first())
        yield dict(description=re.sub('<[^>]+?>', '', response.xpath('//p').extract_first()))
        #-------salvar as linhas da tabela para percorrê-las------
        tr = response.xpath('//table[@class="infobox vevent"]//tr')
        #-------lista com os possíveis atributos de uma tabela-------
        attribute = ['author', 'developer', 'release', 'repository',  'system', 'platform', 'available', 'categories', 'license', 'website', 'written']
        #-------laço para percorrer as linahs da tabela------------
        for n in range(len(tr)):
            #-------conversão dos elementos em string para fazer a comparação através do re--------
            line = tr[n].extract()
            ', '.join(line)
            #------laço para verificar se a linha possui o atributo e salvá-la no dicionario correspondente-------
            for m in range(len(attribute)):
                result_line = re.search(attribute[m], line, re.IGNORECASE)

                if result_line and (attribute[m] == "author"):
                    yield dict(original_author=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "developer"):
                    yield dict(developer=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "release"):
                    yield dict(release=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "repository"):
                    yield dict(repository=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "system"):
                    yield dict(operating_system=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "platform"):
                    yield dict(platform=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "available"):
                    yield dict(available_in=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "categories"):
                    yield dict(category=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "license"):
                    yield dict(license=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "website"):
                    yield dict(website=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line and (attribute[m] == "written"):
                    yield dict(written_in=re.sub('<[^>]+?>', '', tr[n].extract()))







