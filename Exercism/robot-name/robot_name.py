import random
import string


class Robot:
    names_used = []

    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
#        random.seed()
        robo_name = random.choice(string.ascii_uppercase) + (random.choice(string.ascii_uppercase))
        for tres_digit in range(3):
            robo_name += str(random.randrange(0, 10))
        if robo_name not in self.names_used:
            self.names_used.append(str(robo_name))
            return robo_name

    def reset(self):
        self.names_used.remove(self.name)
        self.name = self.generate_name()
        return self.name


name_rb = Robot()
name1 = name_rb.name
print("NAME 1: ", name1)
name_rb.reset()
name2 = name_rb.name
random.seed(name2)
print("NAME 2: ", name2)
