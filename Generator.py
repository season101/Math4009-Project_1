import random as rand

class Generator:

    def __init__(self):
        self.ranNums = {}

    def random_generator(self):       
        for i in range(0,1000):
            a = rand.randrange(-1000,1000,1)
            if a not in self.ranNums:
                self.ranNums[a]=1
            else:
                self.ranNums[a] = self.ranNums.get(a)+1 
            print(((str)(i+1))+" :  "+(str)(a))
        return list(self.ranNums.keys())

    def print_nums(self):
        x = self.random_generator()
        for i in range(0,len(x)):
            print((str)(x[i]) + " " + "count: "+(str) (self.ranNums.get(x[i])))

    def plot_dist(self):
        x_values = self.ranNums.keys()
        y_values = self.ranNums.values()
        return x_values,y_values