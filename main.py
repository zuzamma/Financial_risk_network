import pandas as pd
import networkx as nx
import yfinance as yf
import matplotlib.pyplot as plt

# 1. Configuration
tickers = ['AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'TSLA', 'META']
print(f"Fetching data for: {tickers}...")

network_data = []

# 2. Data Acquisition
for t in tickers:
    try:
        stock = yf.Ticker(t)
        holders = stock.institutional_holders
        if holders is not None:
            # We use 'Holder' as Investor and 't' as Company
            for index, row in holders.iterrows():
                network_data.append({
                    'Company': t,
                    'Investor': row['Holder'],
                    'Shares': row['Shares']
                })
    except Exception as e:
        print(f"Error for {t}: {e}")

df = pd.DataFrame(network_data)

# 3. Network Construction
G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row['Investor'], row['Company'])

# 4. Analysis
centrality = nx.degree_centrality(G)
top_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]

# --- THIS WILL SHOW UP AT THE VERY BOTTOM ---
print("\n" + "="*40)
print("PROJECT RESULTS (TOP 5 INFLUENTIAL)")
print("="*40)
for node, score in top_nodes:
    print(f"NODE: {node:25} | SCORE: {score:.4f}")
print("="*40)

# 5. Visualization
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=0.5, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightcoral', node_size=50, font_size=6)
plt.title("Financial Network Analysis")
plt.savefig("network_map.png")
print("\nSUCCESS: Graph saved as 'network_map.png'")
plt.show()