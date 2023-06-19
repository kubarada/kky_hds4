import numpy as np
import requests
import pandas as pd
from datetime import datetime



def download_data(link, name):
    csv_url = link
    response = requests.get(csv_url)
    if response.status_code == 200:
        file_name = name
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"CSV file downloaded and saved as '{file_name}'")
    else:
        print("Failed to download CSV file")

def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df.values

def available_places(csv_matrix): # returns np.array where first index is num of free plaaces and second is percentage
    availability = csv_matrix[0,5]/csv_matrix[0,1]*100
    return np.array([csv_matrix[0,5], availability]).astype(int)

def day_matrix(csv_matrix, day):
    days = {'pondělí' : 0, 'úterý' : 1, 'středa' : 2, 'čtvrtek' : 3, 'pátek' : 4, 'sobota' : 5, 'neděle' : 6}
    day_rows = list()

    for row in csv_matrix:
        date_string = row[-1]
        date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        if date.weekday() == days[day]:
            day_rows.append(row)
    return np.array(day_rows)

def day_stats(day):
    return 0

def hour_stat(hour):
    return 0

def day_hour_stat(day, hour):
    return 0



