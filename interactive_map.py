import sqlite3
import pandas as pd
from pyvis.network import Network

def create_final_map():
    conn = sqlite3.connect('data/financial_network.db')
    df = pd.read_sql_query("SELECT company, investor FROM ownership", conn)
    conn.close()

    # Inicjalizacja z ciemnym tłem (Dopasowane do Dashboardu)
    net = Network(height="850px", width="100%", bgcolor="#0b101a", font_color="#e2e8f0")

    for _, row in df.iterrows():
        # Inwestorzy (Błękit - Cyan)
        net.add_node(row['investor'], label=row['investor'], 
                     color='#00d4ff', size=20, 
                     title=f"Institutional Investor: {row['investor']}",
                     font={'size': 12, 'face': 'Inter'})
        
        # Spółki (Złoto/Pomarańcz - Gold)
        net.add_node(row['company'], label=row['company'], 
                     color='#ffaa00', size=45, 
                     title=f"Target Asset: {row['company']}",
                     font={'size': 18, 'face': 'Inter', 'weight': 'bold'})
        
        # Połączenia (Subtelne linie)
        net.add_edge(row['investor'], row['company'], color='rgba(255,255,255,0.15)', width=1.5)

    # USPOKOJONA FIZYKA: Zapobiega nadmiernemu kręceniu się i drganiu
    net.set_options("""
    var options = {
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -50,
          "centralGravity": 0.01,
          "springLength": 100,
          "springConstant": 0.08,
          "damping": 0.4
        },
        "maxVelocity": 10,
        "minVelocity": 0.1,
        "solver": "forceAtlas2Based",
        "stabilization": {
          "enabled": true,
          "iterations": 1000,
          "updateInterval": 25
        }
      },
      "interaction": {
        "hover": true,
        "navigationButtons": true,
        "hideEdgesOnDrag": true
      }
    }
    """)

    net.write_html("data/financial_network_interactive.html")
    print("🕸️ Global Exposure Map finalized with stable physics.")

if __name__ == "__main__":
    create_final_map()