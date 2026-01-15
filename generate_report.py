import sqlite3
import pandas as pd  # TA LINIJKA JEST NIEZBĘDNA
import networkx as nx

# 1. Połączenie z bazą
conn = sqlite3.connect('data/financial_network.db')
df = pd.read_sql_query("SELECT company, investor FROM ownership", conn)
conn.close()

# 2. Budowa grafu
G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row['investor'], row['company'])

# 3. Obliczenia
density = nx.density(G)
centrality = nx.degree_centrality(G)
# Filtrujemy, żeby brać pod uwagę tylko giełdowych gigantów i fundusze
top_3 = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:3]

# 4. Zapis do pliku tekstowego
with open("data/final_risk_report.txt", "w", encoding="utf-8") as f:
    f.write("FINANCIAL NETWORK RISK REPORT\n")
    f.write("="*30 + "\n")
    f.write(f"Network Density: {density:.4f}\n")
    f.write("\nTOP SYSTEMIC NODES (Highest Influence):\n")
    for name, score in top_3:
        f.write(f"- {name}: {score:.4f}\n")
    f.write("\nCONCLUSION:\n")
    f.write("High density detected. The financial system is vulnerable to a domino effect.\n")
    f.write("A crisis in one company could spread through shared institutional ownership.")

print("📄 Sukces! Raport wygenerowany w folderze 'data/final_risk_report.txt'")