import random
import time
import threading

def random_one():
    while True:
        load = random.randint(1,1000)
        time.sleep(1)
        print(f'random_one:{load}')
    

def random_five():
    while True:
        load = random.randint(1,1000)
        time.sleep(5)
        print(f'random_five:{load}')
    
thread_01 = threading.Thread(target=random_one)  
thread_02 = threading.Thread(target=random_five) 

thread_01.daemon = True
thread_02.daemon = True

thread_01.start()
thread_02.start()

thread_01.join()
thread_02.join()
    
