import subprocess
import os
import time

def run_script(script_name, description):
    """Pomocnicza funkcja do uruchamiania modułów projektu"""
    print(f"\n[SYSTEM] {description}...")
    try:
        # Używamy "python" dla środowiska Anaconda
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

    # KROK 1: Aktualizacja danych z yFinance
    run_script("database_manager.py", "Aktualizacja bazy danych SQL")

    # KROK 2: Analiza sieciowa
    run_script("network_analysis.py", "Analiza statystyk sieci")

    # KROK 3: Interaktywna mapa Neon-Glow
    run_script("interactive_map.py", "Budowanie interaktywnej mapy HTML")

    # KROK 4: Symulacja efektu domina
    run_script("risk_simulator.py", "Uruchamianie symulacji Stress-Test")

    # KROK 5: Raport tekstowy
    run_script("generate_report.py", "Generowanie raportu tekstowego")

    # KROK 6: Dashboard Statystyk
    run_script("final_presentation.py", "Generating Premium Analytics Dashboard")

    # KROK 7: Strona Powitalna (Executive Summary)
    run_script("project_presentation.py", "Generating Executive Summary")

    print("\n" + "="*60)
    print("🚀 ALL SYSTEMS OPERATIONAL - REPORTS READY")
    print("="*60)

    # Automatyczne otwieranie wyników w Safari
    print("\nOtwieranie raportów...")
    os.system("open data/project_story.html")
    os.system("open data/pro_dashboard.html")
    os.system("open data/financial_network_interactive.html")

# --- KLUCZOWY ELEMENT: TO URUCHAMIA CAŁY PROGRAM ---
if __name__ == "__main__":
    main()