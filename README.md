# TechPrice Scout: Pipeline de Monitoramento de Preços

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Focus](https://img.shields.io/badge/Focus-Data_Engineering-green)

> "O mundo real é sujo. O valor está em quem sabe limpar e estruturar."

## Sobre o Projeto

O **TechPrice Scout** é um projeto de Engenharia de Dados focado na construção de um pipeline **ETL (Extract, Transform, Load)** para monitoramento de preços de hardware.

Diferente de projetos que utilizam datasets prontos e limpos (Kaggle), este projeto enfrenta o desafio da "Internet Real": extrair dados de HTML não estruturado, lidar com inconsistências de formatação (moedas, textos sujos, erros de encoding) e entregar um dado analítico confiável em um banco de dados SQL.

### Objetivo
Automatizar a busca por oportunidades de hardware (ex: Placas de Vídeo), permitindo análises históricas de preço e detecção de ofertas reais.

---

## Arquitetura do Pipeline

O projeto segue o fluxo clássico de ETL:

1.  **Extract (Coleta):** Robôs (Spiders) baseados em `Requests` e `BeautifulSoup` navegam em e-commerces simulando um browser real (User-Agent rotation) para evitar bloqueios.
2.  **Transform (Limpeza):** O coração do projeto. Utilização de **Pandas** e **Regex** para normalizar nomes de produtos e converter moedas formatadas (`R$ 1.200,00`) em floats computáveis (`1200.00`).
3.  **Load (Armazenamento):** Persistência dos dados em um banco **SQLite**, garantindo integridade e permitindo consultas SQL complexas (ex: "Menor preço dos últimos 30 dias").

---

## O Diferencial: Data Cleaning (Antes e Depois)

A maior complexidade deste projeto não é baixar a página, mas tornar o dado utilizável. Abaixo, exemplos reais do tratamento realizado pelo script `src/cleaning/processor.py`:

| Dado Bruto (Coletado da Web) | Tratamento Aplicado | Dado Limpo (Salvo no SQL) |
| :--- | :--- | :--- |
| `\n PLACA DE VÍDEO RTX 3060 -- OFERTA \n` | `.lower()`, `.strip()`, Remoção de Stopwords | `rtx 3060` |
| `R$ 1.899,90 à vista` | Regex `[^\d,]`, conversão float | `1899.90` |
| `(Esgotado)` ou `Vazio` | Validação Lógica (`if not`) | *(Ignorado/Não Salvo)* |

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Web Scraping:** BeautifulSoup4, Requests
* **Manipulação de Dados:** Pandas, Regex (re)
* **Banco de Dados:** SQLite3
* **Agendamento:** Time / Schedule (Simulação de Daemon)

---

## Estrutura do Projeto

```text
monitor-precos/
│
├── data/
│   └── db/             # Banco de dados SQLite (gerado automaticamente)
│
├── src/
│   ├── spiders/        # Scripts de coleta (Crawler)
│   ├── cleaning/       # Lógica de limpeza (Regex/Pandas)
│   └── database.py     # Gerenciamento de conexões SQL
│
├── main.py             # Orquestrador do Pipeline
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
```

Como Rodar Localmente
Pré-requisitos
Python 3 instalado.

Passo a passo
Clone o repositório:

Bash

git clone https://github.com/vinimachado81/tech-price-scout.git
cd tech-price-scout
Crie um ambiente virtual (Recomendado):

Bash

python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Execute o Pipeline:

Bash

python main.py
O script irá criar o banco de dados automaticamente na primeira execução.

Próximos Passos (Roadmap)
[ ] Implementar Dashboards com Streamlit para visualização dos preços.

[ ] Adicionar notificação via Telegram quando o preço atingir um alvo.

[ ] Dockerizar a aplicação para rodar em nuvem.

[ ] Migrar do SQLite para PostgreSQL.

## Contato

Gostou do projeto? Vamos conectar!

* **LinkedIn:** [Acesse meu perfil](https://www.linkedin.com/in/vinícius-machado-de-carvalho81/)
* **Email:** [Entre em contato](mailto:vinimachado81@gmail.com)
