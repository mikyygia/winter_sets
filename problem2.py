class Collection:
    def __init__(self, values):
        self._values = values

    def __eq__(self, other) -> bool:
        try:
            if not isinstance(other, Collection):
                return False

            if len(self._values) != len(other._values):
                return False

            # Determining whether a Collection of n elements is equivalent to a Collection of m
            for x in range(min(len(self._values), len(other._values))):
                if self._values[x] != other._values[x]:
                    return False

        except Exception as msg:
            raise Exception(msg)

        return True

    def __lt__(self, other):
        if not isinstance(other, Collection):
            return TypeError("Can't compare non-collection types")

        try:
            return list(self._values) < list(other._values)

        except Exception as msg:
            raise Exception(msg)
