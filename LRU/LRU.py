import csv
class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Pojemność cache (maksymalna liczba stron w pamięci)
        self.cache = []  # Lista reprezentująca cache stron w pamięci
        self.page_faults = 0  # Licznik błędów stron

    def access_page(self, page: int):
        if page not in self.cache:
            # Brak strony w pamięci (page fault)
            if len(self.cache) >= self.capacity:
                # Usunięcie najstarszej strony z cache
                self.cache.pop(0)
            # Dodanie nowej strony na koniec cache
            self.cache.append(page)
            self.page_faults += 1  # Zwiększenie licznika błędów stron
            print(f"Page {page} added, page fault.")
        else:
            # Strona znajduje się w pamięci (page hit): przesunięcie strony na koniec, aby oznaczyć ją jako ostatnio używaną
            self.cache.append(self.cache.pop(self.cache.index(page)))
            print(f"Page {page} accessed, no page fault.")

    def display(self):
        # Wyświetlenie bieżących stron w pamięci
        print("Current pages in memory: ", self.cache)


def main(n):

    lru = LRU(n)  # Utworzenie obiektu LRU z pojemnością n

    pages = []  # Lista stron
    with open(r'/SEKWENCJE.csv', 'r') as file:
        reader = csv.reader(file)

        # Iteracja przez wiersze w pliku CSV
        for row in reader:
            # Dodanie strony do listy na podstawie danych z pliku
            pages.append(int(row[0]))


    # pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2]   # Lista stron do załadowania

    for page in pages:
        lru.access_page(page)  # Dostęp do strony
        lru.display()  # Wyświetlenie bieżących stron w pamięci

    print(f"Number of page fault's: {lru.page_faults}")  # Wyświetlenie liczby błędów stron


if __name__ == "__main__":
    n = int(input("Podaj pojemność pamięci: "))  # Pobranie od użytkownika pojemności pamięci
    main(n)  # Uruchomienie głównej funkcji programu
