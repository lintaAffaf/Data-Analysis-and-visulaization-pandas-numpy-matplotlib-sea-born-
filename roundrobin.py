import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, burst_time, arrival_time=0):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_time = burst_time


def round_robin(processes, quantum=2):
    time = 0
    gantt_chart = []
    queue = processes.copy()

    while queue:
        p = queue.pop(0)
        if time < p.arrival_time:
            time = p.arrival_time
        start_time = time
        if p.remaining_time > quantum:
            time += quantum
            p.remaining_time -= quantum
            end_time = time
            gantt_chart.append((p.pid, start_time, end_time))
            queue.append(p)
        else:
            time += p.remaining_time
            end_time = time
            p.waiting_time = time - p.arrival_time - p.burst_time
            p.turnaround_time = p.waiting_time + p.burst_time
            gantt_chart.append((p.pid, start_time, end_time))
            p.remaining_time = 0
    return gantt_chart


def plot_gantt_chart(gantt_chart):
    fig, gnt = plt.subplots(figsize=(10, 3))
    gnt.set_title("Gantt Chart - Round Robin Scheduling")
    gnt.set_xlabel("Time")
    gnt.set_ylabel("Processes")

    for i, (pid, start, end) in enumerate(gantt_chart):
        gnt.broken_barh([(start, end - start)], (10 * (i + 1), 9), facecolors=("pink"))
        gnt.text((start + end) / 2, 10 * (i + 1) + 4, f"P{pid}", ha="center")

    gnt.set_ylim(5, 15 * (len(gantt_chart) + 1))
    gnt.grid(True)
    plt.show()


# Example
if __name__ == "__main__":
    processes = [Process(1, 5, 0), Process(2, 3, 1), Process(3, 8, 2)]
    gantt_chart = round_robin(processes, quantum=2)
    plot_gantt_chart(gantt_chart)
