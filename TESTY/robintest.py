import csv


class Process:
    def __init__(self, pid, arrival_time, execution_time):
        self.pid = pid  # ID procesu
        self.arrival_time = arrival_time  # Czas przybycia procesu
        self.execution_time = execution_time  # Czas wykonywania się procesu
        self.remaining_time = execution_time  # Pozostały czas wykonywania się procesu
        self.completion_time = 0  # Czas zakończenia się procesu
        self.waiting_time = 0  # Czas oczekiwania na rozpoczęcie procesu
        self.start_time = None  # Czas rozpoczęcia procesu
        self.executions = 0  # Liczba wykonanych kwantów czasu
        self.turnaround_time = 0

def round_robin(process_list, time_quantum):
    current_time = 0  # Bieżący czas
    queue = []  # kolejka procesów
    completed_processes = []  # Lista zakończonych procesów

    while any(process.remaining_time > 0 for process in process_list):

        available_processes = []

        for process in process_list:
            if process.arrival_time <= current_time:
                if process not in queue:
                    queue.append(process)

        if queue:
            # Wybór procesu do wykonania
            current_process = queue.pop(0)
            process_list.remove(current_process)

            if current_process.start_time is None:
                current_process.start_time = current_time


            # Jeśli pozostały czas procesu jest mniejszy lub równy kwantowi czasu
            if current_process.remaining_time <= time_quantum:
                current_time += current_process.remaining_time
                current_process.remaining_time = 0
                current_process.completion_time = current_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.arrival_time
                completed_processes.append(current_process)

                for process in process_list:
                    if process.arrival_time <= current_time:
                        available_processes.append(process)
                available_processes.sort(key=lambda process: process.arrival_time)
                for process in available_processes:
                    if process not in queue:
                        queue.append(process)

            else:
                # Jeśli proces nie może zostać zakończony w jednym kwancie czasu
                current_time += time_quantum
                current_process.remaining_time -= time_quantum

                for process in process_list:
                    if process.arrival_time <= current_time:
                        available_processes.append(process)
                available_processes.sort(key=lambda process: process.arrival_time)
                for process in available_processes:
                    if process not in queue:
                        queue.append(process)
                queue.append(current_process)
                process_list.append(current_process)
        else:
            # Jeśli nie ma dostępnych procesów, przesuń czas do przodu
            current_time += 1

    return completed_processes


# Funkcja zapisująca wyniki do pliku CSV
def save_to_csv(processes):
    try:
        with open("ROUNDROBIN.csv", "w+", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["PID", "Arrival", "Execution", "Start", "Completion","Turnaround","Waiting"])
            for process in processes:
                writer.writerow([process.pid, process.arrival_time, process.execution_time, process.start_time,
                                 process.completion_time, process.turnaround_time, process.waiting_time])

        print("Zapisano pomyślnie do pliku ROUNDROBIN.csv!")
    except:
        print("Nie udało się zapisać do pliku ROUNDROBIN.csv")


# Główna funkcja programu
def main(time_quanta=2):
    process_list = []  # Lista procesów
    with open(r'C:\Users\TOMEK\PycharmProjects\SYSTEMY\PROCESY.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pominięcie nagłówka

        # Iteracja przez wiersze w pliku CSV
        for row in reader:
            # Dodanie procesu do listy na podstawie danych z pliku
            process_list.append(Process(row[0], int(row[1]), int(row[2])))

    # Obliczenie czasów dla procesów
    completed = round_robin(process_list, time_quanta)

    # Zapisanie wyników do pliku CSV
    save_to_csv(completed)


# Uruchomienie programu
if __name__ == "__main__":
    main()
