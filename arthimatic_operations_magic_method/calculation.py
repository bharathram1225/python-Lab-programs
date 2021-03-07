
class Operation:
    def __init__(self):
        self.listss=[]

    def accept(self):
        n = int(input("Enter the size of the list: "))
        for i in range(n):
            self.listss.append(int(input("Enter the element: ")))

    def __add__(self, num2):
        newlist = []
        for i in range(len(self.listss)):
            newlist.append(self.listss[i]+num2.listss[i])
        return newlist

    def __sub__(self, num2):
        newlist = []
        for i in range(len(self.listss)):
            newlist.append(self.listss[i]-num2.listss[i])
        return newlist

    def __mul__(self, num2):
        newlist = []
        for i in range(len(self.listss)):
            newlist.append(self.listss[i]*num2.listss[i])
        return newlist

    def __floordiv__(self, num2):
        newlist = []
        for i in range(len(self.listss)):
            newlist.append(self.listss[i]//num2.listss[i])
        return newlist




