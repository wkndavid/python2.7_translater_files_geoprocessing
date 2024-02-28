# -*- coding: utf-8 -*-

import pandas as pd
import re
from openpyxl import load_workbook

translate = {
    'SHIGS' : 'Setor de Habitações Individuais Geminadas Sul',
    'CCSW' : 'Centro Comercial Sudoeste',
    'PMU' : 'Praça Municipal',
    'SCES' : 'Setor de Clubes Esportivos Sul',
    'SCRN' : 'Setor Comercial Residencial Norte',
    'SHGC' : 'Setor Habitacional Grande Colorado',
    'SCRS' : 'Setor Comercial Residencial Sul',
    'SHCNW' : 'Setor de Habitações Coletivas Noroeste',
    'SHTQ' : 'Setor Habitacional Taquari - Lago Norte',
    'SHMD' : 'Setor Habitacional Mestre D`Armas',
    'EPAA' : 'Estrada Parque Armazenagem e Abastecimento Plano Piloto',
    'EPAR' : 'Estrada Parque Aeroporto',
    'EPCB' : 'Estrada Parque Contorno do Bosque	Plano Piloto',
    'EPCL' : 'Estrada Parque Ceilândia',
    'EPCT' : 'Estrada Parque Contorno Cerca a bacia de águas do lago Paranoá',
    'EPCV' : 'Estrada Parque Cabeça de Veado',
    'EPDB' : 'Estrada Parque Dom Bosco Lago Sul',
    'EPGU' : 'Estrada Parque Guará',
    'EPIA' : 'Estrada Parque Indústria e Abastecimento Norte-Sul',
    'EPIG' : 'Estrada Parque Indústrias Gráficas',
    'EPNB' : 'Estrada Parque Núcleo Bandeirante',
    'EPPN' : 'Estrada Parque Península Norte Lago Norte - Península',
    'EPPR' : 'Estrada Parque Paranoá',
    'EPTG' : 'Estrada Parque Taguatinga',
    'EPTM' : 'Estrada Parque Tamanduá',
    'ERR' : 'Eixo Rodoviária-Residencial',
    'PEVC' : 'Parque Ecológico e Vivencial da Candangolândia',
}

def traduzir_colunas(coluna, translate):
    return ' '.join(translate.get(palavra, palavra) for palavra in re.findall(r'\b\w+\b', unicode(coluna, 'latin-1'))).upper()

def carregar_excel(caminho_excel):
    workbook = load_workbook(caminho_excel)
    sheet = workbook.active
    data = sheet.values
    columns = next(data)[:5]
    return pd.DataFrame(data, columns=columns, dtype=str)

def main():
    caminho_excel = '/var/www/html/python2.7_translater_files_geoprocessing/files/for_test_setor.xlsx'
    tabela = carregar_excel(caminho_excel)

    # translate
    colunas_a_traduzir = ['se_setor', 'qu_setor', 'nome']
    
    tabela_traduzida = pd.DataFrame()
    for coluna in colunas_a_traduzir:
        tabela_traduzida[coluna] = tabela[coluna].apply(lambda x: ' '.join(traduzir_colunas(palavra, translate) for palavra
                                in re.findall(r'\b\w+\b')))

    caminho_saida_excel = '/var/www/html/python2.7_translater_files_geoprocessing/files/resultados/traducao_results/translate_table.xlsx'
    tabela_traduzida.to_excel(caminho_saida_excel, index=False, encoding='utf-8')

if __name__ == "__main__":
    main()