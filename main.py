import matplotlib.pyplot as plt
import requests
import json 
import random
import datetime

start_date = datetime.date(1970, 1, 1)
end_date = datetime.date.today()

num_queries = 5  # Nombre de requêtes à effectuer
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
    res = requests.get(f'https://data.nasdaq.com/api/v3/datasets/LBMA/GOLD.json?start_date={query_start_str}&end_date={query_end_str}')
    response = json.loads(res.text)
    data = response['dataset']['data']

    dates = [row[0] for row in data[::-1]]  # Inverser l'ordre des dates
    values = [row[1] for row in data[::-1]]  # Inverser l'ordre des valeurs

    # Tracer le graphique
    plt.plot(dates, values)
    plt.xlabel('Date')
    plt.ylabel('Gold Price (USD)')
    plt.title('Gold Price: London Fixing')
    plt.xticks(rotation=45)

    # Générer un nom de fichier unique pour chaque capture
    filename = f'graph_{query_start_str}_{query_end_str}.png'
    filepath = output_folder + filename

    # Sauvegarder le graphique en haute qualité
    plt.savefig(filepath, dpi=300)

    # Afficher le graphique
    # plt.show()
