import matplotlib.pyplot as plt
from process import Process
def display_results(name, processes, gantt_chart):
    print(f"\n{name} Scheduling Results:")
    print("PID\tAT\tBT\tWT\tTAT")
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}")

    avg_wt = sum(p.waiting_time for p in processes) / len(processes)
    avg_tat = sum(p.turnaround_time for p in processes) / len(processes)
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

    # Gantt Chart
    plt.figure(figsize=(8, 2))
    for pid, start, end in gantt_chart:
        plt.barh(0, end - start, left=start, edgecolor="black")
        plt.text((start + end) / 2, 0, f"P{pid}", ha="center", va="center", color="white")
    plt.title(f"{name} Gantt Chart")
    plt.xlabel("Time")
    plt.yticks([])
    plt.show()
