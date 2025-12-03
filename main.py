import time
from src.spiders.hardware_spider import buscar_produtos
from src.cleaning.processor import limpar_preco, padronizar_nome
from src.database import setup_db, salvar_dados

def job():
    print("\n⏰ Iniciando rodada de monitoramento...")
    
    # URL de exemplo (Google) só para testar a conexão sem bloquear
    urls = ["https://www.google.com"] 
    
    todos_produtos = []

    for url in urls:
        raw_data = buscar_produtos(url)
        
        for item in raw_data:
            # Como nosso spider é genérico, vamos simular um preço para teste
            # No mundo real, o spider traria o preço certo
            preco_fake = "R$ 1.500,00" 
            
            preco_limpo = limpar_preco(preco_fake)
            nome_limpo = padronizar_nome(item['produto'])
            
            if preco_limpo > 0:
                todos_produtos.append({
                    'produto': nome_limpo,
                    'preco': preco_limpo,
                    'loja': 'Teste'
                })
        
        time.sleep(1)

    if todos_produtos:
        salvar_dados(todos_produtos)
    else:
        print("Nenhum dado válido coletado nesta rodada.")

if __name__ == "__main__":
    setup_db()
    job()