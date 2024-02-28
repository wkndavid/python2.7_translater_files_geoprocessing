#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-

import dbfread
import shapefile
import codecs
import sys
sys.path.append('/var/www/html/python2.7_translater_files_geoprocessing/scripts/resources')
from traducoes import traducoes  # Importe o dicionário de traduções

# Caminho para o arquivo /DBF
caminho_arquivo_dbf = "/var/www/html/python2.7_translater_files_geoprocessing/files/teste/teste1.dbf"

r = shapefile.Reader("shapefiles/test/latin1.shp", encoding="latin1")
# Le o arquivo DBF usando dbfread
tabela_dbf = dbfread.DBF(caminho_arquivo_dbf, encoding="utf-8")

# Traduzi os valores no arquivo DBF
for rec in tabela_dbf:
    for campo, valor in rec.items():
        if valor in traducoes:
            rec[campo] = traducoes[valor]

# Caminho para o arquivo de saída DBF traduzido
caminho_arquivo_saida = "/var/www/html/python2.7_translater_files_geoprocessing/files/resultados/traducao_results/arquivo_traduzido.dbf"
with codecs.open(caminho_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
    dbfread.write(rec, arquivo_saida)