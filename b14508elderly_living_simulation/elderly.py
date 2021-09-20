import random


class OldMan:
    def __init__(self, behavior_type):
        self.age = random.randint(60, 100)
        
        self.behavior_type = behavior_type
        if behavior_type != 3:
            self.self_help = 'self_help'
        else:
            self.self_help = 'need_care'


    def myprint(self):
        print("I am an old man with age", self.age, " ", self.self_help,
                ", my behavior_type is ", self.behavior_type)


