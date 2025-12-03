import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

def buscar_produtos(url_alvo):
    print(f"🕷️ Iniciando coleta em: {url_alvo}")
    
    try:
        response = requests.get(url_alvo, headers=HEADERS, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ Erro ao acessar: Status {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        produtos_encontrados = []

        # --- ATENÇÃO: Seletor Genérico para Teste ---
        # Em um site real, você terá que trocar 'div' e 'product-card' pelas classes reais
        # Se não encontrar nada, ele avisa.
        cards = soup.find_all('div', class_='product-card') 
        
        # fallback para teste se não achar a classe especifica (tenta achar qualquer link)
        if not cards:
            print("⚠️ Nenhum card específico encontrado. Tentando buscar links genéricos para teste...")
            cards = soup.find_all('a')[:5] # Pega os 5 primeiros links só para não vir vazio

        for card in cards:
            try:
                # Tenta pegar nome (se for um card estruturado) ou o texto do link
                nome = card.get_text().strip()
                if len(nome) > 50: nome = nome[:50] # Corta se for muito longo
                
                # Simulação de preço (já que sites reais variam muito o HTML)
                preco = "R$ 0,00" 
                
                produtos_encontrados.append({
                    'produto': nome,
                    'preco': preco,
                    'loja': 'Loja Detectada'
                })
            except:
                continue

        return produtos_encontrados

    except Exception as e:
        print(f"❌ Erro crítico: {e}")
        return []