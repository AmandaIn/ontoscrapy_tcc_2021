import os, autopep8

def search_metadata(list_programs):
    ontoscrapy = open("ontoscrapy_tcc/spiders/wiki_scraping.py", "r")
    indice = ""
    with open("ontoscrapy_tcc/spiders/wiki_scraping.py",'r') as f:
        texto=f.readlines()
    # print(texto[0])
    for i in texto:
        if "start_urls" in i:
            print(texto.index(i))
            indice = (texto.index(i))
            # return
    # a linha new_line precisa ter exatamente essa configuração com 4 espaços antes do start_urls
    # senão o python reclama da identação        
    new_line = "    start_urls = "+str(list_programs)+'\n'
    with open("ontoscrapy_tcc/spiders/wiki_scraping.py",'w') as f:
        for i in texto:
            if texto.index(i)==indice:
                f.write((new_line))
            else:
                f.write(i)


search_metadata([ "https://en.wikipedia.org/wiki/Clustal#ClustalW", 
                    "https://en.wikipedia.org/wiki/MAFFT",
                    "https://en.wikipedia.org/wiki/MUSCLE_(alignment_software)",
                    "https://en.wikipedia.org/wiki/JAligner"])
                    
os.system("scrapy crawl inf_program")