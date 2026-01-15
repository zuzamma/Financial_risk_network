import sqlite3
import pandas as pd
import networkx as nx

def run_stress_test(target_company):
    conn = sqlite3.connect('data/financial_network.db')
    df = pd.read_sql_query("SELECT company, investor FROM ownership", conn)
    conn.close()

    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['investor'], row['company'])

    if target_company not in G:
        print(f"❌ Error: {target_company} not found.")
        return

    # Symulacja efektu domina
    investors = list(G.neighbors(target_company))
    exposed_companies = set()
    for inv in investors:
        for sibling_co in G.neighbors(inv):
            # Filtr: to musi być inna firma (krótki ticker) a nie fundusz
            if sibling_co != target_company and len(sibling_co) <= 5:
                exposed_companies.add(sibling_co)

    # Obliczanie wskaźnika systemowego
    total_market_firms = len([n for n in G.nodes() if len(n) <= 5])
    risk_pct = len(exposed_companies) / (total_market_firms - 1) if total_market_firms > 1 else 0

    # Wydruk w stylu profesjonalnego terminala
    print("\n" + "═"*50)
    print(f" ⚠️  SYSTEMIC STRESS TEST: CRISIS AT {target_company} ".center(50, "═"))
    print("═"*50)
    print(f"[{target_company}] is failing...")
    print(f"├── Direct Impact: {len(investors)} institutional holders affected.")
    print(f"└── Indirect Impact: {len(exposed_companies)} other giants at risk.")
    print("-" * 50)
    print(f"🔥 CONTAGION RISK SCORE: {risk_pct:.2%}")
    print("-" * 50)
    print("EXPOSED TICKERS:", ", ".join(exposed_companies))
    print("═"*50)
    print("ANALYSIS: Shared ownership creates a liquidity bridge.")
    print("In a crash, investors might sell ALL of these to cover losses.")

run_stress_test('NVDA')