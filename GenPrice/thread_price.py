from random import random
import time
import threading

# daemon

L = [[0] for i in range(100)]
#lock = threading.Lock()


def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement


def add_price():
    while True:
      t1 = time.perf_counter()
      for i in L:
        i.append(i[-1] + generate_movement())
      t2 = time.perf_counter()
      time.sleep(1-t2+t1)
      #print(1-t2+t1)


threading.Thread(target = add_price, daemon = True).start()
