import requests
import zipfile
import os

from tqdm import tqdm

def baixar_arquivo(url_arquivo, nome_diretorio):
    response = requests.get(url_arquivo, stream=True)
    
    nome_arquivo = str(url_arquivo).split('/')[-1]

    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024

    if response.status_code == 200:
        print(f"Arquivo '{nome_arquivo}' iniciando download...")

        # Criando diretório se ele não existir
        if not os.path.exists(nome_diretorio):
            print(f"Criando diretório '{nome_diretorio}'...")
            os.makedirs(nome_diretorio)

        print(f"Baixando arquivo '{nome_arquivo}'...")
        with open(f'{nome_diretorio}/{nome_arquivo}', 'wb') as file:
            for data in tqdm(response.iter_content(block_size), total=total_size_in_bytes//block_size):
                if data:
                    file.write(data)                
        print(f"Arquivo '{nome_arquivo}' baixado com sucesso!")
        
        # Descompactar arquivo zip    
        with zipfile.ZipFile(f'{nome_diretorio}/{nome_arquivo}', 'r') as z:
            z.extractall(f'{nome_diretorio}')
        print(f"Arquivo '{nome_arquivo}' descompactado com sucesso!")
        
        # Removendo arquivo zipado
        os.remove(f'{nome_diretorio}/{nome_arquivo}')
        print(f"Arquivo '{nome_arquivo}' removido com sucesso!")
                
    else:
        raise Exception(f'Erro ao baixar o arquivo: {response.text}')
    

def main():

    url_arquivo = 'https://networksciencebook.com/translations/en/resources/networks.zip'
    nome_diretorio = 'datasets'        
    
    try:
        baixar_arquivo(url_arquivo, nome_diretorio)        
    except Exception as e:
        print(f"Erro ao baixar ou descompactar arquivo: {e}")

if __name__ == '__main__':
    main()