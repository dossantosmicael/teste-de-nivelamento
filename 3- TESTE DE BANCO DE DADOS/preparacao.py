import wget
import os
import zipfile
from ftplib import FTP

# Função para baixar os arquivos dos anos 2022 e 2023 do repositório da ANS via FTP
def baixar_arquivos_ans():
    # Diretórios dos anos 2022 e 2023
    anos = ["2022", "2023"]
    
    # Diretório de destino onde os arquivos serão salvos
    destino = r"D:\GitHubRepositorio\teste-de-nivelamento\3- TESTE DE BANCO DE DADOS\DADOS"
    
    # Conectar ao servidor FTP
    with FTP("dadosabertos.ans.gov.br") as ftp:
        ftp.login()  # Login anônimo

        for ano in anos:
            try:
                # Entrar no diretório do ano
                ftp.cwd(f"/FTP/PDA/demonstracoes_contabeis/{ano}/")

                # Listar os arquivos no diretório
                arquivos = ftp.nlst()

                # Baixar os arquivos ZIP
                for arquivo in arquivos:
                    if arquivo.endswith(".zip"):
                        with open(os.path.join(destino, arquivo), "wb") as f:
                            ftp.retrbinary(f"RETR {arquivo}", f.write)
                        print(f"Arquivo ZIP baixado com sucesso: {arquivo}")
                        
                        # Descompactar o arquivo ZIP
                        with zipfile.ZipFile(os.path.join(destino, arquivo), 'r') as zip_ref:
                            zip_ref.extractall(destino)
                        # Excluir o arquivo ZIP
                        os.remove(os.path.join(destino, arquivo))
                        print(f"Arquivo ZIP descompactado com sucesso: {arquivo}")
                    else:
                        print(f"Arquivo {arquivo} não é um arquivo ZIP.")
            except Exception as e:
                # Em caso de falha ao baixar os arquivos, imprime uma mensagem de erro
                print(f"Falha ao baixar/arquivos do diretório: {ano}")
                print(f"Erro: {e}")

# Função para baixar os dados cadastrais das operadoras da ANS
def baixar_dados_cadastrais_operadoras():
    # URL do arquivo CSV contendo os dados cadastrais das operadoras
    url = "https://dados.gov.br/dataset/59eae6e9-7232-4e13-bbf3-00fdd040d711/resource/eb49bf90-78fe-4df3-a2ed-f1819fdac8f5/download/cadop.csv"
    
    # Diretório de destino onde o arquivo será salvo
    destino = r"D:\GitHubRepositorio\teste-de-nivelamento\3- TESTE DE BANCO DE DADOS\DADOS\cadop.csv"
    
    # Mensagem de depuração para indicar que o arquivo está sendo baixado
    print(f"Tentando baixar o arquivo de URL: {url}")
    
    try:
        # Tenta baixar o arquivo usando wget
        wget.download(url, out=destino)
        
        # Mensagem indicando que o arquivo foi baixado com sucesso
        print(f"Arquivo baixado com sucesso para:  {destino}")
    except Exception as e:
        # Em caso de falha ao baixar o arquivo, imprime uma mensagem de erro
        print("Falha ao baixar o arquivo.")
        print(f"URL utilizada: {url}")
        print(f"Erro: {e}")

# Chamar as funções para baixar os arquivos
baixar_arquivos_ans()
baixar_dados_cadastrais_operadoras()