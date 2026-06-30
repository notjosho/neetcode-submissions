from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self._top = x

    def pop(self) -> int:
        if len(self.q1) == 1:
            self._top = None
            return self.q1.popleft()

        while len(self.q1) > 1:
            if len(self.q1) == 2:
                self._top = self.q1.popleft()
                continue
            self.q2.append(self.q1.popleft())
        self.q2, self.q1 = self.q1, self.q2
        self.q1.append(self._top)
        return self.q2.popleft()

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return self._top is None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()