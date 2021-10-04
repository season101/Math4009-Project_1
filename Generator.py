import random as rand

class Generator:

    def __init__(self, leftRange, rightRange):
        self.ranNums = {}
        self.leftRange = leftRange
        self.rightRange = rightRange
        self.random_generator()

    def random_generator(self):       
        for i in range(0,10000):
            a = rand.randrange(self.leftRange,self.rightRange,1)
            if a not in self.ranNums:
                self.ranNums[a]=1
            else:
                self.ranNums[a]= self.ranNums.get(a)+1

'''
def get_nums(self):
    return list(self.ranNums.keys())

def get_counts(self):
    return list(self.ranNums.values())
    '''