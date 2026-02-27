import pandas as pd
from db_connection import get_engine

engine = get_engine()

files = {
    "customers": "customers.csv",
    "properties": "properties.csv",
    "customer_search_history": "customer_search_history.csv",
    "wishlist": "wishlist.csv",
    "visit_history": "visit_history.csv",
    "contact_history": "contact_history.csv"
}

for table, file in files.items():

    df = pd.read_csv(file)   # read CSV

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

print("All tables loaded successfully")