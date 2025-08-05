import csv
from collections import deque

class Process:
    def __init__(self, pid, arrival_time, execution_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.remaining_time = execution_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.start_time = None

def round_robin(process_list, time_quantum):
    time = 0
    queue = deque()
    completed_processes = []
    waiting_processes = process_list.copy()

    while waiting_processes or queue:
        while waiting_processes and waiting_processes[0].arrival_time <= time:
            queue.append(waiting_processes.pop(0))

        if queue:
            current_process = queue.popleft()

            if current_process.start_time is None:
                current_process.start_time = time

            if current_process.remaining_time <= time_quantum:
                time += current_process.remaining_time
                current_process.remaining_time = 0
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.start_time - current_process.arrival_time
                completed_processes.append(current_process)
            else:
                time += time_quantum
                current_process.remaining_time -= time_quantum
                queue.append(current_process)

            while waiting_processes and waiting_processes[0].arrival_time <= time:
                queue.append(waiting_processes.pop(0))
        else:
            time += 1

    return completed_processes

def save_to_csv(processes):
    try:
        with open("ROUNDROBIN.csv", "w+", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["PID", "Arrival", "Execution", "Start", "Completion", "Turnaround", "Waiting"])
            for process in processes:
                writer.writerow([process.pid, process.arrival_time, process.execution_time, process.start_time,
                                 process.completion_time, process.turnaround_time, process.waiting_time])
        print("Saved successfully to ROUNDROBIN.csv!")
    except Exception as e:
        print(f"Failed to save to ROUNDROBIN.csv: {e}")

def main(time_quanta=2):
    process_list = [
        Process("P1", 2, 6),
        Process("P2", 5, 2),
        Process("P3", 1, 8),
        Process("P4", 0, 3),
        Process("P5", 4, 4)
    ]

    process_list.sort(key=lambda process: process.arrival_time)
    completed_processes = round_robin(process_list, time_quanta)
    completed_processes.sort(key=lambda process: process.arrival_time)
    save_to_csv(completed_processes)

if __name__ == "__main__":
    main()
