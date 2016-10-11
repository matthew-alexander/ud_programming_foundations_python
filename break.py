import webbrowser
import time

loop = 1
current_time = time.ctime()
work_interval = 1800

print("this work session started at " + time.ctime())
while(loop <= 3):
    time.sleep(work_interval)
    webbrowser.open("https://www.youtube.com/watch?v=a_XgQhMPeEQ")
    loop += 1



# other songs https://www.youtube.com/watch?v=a_XgQhMPeEQ
# https://www.youtube.com/watch?v=MsW8rXPcnM0

#webbrowser.open("https://www.youtube.com/watch?v=r-gvIeNWAPo")
