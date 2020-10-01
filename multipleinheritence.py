class A(object):
    def __init__(self):
        super().__init__()
        self.a = 'a'
        print(self.a)


class B(object):
    def __init__(self):
        super().__init__()
        self.b='b'
        print(self.b)


class C(B,A):
    def __init__(self):
        super().__init__()
        self.c = 'c'
        print(self.c)


c = C()
