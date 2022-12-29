import pandas as pd
import requests
from pandas import json_normalize

pd.set_option('expand_frame_repr', False)
df_res = pd.DataFrame()
time = ['00:00:01', '06:00:00', '12:00:00', '18:00:00', '23:59:59']
for i in range(1, len(time)):
    for j in range(20):
        req_page = requests.get(f'https://api.hh.ru/vacancies?specialization=1&per_page=100&page={j}&date_from=2022-12-07T{time[i - 1]}&date_to=2022-12-07T{time[i]}').json()
        vacancies = req_page['items']
        if len(vacancies) == 0:
            break
        df = json_normalize(vacancies)
        df1 = df[['name', 'salary.from', 'salary.to', 'salary.currency', 'area.name', 'published_at']]
        df1.columns = df1.columns.str.replace('.', '_')
        df_res = df_res.append(df1)
df_res.to_csv('vacancies(3.3.3).csv', index=False)