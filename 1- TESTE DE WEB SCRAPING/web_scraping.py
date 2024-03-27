import requests
import os
import shutil
import zipfile
from bs4 import BeautifulSoup

# Função para fazer o download dos arquivos
def download_file(url, directory):
    filename = os.path.join(directory, url.split('/')[-1])  # Busca o nome do arquivo na URL
    with open(filename, 'wb') as f:  # Faz o download do arquivo para o 
        response = requests.get(url)
        f.write(response.content)
    return filename

def download_anexos():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    response = requests.get(url)  # Faz a requisição para o site
    soup = BeautifulSoup(response.text, 'html.parser')  # Cria um objeto BeautifulSoup

    # Encontra todos os links para os arquivos PDF
    pdf_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('.pdf'):
            pdf_links.append(href)

    # Filtrar os dois arquivos PDF desejados (Anexo I e Anexo II)
    pdf_files = []
    for pdf_link in pdf_links:
        if "Anexo_I_Rol_2021RN_465.2021_RN599_RN600" in pdf_link or "Anexo_II_DUT_2021_RN_465.2021_RN599" in pdf_link:
            # Baixa os arquivos PDF e adiciona à lista de arquivos baixados
            pdf_file = download_file(pdf_link, os.path.dirname(os.path.abspath(__file__)))
            pdf_files.append(pdf_file)
            print(f"Download realizado: {pdf_file}")

    # Define o nome do arquivo ZIP
    zip_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'anexos.zip')

    # Cria o arquivo ZIP a partir dos arquivos PDF baixados
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for i, pdf_file in enumerate(pdf_files, start=1):
            zipf.write(pdf_file, os.path.basename(pdf_file))

    print(f"Arquivos compactados em: {zip_filename}")

    # Excluir os arquivos PDF após a criação do arquivo ZIP
    for pdf_file in pdf_files:
        os.remove(pdf_file)

def main():
    download_anexos()

if __name__ == "__main__":
    main()
