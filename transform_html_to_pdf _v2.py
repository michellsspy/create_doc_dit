"""
✅ Conversão de arquivos .py (ou .ipynb convertidos) para PDF com destaque de sintaxe usando pygments + WeasyPrint.
"""

import os
import platform
import subprocess
import ctypes.util
from pathlib import Path
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from weasyprint import HTML, CSS

# --- CONFIGURAÇÕES ---
PASTAS = ['doc', 'html', 'notebooks', 'pdf', 'scripts']
CSS_STYLE = """
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
# ----------------------

def instalar_gtk_local():
    base_dir = Path(__file__).resolve().parent
    instalador_path = base_dir / "lib" / "gtk-installer.exe"
    if not instalador_path.exists():
        print(f"[ERRO] Instalador não encontrado: {instalador_path}")
        return
    print(f"[INFO] Executando instalador GTK: {instalador_path}")
    try:
        subprocess.run([str(instalador_path)], check=True)
        print("[OK] Instalação concluída! Reinicie o terminal.")
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] A instalação falhou: {e}")

def verificar_e_instalar_gtk():
    if platform.system() != "Windows":
        return
    print("[INFO] Verificando dependência GTK...")
    lib = ctypes.util.find_library('gobject-2.0')
    if lib:
        print(f"[OK] GTK encontrado: {lib}")
    else:
        print("[AVISO] GTK não encontrado. Tentando instalação.")
        instalar_gtk_local()

def criar_pastas(base_dir: Path):
    for pasta in PASTAS:
        dir_path = base_dir / pasta
        if not dir_path.exists():
            dir_path.mkdir(parents=True)
            print(f"[+] Criada pasta: {dir_path}")
        else:
            print(f"[=] Pasta já existe: {dir_path}")

def converter_para_pdf(arquivo_path: Path, base_dir: Path):
    nome_arquivo = arquivo_path.stem
    input_path = arquivo_path
    output_html = base_dir / "html" / f"{nome_arquivo}.html"
    output_pdf = base_dir / "pdf" / f"{nome_arquivo}.pdf"
    temp_css_path = base_dir / "html" / f"{nome_arquivo}.css"

    # Lê o conteúdo
    with input_path.open("r", encoding="utf-8") as f:
        code = f.read()

    formatter = HtmlFormatter(full=True, style="friendly")
    html_code = highlight(code, PythonLexer(), formatter)

    with output_html.open("w", encoding="utf-8") as f:
        f.write(html_code)

    with temp_css_path.open("w", encoding="utf-8") as f:
        f.write(CSS_STYLE)

    HTML(str(output_html)).write_pdf(str(output_pdf), stylesheets=[CSS(str(temp_css_path))])
    print(f"[✓] PDF gerado: {output_pdf}")

def main():
    base_dir = Path(__file__).resolve().parent
    criar_pastas(base_dir)
    verificar_e_instalar_gtk()

    notebooks_dir = base_dir / "notebooks"
    arquivos_py = [f for f in notebooks_dir.glob("*.py") if f.is_file()]

    if not arquivos_py:
        print("[!] Nenhum arquivo .py encontrado em /notebooks")
        return

    for arquivo in arquivos_py:
        converter_para_pdf(arquivo, base_dir)

if __name__ == "__main__":
    main()
