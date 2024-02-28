#!/usr/local/bin/python 
import os, sys # using for python2 encoding ASCII
import pandas as pd
from dbfread import DBF


# Caminho para o arquivo DBF
caminho_dbf = '/var/www/html/python2.7_translater_files_geoprocessing/files/teste/teste.dbf'

# Ler o arquivo DBF usando pandas
table = DBF(caminho_dbf, encoding='utf-8')
df = pd.DataFrame(list(table))

# Caminho para salvar o arquivo XLSX
caminho_xlsx = '/var/www/html/python2.7_translater_files_geoprocessing/files/resultados/results_dbf_xlsx/results_dbf_xlsx.xlsx'

# Salvar o DataFrame como XLSX usando pandas
df.to_excel(caminho_xlsx, index=False, engine='openpyxl')
