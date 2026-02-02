import sqlite3
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

conn = sqlite3.connect('data/financial_network.db')
df = pd.read_sql_query("SELECT company, investor FROM ownership", conn)
conn.close()

G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row['investor'], row['company'])

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

plt.figure(figsize=(14, 10), facecolor='#0b0f19')
ax = plt.gca()
ax.set_facecolor('#0b0f19')

pos = nx.spring_layout(G, k=0.8, iterations=100)

nx.draw_networkx_edges(G, pos, alpha=0.15, edge_color='white', width=0.8)

companies = [n for n in G.nodes() if len(n) <= 5]
investors = [n for n in G.nodes() if len(n) > 5]

nx.draw_networkx_nodes(G, pos, nodelist=companies, node_size=1200, 
                       node_color='#ffaa00', label='Tech Giants')

nx.draw_networkx_nodes(G, pos, nodelist=investors, node_size=800, 
                       node_color='#00d4ff', label='Institutional Investors')

nx.draw_networkx_labels(G, pos, font_size=7, font_color='white', 
                        font_weight='bold', font_family='sans-serif')

plt.title("SYSTEMIC RISK: INTERCONNECTED OWNERSHIP MAP", 
          color='#ffffff', fontsize=18, fontweight='bold', pad=25)

leg = plt.legend(scatterpoints=1, facecolor='#1a1f2b', edgecolor='#00d4ff', labelcolor='white')

plt.axis('off')

output_image = "data/network_map_modern.png"
plt.savefig(output_image, dpi=300, bbox_inches='tight', facecolor='#0b0f19')

print(f"\n📸 SUCCESS: Modern graph saved to {output_image}")
