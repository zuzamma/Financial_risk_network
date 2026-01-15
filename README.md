# 🛡️ Systemic Financial Risk Network Analysis
**An advanced quantitative tool for mapping institutional interdependencies and simulating financial contagion.**

---

## 📊 Project Preview
<p align="center">
  <img src="https://github.com/user-attachments/assets/1b451932-706c-4fa9-b20d-8242a918231b" width="100%" alt="Executive Dashboard" />
  <br>
  <em>Real-time market metrics & risk scoring dashboard</em>
</p>

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
| **Visualization** | `Plotly`, `PyVis`, `HTML/CSS` |

## ⚙️ Installation & Usage
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/zuzamma/Financial_risk_network.git](https://github.com/zuzamma/Financial_risk_network.git)