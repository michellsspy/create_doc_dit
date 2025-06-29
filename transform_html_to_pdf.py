"""
Você pode transformar um arquivo HTML em PDF em Python utilizando a biblioteca pdfkit, que é um wrapper para o wkhtmltopdf, uma ferramenta poderosa baseada em WebKit.

✅ Passos para usar:
Instale o pdfkit e o wkhtmltopdf.

pip install pdfkit

No Windows, Linux ou macOS, você também precisa instalar o wkhtmltopdf:

Windows: https://wkhtmltopdf.org/downloads.html

Linux (Ubuntu/Debian):

sudo apt install wkhtmltopdf


Use o script para converter o HTML em PDF.
"""

import pdfkit

# Caminho para o wkhtmltopdf (use apenas se necessário)
# path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Caminho do arquivo HTML e PDF
html_file = 'C:\Users\MichelSouzaSantana\OneDrive - Dataside\Documentos\create_doc_dit\html\d_empresas_farol.html'
output_pdf = 'C:\Users\MichelSouzaSantana\OneDrive - Dataside\Documentos\create_doc_dit\pdf\d_empresas_farol.pdf'

# Convertendo (adicione `configuration=config` se necessário)
pdfkit.from_file(html_file, output_pdf)

print(f"PDF gerado com sucesso em: {output_pdf}")
