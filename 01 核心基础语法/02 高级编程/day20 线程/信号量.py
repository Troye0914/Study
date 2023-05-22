import multiprocessing
import time
import multiprocessing
from multiprocessing import Process, Semaphore

multiprocessing.set_start_method('fork')


def black_room(name, s):
    s.acquire()
    print(f'{name}被拖进小黑屋')
    time.sleep(3)
    print(f'{name}被抬出小黑屋')
    s.release()


if __name__ == '__main__':
    # 设置信号量，设置多少个锁
    s = Semaphore(3)
    for i in range(10):
        p = Process(target=black_room, args=(f'李四{i}号', s))
        p.start()
