class MyRange:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration
        else:
            result = self.current
            self.current += self.step
            return result

for i in MyRange(1, 10, 2):
    print(i)
