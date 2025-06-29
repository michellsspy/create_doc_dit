"""
Você pode transformar um arquivo HTML em PDF em Python utilizando a biblioteca pdfkit, que é um wrapper para o wkhtmltopdf, uma ferramenta poderosa baseada em WebKit.

✅ Passos para usar:
Instale o pdfkit e o wkhtmltopdf.

No Windows, Linux ou macOS, você também precisa instalar o wkhtmltopdf:

Windows: https://wkhtmltopdf.org/downloads.html

Linux (Ubuntu/Debian):

sudo apt install wkhtmltopdf


Use o script para converter o HTML em PDF.
"""

import pdfkit

html_file = '/home/michel/Documentos/create_doc_dit/html/d_empresas_farol - Databricks.html'
output_pdf = '/home/michel/Documentos/create_doc_dit/pdf/d_empresas_farol.pdf'

options = {
    'enable-local-file-access': None,
    'no-stop-slow-scripts': None,
    'load-error-handling': 'ignore',
    'debug-javascript': None
}

pdfkit.from_file(html_file, output_pdf, options=options)

print(f"PDF gerado com sucesso em: {output_pdf}")

