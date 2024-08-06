from multiprocessing import Process
from time import sleep


def func1():
    print('func1: starting')
    pos = 0
    while True:
        print(pos)
        pos += 10
        sleep(10)
    print('func1: finishing')


def func2():
    print('func2: starting')
    for pos in range(1000):
        print(pos)
        sleep(1)
    print('func2: finishing')


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join()
    p2.join()
