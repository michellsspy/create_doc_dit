"""
✅ Opções para converter .py em PDF:
✅ **1. Usar pygments para gerar um PDF com sintaxe colorida (recomendado)

pip install pygments
"""

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from weasyprint import HTML, CSS
import os

diretorio = '/home/michel/Documentos/create_doc_dit/templates'

arquivos_py = [f for f in os.listdir(diretorio) if f.endswith('.ipynb') and os.path.isfile(os.path.join(diretorio, f))]


for arquivo in arquivos_py:
    input_path = f'templates/{arquivo}'
    arquivo = arquivo.split('.')[0]
    output_html_dir = '/home/michel/Documentos/create_doc_dit/html'
    output_pdf_dir = '/home/michel/Documentos/create_doc_dit/pdf'

    output_html = os.path.join(output_html_dir, f'{arquivo}.html')
    output_pdf = os.path.join(output_pdf_dir, f'{arquivo}.pdf')
    temp_css_path = os.path.join(output_html_dir, f'{arquivo}.css')

    os.makedirs(output_html_dir, exist_ok=True)
    os.makedirs(output_pdf_dir, exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as f:
        code = f.read()

    cssstyles = """
    pre {
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
    overflow-wrap: anywhere !important;
    word-break: break-all !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    font-size: 9pt !important;
    margin: 0;
    padding: 0.5em;
    }

    body {
    background: white !important;
    margin: 1cm;
    }

    @page {
    size: A4 portrait;
    margin: 2cm;
    }

    div.highlight {
    max-width: 100% !important;
    overflow-x: auto;
    }
    """

    # Gera o HTML com o CSS inline do pygments para estilos de syntax highlight
    formatter = HtmlFormatter(full=True, style='friendly', cssstyles="pre { white-space: pre-wrap !important; }")
    html_code = highlight(code, PythonLexer(), formatter)

    # Escreve o HTML em arquivo
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_code)

    # Salva o CSS customizado para usar no PDF
    with open(temp_css_path, 'w', encoding='utf-8') as f:
        f.write(cssstyles)

    # Gera o PDF aplicando o CSS customizado para controle de quebra e layout
    HTML(output_html).write_pdf(output_pdf, stylesheets=[CSS(temp_css_path)])

    print(f"PDF gerado em: {output_pdf}")











