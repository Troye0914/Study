from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    @staticmethod
    def eat(name):
        print(f'{name}，等下吃饭')

    def run(self):
        self.eat(self.name)


if __name__ == '__main__':
    m = MyThread('墨离')
    m.start()
