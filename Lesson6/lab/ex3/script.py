# Method which uses a lot of space
def use_space(loops):
    for i in range(0, loops):
        arr = bytearray(512000000)

# Program
import time
start_time = int(round(time.time() * 1000))
use_space(2)
end_time = int(round(time.time() * 1000))
print('time: ' + str(end_time - start_time))

