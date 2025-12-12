import requests
import json
from bs4 import BeautifulSoup
import random

def get_headers():
    # Lista de user-agents para simular uma solicitação de um navegador real, evitando bloqueios do site (como erro 403)
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        'Mozilla/5.0 (X11; Linux x86_64)'
    ]
    return {
        "user-agent": random.choice(user_agents),
        "accept-language": "en-US,en;q=0.9"
    }

def extract_items(json_data):
    # Tenta encontrar a lista de filmes em diferentes caminhos do JSON
    caminhos = [
        ["props", "pageProps", "pageData", "chartTitles", "edges"],
        ["props", "pageProps", "pageData", "chartTitles", "titleList"],
        ["props", "pageProps", "pageData", "titles"]
    ]

    for caminho in caminhos:
        data = json_data
        for key in caminho:
            data = data.get(key) if isinstance(data, dict) else None
            if data is None:
                break
        if data is not None:
            return data
    return []

def top250_movies():
    url = "https://www.imdb.com/chart/top/"
    
    # Faz a requisição HTTP para a página
    response = requests.get(url, headers=get_headers())
    soup = BeautifulSoup(response.text, "html.parser")

    # Localiza o script JSON que contém os dados dos filmes
    script_json = soup.find("script", id="__NEXT_DATA__")
    if not script_json:
        return []

    data = json.loads(script_json.string)
    itens = extract_items(data)

    filmes = []
    for entry in itens:
        movie = entry.get("node", entry)
        filmes.append({
            "titulo": movie.get("titleText", {}).get("text"),
            "ano": movie.get("releaseYear", {}).get("year"),
            "nota": movie.get("ratingsSummary", {}).get("aggregateRating"),
            "link": "https://www.imdb.com" + movie.get("id", "")
        })
    return filmes