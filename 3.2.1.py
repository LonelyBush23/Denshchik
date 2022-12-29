import pandas as pd

file = input("Введите название файла: ")
reader = pd.read_csv(file)
reader['published_at'] = reader['published_at'].apply(lambda s: s[:4])
years = reader['published_at'].unique()
for year in years:
    data = reader[reader['published_at'] == year]
    data.to_csv(f'csv_files\\year_{year}.csv')