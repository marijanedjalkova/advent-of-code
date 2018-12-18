class Cart:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        return "({},{}){}".format(self.x, self.y, self.direction)

    def print_cart(self):
        if self.direction == "UP":
            return "^"
        elif self.direction == "DOWN":
            return "V"
        elif self.direction == "LEFT":
            return "<"
        return ">"


