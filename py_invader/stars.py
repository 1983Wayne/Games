import random

# SIZE is the screen size, a tuple of (x, y) DEFAULT in main.py is (1024 x 768)
star_start_height = -10

# Gets are random value between 0 and SCREEN SIZE for x values
def get_random_x(SIZE):
    return random.randint(0, SIZE[0])


##################################################################

class Star:
    def __init__(self, name, SIZE):
        self.speed = random.randint(1, 4)
        self.size = random.randint(1, 3)
        self.x = get_random_x(SIZE)
        self.y = random.randint(star_start_height, SIZE[1])


    def move_star(self, SIZE):
        self.y += self.speed
        if self.y >= SIZE[1] + 5:
            self.x = get_random_x(SIZE)
            self.y = star_start_height
