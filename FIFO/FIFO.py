import csv


class FIFO:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Pojemność kolejki (maksymalna liczba stron w pamięci)
        self.queue = []  # Lista reprezentująca kolejkę stron w pamięci
        self.cache = set()  # Zbiór przechowujący strony w pamięci dla szybkiego sprawdzania obecności
        self.page_faults = 0  # Licznik błędów stron

    def access_page(self, page):
        if page not in self.cache:
            # Brak strony w pamięci (page fault)
            if len(self.queue) >= self.capacity:
                # Usunięcie najstarszej strony z kolejki i z pamięci cache
                oldest_page = self.queue.pop(0)
                self.cache.remove(oldest_page)
            # Dodanie nowej strony do kolejki i do pamięci cache
            self.queue.append(page)
            self.cache.add(page)
            self.page_faults += 1  # Zwiększenie licznika błędów stron
            print(f"Page {page} added, page fault.")
        else:
            # Strona znajduje się w pamięci (page hit)
            print(f"Page {page} accessed, no page fault.")

    def display(self):
        # Wyświetlenie bieżących stron w pamięci
        print("Current pages in memory: ", self.queue)


def main(n):

    fifo = FIFO(n)  # Utworzenie obiektu FIFO z pojemnością zadaną przez użytkownika

    pages = []  # Lista stron
    with open(r'C:\Users\TOMEK\PycharmProjects\SYSTEMY\SEKWENCJE.csv', 'r') as file:
        reader = csv.reader(file)

        # Iteracja przez wiersze w pliku CSV
        for row in reader:
            # Dodanie strony do listy na podstawie danych z pliku
            pages.append(int(row[0]))



    # pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2]    # Lista stron do załadowania

    for page in pages:
        fifo.access_page(page)  # Dostęp do strony
        fifo.display()  # Wyświetlenie bieżących stron w pamięci

    print(f"Number of page fault's: {fifo.page_faults}")  # Wyświetlenie liczby błędów stron


if __name__ == "__main__":
    n = int(input("Podaj pojemność pamięci: "))  # Pobranie od użytkownika pojemności pamięci
    main(n)  # Uruchomienie głównej funkcji programu
