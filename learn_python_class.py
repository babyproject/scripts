def add(self, x, y):
    xy=x+y
    print("the sum is: {}".format(xy))

class example:
    def __init__(self, name):
        self.name=name
        self.val=0
        self.lis=[]
    add2=add
    def power(self, x, y):
        ans=x**2+y**2
        print("the answer is: {}".format(ans))
        self.val=ans
        self.lis.append(ans)

ins=example("math")
ins.add2(32,43)
ins.power(12,34)
print ins.val, ins.lis
