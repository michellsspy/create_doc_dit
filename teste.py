
import os
import platform
import subprocess
import ctypes.util
import requests
from pathlib import Path
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from weasyprint import HTML, CSS

base_dir = Path(__file__).resolve().parent

def baixar_arquivo(base_dir: Path):     
    # Exemplo de uso
    url = 'https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2022-01-04/gtk3-runtime-3.24.31-2022-01-04-ts-win64.exe'
    nome_arquivo = f'{base_dir}/.exec/gtk3-runtime-3.24.30-2021-01-12-ts-win64.exe'
    
    try:
        resposta = requests.get(url, stream=True)
        resposta.raise_for_status()  # Levanta erro se a resposta for ruim (ex: 404, 500)

        with open(nome_arquivo, 'wb') as arquivo:
            for bloco in resposta.iter_content(chunk_size=8192):
                if bloco:
                    arquivo.write(bloco)
        print(f"Download concluído: {nome_arquivo}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")
        
baixar_arquivo(base_dir)