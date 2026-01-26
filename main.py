"""
Čtvrtý projekt do Engeto Online Python Akademie - Task manager
author: Květoslav Leidorf
email: k.leidorf@gmail.com
discord: kvetos_95684
"""

import sys

# Globální seznam pro ukládání úkolů
ukoly = []


def hlavni_menu() -> str:
    """Zobrazí hlavní menu a vrátí volbu uživatele."""
    while True:
        print(
            "\n" + "-" * 27,
            "Správce úkolů - Hlavní menu",
            "1. Přidat nový úkol",
            "2. Zobrazit všechny úkoly",
            "3. Odstranit úkol",
            "4. Konec programu",
            "-" * 27,
            sep="\n"
        )
        
        volba = input("Vyberte možnost (1-4): ").strip()
        
        if volba in ("1", "2", "3", "4"):
            return volba
        
        print("Neplatná volba, zkuste to prosím znovu.")


def pridat_ukol() -> None:
    """Umožní uživateli zadat název a popis úkolu a uloží jej."""
    while True:
        nazev = input("\nZadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()
        
        if not nazev or not popis:
            print("Chyba: Název i popis úkolu nesmí být prázdný! Zadejte znovu.")
            continue
        
        ukol = {"nazev": nazev, "popis": popis}
        ukoly.append(ukol)
        
        print(f"Úkol '{nazev}' byl úspěšně přidán.")
        break


def zobrazit_ukoly() -> None:
    """Zobrazí všechny uložené úkoly s pořadovým číslem."""
    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")
    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol() -> None:
    """
    Umožní uživateli odstranit konkrétní úkol podle jeho čísla.
    Opakuje dotaz, dokud není zadán platný vstup.
    """
    if not ukoly:
        print("\nNení co odstranit, seznam je prázdný.")
        return

    while True:
        zobrazit_ukoly()
        print("(Pro zrušení a návrat do menu zadejte 'q')")
        
        vstup = input("\nZadejte číslo úkolu k odstranění: ").strip().lower()
        
        if vstup == 'q':
            print("Odstraňování zrušeno.")
            break

        try:
            # Převod na index (uživatel 1 -> Python 0)
            index = int(vstup) - 1
            
            if 0 <= index < len(ukoly):
                odstraneny = ukoly.pop(index)
                print(f"Úkol '{odstraneny['nazev']}' byl úspěšně odstraněn.")
                break
            else:
                print(f"Chyba: Zadejte číslo v rozmezí 1 až {len(ukoly)}.")
                
        except ValueError:
            print("Chyba: Neplatný vstup. Zadejte prosím číslo úkolu nebo 'q'.")


def spusti_program() -> None:
    """Hlavní řídicí smyčka programu."""
    while True:
        volba = hlavni_menu()
        
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            # TC08: Specifikace očekávaného ukončení
            print("\nUkončuji program. Žádné další výstupy nebudou generovány.")
            sys.exit(0)  # Standardní exit kód pro úspěšné ukončení


if __name__ == "__main__":
    spusti_program()
