import os
import sys
from dotenv import load_dotenv
import pyathena as pa
from pyathena.pandas.cursor import PandasCursor
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))

sys.path.append(project_root)

env_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path=env_path)

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")

def athena_connect(access_key: str, secret_access_key: str):
    conn = pa.connect(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key,
        s3_staging_dir="s3://miac-2026/athena-results/",
        region_name="us-east-1",
        cursor_class=PandasCursor)
    print("Successfully connected to AWS Athena database!")
    cursor = conn.cursor()
    return cursor


def query_athena(query: str, cursor) -> pd.DataFrame:    
    return cursor.execute(query).as_pandas()


def read_sql_query(sql_file_path: str) -> str:
    with open(sql_file_path, "r", encoding="utf-8") as file:
        sql_query = file.read()
    print(f"Returning SQL query from file {sql_file_path}")
    return sql_query


if __name__ == "__main__":
    athena_connection = athena_connect(ACCESS_KEY, SECRET_ACCESS_KEY)
    sql_query = read_sql_query("model/queries/filter_2020_loans.sql")
    df = query_athena(sql_query, athena_connection)
    print(df.info())
