import pandas as pd
import re

def limpar_preco(valor):
    """
    Recebe uma string suja (ex: 'R$ 1.899,90') e retorna um float (1899.90).
    """
    if not valor or valor == "":
        return 0.0
    
    valor = str(valor)
    # Remove tudo que não for dígito ou vírgula
    apenas_numeros = re.sub(r'[^\d,]', '', valor)
    
    # Troca vírgula por ponto
    preco_formatado = apenas_numeros.replace(',', '.')
    
    try:
        return float(preco_formatado)
    except ValueError:
        return 0.0

def padronizar_nome(texto):
    """
    Limpa o nome do produto para facilitar a busca.
    """
    if not texto:
        return "produto_desconhecido"
    
    texto = texto.lower()
    
    palavras_inuteis = ['promoção', 'oferta', 'placa', 'video', 'vídeo', '-']
    for palavra in palavras_inuteis:
        texto = texto.replace(palavra, '')
        
    texto = texto.strip()
    texto = " ".join(texto.split()) 
    
    return texto