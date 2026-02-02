import os

def create_aesthetic_presentation():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Financial Risk Network | Executive Summary</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@300&display=swap" rel="stylesheet">
        <style>
            body {
                background-color: #0b101a;
                color: #e2e8f0;
                font-family: 'Inter', sans-serif;
                margin: 0;
                padding: 60px 20px;
                line-height: 1.7;
            }
            .container {
                max-width: 1100px;
                margin: 0 auto;
            }
            .header {
                border-left: 5px solid #00d4ff;
                padding-left: 30px;
                margin-bottom: 80px;
            }
            h1 {
                font-size: 3.5rem;
                letter-spacing: -2.5px;
                margin: 0;
                color: #ffffff;
                font-weight: 700;
            }
            .subtitle {
                color: #00d4ff;
                font-family: 'JetBrains+Mono', monospace;
                text-transform: uppercase;
                letter-spacing: 4px;
                font-size: 0.9rem;
                margin-bottom: 10px;
            }
            .grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 40px;
                margin-bottom: 50px;
            }
            .card {
                background: linear-gradient(145deg, #161b2a, #0f1420);
                border: 1px solid rgba(255, 255, 255, 0.08);
                padding: 40px;
                border-radius: 24px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.4);
            }
            .card h2 {
                color: #ffaa00;
                font-size: 1.1rem;
                margin-top: 0;
                text-transform: uppercase;
                letter-spacing: 2px;
                margin-bottom: 20px;
            }
            .stat-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 30px;
                margin-top: 60px;
            }
            .stat-card {
                text-align: center;
                background: rgba(255, 255, 255, 0.03);
                padding: 30px;
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.05);
            }
            .stat-value {
                display: block;
                font-size: 2.5rem;
                font-weight: 700;
                color: #00d4ff;
                margin-bottom: 5px;
            }
            .stat-label {
                font-size: 0.75rem;
                color: #94a3b8;
                text-transform: uppercase;
                letter-spacing: 1.5px;
            }
            .highlight {
                color: #ffffff;
                font-weight: 600;
                border-bottom: 1px solid #00d4ff;
            }
            .footer {
                margin-top: 80px;
                font-size: 0.85rem;
                color: #475569;
                text-align: center;
                font-family: 'JetBrains+Mono', monospace;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="subtitle">Quantitative Risk Intelligence</div>
                <h1>Systemic Exposure Analysis</h1>
            </div>

            <div class="grid">
                <div class="card">
                    <h2>Objective & Hypothesis</h2>
                    <p>Quantifying <span class="highlight">ownership interdependencies</span> within the technology sector. This study investigates the hypothesis that high "Common Ownership" creates critical transmission channels for financial contagion during market volatility.</p>
                </div>
                <div class="card">
                    <h2>Methodology</h2>
                    <p>Utilizing <span class="highlight">Graph Theory algorithms</span> to map structural relationships between Big Tech entities (NVDA, AAPL, MSFT) and institutional giants. Data is processed through an automated SQL and Python-based ETL pipeline.</p>
                </div>
            </div>

            <div class="card" style="width: 100%; box-sizing: border-box;">
                <h2>Executive Insights</h2>
                <p>The analysis reveals an extreme level of institutional clustering. With a network density of <span class="highlight">33%</span>, traditional portfolio diversification between these assets is largely superficial. The shared liquidity bridges mean that a shock to a single node (e.g., NVIDIA) poses an immediate systemic risk to the entire cluster due to overlapping institutional mandates.</p>
            </div>

            <div class="stat-grid">
                <div class="stat-card">
                    <span class="stat-value">0.33</span>
                    <span class="stat-label">Network Density</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value">High</span>
                    <span class="stat-label">Contagion Risk</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value">Top 3</span>
                    <span class="stat-label">Critical Nodes</span>
                </div>
            </div>

            <div class="footer">
                STK-ENGINE v1.0 • Python • NetworkX • Plotly • SQLite3 • yFinance API
            </div>
        </div>
    </body>
    </html>
    """
    
    file_path = "data/project_story.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✨ Professional English presentation generated: {file_path}")
    
    os.system(f"open {file_path}")

if __name__ == "__main__":
    create_aesthetic_presentation()
