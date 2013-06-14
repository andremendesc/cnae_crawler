##Exemplo de uso: python url.py 29
import urllib
import urllib2
import sys

parametro = sys.argv[1]
url = 'http://www.cnae.ibge.gov.br/pesquisa.asp'

values = {'pesquisa' : parametro,
          'sourcepage' : 'index',
          'tabelabusca' : 'CNAE_201@CNAE 2.1 - Subclasses@0@cnaefiscal@0',
          'tipoordenacao' : 'C'
          }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.readlines()

for url in the_page:
    if url.find('<TD style="FONT: 8pt \'Verdana\'; COLOR: black; BACKGROUND-COLOR: #ffffff" width=680 height=16>') != -1:
        print url[106:-15]

