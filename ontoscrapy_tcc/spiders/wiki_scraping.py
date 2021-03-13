import scrapy
import re



class WikiScraping(scrapy.Spider):
    name = "inf_program"

    start_urls = ["https://en.wikipedia.org/wiki/Clustal#ClustalW",
                  "https://en.wikipedia.org/wiki/MAFFT"
                  ]

    def parse(self, response):
        tr = response.xpath('//table[@class="infobox vevent"]//tr')
        y = "vida"

        vida = "developer"
        for n in range(len(tr)):

            line = tr[n].extract()
            ', '.join(line)
            resultado = re.search(vida, line)

            if resultado.group(0) == "developer":
                yield dict(developer=re.sub('<[^>]+?>', '', tr[n].extract()))
                print(resultado.group(0))

