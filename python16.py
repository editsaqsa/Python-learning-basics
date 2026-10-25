import time
hour = int(time.strftime("%H"))
print("my live routine alert")
if hour >= 5 and hour < 12:
    print("study and coding time")
elif hour >= 12 and hour < 17:
    print("relax and take a break")
elif hour >= 17 and hour < 22:
    print("martial art time")
else:
    print("sleep time")
    