import matplotlib.pyplot as plt
import numpy as np

class Process:
    def __init__(self, pid, burst_time, arrival_time=0, priority=0):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_time = burst_time


# ---------- FCFS Scheduling ----------
def fcfs(processes):
    time = 0
    gantt_chart = []
    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time
        p.waiting_time = time - p.arrival_time
        start_time = time
        time += p.burst_time
        p.turnaround_time = p.waiting_time + p.burst_time
        gantt_chart.append((p.pid, start_time, time))  # Now has 3 values
    return gantt_chart


def plot_gantt_chart(gantt_chart):
    fig, gnt = plt.subplots(figsize=(8, 3))
    gnt.set_title("Gantt Chart - FCFS Scheduling")
    gnt.set_xlabel("Time")
    gnt.set_ylabel("Processes")

    yticks = []
    ylabels = []

    for i, (pid, start, end) in enumerate(gantt_chart):
        yticks.append(10 * (i + 1))
        ylabels.append(f"P{pid}")
        gnt.broken_barh([(start, end - start)], (10 * (i + 1), 9), facecolors=("skyblue"))
        gnt.text((start + end) / 2, 10 * (i + 1) + 4, f"P{pid}", ha="center", va="center")

    gnt.set_yticks(yticks)
    gnt.set_yticklabels(ylabels)
    gnt.set_ylim(5, 15 * (len(gantt_chart) + 1))
    gnt.grid(True)
    plt.show()

# ---------- Example ----------
processes = [
    Process(1, 5, 0),
    Process(2, 3, 1),
    Process(3, 8, 2)
]

gantt_chart = fcfs(processes)
plot_gantt_chart(gantt_chart)


plt.show()

