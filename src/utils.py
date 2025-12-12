import csv
import os

def salvar_csv(lista_filmes, caminho="data/top250.csv"):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(
            arquivo,
            fieldnames=["titulo", "ano", "nota", "link"]
        )
        writer.writeheader()
        writer.writerows(lista_filmes)