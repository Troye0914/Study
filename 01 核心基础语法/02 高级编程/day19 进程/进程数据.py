from multiprocessing import Process

age = 18


def fun():
    global age
    age += 10
    print(age)


if __name__ == '__main__':
    p = Process(target=fun)
    p.start()
    p.join()
    print(f'主进程的age{age}')
