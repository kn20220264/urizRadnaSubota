# Script that checks password strength based on length, characters and numbers
# Outputs Weak / Medium / Strong rating with colors using colorama
# Provides one personalized tip to improve password security

import re
from colorama import init, Fore, Style

init(autoreset=True)

def check_password_strength(password):
    score = 0
    tips = []

    # Duzina
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Povecajte duzinu lozinke na najmanje 8 karaktera.")

    # Mala slova
    if re.search(r'[a-z]', password):
        score += 1
    else:
        tips.append("Dodajte mala slova (a-z).")

    # Velika slova
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        tips.append("Dodajte velika slova (A-Z).")

    # Brojevi
    if re.search(r'\d', password):
        score += 1
    else:
        tips.append("Dodajte bar jedan broj (0-9).")

    # Specijalni karakteri
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|<>?,./]', password):
        score += 2
    else:
        tips.append("Dodajte specijalne karaktere kao sto su !@#$%.")

    # Ocena
    if score >= 6:
        rating = "Strong"
        color = Fore.GREEN
    elif score >= 3:
        rating = "Medium"
        color = Fore.YELLOW
    else:
        rating = "Weak"
        color = Fore.RED

    # Jedan personalizovan savet
    tip = tips[0] if tips else "Odlicno! Lozinka ispunjava sve kriterijume."

    return rating, color, tip


def main():
    print(Style.BRIGHT + "\n=== Provera Jacine Lozinke ===\n")

    password = input("Unesite lozinku: ").strip()

    if not password:
        print(Fore.YELLOW + "Niste uneli lozinku.")
        return

    rating, color, tip = check_password_strength(password)

    print(color + Style.BRIGHT + f"\nOcena: {rating}")
    print(Fore.CYAN + f"Savet: {tip}\n")


if __name__ == "__main__":
    main()