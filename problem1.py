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
        # Sequence = multiplier * index
        if type(index) == int:
            return self.multiplier * index

        elif type(index) == slice:
            start = 0 if not index.start else index.start
            stop = self.length if not index.stop else index.stop
            step = 1 if not index.step else index.step

            if stop > self.length:
                raise IndexError

            if stop < 0:
                stop = self.length + stop

            elif start < 0:
                start = self.length + start

            return tuple(self.multiplier * i for i in range(start, stop, step))


a = MultipleSequence(5, 3)
