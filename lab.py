
# Define a function to calculate average waiting time and average turnaround time for FCFS scheduling.
def calculate_fcfs(processes, burst_times):

    
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting times
    for i in range(1, n):
        waiting_time[i] = burst_times[i - 1] + waiting_time[i - 1]

    # Calculate turnaround times
    for i in range(n):
        turnaround_time[i] = burst_times[i] + waiting_time[i]

    # Calculate the average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

# Define a function to calculate average waiting time and average turnaround time for SJF scheduling.
def calculate_sjf(processes, burst_times):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = burst_times.copy()

    total_burst_time = sum(burst_times)
    current_time = 0

    # Simulate SJF scheduling
    while current_time < total_burst_time:
        min_burst_time = float('inf')
        shortest_job = None

        # Find the shortest job
        for i in range(n):
            if remaining_time[i] > 0 and burst_times[i] < min_burst_time:
                min_burst_time = burst_times[i]
                shortest_job = i

        if shortest_job is None:
            current_time += 1
            continue

        # Update waiting time, current time, and turnaround time for the shortest job
        waiting_time[shortest_job] = current_time
        current_time += burst_times[shortest_job]
        turnaround_time[shortest_job] = current_time
        remaining_time[shortest_job] = 0

    # Calculate the average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

# Define a function to calculate average waiting time and average turnaround time for Round Robin scheduling.
def calculate_round_robin(processes, burst_times, quantum):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    remaining_time = burst_times.copy()
    current_time = 0

    # Simulate Round Robin scheduling
    while any(remaining_time):
        for i in range(n):
            if remaining_time[i] > 0:
                execute_time = min(quantum, remaining_time[i])
                remaining_time[i] -= execute_time
                current_time += execute_time
                waiting_time[i] += current_time

                if remaining_time[i] == 0:
                    turnaround_time[i] = current_time

    # Calculate the average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

if __name__ == '__main__':
    n = int(input("Enter the number of processes: "))
    processes = [i for i in range(1, n + 1)]
    burst_times = []

    # Input burst times for each process
    for i in range(n):
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        burst_times.append(burst_time)

    # Calculate and display results for FCFS
    fcfs_avg_waiting, fcfs_avg_turnaround = calculate_fcfs(processes, burst_times)
    
    # Input time quantum for Round Robin
    quantum = int(input("Enter time quantum for Round Robin: "))
    
    # Calculate and display results for SJF and Round Robin
    sjf_avg_waiting, sjf_avg_turnaround = calculate_sjf(processes, burst_times)
    rr_avg_waiting, rr_avg_turnaround = calculate_round_robin(processes, burst_times, quantum)

    print(f"Average Waiting Time (FCFS): {fcfs_avg_waiting}")
    print(f"Average Turnaround Time (FCFS): {fcfs_avg_turnaround}")

    print(f"Average Waiting Time (SJF): {sjf_avg_waiting}")
    print(f"Average Turnaround Time (SJF): {sjf_avg_turnaround}")

    print(f"Average Waiting Time (Round Robin): {rr_avg_waiting}")
    print(f"Average Turnaround Time (Round Robin): {rr_avg_turnaround}")
