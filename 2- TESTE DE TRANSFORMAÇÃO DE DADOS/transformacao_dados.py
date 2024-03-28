import pandas as pd
import tabula
import zipfile
import os

# Função para extrair o arquivo PDF específico de dentro de um arquivo ZIP
def extrair_pdf_especifico_de_zip(zip_path, extract_path, target_pdf):
    print("Extraindo arquivo PDF do arquivo ZIP...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Lista de arquivos no zip
        zip_files = zip_ref.namelist()
        # Verificar se o arquivo PDF alvo está presente no zip
        if target_pdf in zip_files:
            # Extrair o arquivo PDF alvo
            zip_ref.extract(target_pdf, extract_path)
            print("Extração concluída.")
        else:
            print(f"Arquivo PDF '{target_pdf}' não encontrado no arquivo ZIP.")

# Função para extrair os dados da tabela de PDF
def extrair_dados_pdf(pdf_path):
    print("Extraindo dados do arquivo PDF...")
    dfs = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    print("Extração de dados do PDF concluída.")
    return pd.concat(dfs)

# Função para salvar os dados em CSV
def salvar_para_csv(dataframe, csv_path):
    print("Salvando dados em arquivo CSV...")
    dataframe.to_csv(csv_path, index=False)
    print("Dados salvos em", csv_path)

# Função para substituir abreviações nas colunas
def substituir_abreviacoes(dataframe):
    print("Substituindo abreviações nas colunas...")
    # Mapeamento das abreviações para descrições completas
    abreviacoes = {
        'OD': 'Oftalmologia Diagnóstica',
        'AMB': 'Ambulatório'
    }
    # Substituição das abreviações nas colunas específicas
    dataframe['OD'] = dataframe['OD'].map(abreviacoes)
    dataframe['AMB'] = dataframe['AMB'].map(abreviacoes)
    print("Abreviações substituídas.")
    return dataframe

# Nome do arquivo zip
zip_path = r'D:\GitHubRepositorio\teste-de-nivelamento\1- TESTE DE WEB SCRAPING\anexos.zip'

# Diretório de extração para o PDF
extract_path = r'D:\GitHubRepositorio\teste-de-nivelamento\1- TESTE DE WEB SCRAPING'

# Nome do arquivo PDF específico que deseja extrair
target_pdf = 'Anexo_I_Rol_2021RN_465.2021_RN599_RN600.pdf'

# Extrair o arquivo PDF específico do arquivo zip
extrair_pdf_especifico_de_zip(zip_path, extract_path, target_pdf)

# Nome do arquivo PDF extraído
pdf_path = os.path.join(extract_path, target_pdf)

print("Iniciando processamento...")

dados_pdf = extrair_dados_pdf(pdf_path) # Extrair dados do PDF
# Salvar dados em CSV
csv_path = 'Teste_Micael_dos_Santos.csv'
salvar_para_csv(dados_pdf, csv_path)

dados_pdf = substituir_abreviacoes(dados_pdf) # Substituir abreviações

nome_zip = 'Teste_Micael_dos_Santos.zip' # Nome do arquivo zip

# Criar arquivo zip e adicionar o CSV
with zipfile.ZipFile(nome_zip, 'w') as zipf:
    zipf.write(csv_path, os.path.basename(csv_path))

os.remove(csv_path) # Remover arquivo CSV
os.remove(pdf_path) # Remover arquivo PDF extraído

print("Processo concluído. Arquivo zip criado:", nome_zip)
