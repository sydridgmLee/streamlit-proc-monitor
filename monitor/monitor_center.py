from .process_info import ProcessInfo
from multiprocessing import Manager
import psutil


class MonitorCenter:
    manager = Manager()
    processes = manager.dict()

    @staticmethod
    def register_process(pid, name):
        MonitorCenter.processes[pid] = ProcessInfo(
            pid,
            name,
        )

    @staticmethod
    def unregister_process(pid):
        MonitorCenter.processes.pop(pid)

    @staticmethod
    def get_process(pid):
        return MonitorCenter.processes.get(pid)

    @staticmethod
    def get_processes():
        return MonitorCenter.processes.values()

    @staticmethod
    def update_processes():
        dead_pids = []
        for process_info in MonitorCenter.processes.values():

            if not process_info.is_alive():
                print(f"Process {process_info.pid} is dead")
                dead_pids.append(process_info.pid)
                continue

            process_info.update()

        for pid in dead_pids:
            MonitorCenter.unregister_process(pid)

    @staticmethod
    def update_process_status(pid, status):
        process_info = MonitorCenter.get_process(pid)
        if process_info:
            process_info.update_status(status)
            MonitorCenter.processes[pid] = process_info

    @staticmethod
    def terminate_process(pid):
        process_info = MonitorCenter.get_process(pid)
        if process_info:
            process_info.terminate()

    @staticmethod
    def terminate_all_processes():
        for pid in list(MonitorCenter.processes.keys()):
            MonitorCenter.terminate_process(pid)
