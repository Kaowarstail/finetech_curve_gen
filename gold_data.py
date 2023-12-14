import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import random
import datetime

import os
from dotenv import load_dotenv

data_file = '/home/kaowarstail/Documents/finetech/finetech_curve_gen/Data OR.xlsx'  # Chemin vers le fichier de données

# Charger les données depuis le fichier Excel
df = pd.read_excel(data_file)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
# Define the start and end dates
start_date = datetime.date(2006, 1, 9)
end_date = datetime.date(2023, 11, 3)

# Maintenant, vous pouvez sélectionner les données en utilisant des dates
# df_selected = df.loc[start_date:end_date]



# Define the maximum duration in days (3 months)
max_duration = datetime.timedelta(days=90)

# Generate random start dates within the range
num_periods = 250  # Number of periods to generate
periods = []
for _ in range(num_periods):
    duration = random.randint(60, max_duration.days)
    start = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days - duration))
    end = start + datetime.timedelta(days=duration)
    periods.append((start, end))

# Define market colors
mc = mpf.make_marketcolors(up='g', down='r', wick={'up':'g', 'down':'r'}, volume='inherit')

# Define style
s  = mpf.make_mpf_style(marketcolors=mc)


# Execute the code for each period
for start, end in periods:
    start_date_str = start.strftime("%Y-%m-%d")
    end_date_str = end.strftime("%Y-%m-%d")
    # Update the code to use the selected start and end dates
    start_datetime = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
    df_selected = df.loc[end_datetime:start_datetime]
    # Inverser l'ordre des données
    df_selected = df_selected.iloc[::-1]

    
    # Check if df_selected is not empty
    if not df_selected.empty:
        filename = f'screenshot/graph_{start_date_str}_{end_date_str}.png'
        mpf.plot(df_selected, type='candle', style=s, title='Gold Price', ylabel='Gold Price (USD)', savefig=filename)
    else:
        print(f"No data available for the period {start_date_str} to {end_date_str}")
