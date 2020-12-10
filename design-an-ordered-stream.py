from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.l = [0 for _ in range(n)]
        self.ptr = 0
        self.n = n

    def insert(self, id: int, value: str) -> List[str]:
        self.l[id-1] = value
        res = []
        if id - 1 == self.ptr:
            while self.ptr < self.n and self.l[self.ptr] != 0:
                res.append(self.l[self.ptr])
                self.ptr += 1
        return res



# Your OrderedStream object will be instantiated and called as such:
n = 5

obj = OrderedStream(n)
print(obj.insert(3,"ccccc"))
print(obj.insert(1,"aaaaa"))
print(obj.insert(2,"bbbbb"))
print(obj.insert(5,"eeeee"))
print(obj.insert(4,"ddddd"))