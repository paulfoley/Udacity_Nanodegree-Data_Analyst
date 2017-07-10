import time
import webbrowser

total_breaks = 0
break_count = 0

print("This program started on " + time.ctime())
while total_breaks < 3:
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=VDvr08sCPOc")
    total_breaks += 1
    break_count += 1
