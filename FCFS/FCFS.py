import random
import csv
from operator import attrgetter


# Utworzenie obiektu Process
class Process:
    def __init__(self, pid, arrival_time, execution_time):
        self.pid = pid  # ID procesu
        self.arrival_time = arrival_time  # Czas przybycia procesu
        self.execution_time = execution_time  # Czas wykonywania się procesu
        self.start_time = 0  # Czas rozpoczęcia się procesu
        self.completion_time = 0  # Czas zakończenia się procesu
        self.turnaround_time = 0  # Czas obrotu procesu (od przybycia do zakończenia)
        self.waiting_time = 0  # Czas oczekiwania na rozpoczęcie procesu



def calculate_times(processes):
    current_time = 0
    completed_processes = []

    while processes:
        # Znajdź procesy, które są dostępne do wykonania (ich czas przybycia jest mniejszy lub równy aktualnemu czasowi)
        available_processes = []
        for process in processes:
            if process.arrival_time <= current_time:
                available_processes.append(process)

        if available_processes:
            # Wybierz proces z minimalnym czasem przybycia spośród dostępnych procesów
            current_process = min(available_processes, key=attrgetter('arrival_time'))

            # Ustawienia czasów dla wybranego procesu
            current_process.start_time = max(current_time, current_process.arrival_time)
            current_process.completion_time = current_process.start_time + current_process.execution_time
            # current_process.waiting_time = current_process.start_time - current_process.arrival_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.execution_time

            # Aktualizacja bieżącego czasu do czasu zakończenia wybranego procesu
            current_time = current_process.completion_time

            # Dodanie procesu do zakończonych procesów i usunięcie go z listy procesów
            completed_processes.append(current_process)
            processes.remove(current_process)
        else:
            # Jeśli nie ma dostępnych procesów, przesuń czas do przodu
            current_time += 1

    return completed_processes


def save_to_csv(processes,avg_turnaround, avg_waiting):
    try:
        with open("FCFS.csv", "w+", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["PID", "Arrival", "Execution", "Start", "Completion","Turnaround", "Waiting"])
            for process in processes:
                writer.writerow([process.pid, process.arrival_time, process.execution_time, process.start_time,
                                 process.completion_time,process.turnaround_time, process.waiting_time])

            writer.writerow(["", "", "", "", "", avg_turnaround, avg_waiting])


        print("Zapisano pomyślnie do pliku FCFS.csv!")
    except Exception as e:
        print(f"Nie udało się zapisać do pliku FCFS.csv: {e}")

def calculate_average_times(processes):
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    total_waiting_time = sum(process.waiting_time for process in processes)
    average_turnaround_time = total_turnaround_time / len(processes)
    average_waiting_time = total_waiting_time / len(processes)
    return average_turnaround_time, average_waiting_time


def main():

    process_list = []
    # Odczyt pliku CSV z danymi procesów
    with open(r'C:\Users\TOMEK\PycharmProjects\SYSTEMY\PROCESY.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pominięcie nagłówka

        # Iteracja przez wiersze w pliku CSV2
        for row in reader:
            # Dodanie procesu do listy na podstawie danych z pliku
            process_list.append(Process(row[0], int(row[1]), int(row[2])))

    # Obliczenie czasów dla procesów
    completed = calculate_times(process_list)
    avg_turnaround_time, avg_waiting_time = calculate_average_times(completed)

    # Zapisanie wyników do pliku CSV
    save_to_csv(completed,avg_turnaround_time,avg_waiting_time)


if __name__ == "__main__":
    main()
