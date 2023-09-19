class a():
    def __init__(self,cc, aa = 'aaa'):
        self.aa = aa
        print('init in class:',self.aa)

class b(a):
    def __init__(self,cc, bb):
        super().__init__(cc, aa='aaa')
        self.bb = bb
        self.cc = cc
        print('init in class:', self.bb)
        print(self.cc)

obj_b = b('ccc','bbb',)
print(obj_b.aa)
print(obj_b.bb)
print(obj_b.cc)