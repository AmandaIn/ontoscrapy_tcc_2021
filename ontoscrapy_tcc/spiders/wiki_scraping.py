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

        attribute = ['release', 'developer']
        for n in range(len(tr)):

            line = tr[n].extract()
            ', '.join(line)

            for m in range(len(attribute)):
                result_line = re.search(attribute[m], line)

                if result_line:
                    yield dict(developer=re.sub('<[^>]+?>', '', tr[n].extract()))

                if result_line:
                    yield dict(stable_release=re.sub('<[^>]+?>', '', tr[n].extract()))






            #print(result_line.group(0))

            #print(result_line)
            #result_line2 = re.search("system", line)

            # if result_line.group(0) == "developer":
              # yield dict(developer=re.sub('<[^>]+?>', '', tr[n].extract()))
              # print(result_line.group(0))

            #f result_line2.group(0) == "system":
               # yield dict(sistema=re.sub('<[^>]+?>', '', tr[n].extract()))
                #print(result_line2.group(0))


