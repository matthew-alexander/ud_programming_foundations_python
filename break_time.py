import webbrowser
import time

loop=1
current_time=time.ctime()
work_interval = 10
print("this work session started at " + time.ctime())
while (loop<=3):
    time.sleep(work_interval)
    webbrowser.open("http://www.youtube.com/watch?v=r-gvleNWAPo")
    loop+=1



