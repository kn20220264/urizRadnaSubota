# Function that returns the sentiment of a text using TextBlob and coloring answer with colorama
# Supports Serbian language via custom keyword dictionary

from textblob import TextBlob
from colorama import init, Fore, Style

init(autoreset=True)

# Srpski recnik za sentiment
POZITIVNE_RECI = [
    "pozitivan", "dobar", "odlican", "super", "sjajan", "lep", "lepo",
    "sretan", "srecan", "volim", "svidja", "svidja", "bravo", "hvala",
    "savrseno", "savrseno", "divno", "krasno", "veseo", "vesela",
    "radostan", "zadovoljan", "uspesno", "pobeda", "ljubav",
    "prijatan", "prijatno", "fenomenalno", "prekrasno", "odlicno"
]

NEGATIVNE_RECI = [
    "negativan", "los", "los", "grozan", "uzasno", "uzasno", "mrzim",
    "ne volim", "problem", "greska", "greska", "tuzno", "tuzno",
    "zao", "zao", "bol", "plac", "ljut", "ljuta", "besan", "besna",
    "lose", "lose", "katastrofa", "uzasan", "uzasan",
    "neuspeh", "neuspesno", "nesrecan", "nesrecan"
]

def analyze_sentiment(text):
    """
    Analizira sentiment teksta.
    Prvo proverava srpski recnik, zatim koristi TextBlob za engleski.
    """
    text_lower = text.lower()

    # Provera srpskog recnika
    pozitivnih = sum(1 for rec in POZITIVNE_RECI if rec in text_lower)
    negativnih = sum(1 for rec in NEGATIVNE_RECI if rec in text_lower)

    if pozitivnih > negativnih:
        return "Pozitivan", Fore.GREEN
    elif negativnih > pozitivnih:
        return "Negativan", Fore.RED

    # Fallback na TextBlob (za engleski tekst)
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "Pozitivan", Fore.GREEN
    elif polarity < -0.1:
        return "Negativan", Fore.RED
    else:
        return "Neutralan", Fore.YELLOW

def main():
    print(Style.BRIGHT + "\n=== Analiza Sentimenta Teksta ===")
    print("Unesite tekst za analizu ili 'exit' za izlaz.\n")

    while True:
        user_input = input("Unesite tekst: ").strip()

        if user_input.lower() == "exit":
            print(Fore.CYAN + "\nDovidjenja! Hvala na koriscenju programa.")
            break

        if not user_input:
            print(Fore.YELLOW + "⚠ Unesite neki tekst!")
            continue

        sentiment, color = analyze_sentiment(user_input)
        print(color + Style.BRIGHT + f"-> Rezultat: {sentiment}\n")

if __name__ == "__main__":
    main()