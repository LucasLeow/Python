import time
import multiprocessing

def calc_square(numbers):
    print("calculating square numbers")
    for n in numbers:
        print("square: ", n*n)

def calc_cube(numbers):
    print("calculating cube numbers")
    for n in numbers:
        print("cube: ", n*n*n)

if __name__ == "__main__":
    arr = [1,2,3,4]

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    t = time.time()

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to end
    p1.join()
    p2.join()

    print("done in: ", time.time() - t)