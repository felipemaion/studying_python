## Raul 1
# import asyncio
# from concurrent.futures import ThreadPoolExecutor
# def func(a, b):
#     # Do time intensive stuff...
#     return a + b


# async def main(loop):
#     executor = ThreadPoolExecutor()
#     result = await loop.run_in_executor(executor, func, "Hello,", " world!")
#     print(result)
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main(loop))


## Raul 2
# import multiprocessing
# import time
# def countdown(n):
#     while n > 0:
#         n -= 1
# COUNT = 10000000
# start = time.time()
# with multiprocessing.Pool as pool:
#     pool.map(countdown, [COUNT/2, COUNT/2])  #two processes running on backgrounds
#     pool.close()
#     pool.join()
# end = time.time()
# print(end-start)

#!/usr/bin/python3

import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass