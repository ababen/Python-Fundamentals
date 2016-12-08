import time
import webbrowser
i = 0

while i < 3:
    time.sleep(10)
    webbrowser.open("http://www.google.com")
    print "Take a break!"
    i = i + 1
