import pandas as pd
import sqlite3
from sqlalchemy import create_engine

conn = sqlite3.connect('project(3.5.1).db')
engine = create_engine('sqlite:///C:\\Users\\66ava\\PycharmProjects\\Denshchik\\project(3.5.1).db')
df = pd.read_csv('data_currencies(3.3.1).csv')
df.to_sql('currencies', con=engine, index=False)