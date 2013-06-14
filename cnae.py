##Exemplo de uso: python url.py 29
import urllib
import urllib2
import sys
import web
import json

url = 'http://www.cnae.ibge.gov.br/pesquisa.asp'
urls_aceitas = (
    '/(.*)', 'cnae'
)
app = web.application(urls, globals())

class cnae:        
    def GET(self, param):
        if not param: 
            return 'Faltou o codigo do cnae!'
        parametro = param

        values = {'pesquisa' : parametro,
                  'sourcepage' : 'index',
                  'tabelabusca' : 'CNAE_201@CNAE 2.1 - Subclasses@0@cnaefiscal@0',
                  'tipoordenacao' : 'C'
                  }

        data = urllib.urlencode(values)
        req = urllib2.Request(urls_aceitas, data)
        response = urllib2.urlopen(req)
        the_page = response.readlines()
        results = []

        for url in the_page:
            if url.find('<TD style="FONT: 8pt \'Verdana\'; COLOR: black; BACKGROUND-COLOR: #ffffff" width=680 height=16>') != -1:
                results.append(url[106:-15])
		web.header('Content-Type', 'application/json')
		return json.dumps(results)

if __name__ == "__main__":
    app.run()
         

