import sqlite3
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 1. Connect to our Database
conn = sqlite3.connect('data/financial_network.db')
df = pd.read_sql_query("SELECT company, investor FROM ownership", conn)
conn.close()

# 2. Build the graph
G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row['investor'], row['company'])

# --- ANALYTICS SECTION ---
print("\n" + "="*50)
print("   PROFESSIONAL NETWORK RISK ANALYSIS")
print("="*50)

density = nx.density(G)
print(f"[+] Market Density: {density:.4f}")

centrality = nx.degree_centrality(G)
top_investors = sorted([n for n in centrality.items() if len(n[0]) > 5], 
                       key=lambda x: x[1], reverse=True)[:3]

print("\n[+] Top 3 Systemic Owners (Highest Influence):")
for name, score in top_investors:
    print(f" - {name}: {score:.4f}")

clustering = nx.average_clustering(G)
print(f"\n[+] Clustering Coefficient: {clustering:.4f}")

is_connected = nx.is_connected(G)
print(f"[+] Is the network fully interconnected? {is_connected}")
print("="*50)

# --- NEW: MODERN VISUALIZATION SECTION ---
# Ustawiamy styl "Dark Mode"
plt.figure(figsize=(14, 10), facecolor='#0b0f19')
ax = plt.gca()
ax.set_facecolor('#0b0f19')

# Układ grafu (Spring layout sprawia, że kropki "pływają" naturalnie)
pos = nx.spring_layout(G, k=0.8, iterations=100)

# 1. Rysujemy krawędzie (półprzezroczyste, białe linie)
nx.draw_networkx_edges(G, pos, alpha=0.15, edge_color='white', width=0.8)

# 2. Rozdzielamy węzły na Inwestorów i Firmy dla różnych kolorów
companies = [n for n in G.nodes() if len(n) <= 5]
investors = [n for n in G.nodes() if len(n) > 5]

# Firmy: Neonowe Złoto
nx.draw_networkx_nodes(G, pos, nodelist=companies, node_size=1200, 
                       node_color='#ffaa00', label='Tech Giants')

# Inwestorzy: Neonowy Błękit
nx.draw_networkx_nodes(G, pos, nodelist=investors, node_size=800, 
                       node_color='#00d4ff', label='Institutional Investors')

# 3. Dodajemy etykiety (czcionka bezszeryfowa, biała)
nx.draw_networkx_labels(G, pos, font_size=7, font_color='white', 
                        font_weight='bold', font_family='sans-serif')

plt.title("SYSTEMIC RISK: INTERCONNECTED OWNERSHIP MAP", 
          color='#ffffff', fontsize=18, fontweight='bold', pad=25)

# Dodajemy legendę w nowoczesnym stylu
leg = plt.legend(scatterpoints=1, facecolor='#1a1f2b', edgecolor='#00d4ff', labelcolor='white')

plt.axis('off')

# Zapisujemy jako wysokiej jakości obrazek PNG
output_image = "data/network_map_modern.png"
plt.savefig(output_image, dpi=300, bbox_inches='tight', facecolor='#0b0f19')

print(f"\n📸 SUCCESS: Modern graph saved to {output_image}")