from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.l = deque()

    def pushFront(self, val: int) -> None:
        self.l.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        self.l.insert(len(self.l) // 2,val)

    def pushBack(self, val: int) -> None:
        self.l.append(val)

    def popFront(self) -> int:
        try:
            return self.l.popleft()
        except IndexError:
            return -1

    def popMiddle(self) -> int:
        try:
            res = self.l[(len(self.l) -1) // 2]
            del self.l[(len(self.l) -1) // 2]
            return res
        except IndexError:
            return -1

    def popBack(self) -> int:
        try:
            return self.l.pop()
        except IndexError:
            return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
obj = FrontMiddleBackQueue()
obj.pushFront(1)
obj.pushBack(2)
obj.pushMiddle(3)
obj.pushMiddle(4)
param_4 = obj.popFront()
param_5 = obj.popMiddle()
param_6 = obj.popBack()