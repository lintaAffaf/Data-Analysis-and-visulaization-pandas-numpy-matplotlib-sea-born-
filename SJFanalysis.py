import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, burst_time, arrival_time=0):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_time = burst_time


def sjf(processes):
    time = 0
    gantt_chart = []
    processes = sorted(processes, key=lambda x: (x.arrival_time, x.burst_time))

    while processes:
        available = [p for p in processes if p.arrival_time <= time]
        if not available:
            time += 1
            continue
        p = min(available, key=lambda x: x.burst_time)
        processes.remove(p)
        start_time = time
        p.waiting_time = time - p.arrival_time
        time += p.burst_time
        end_time = time
        p.turnaround_time = p.waiting_time + p.burst_time
        gantt_chart.append((p.pid, start_time, end_time))
    return gantt_chart


def plot_gantt_chart(gantt_chart):
    fig, gnt = plt.subplots(figsize=(8, 3))
    gnt.set_title("Gantt Chart - SJF Scheduling")
    gnt.set_xlabel("Time")
    gnt.set_ylabel("Processes")

    for i, (pid, start, end) in enumerate(gantt_chart):
        gnt.broken_barh([(start, end - start)], (10 * (i + 1), 9), facecolors=("orange"))
        gnt.text((start + end) / 2, 10 * (i + 1) + 4, f"P{pid}", ha="center")

    gnt.set_ylim(5, 15 * (len(gantt_chart) + 1))
    gnt.grid(True)
    plt.show()


# Example
if __name__ == "__main__":
    processes = [Process(1, 5, 0), Process(2, 3, 1), Process(3, 8, 2)]
    gantt_chart = sjf(processes)
    plot_gantt_chart(gantt_chart)
