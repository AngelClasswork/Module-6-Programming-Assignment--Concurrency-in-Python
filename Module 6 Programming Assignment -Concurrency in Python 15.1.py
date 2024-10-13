#15.1 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit.
import multiprocessing
import time
import random
from datetime import datetime

#create the function that makes a random wait time
def process():
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    print(f"Current time: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    processes = []
    
#Make the loop for the three seperate processes
    for _ in range(3):
        p = multiprocessing.Process(target=process)
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
