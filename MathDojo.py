class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self
    
    def subtract1(self, num, *nums):
        self.result = num
        for n in nums:
            self.result -= n
        return self
    
    def resultado(self):
        print (self.result)
        return self

md = MathDojo()
md1 = MathDojo()
md2 = MathDojo()
md3 = MathDojo()
md4 = MathDojo()
md5 = MathDojo()
md6 = MathDojo()

md.add(2,4).resultado()
md1.add(5,6).resultado()
md2.add(7,8,6).resultado()
md3.subtract1(9,5).resultado()
md4.subtract1(9,2).resultado()
md5.subtract1(7,3,1).resultado()

x = md6.add(2).add(2,5,1).subtract(3,2).resultado()
print(x)

