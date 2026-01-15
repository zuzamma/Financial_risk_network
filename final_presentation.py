import sqlite3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_premium_analytics():
    conn = sqlite3.connect('data/financial_network.db')
    df = pd.read_sql_query("SELECT company, investor FROM ownership", conn)
    conn.close()

    # Data Processing: Top 8 Institutional Holders
    top_investors = df['investor'].value_counts().head(8).reset_index()
    top_investors.columns = ['Investor', 'Count']

    # POPRAWKA: Dodano "None" w specs, aby zamknąć strukturę siatki 2x2
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "indicator"}, {"type": "indicator"}],
               [{"colspan": 2, "type": "bar"}, None]], 
        vertical_spacing=0.25
    )

    # Metric 1: Network Connectivity
    fig.add_trace(go.Indicator(
        mode="number",
        value=len(df),
        title={"text": "<span style='font-size:0.8em;color:#94a3b8;letter-spacing:2px'>TOTAL CONNECTIONS</span>"},
        number={'font': {'color': '#00d4ff', 'size': 55, 'family': 'Inter'}},
    ), row=1, col=1)

    # Metric 2: Asset Coverage
    fig.add_trace(go.Indicator(
        mode="number",
        value=len(df['company'].unique()),
        title={"text": "<span style='font-size:0.8em;color:#94a3b8;letter-spacing:2px'>ANALYZED ASSETS</span>"},
        number={'font': {'color': '#ffaa00', 'size': 55, 'family': 'Inter'}},
    ), row=1, col=2)

    # Chart: Institutional Dominance
    fig.add_trace(go.Bar(
        x=top_investors['Investor'],
        y=top_investors['Count'],
        marker=dict(
            color='#00d4ff',
            line=dict(color='rgba(255,255,255,0.1)', width=1),
            opacity=0.85
        ),
        hovertemplate="<b>%{x}</b><br>Holdings: %{y}<extra></extra>"
    ), row=2, col=1)

    # Professional Dark Theme Styling
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0b101a",
        plot_bgcolor="#0b101a",
        font_family="Inter",
        title={"text": "SYSTEMIC EXPOSURE METRICS", "font": {"size": 22, "color": "white", "letter-spacing": "1px"}},
        margin=dict(t=120, b=50, l=60, r=60),
        height=750,
        showlegend=False
    )

    fig.update_xaxes(showgrid=False, zeroline=False, tickfont=dict(color='#94a3b8'))
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.05)', zeroline=False, tickfont=dict(color='#94a3b8'))

    fig.write_html("data/pro_dashboard.html")
    print("📊 Premium Analytics Dashboard generated (English).")

if __name__ == "__main__":
    create_premium_analytics()