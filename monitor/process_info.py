import psutil


class ProcessInfo:
    def __init__(self, pid, name, status="init"):
        self.pid = pid
        self.name = name
        self.status = status

        self.username = psutil.Process(self.pid).username()

        self.cpu_percent = 0
        self.memory_percent = 0

    def update(self):
        p = psutil.Process(self.pid)
        self.cpu_percent = p.cpu_percent()
        self.memory_percent = p.memory_percent()

    def is_alive(self):
        try:
            p = psutil.Process(self.pid)
            return p.is_running()
        except psutil.NoSuchProcess:
            return False

    def update_status(self, status):
        self.status = status

    def terminate(self):
        print(f"Terminating process {self.pid}")
        p = psutil.Process(self.pid)
        p.kill()

    def __str__(self):
        return f"Process {self.pid} - {self.name} - {self.status} - {self.cpu_percent} - {self.memory_percent} - {self.username}"
