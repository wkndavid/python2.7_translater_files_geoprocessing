import pandas as pd
from dbfread import DBF

# Caminho para o arquivo DBF
caminho_dbf = '/var/www/html/version2/files/teste/teste.dbf'

# Ler o arquivo DBF usando pandas
table = DBF(caminho_dbf, encoding='utf-8')
# change version (iter(table)) O motivo é que o método DataFrame do pandas espera uma lista como entrada no Python 2.7, enquanto no Python 3 ele pode receber um iterador diretamente. Certifique-se de ajustar os caminhos dos arquivos conforme necessário.
df = pd.DataFrame(list(table))

# Caminho para salvar o arquivo XLSX
caminho_xlsx = '/var/www/html/version2/files/resultados/results_dbf_xlsx/results_dbf_xlsx.xlsx'

# Salvar o DataFrame como XLSX usando pandas
df.to_excel(caminho_xlsx, index=False, engine='openpyxl')
