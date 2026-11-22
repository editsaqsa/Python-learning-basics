# Time module in python
import time

print("Current readable time:", time.ctime())

formatted_now = time.strftime("%d-%m-%Y , %I:%M:%S:%P", time.localtime())
print("Formatted time:", formatted_now)

start_time = time.time()
print("\nStarting practice loop...")
for i in range(1,4):
    print(f"step{i} runnining...")
    time.sleep(1)


end_time = time.time()
elapsed = end_time- start_time
print(f"\nTotal time taken: {elapsed:.2f} second")

