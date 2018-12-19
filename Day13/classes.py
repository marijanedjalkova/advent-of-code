class Cart:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.choice_counter = 0
        self.route = [(self.x, self.y)]

    def __repr__(self):
        return "({},{}){}".format(self.x, self.y, self.direction)

    def turn(self, is_left):
        switcher = {
            "^": "<" if is_left else ">",
            "v": ">" if is_left else "<",
            "<": "v" if is_left else "^",
            ">": "^" if is_left else "v"
        }
        return switcher[self.direction]

    def make_step(self, road_map):
        current_square = road_map[self.x][self.y]
        next_square_switcher = {
            "^": (self.x, self.y - 1),
            "v": (self.x, self.y + 1),
            "<": (self.x - 1, self.y),
            ">": (self.x + 1, self.y)
        }
        next_x, next_y = next_square_switcher[self.direction]
        next_square = road_map[next_x][next_y]
        if next_square == "/":
            if current_square == "-":
                new_direction = "^" if self.direction == ">" else "v"
            elif current_square == "|":
                new_direction = ">" if self.direction == "^" else "<"
            elif current_square == "+":
                next_direction_switcher = {
                    "^": ">",
                    "v": "<",
                    "<": "v",
                    ">": "^"
                }
                new_direction = next_direction_switcher[self.direction]
        elif next_square == "\\":
            if current_square == "-":
                new_direction = "v" if self.direction == ">" else "^"
            elif current_square == "|":
                new_direction = "<" if self.direction == "^" else ">"
            elif current_square == "+":
                next_direction_switcher = {
                    "^": "<",
                    "v": ">",
                    "<": "^",
                    ">": "v"
                }
                new_direction = next_direction_switcher[self.direction]
        elif next_square == "+":
            turn_switcher = {
                0: self.turn(True),
                1: self.direction,
                2: self.turn(False)
            }
            new_direction = turn_switcher[self.choice_counter % 3]
            self.choice_counter += 1
        else:
            new_direction = self.direction
        self.x = next_x
        self.y = next_y
        self.direction = new_direction
        self.route.append((self.x, self.y))




