class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return False

        return (self.name == other.name) and (self.age == other.age)


class Student(Person):
    def __init__(self, name, age, major) -> None:
        super().__init__(name, age)
        self.major = major

    def __eq__(self, other: object) -> bool:
        return (super().__eq__(other)) and (self.major == other.major)
