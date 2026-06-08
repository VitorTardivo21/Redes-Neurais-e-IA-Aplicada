# src/extract_text.py
# Responsavel: extrair texto de PDFs e HTML
import pdfplumber, requests, re
from bs4 import BeautifulSoup
from pathlib import Path
def extrair_de_pdf(caminho):
"""Extrai texto de um arquivo PDF local."""
textos = []
with pdfplumber.open(caminho) as pdf:
for p in pdf.pages:
t = p.extract_text()
if t: textos.append(t)
return '\n'.join(textos)
def extrair_de_html(url):
"""Extrai texto de uma pagina HTML remota."""
r = requests.get(url, timeout=10, headers={'User-Agent':'ProjetoFEAP/1.0'})
soup = BeautifulSoup(r.text, 'html.parser')
for tag in soup(['script','style','nav','header','footer']):
tag.decompose()
return soup.get_text(separator='\n', strip=True)
