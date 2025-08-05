class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0


def calculate_times(processes):
    n = len(processes)
    current_time = 0

    for process in processes:
        # The process starts as soon as the CPU is free, which is max of current time or arrival time
        process.start_time = max(current_time, process.arrival_time)
        # The process completes after its burst time
        process.completion_time = process.start_time + process.burst_time
        # Turnaround time is the total time taken from arrival to completion
        process.turnaround_time = process.completion_time - process.arrival_time
        # Waiting time is turnaround time minus burst time
        process.waiting_time = process.turnaround_time - process.burst_time

        # Update current time to the completion time of this process
        current_time = process.completion_time


def print_processes(processes):
    print("PID\tArrival\tBurst\tStart\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(
            f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.start_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")


def main():
    # Sample processes: (pid, arrival_time, burst_time)
    processes = [
        Process("P1", 0, 4),
        Process("P2", 0, 3),
        Process("P3", 0, 2),
    ]

    # Sort processes by their arrival time
    processes.sort(key=lambda p: p.arrival_time)

    # Calculate all times
    calculate_times(processes)

    # Print process details
    print_processes(processes)


if __name__ == "__main__":
    main()
