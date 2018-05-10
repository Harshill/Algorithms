class Stack(object):
    def __init__(self, size=50):
        self.items = []
        self.length = 0
        self.size = size

    def __str__(self):
        print(self.items)
        return ''

    def push(self, value):
        if len(self.items) > self.size:
            raise StackOverflowError

        self.items.append(value)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def get_size(self):
        return self.length

    def is_empty(self):
        return not bool(self.items)


class Queue(object):
    def __init__(self, size=50):
        self.items = []
        self.size = size
        self.length = 0

    def __str__(self):
        print(self.items)
        return ''

    def enqueue(self, value):
        if len(self.items) > self.size:
            raise StackOverflowError

        self.items.append(value)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.items.pop(0)

    def get_size(self):
        return self.length

    def peek(self):
        return self.items[0]


class StackOverflowError(BaseException):
    pass
