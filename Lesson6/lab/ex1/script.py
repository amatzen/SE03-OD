import time

def fib(x):
  if x < 0:
    return
  
  elif x == 0:
    return 0

  elif x == 1 or x == 2:
    return 1

  else:
    return fib(x-1) + fib(x-2)

start_time = time.time()
fib(35)
print("%s seconds" % (time.time() - start_time))
