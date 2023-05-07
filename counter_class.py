# 2. Feladat - Counter osztály (OOP) - 15 Pont


class Counter:

    value = 0
    step = 1

    def __init__(self, value) -> None:
        self.value = value

    def increment(self):
        self.value = self.value + self.step

    def decrement(self):
        self.value = self.value - self.step

    def set_value(self, new_value):
        self.value = new_value

    def set_step(self, new_step):
        self.step = new_step

    def get_value(self):
        print(self.value)


myCounter = Counter(10)
myCounter.increment()
myCounter.increment()
myCounter.get_value()
myCounter.set_step(5)
myCounter.decrement()
myCounter.get_value()
myCounter.set_value(100)
myCounter.increment()
myCounter.get_value()


class ScoreCounter(Counter):

    name = ""
    age = ""
    winner: bool = False

    def __init__(self, value, name, age) -> None:
        super().__init__(value)
        self.name = name
        self.age = age

    def increment(self):
        super().increment()
        if self.value > 11:
            self.winner = True


myScoreCounter = ScoreCounter(10, 'Zsolt', 34)
myScoreCounter.increment()
myScoreCounter.get_value()
myScoreCounter.increment()
myScoreCounter.get_value()
print(myScoreCounter.winner)