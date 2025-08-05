import csv
import random

def main(n):
    try:
        # Otwarcie pliku SEKWENCJE.csv do zapisu, jeśli plik nie istnieje, tworzenie nowego
        with open("SEKWENCJE.csv", "w+", newline="") as file:
            writer = csv.writer(file)

            for i in range(n):
                writer.writerow([random.randint(1,7)])


        # Informacja o pomyślnym zapisie do pliku
        print("Zapisano pomyślnie do pliku SEKWENCJE.csv!")
    except:
        # Informacja o nieudanym zapisie do pliku
        print("Nie udało się zapisać do pliku SEKWENCJE.csv")

if __name__ == "__main__":
    # Pobranie liczby stron od użytkownika
    n = int(input("Podaj liczbę stron: "))
    # Wywołanie funkcji main z podaną liczbą stron
    main(n)
