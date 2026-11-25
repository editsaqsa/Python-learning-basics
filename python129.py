# Multiprocess in python
import multiprocessing
import time

def heavy_task(n: int):
    total = 0
    for i in range(1, n+1):
        total += i * i
        print(f"Done for {n} , totall = {total}")


    if __name__ == "__main__":
        t0 = time.perf_counter()

        p1 = multiprocessing.Process(target=heavy_task, args=(5_000_000,))
        p2 = multiprocessing.Process(target=heavy_task, args=(5_000_000,))

        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print(f"Total time: {time.perf_counter()- t0:.2f}s")
        
