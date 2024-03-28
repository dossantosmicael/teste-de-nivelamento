import wget
import os
from datetime import datetime, timedelta

# Função para baixar os arquivos dos últimos 2 anos do repositório da ANS
def baixar_arquivos_ansi_2_anos():
    # URL base onde os arquivos estão localizados
    base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
    
    # Diretório de destino onde os arquivos serão salvos
    destino = r"D:\GitHubRepositorio\teste-de-nivelamento\3- TESTE DE BANCO DE DADOS\DADOS"
    
    # Obtém o ano atual
    ano_atual = datetime.now().year
    
    # Itera sobre os anos dos últimos 2 anos
    for ano in range(ano_atual - 2, ano_atual):
        # Itera sobre os meses (de 1 a 12)
        for mes in range(1, 13):
            # Cria uma data de referência para o ano e mês atual
            data_referencia = datetime(ano, mes, 1)
            
            # Formata o nome do arquivo conforme o padrão fornecido
            nome_arquivo = f"{data_referencia.strftime('%Y%m')}_DemonstrativoFinanceiroOperadoras.csv.zip"
            
            # Monta a URL completa do arquivo
            url_arquivo = base_url + nome_arquivo
            
            # Mensagem de depuração para indicar qual arquivo está sendo baixado
            print(f"Tentando baixar o arquivo de URL: {url_arquivo}")
            
            try:
                # Tenta baixar o arquivo usando wget
                wget.download(url_arquivo, out=destino)
                
                # Mensagem indicando que o arquivo foi baixado com sucesso
                print(f"Arquivo baixado com sucesso para: {destino}")
            except Exception as e:
                # Em caso de falha ao baixar o arquivo, imprime uma mensagem de erro
                print("Falha ao baixar o arquivo.")
                print(f"URL utilizada: {url_arquivo}")
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
baixar_arquivos_ansi_2_anos()
baixar_dados_cadastrais_operadoras()
