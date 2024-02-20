class MultipleSequence:
    def __init__(self, length, multiplier) -> None:
        self.length = length

        if multiplier:
            self.multiplier = multiplier
        else:
            self.multiplier = 1

        self.sequence = tuple(self)

    def __str__(self):
        return f'{self.sequence}'

    def __iter__(self):
        self.curr = 0
        return self

    def __next__(self):
        if self.curr >= self.length:
            raise StopIteration

        else:
            element = self.curr * self.multiplier
            self.curr += 1
            return element

    def __getitem__(self, index):
        return self.sequence[index]


a = MultipleSequence(5, 3)
print(a)
print(a[3])
