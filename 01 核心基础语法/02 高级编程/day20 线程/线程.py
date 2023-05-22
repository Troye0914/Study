from threading import Thread


def work():
    print('他在抄作业')


if __name__ == '__main__':
    print('主线程')
    # 创建线程对象
    t = Thread(target=work)
    t.start()
