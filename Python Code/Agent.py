import random
import mesa

class Exhaust(mesa.Agent): #An Exhaust agent class

    def __init__(self, pos, model):

        super().__init__(pos,model)
        self.pos = pos
        self.accumulation_size = 1 #all exhaust agents start with an accumulation size of 1

    def move(self): #Defines how exhaust can move in the environment
        possible_movement = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=True)

        new_position = random.choice(possible_movement)

        self.model.grid.move_agent(self, new_position)

    def accumulation(self): #defines how the exhaust accumulates in the environment
        accumulation_prob = 0.65
        accumulation_chance = self.model.grid.get_neighbors(self.pos, moore=True, include_center = False)
        if len(accumulation_chance) > 4: #checks to see how much exhaust agents are next to the agent for it to accumulate
            if self.random.random < accumulation_prob: #chance to accumulate
                self.accumulation_size += 1 #increases the "size" of the exhaust agent


    def step(self):
        self.move()
        self.accumulation()
