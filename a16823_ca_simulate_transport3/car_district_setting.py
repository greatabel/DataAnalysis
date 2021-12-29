import random


class CarSetting:
    def __init__(self, behavior_type):
        self.speedup = random.randint(60, 100)

        self.behavior_type = behavior_type

    def myprint(self):
        print(
            "A car with speedup",
            self.speedup,
            " ",
            ", my behavior_type is ",
            self.behavior_type,
        )
