import csv
import random


class Process:
    def __init__(self, pid, arrival_time, execution_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.remaining_time = execution_time
        self.start_time = None
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


def round_robin(processes, time_quanta):
    time = 0
    queue = []
    processes_remaining = len(processes)

    while processes_remaining > 0:
        for process in processes:
            if process.arrival_time <= time and process.remaining_time > 0 and process not in queue:
                queue.append(process)

        if not queue:
            time += 1
            continue

        current_process = queue.pop(0)

        if current_process.start_time is None:
            current_process.start_time = time

        execution_time = min(time_quanta, current_process.remaining_time)
        time += execution_time
        current_process.remaining_time -= execution_time

        for process in processes:
            if process.arrival_time <= time and process.remaining_time > 0 and process not in queue and process != current_process:
                queue.append(process)

        if current_process.remaining_time == 0:
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.start_time - current_process.arrival_time
            processes_remaining -= 1


def save_to_csv(processes):
    try:
        with open("ROUNDROBIN.csv", "w+", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["PID", "Arrival", "Execution", "Start", "Completion", "Turnaround", "Waiting"])
            for process in processes:
                writer.writerow([process.pid, process.arrival_time, process.execution_time, process.start_time,
                                 process.completion_time, process.turnaround_time, process.waiting_time])

        print("Zapisano pomyślnie do pliku ROUNDROBIN.csv!")
    except Exception as e:
        print(f"Nie udało się zapisać do pliku ROUNDROBIN.csv: {e}")


def main(n, time_quanta):
    process_list = []

    for pid in range(1, n + 1):
        random_number = random.randint(0, 100)
        process_list.append(Process(pid, random_number, 5))

    process_list.sort(key=lambda process: process.arrival_time)

    round_robin(process_list, time_quanta)

    save_to_csv(process_list)


if __name__ == "__main__":
    n = int(input("Podaj liczbę procesów: "))
    quanta = int(input("Podaj time quantum: "))

    main(n, quanta)
