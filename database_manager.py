import sqlite3
import pandas as pd
import yfinance as yf
import os

class FinancialDB:
    def __init__(self, db_name="data/financial_network.db"): # DODANO "data/"
        if not os.path.exists('data'):
            os.makedirs('data')
            
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS ownership (
            company TEXT,
            investor TEXT,
            shares REAL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def save_ownership(self, df):
        df.to_sql('ownership', self.conn, if_exists='replace', index=False) # ZMIENIONO na 'replace', żeby nie dublować danych przy każdym uruchomieniu
        print("\n" + "="*30)
        print("SUCCESS: Data saved to SQL!")
        print("="*30)

# --- EXECUTION ---
tickers = ['AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'TSLA', 'META']
db = FinancialDB()

all_data = []
for t in tickers:
    print(f"Fetching professional data for: {t}...")
    try:
        stock = yf.Ticker(t)
        holders = stock.institutional_holders
        if holders is not None:
            # Standaryzacja nazw kolumn dla Yahoo Finance
            for _, row in holders.iterrows():
                all_data.append({
                    'company': t, 
                    'investor': row['Holder'], 
                    'shares': row['Shares']
                })
    except Exception as e:
        print(f"Error fetching {t}: {e}")

if all_data:
    df_to_save = pd.DataFrame(all_data)
    db.save_ownership(df_to_save)
else:
    print("No data collected. Check your internet connection.")
