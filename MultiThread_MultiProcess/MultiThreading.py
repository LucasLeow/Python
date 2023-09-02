import time
import threading 

def calc_square(numbers):
    print("calculating square numbers")
    for n in numbers:
        time.sleep(0.1)
        print("square: ", n*n)

def calc_cube(numbers):
    print("calculating cube numbers")
    for n in numbers:
        time.sleep(0.1)
        print("cube: ", n*n*n)
        
arr = [1,2,3,4]
t = time.time()

t1 = threading.Thread(target = calc_square, args = (arr,))
t2 = threading.Thread(target = calc_cube, args = (arr,))

# Start thread (tasks)
t1.start()
t2.start()

# Wait till threads are done
t1.join()
t2.join()

print("done in: ", time.time() - t)

