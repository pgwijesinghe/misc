import multiprocessing as mp
import time
import math

a = []
b = []
c = []

def calculation1(numbers):
    for number in numbers:
        a.append(math.sqrt(number**3))

def calculation2(numbers):
    for number in numbers:
        a.append(math.sqrt(number**4))

def calculation3(numbers):
    for number in numbers:
        a.append(math.sqrt(number**5))

if __name__ == "__main__": # this is mandatory in multiprocessing
    number_list = list(range(5000000))

    p1 = mp.Process(target=calculation1, args=(number_list,))
    p2 = mp.Process(target=calculation2, args=(number_list,))
    p3 = mp.Process(target=calculation3, args=(number_list,))

    start = time.time()
    # calculation1(number_list)
    # calculation2(number_list)
    # calculation3(number_list)
    p1.start()
    print("process1")
    p2.start()
    print("process2")
    p3.start()
    print("process3")
    end = time.time()

    print(f"Time taken: {end-start}")