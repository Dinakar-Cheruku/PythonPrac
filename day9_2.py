import sqlite3
import pandas as pd

# conn = sqlite3.connect('sqlalchemy1.db')
# df = pd.read_sql_query("select * from student", conn)
# print(df)


#to connect to postgres server we need psycopg2-binary driver from sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, select, text

# Database credentials
db_user = "evr_sql_app"
db_password = "5LViU5pLkSjRHECec9NF4wRxxV"
db_host = "endeavourtech.ddns.net"          # or your server host
db_port = "50271"
db_name = "StocksDB"

# Connection string
DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create MetaData object to reflect existing tables
metadata = MetaData()
metadata.reflect(bind=engine, schema='endeavour')  # automatically loads existing tables


company = metadata.tables['endeavour.company_locations']

# Query data
with engine.connect() as conn:
    result = conn.execute(select(company))
    for row in result:
        print(row)

#