from greenlet import greenlet


def eat(name):
    print(f'{name}在吃炸串')
    s.switch('张三')
    print(f'{name}还在吃炸串')


def sleep(name):
    print(f'{name}在睡觉')
    e.switch()
    print(f'{name}还在睡觉')


if __name__ == '__main__':
    e = greenlet(eat)
    s = greenlet(sleep)
    # 协程的任务参数是写在开启协程的方法里面的
    e.switch('墨离')