# src/preprocess.py
# Responsavel: limpeza e normalizacao dos textos
import re, unicodedata
def limpar_texto(texto):
texto = re.sub(r'[ \t]+', ' ', texto)
texto = re.sub(r'\n{3,}', '\n\n', texto)
texto = re.sub(r'^\s*\d+\s*$', '', texto, flags=re.MULTILINE)
texto = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', texto)
return texto.strip()
def normalizar_texto(texto):
texto = unicodedata.normalize('NFC', texto)
texto = texto.replace('--','-').replace(' ',' ')
return texto
def processar(texto):
return normalizar_texto(limpar_texto(texto))
