import time

class Timer:
    def __enter__(self):
        self.start = time.process_time()
    def __exit__(self, *args):
        self.end = time.process_time()
        print(f"Executed in {self.end-self.start} time\n")