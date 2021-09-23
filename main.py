class FirstCycleBufferClass:
    def __init__(self, length):
        self.buffer = []
        for i in range(length):
            self.buffer.append(0)

    def get_full(self):
        return self.buffer

    def get_last(self):
        return self.buffer[-1]

    def put(self, value):
        self.buffer = self.buffer[1:] + [value]


class SecondCycleBufferClass:

    def __init__(self):
        self.buffer = []
        self.index = 0
        for i in range(10):
            self.buffer.append(0)

    def get_full(self):
        return self.buffer

    def get_last_input(self):
        return self.buffer[self.index]

    def get_by_index(self, i):
        return self.buffer[i]

    def put(self, value):
        self.index += 1
        if self.index >= 10:
            self.index = 0
        self.buffer[self.index] = value
        return self.index
