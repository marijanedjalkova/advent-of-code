class Point:

    def __init__(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def get_pos_at_time(self, time=0):
        return self.x + time * self.x_velocity, self.y + time * self.y_velocity

