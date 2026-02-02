import subprocess
import os
import time

def run_script(script_name, description):
    """Pomocnicza funkcja do uruchamiania modułów projektu"""
    print(f"\n[SYSTEM] {description}...")
    try:
        result = subprocess.run(["python", script_name], check=True)
        if result.returncode == 0:
            print(f"✅ {script_name} zakończony sukcesem.")
    except Exception as e:
        print(f"❌ Błąd w {script_name}: {e}")

def main():
    print("="*60)
    print("      FINANCIAL RISK NETWORK - PROFESSIONAL DASHBOARD v1.0")
    print("="*60)
    print("Inicjalizacja pełnej analizy systemowej...")
    time.sleep(1)

    run_script("database_manager.py", "Aktualizacja bazy danych SQL")

    run_script("network_analysis.py", "Analiza statystyk sieci")

    run_script("interactive_map.py", "Budowanie interaktywnej mapy HTML")
    
    run_script("risk_simulator.py", "Uruchamianie symulacji Stress-Test")

    run_script("generate_report.py", "Generowanie raportu tekstowego")

    run_script("final_presentation.py", "Generating Premium Analytics Dashboard")

    run_script("project_presentation.py", "Generating Executive Summary")

    print("\n" + "="*60)
    print("🚀 ALL SYSTEMS OPERATIONAL - REPORTS READY")
    print("="*60)

    print("\nOtwieranie raportów...")
    os.system("open data/project_story.html")
    os.system("open data/pro_dashboard.html")
    os.system("open data/financial_network_interactive.html")

if __name__ == "__main__":
    main()
