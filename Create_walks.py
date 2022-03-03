from random import choice

class RandomWalk():
    def __init__(self, numberofpoints = 5000):
        self.numberofpoints = numberofpoints
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):

        while len(self.x_values) < self.numberofpoints:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_distance*x_direction

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_distance*y_direction

            if y_step and x_step == 0:
                pass
            next_x_point = self.x_values[-1] + x_step
            next_y_point = self.y_values[-1] + y_step

            self.x_values.append(next_x_point)
            self.y_values.append(next_y_point)