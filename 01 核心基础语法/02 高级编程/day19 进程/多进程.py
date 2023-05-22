from multiprocessing import Process


def eat(name, num):
    print(f'这是{name}吃的第{num}碗面')


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=eat, args=('墨离', i))
        p.start()
        p.join()
        '''
        让主进程等待子进程任务结束之后再往后继续——阻塞
        这个时候某一个进程需要的时间比较长的话，那么所需的时间就比较长
        '''