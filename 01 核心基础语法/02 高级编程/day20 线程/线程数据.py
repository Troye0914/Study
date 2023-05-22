from threading import Thread

num = 10


def func():
    global num
    num += 12
    print(f'子线程中的num:{num}')


if __name__ == '__main__':
    print('主线程')
    t = Thread(target=func)
    t.start()
    t.join()
    print(f'主线程的num{num}')
