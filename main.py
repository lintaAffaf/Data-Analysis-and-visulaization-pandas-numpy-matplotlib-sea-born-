from FCFSanalysis import fcfs
from SJFanalysis import sjf
from priorityscheduling import priority_scheduling
from roundrobin import round_robin
from utility import display_results

# ---------------- Process Class ----------------
class Process:
    def __init__(self, pid, burst_time, arrival_time=0, priority=0):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_time = burst_time

# ---------------- Main Driver ----------------
if __name__ == "__main__":
    processes = [
        Process(1, 6, 0, 2),
        Process(2, 8, 1, 1),
        Process(3, 7, 2, 3),
        Process(4, 3, 3, 2)
    ]

    # FCFS
    fcfs_chart = fcfs([Process(p.pid, p.burst_time, p.arrival_time, p.priority) for p in processes])
    display_results("FCFS", processes, fcfs_chart)

    # SJF
    sjf_chart = sjf([Process(p.pid, p.burst_time, p.arrival_time, p.priority) for p in processes])
    display_results("SJF", processes, sjf_chart)

    # Priority
    priority_chart = priority_scheduling([Process(p.pid, p.burst_time, p.arrival_time, p.priority) for p in processes])
    display_results("Priority", processes, priority_chart)

    # Round Robin
    rr_chart = round_robin([Process(p.pid, p.burst_time, p.arrival_time, p.priority) for p in processes], quantum=3)
    display_results("Round Robin", processes, rr_chart)
