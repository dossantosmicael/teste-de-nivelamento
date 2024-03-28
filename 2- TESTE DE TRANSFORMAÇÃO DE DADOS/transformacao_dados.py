import pandas as pd
import tabula
import zipfile
import os

# Função para extrair arquivos PDF de dentro de um arquivo ZIP
def extrair_pdf_de_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Função para extrair os dados da tabela de PDF
def extrair_dados_pdf(pdf_path):
    dfs = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return pd.concat(dfs)

# Função para salvar os dados em CSV
def salvar_para_csv(dataframe, csv_path):
    dataframe.to_csv(csv_path, index=False)

# Função para substituir abreviações nas colunas
def substituir_abreviacoes(dataframe):
    # Mapeamento das abreviações para descrições completas
    abreviacoes = {
        'OD': 'Oftalmologia Diagnóstica',
        'AMB': 'Ambulatório'
    }
    # Substituição das abreviações nas colunas específicas
    dataframe['OD'] = dataframe['OD'].map(abreviacoes)
    dataframe['AMB'] = dataframe['AMB'].map(abreviacoes)
    return dataframe

pdf_path = r'D:\GitHubRepositorio\teste-de-nivelamento\1- TESTE DE WEB SCRAPING\Anexo_I_Rol_2021RN_465.2021_RN599_RN600.pdf' # Nome do arquivo PDF
dados_pdf = extrair_dados_pdf(pdf_path) # Extrair dados do PDF

# Salvar dados em CSV
csv_path = 'Teste_Micael_dos_Santos.csv'
salvar_para_csv(dados_pdf, csv_path)

dados_pdf = substituir_abreviacoes(dados_pdf) # Substituir abreviações
nome_zip = 'Teste_Micael_dos_Santos.zip' # Nome para o arquivo zip

# Criar arquivo zip e adicionar o CSV
with zipfile.ZipFile(nome_zip, 'w') as zipf:
    zipf.write(csv_path, os.path.basename(csv_path))

os.remove(csv_path) # Remover arquivo CSV

print("Processo concluído. Arquivo zip criado:", nome_zip)
