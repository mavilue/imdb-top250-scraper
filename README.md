# IMDB Top 250 Scraper

Um projeto em Python para coletar automaticamente informações dos filmes mais bem avaliados do **IMDb Top 250**.  
O script realiza scraping da página oficial do ranking *Top 250*, extrai dados essenciais e salva tudo em um arquivo CSV estruturado na pasta `data/`.  
O código é modular e organizado em funções reutilizáveis, tornando o scraper estável e fácil de manter.

---

## Funcionalidades

Este projeto realiza a extração estruturada dos filmes presentes na lista *IMDb Top 250*, fornecendo dados prontos para análise. As principais funcionalidades incluem:

- Seleção aleatória de **user agents** para simular uma solicitação de navegador real e evitar bloqueios do IMDb  
- Criação automática da pasta `data/` e geração do arquivo `top250.csv` com todos os filmes extraídos  
- Organização do código em funções reutilizáveis (`scraper.py` e `utils.py`), facilitando manutenção e expansão  
- Numeração do DataFrame e CSV iniciando em **1**  

### Dados coletados por filme:

- Título  
- Ano de lançamento  
- Nota (rating)  
- Link oficial do IMDb  

> Observação: Campos como classificação indicativa e duração não estão disponíveis diretamente na lista Top 250, mas podem ser adicionados em melhorias futuras.

---

## Estrutura do projeto
top250_imdb/
│
├─ main.py # arquivo principal que executa o scraper
├─ scraper.py # funções de requisição e extração do IMDb
├─ utils.py # funções auxiliares, como salvar CSV
├─ data/ # pasta onde o CSV será salvo automaticamente
│ └─ top250.csv
└─ README.md # documentação do projeto

---

## Stack utilizada

- Python 3  
- Requests  
- BeautifulSoup (bs4)  
- CSV (biblioteca padrão do Python)  
- Pandas (para exibição e manipulação dos dados)