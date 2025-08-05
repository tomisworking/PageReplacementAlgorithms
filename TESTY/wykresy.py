import matplotlib.pyplot as plt

# Dane
# liczba_stron = [10, 50, 100, 10, 50, 100]
# pojemnosc = [3, 3, 3, 5, 5, 5]
# fifo_page_faults = [7, 27, 54, 6, 18, 28]
# lru_page_faults = [7, 25, 51, 6, 20, 28]
#
# # Wykres Page Faults
# fig, ax = plt.subplots(figsize=(9, 6))
#
# # Wykres dla pojemności 3
# ax.plot(liczba_stron[:3], fifo_page_faults[:3], label='FIFO (Pojemność 3)', marker='o')
# ax.plot(liczba_stron[:3], lru_page_faults[:3], label='LRU (Pojemność 3)', marker='o')
#
# # Wykres dla pojemności 5
# ax.plot(liczba_stron[3:], fifo_page_faults[3:], label='FIFO (Pojemność 5)', marker='s')
# ax.plot(liczba_stron[3:], lru_page_faults[3:], label='LRU (Pojemność 5)', marker='s')
#
# ax.set_xlabel('Liczba Stron')
# ax.set_ylabel('Liczba Page Faults')
# ax.set_title('Porównanie liczby Page Faults dla FIFO i LRU przy różnych pojemnościach pamięci')
# ax.legend()
# ax.grid(True)
#
# plt.show()







# Dane
num_processes = [25, 75, 125]

rr_turnaround = [74.0, 269.48, 373.832]
rr_waiting = [69.24, 264.0, 368.848]
fcfs_turnaround = [66.24, 208.72, 334.128]
fcfs_waiting = [61.48, 203.24, 329.144]

# Wykres Turnaround Time
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(num_processes, rr_turnaround, label='Round Robin', marker='o')
plt.plot(num_processes, fcfs_turnaround, label='FCFS', marker='o')
plt.xlabel('Liczba Procesów')
plt.ylabel('Średni Turnaround Time')
plt.title('Porównanie Średniego Turnaround Time')
plt.legend()

# Wykres Waiting Time
plt.subplot(1, 2, 2)
plt.plot(num_processes, rr_waiting, label='Round Robin', marker='o')
plt.plot(num_processes, fcfs_waiting, label='FCFS', marker='o')
plt.xlabel('Liczba Procesów')
plt.ylabel('Średni Waiting Time')
plt.title('Porównanie Średniego Waiting Time')
plt.legend()

plt.tight_layout()
plt.show()
