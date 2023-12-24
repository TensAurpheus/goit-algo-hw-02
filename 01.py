from queue import Queue
import time
from random import randint

queue = Queue()
id = 0

def generate_requests(q, req_num):
    q.put(f'Request {req_num}')
    print(f'Request {req_num} received')
    time.sleep(0.5)

def process_requests(q, num):
    for i in range(num):
        if not q.empty():
            current_req = q.get()
            print(current_req, ' processed')
            print('Current queue: ', q.queue)
            time.sleep(1)
        else:
            print('Queue empty')
            break

num_generated = 0
num_processed = 0


while True:
    num_generated = randint(1, 5)
    num_processed = randint(1, 5)
    for i in range(num_generated):
        id += 1
        generate_requests(queue, id)
    process_requests(queue, num_processed)
    key = input('press q to exit, any key to continue ')
    if key == 'q':
        break
 