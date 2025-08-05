from ROUNDROBIN import round_robin, calculate_average_times, Process
from GENERATOR_PROCESÓW import main
import csv
import time


try:
    with open("WYNIKI.csv", "w+", newline="") as plik:
        writer = csv.writer(plik)
        writer.writerow(["average_turnaround_time", "average_waiting_time"])
        for i in range(100):
            main(100)
            process_list = []  # Lista procesów
            with open(r'PROCESY.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Pominięcie nagłówka

                # Iteracja przez wiersze w pliku CSV
                for row in reader:
                    # Dodanie procesu do listy na podstawie danych z pliku
                    process_list.append(Process(row[0], int(row[1]), int(row[2])))
            completed = round_robin(process_list,2)
            avg_turnaround_time, avg_waiting_time = calculate_average_times(completed)
            writer.writerow([avg_turnaround_time,avg_waiting_time])

        print("Zapisano pomyślnie do pliku WYNIKI.csv!")
except Exception as e:
        print(f"Nie udało się zapisać do pliku WYNIKI.csv: {e}")


