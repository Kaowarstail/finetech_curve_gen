import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import requests
import json 
import random
import datetime

import os
from dotenv import load_dotenv

load_dotenv()  # Prend l'environnement à partir de .env

NASDAQ_DATA_LINK_API_KEY = os.getenv('NASDAQ_DATA_LINK_API_KEY')

start_date = datetime.date(1970, 1, 1)
end_date = datetime.date.today()

num_queries = 2  # Nombre de requêtes à effectuer
output_folder = '/home/kaowarstail/Documents/finetech/finetech_curve_gen/screenshot/'

for _ in range(num_queries):
    # Générer une période aléatoire de 3 mois
    random_start = random.randint(0, (end_date - start_date).days - 90)
    query_start = start_date + datetime.timedelta(days=random_start)
    query_end = query_start + datetime.timedelta(days=90)

    # Convertir les dates en format requis pour la requête
    query_start_str = query_start.strftime('%Y-%m-%d')
    query_end_str = query_end.strftime('%Y-%m-%d')

    # Effectuer la requête
    res = requests.get(f'https://data.nasdaq.com/api/v3/datasets/LBMA/GOLD.json?start_date={query_start_str}&end_date={query_end_str}&api_key={NASDAQ_DATA_LINK_API_KEY}')
    response = json.loads(res.text)
    # print(response)
    data = response['dataset']['data']

    dates = [row[0] for row in data[::-1]]  # Inverser l'ordre des dates
    values = [row[1] for row in data[::-1]]  # Inverser l'ordre des valeurs

    # Créer un DataFrame avec les données
    df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Column6', 'Column7'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Générer un nom de fichier unique pour chaque capture
    filename = f'graph_{query_start_str}_{query_end_str}.png'
    filepath = output_folder + filename

    df = df.dropna(subset=['Open', 'High', 'Low', 'Close'])


    # Tracer le graphique chandelier
    mpf.plot(df, type='candle', title='Gold Price: London Fixing', ylabel='Gold Price (USD)', savefig=filepath)
    # Sauvegarder le graphique en haute qualité
    plt.savefig(filepath, dpi=300)

    # Afficher le graphique
    # plt.show()
