import threading
import time
import random

flag = [False, False]
turn = 0
BUFFER_SIZE = 5
buffer = []
count = 0

def producer():
    global flag, turn, buffer, count
    while True:
        item = random.randint(1, 100)
        print(f"Producer produced: {item}")
        flag[0] = True
        turn = 1
        while flag[1] and turn == 1: pass
        if count < BUFFER_SIZE:
            buffer.append(item)
            count += 1
            print(f"Buffer: {buffer}")
        else:
            print("Buffer full! Producer waiting...")
        flag[0] = False
        time.sleep(random.random())

def consumer():
    global flag, turn, buffer, count
    while True:
        flag[1] = True
        turn = 0
        while flag[0] and turn == 0: pass
        if count > 0:
            item = buffer.pop(0)
            count -= 1
            print(f"Consumer consumed: {item}")
            print(f"Buffer: {buffer}")
        else:
            print("Buffer empty! Consumer waiting...")
        flag[1] = False
        time.sleep(random.random())

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    producer_thread.start()
    consumer_thread.start()
    time.sleep(3)
    print("\nTerminating after 3 seconds...")
    exit()