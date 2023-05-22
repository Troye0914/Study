from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def eat(self, name):
        print(f'{name}等下要去吃面了')

    # 重写run方法
    def run(self) -> None:
        print('我是自定义进程类的子进程')
        self.eat(self.name)


if __name__ == '__main__':
    print('主进程')
    p = MyProcess('墨离')
    p.start()
