![network_animation](https://github.com/user-attachments/assets/a8a6d658-1368-43e2-aa6c-74c687d78dc4)# 🛡️ Systemic Financial Risk Network Analysis
**An advanced quantitative tool for mapping institutional interdependencies and simulating financial contagion.**

---

## 📊 Project Preview
| 📈 Executive Dashboard | 🕸️ Interactive Risk Network |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/1b451932-706c-4fa9-b20d-8242a918231b" width="400" /> | <img src="https://github.com/user-attachments/assets/a89defb6-db4c-4d55-bf5c-4514349b0d51" width="400" /> |
| *Real-time market metrics & risk scoring* | *Dynamic physics-based institutional mapping* |
![Uploading network_animation.gif<html>
    <head>
        <meta charset="utf-8">
        
            <script src="lib/bindings/utils.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/dist/vis-network.min.css" integrity="sha512-WgxfT5LWjfszlPHXRmBWHkV2eceiWTOBvrKCNbdgDYTHrT2AeLCGbF4sZlZw3UMN3WtL0tGUoIAKsu8mllg/XA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/vis-network.min.js" integrity="sha512-LnvoEWDFrqGHlHmDD2101OrLcbsfkrzoSpvtSQtxK3RMnRV0eOkhhBN2dXHKRrUU8p2DGRTk35n4O8nWSVe1mQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
            
        
<center>
<h1></h1>
</center>

<!-- <link rel="stylesheet" href="../node_modules/vis/dist/vis.min.css" type="text/css" />
<script type="text/javascript" src="../node_modules/vis/dist/vis.js"> </script>-->
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
          crossorigin="anonymous"
        />
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
          crossorigin="anonymous"
        ></script>


        <center>
          <h1></h1>
        </center>
        <style type="text/css">

             #mynetwork {
                 width: 100%;
                 height: 850px;
                 background-color: #0b101a;
                 border: 1px solid lightgray;
                 position: relative;
                 float: left;
             }

             

             

             
        </style>
    </head>


    <body>
        <div class="card" style="width: 100%">
            
            
            <div id="mynetwork" class="card-body"></div>
        </div>

        
        

        <script type="text/javascript">

              // initialize global variables.
              var edges;
              var nodes;
              var allNodes;
              var allEdges;
              var nodeColors;
              var originalNodes;
              var network;
              var container;
              var options, data;
              var filter = {
                  item : '',
                  property : '',
                  value : []
              };

              

              

              // This method is responsible for drawing the graph, returns the drawn network
              function drawGraph() {
                  var container = document.getElementById('mynetwork');

                  

                  // parsing and collecting nodes and edges from the python
                  nodes = new vis.DataSet([{"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Vanguard Group Inc", "label": "Vanguard Group Inc", "shape": "dot", "size": 20, "title": "Institutional Investor: Vanguard Group Inc"}, {"color": "#ffaa00", "font": {"color": "#e2e8f0"}, "id": "AAPL", "label": "AAPL", "shape": "dot", "size": 45, "title": "Target Asset: AAPL"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Blackrock Inc.", "label": "Blackrock Inc.", "shape": "dot", "size": 20, "title": "Institutional Investor: Blackrock Inc."}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "State Street Corporation", "label": "State Street Corporation", "shape": "dot", "size": 20, "title": "Institutional Investor: State Street Corporation"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "JPMORGAN CHASE \u0026 CO", "label": "JPMORGAN CHASE \u0026 CO", "shape": "dot", "size": 20, "title": "Institutional Investor: JPMORGAN CHASE \u0026 CO"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Geode Capital Management, LLC", "label": "Geode Capital Management, LLC", "shape": "dot", "size": 20, "title": "Institutional Investor: Geode Capital Management, LLC"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "FMR, LLC", "label": "FMR, LLC", "shape": "dot", "size": 20, "title": "Institutional Investor: FMR, LLC"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Berkshire Hathaway, Inc", "label": "Berkshire Hathaway, Inc", "shape": "dot", "size": 20, "title": "Institutional Investor: Berkshire Hathaway, Inc"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Morgan Stanley", "label": "Morgan Stanley", "shape": "dot", "size": 20, "title": "Institutional Investor: Morgan Stanley"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Price (T.Rowe) Associates Inc", "label": "Price (T.Rowe) Associates Inc", "shape": "dot", "size": 20, "title": "Institutional Investor: Price (T.Rowe) Associates Inc"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "NORGES BANK", "label": "NORGES BANK", "shape": "dot", "size": 20, "title": "Institutional Investor: NORGES BANK"}, {"color": "#ffaa00", "font": {"color": "#e2e8f0"}, "id": "MSFT", "label": "MSFT", "shape": "dot", "size": 45, "title": "Target Asset: MSFT"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Northern Trust Corporation", "label": "Northern Trust Corporation", "shape": "dot", "size": 20, "title": "Institutional Investor: Northern Trust Corporation"}, {"color": "#ffaa00", "font": {"color": "#e2e8f0"}, "id": "NVDA", "label": "NVDA", "shape": "dot", "size": 45, "title": "Target Asset: NVDA"}, {"color": "#ffaa00", "font": {"color": "#e2e8f0"}, "id": "GOOGL", "label": "GOOGL", "shape": "dot", "size": 45, "title": "Target Asset: GOOGL"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Bank of America Corporation", "label": "Bank of America Corporation", "shape": "dot", "size": 20, "title": "Institutional Investor: Bank of America Corporation"}, {"color": "#ffaa00", "font": {"color": "#e2e8f0"}, "id": "AMZN", "label": "AMZN", "shape": "dot", "size": 45, "title": "Target Asset: AMZN"}, {"color": "#ffaa00", "font": {"color": "#e2e8f0"}, "id": "TSLA", "label": "TSLA", "shape": "dot", "size": 45, "title": "Target Asset: TSLA"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Capital World Investors", "label": "Capital World Investors", "shape": "dot", "size": 20, "title": "Institutional Investor: Capital World Investors"}, {"color": "#00d4ff", "font": {"color": "#e2e8f0"}, "id": "Goldman Sachs Group Inc", "label": "Goldman Sachs Group Inc", "shape": "dot", "size": 20, "title": "Institutional Investor: Goldman Sachs Group Inc"}, {"color": "#ffaa00", "font": {"color": "#e2e8f0"}, "id": "META", "label": "META", "shape": "dot", "size": 45, "title": "Target Asset: META"}]);
                  edges = new vis.DataSet([{"color": "rgba(255,255,255,0.15)", "from": "Vanguard Group Inc", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Blackrock Inc.", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "State Street Corporation", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "JPMORGAN CHASE \u0026 CO", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Geode Capital Management, LLC", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "FMR, LLC", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Berkshire Hathaway, Inc", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Morgan Stanley", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Price (T.Rowe) Associates Inc", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "NORGES BANK", "to": "AAPL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Vanguard Group Inc", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Blackrock Inc.", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "JPMORGAN CHASE \u0026 CO", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "State Street Corporation", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "FMR, LLC", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Geode Capital Management, LLC", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Price (T.Rowe) Associates Inc", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Morgan Stanley", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "NORGES BANK", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Northern Trust Corporation", "to": "MSFT", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Vanguard Group Inc", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Blackrock Inc.", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "FMR, LLC", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "State Street Corporation", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "JPMORGAN CHASE \u0026 CO", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Geode Capital Management, LLC", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Price (T.Rowe) Associates Inc", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "NORGES BANK", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Morgan Stanley", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Northern Trust Corporation", "to": "NVDA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Vanguard Group Inc", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Blackrock Inc.", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "FMR, LLC", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "State Street Corporation", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Geode Capital Management, LLC", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "JPMORGAN CHASE \u0026 CO", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "NORGES BANK", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Morgan Stanley", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Price (T.Rowe) Associates Inc", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Bank of America Corporation", "to": "GOOGL", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Vanguard Group Inc", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Blackrock Inc.", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "State Street Corporation", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "JPMORGAN CHASE \u0026 CO", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "FMR, LLC", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Geode Capital Management, LLC", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Morgan Stanley", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Price (T.Rowe) Associates Inc", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "NORGES BANK", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Northern Trust Corporation", "to": "AMZN", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Vanguard Group Inc", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Blackrock Inc.", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "State Street Corporation", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "JPMORGAN CHASE \u0026 CO", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Geode Capital Management, LLC", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Capital World Investors", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "NORGES BANK", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "FMR, LLC", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Morgan Stanley", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Goldman Sachs Group Inc", "to": "TSLA", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Vanguard Group Inc", "to": "META", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Blackrock Inc.", "to": "META", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "FMR, LLC", "to": "META", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "JPMORGAN CHASE \u0026 CO", "to": "META", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "State Street Corporation", "to": "META", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Geode Capital Management, LLC", "to": "META", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Capital World Investors", "to": "META", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Price (T.Rowe) Associates Inc", "to": "META", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "Morgan Stanley", "to": "META", "width": 1.5}, {"color": "rgba(255,255,255,0.15)", "from": "NORGES BANK", "to": "META", "width": 1.5}]);

                  nodeColors = {};
                  allNodes = nodes.get({ returnType: "Object" });
                  for (nodeId in allNodes) {
                    nodeColors[nodeId] = allNodes[nodeId].color;
                  }
                  allEdges = edges.get({ returnType: "Object" });
                  // adding nodes and edges to the graph
                  data = {nodes: nodes, edges: edges};

                  var options = {"physics": {"forceAtlas2Based": {"gravitationalConstant": -50, "centralGravity": 0.01, "springLength": 100, "springConstant": 0.08, "damping": 0.4}, "maxVelocity": 10, "minVelocity": 0.1, "solver": "forceAtlas2Based", "stabilization": {"enabled": true, "iterations": 1000, "updateInterval": 25}}, "interaction": {"hover": true, "navigationButtons": true, "hideEdgesOnDrag": true}};

                  


                  

                  network = new vis.Network(container, data, options);

                  

                  

                  


                  

                  return network;

              }
              drawGraph();
        </script>
    </body>
</html>…]()

---

## 💡 Overview
This project addresses the complexity of modern financial markets by quantifying **systemic risk**. By analyzing the ownership structures of major technology assets (e.g., AAPL, NVDA, MSFT), the system identifies "Too Interconnected to Fail" nodes and simulates how a localized shock can trigger a domino effect across the global financial network.

## 🚀 Key Features
* **📡 Automated Data Acquisition**: Seamless integration with `yFinance` to fetch real-time institutional holders and market prices.
* **🗄️ Robust Data Architecture**: Custom SQL-based storage (SQLite) optimized for relational ownership mapping.
* **🔬 Network Theory Engine**: 
    * Calculation of **Clustering Coefficients** and **Network Density**.
    * Identification of bridge nodes (Institutional Investors) connecting diverse assets.
* **🧪 Crisis Simulation (Stress-Test)**: A dedicated module to model the "Domino Effect" – visualizing the propagation of financial distress.
* **🎨 Premium Reporting**: Automated generation of dark-themed HTML dashboards and interactive graph visualizations.

## 🛠️ Tech Stack
| Category | Tools |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Data Science** | `Pandas`, `NumPy`, `yFinance` |
| **Database** | `SQLite3` |
| **Visualization** | `Plotly`, `PyVis (Physics-based Graphs)`, `HTML/CSS` |

## 📈 Analysis Workflow
1.  **Extraction**: Pulling institutional ownership data for high-cap technology tickers.
2.  **Transformation**: Mapping many-to-many relationships between investors and assets.
3.  **Analytics**: Running centrality algorithms to find high-risk nodes.
4.  **Visualization**: Rendering the interactive map and executive dashboard.

## ⚙️ Installation & Usage
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/zuzamma/Financial_risk_network.git](https://github.com/zuzamma/Financial_risk_network.git)
