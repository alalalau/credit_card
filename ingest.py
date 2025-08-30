import os
import csv
from supabase import create_client, Client

from dotenv import load_dotenv
load_dotenv()

url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_KEY", "")

supabase: Client = create_client(url, key)

def ingest_data(transaction_date: str, transaction_type: str, details: str, amount: float):
    data = {
        "transaction_date": transaction_date,
        "type": transaction_type,
        "details": details,
        "amount": amount
    }
    try:
        res = supabase.table("transactions").insert(data).execute()
        return res
    except Exception as e:
        print(e)
        return None

def ingest_data_from_csv(csv_path: str):
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        # skip header
        next(reader)
        for row in reader:
            transaction_date = row[0]
            transaction_type = row[2]
            details = row[3]
            amount = float(row[4])
            ingest_data(transaction_date, transaction_type, details, amount)
            
# if __name__ == "__main__":
#     for file in os.listdir("data"):
#         if file.endswith(".csv"):
#             print(f"Ingesting data from {file}")
#             ingest_data_from_csv(os.path.join("data", file))
            
