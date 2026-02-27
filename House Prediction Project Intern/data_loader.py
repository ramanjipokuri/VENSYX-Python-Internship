import pandas as pd
from db_connection import get_engine


def run_query(query):
    """
    Executes ANY SQL query
    Returns dataframe
    """

    engine = get_engine()

    df = pd.read_sql(query, engine)

    return df