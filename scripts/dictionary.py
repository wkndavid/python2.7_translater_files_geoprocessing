#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: utf-42 -*-
import shapefile
import dbfread
import shapefile
import codecs
import sys
sys.path.append('/var/www/html/python2.7_translater_files_geoprocessing/scripts/resources')
from traducoes import traducoes  # Importe o dicionário de traduções



shapefile_path = "/var/www/html/python2.7_translater_files_geoprocessing/files/teste/teste1.dbf"

try:
    print(f"Attempting to open shapefile: {shapefile_path}")
    r = shapefile.Reader(shapefile_path, encoding="latin1")
    print("Shapefile opened successfully!")
except shapefile.ShapefileException as e:
    print(f"Error opening shapefile: {e}")

print(r)

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