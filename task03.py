class IncreasingList:
    def __init__(self):
        self._data=[]
    def size(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def pop(self):
        if self.is_empty():
            return self._data
        return self._data.pop()
    def append(self, val):
        i=0
        while (i<self.size()):
            if self._data[i]>val:
                temp=self._data[i]
                self._data[i]=self._data[-1]
                self._data[-1]=temp
                self.pop()
            else: i+=1
        self._data.append(val)

if __name__ == '__main__':
    S = IncreasingList()
    q = int(input())
    for i in range (q):
        command = list(map(str, input().split()))
        if command[0]=="pop": S.pop()
        if command[0]=="append": S.append(int(command[1]))
        if command[0]=="size": print(S.size())