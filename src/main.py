import pandas as pd
from scraper import top250_movies
from utils import salvar_csv

# Executa a coleta
filmes = top250_movies()

# Salva CSV
salvar_csv(filmes)

# Exibe como DataFrame
df = pd.DataFrame(filmes)
df.index = range(1, len(df) + 1)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 150)
pd.set_option("display.colheader_justify", "left")

print(df)
print("\nFilmes coletados:", len(df))