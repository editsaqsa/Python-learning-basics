# MultiThreading
import threading
import time


def worker(name: str, delay: int):
    print(f"Start: {name}")
    time.sleep(delay)
    print(f"Done: {name}")


t0 = time.perf_counter()
t1 = threading.Thread(target=worker, args=("Thread-1", 2))
t2 = threading.Thread(target=worker, args=( "Thread-1", 2))
t1 . start()
t2 . start()

t1 . join()
t2 . join()
print(f"Total time: {time.perf_counter()- t0:.2f}s")
