import requests
import os
from datetime import datetime, timedelta

def download_arquivos_ans(url, destino):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destino, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo baixado com sucesso para: {destino}")
    else:
        print("Falha ao baixar o arquivo.")

def baixar_arquivos_ansi_2_anos():
    base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
    ano_atual = datetime.now().year
    for ano in range(ano_atual - 2, ano_atual):
        for mes in range(1, 13):
            data_referencia = datetime(ano, mes, 1)
            nome_arquivo = f"{data_referencia.strftime('%Y%m')}_DemonstrativoFinanceiroOperadoras.csv.zip"
            url_arquivo = base_url + nome_arquivo
            destino = os.path.join(r"C:\Users\micael.santos\Documents\GitHub\teste-de-nivelamento\3- TESTE DE BANCO DE DADOS\DADOS", nome_arquivo)
            download_arquivos_ans(url_arquivo, destino)

def baixar_dados_cadastrais_operadoras():
    url = "https://dados.gov.br/dataset/59eae6e9-7232-4e13-bbf3-00fdd040d711/resource/eb49bf90-78fe-4df3-a2ed-f1819fdac8f5/download/cadop.csv"
    destino = r"C:\Users\micael.santos\Documents\GitHub\teste-de-nivelamento\3- TESTE DE BANCO DE DADOS\DADOS"
    download_arquivos_ans(url, destino)

# Chamar as funções para baixar os arquivos
baixar_arquivos_ansi_2_anos()
baixar_dados_cadastrais_operadoras()
