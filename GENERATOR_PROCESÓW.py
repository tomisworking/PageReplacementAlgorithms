import csv
import random

def main(n):
    try:
        # Otwarcie pliku PROCESY.csv do zapisu, jeśli plik nie istnieje, tworzenie nowego
        with open("PROCESY.csv", "w+", newline="") as file:
            writer = csv.writer(file)
            # Zapis nagłówków kolumn do pliku
            writer.writerow(["PID", "Arrival", "Execution"])
            for pid in range(1, n + 1):
                # Generowanie czasu przybycia
                arrival_time = random.randint(0, 100)
                # Generowanie czasu wykonania
                execution_time = random.randint(5, 5)
                # Zapis danych procesu do pliku
                writer.writerow([pid, arrival_time, execution_time])

        # Informacja o pomyślnym zapisie do pliku
        print("Zapisano pomyślnie do pliku PROCESY.csv!")
    except:
        # Informacja o nieudanym zapisie do pliku
        print("Nie udało się zapisać do pliku PROCESY.csv")

if __name__ == "__main__":
    # Pobranie liczby procesów od użytkownika
    n = int(input("Podaj liczbę procesów: "))
    # Wywołanie funkcji main z podaną liczbą procesów
    main(n)
