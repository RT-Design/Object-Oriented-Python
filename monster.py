#Intro to inheritance

import random

COLORS = ['yellow', 'red', 'blue', 'green']

class Monster:
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points,self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self,key,value)

    def battlecry(self):

        return self.sound.upper()
        

    
