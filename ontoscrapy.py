import os
import mechanize
from urllib.request import urlopen
from bs4 import BeautifulSoup


def search_metadata(list_programs):
    ontoscrapy = open("ontoscrapy_tcc/spiders/wiki_scraping.py", "r")
    indice = ""
    with open("ontoscrapy_tcc/spiders/wiki_scraping.py", 'r') as f:
        texto = f.readlines()
    # print(texto[0])
    for i in texto:
        if "start_urls" in i:
            print(texto.index(i))
            indice = (texto.index(i))
            # return
    # a linha new_line precisa ter exatamente essa configuração com 4 espaços antes do start_urls
    # senão o python reclama da identação        
    new_line = "    start_urls = " + str(list_programs) + '\n'
    with open("ontoscrapy_tcc/spiders/wiki_scraping.py", 'w') as f:
        for i in texto:
            if texto.index(i) == indice:
                f.write((new_line))
            else:
                f.write(i)


def generate_url(name_program):
    url_base = "https://en.wikipedia.org"

    # Criando um mechanize browser e indo para url
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_equiv(False)
    browser.open("https://en.wikipedia.org/wiki/Main_Page")

    # Selecionando o formulário da Wiki para busca da pagina do programa
    browser.select_form(nr=0)

    # Definindo a entrada do formulário de busca
    browser["search"] = name_program

    # Submetendo a busca
    response = browser.submit()

    # Recuperando a url da busca
    url_origen = response.geturl()

    # Procurando na página de busca o link correto da página do programa
    html = urlopen(url_origen)
    soup = BeautifulSoup(html, 'html.parser')
    getValueFromDiv = soup.find('div', class_='mw-search-result-heading')

    # Unindo a url base com o link correto encontrado
    link = url_base + getValueFromDiv.a['href']
    return link


search_metadata([generate_url("clustal")])

os.system("scrapy crawl inf_program")
