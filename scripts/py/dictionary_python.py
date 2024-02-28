#!/usr/local/bin/python 
import os, sys # using for python2 encoding ASCII
import pandas as pd
import re
from openpyxl import load_workbook

#  -*- coding: utf-8 -*-                            
def traduzir_palavra(palavra, dicionario):          
    return dicionario.get(palavra, palavra)         
                                                 

# -*- coding: utf-8 -*-                                                                          
def traduzir_colunas(df, colunas, traducoes):                                                     
    for coluna in colunas:                                                                          
        df[coluna] = df[coluna].apply(lambda x: ' '.join(traduzir_palavra(palavra, traducoes)  
         for palavra in re.findall(r'\b\w+\b', str(x)))).upper() # change version str.upper()              
    return df                                                                                   

# -*- coding: utf-8 -*-                                                               
tabela = ('/var/www/html/python2.7_translater_files_geoprocessing/files/for_test_setor.xlsx')#

workbook = load_workbook(tabela)

# -*- coding: utf-8 -*-                          
colunas_a_traduzir = ['se_setor', 'qu_setor', 'nome'] 

traducoes = {
   'QD' : 'QUADRA',
    'QI' : 'QUADRA INTERNA'
}
tabela_traduzida = traduzir_colunas(tabela, colunas_a_traduzir, traducoes) 

# => Salva o DataFrame atualizado em um novo arquivo xlsx já traduzindo os valores nas células                             
tabela_traduzida.to_excel('/var/www/html/python2.7_translater_files_geoprocessing/files/resultados/traducao_results/translate_table.xlsx', index=False) 
