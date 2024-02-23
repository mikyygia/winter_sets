class Collection:
    def __init__(self, values):
        self._values = values

    def __eq__(self, other) -> bool:
        if type(other) is Collection:
            for x in range(min(len(self._values), len(other._values))):
                if self._values[x] != other._values[x]:
                    return False

            return len(self._values) == len(other._values)

        return False


set1 = (0, 3, 6, 9, 12)
a = Collection(set1)

set2 = [0, 3, 6, 9, 12]
b = Collection(set2)

print(a == b)
