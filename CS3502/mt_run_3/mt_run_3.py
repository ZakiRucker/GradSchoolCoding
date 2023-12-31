import queue
import threading
from urllib.request import urlopen  
import time
#import sched


# called by each thread
def get_url(i, lock, q, url):
     lock.acquire()
     print("This is a new thread ", i,  " \n")
     q.put(url)
     with urlopen(url) as response:
          q.put(response.read())
     lock.release()

def hello():
    print("hello, world")


theurls = ["http://google.com", "http://www.nps.edu", "http://cs.umass.edu"]

q = queue.Queue()
lock = threading.Lock()

i = 0
for u in theurls:
    t = threading.Thread(target=get_url, args = (i, lock, q, u))
#    t.daemon = True
    i+=1
    t.start()

t = threading.Timer(30.0, hello)
t.start()

time.sleep(10)
s = q.qsize()
print("Queue has ", s, "elements.\n") 
for i in range(0, s):
    c = q.get()
    print(c)
    time.sleep(5)
