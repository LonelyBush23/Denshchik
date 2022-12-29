import pandas as pd


file_name = 'vacancies_dif_currencies.csv'
df = pd.read_csv(file_name)
currencies = df['salary_currency'].unique()
right_currencies = []
for cur in currencies:
    if list(df['salary_currency']).count(cur) > 5000:
        right_currencies.append(cur)
del right_currencies[0]
df.sort_values(by='published_at', inplace=True)
first_date = list(df['published_at'])[0]
second_date = list(df['published_at'])[-1]
print(right_currencies, first_date, second_date)
data_currencies = pd.DataFrame(columns=['date', 'BYR', 'USD', 'EUR', 'KZT', 'UAH'])
for year in range(2003, 2023):
    for month in range(1, 13):
        date = f'01/0{month}/{year}' if month < 10 else f'01/{month}/{year}'
        new_row = {'date': date}
        res = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'
        values_cur = pd.read_xml(res, encoding='cp1251')
        for cur in right_currencies:
            if len(values_cur[values_cur['CharCode'] == cur]['Value'].values) != 0:
                value = '.'.join(str(values_cur[values_cur['CharCode'] == cur]['Value'].values[0]).split(','))
                new_row[cur] = float(value) / int(values_cur[values_cur['CharCode'] == cur]['Nominal'].values[0])
        data_currencies = pd.concat([data_currencies, pd.DataFrame.from_records([new_row])], axis=0, ignore_index=True)
        if date == '01/07/2022':
            break
data_currencies.to_csv('data_currencies(3.3.1).csv', index=False)
print(data_currencies)


# file_name = 'vacancies_dif_currencies.csv'
# df = pd.read_csv(file_name)
# currencies = df['salary_currency'].unique()
# dict_cur = {}
# for cur in currencies:
#     count_cur = list(df['salary_currency']).count(cur)
#     if count_cur > 5000:
#         dict_cur[cur] = count_cur
# print(dict_cur)