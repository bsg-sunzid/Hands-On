import time

class Timer:
    """Context manager for timing code execution."""
    
    def __enter__(self):
        self.start = time.perf_counter()  # record start time
        return self  # optional, can return self or anything else

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()    # record end time
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.6f} seconds")


with Timer() as t:
    # Simulate some work
    time.sleep(2)

