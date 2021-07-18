import random

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
light_grass = (167, 209, 61)
dark_grass = (255, 255, 61)
blue = (0, 0, 255)


def rand_col():
    temp = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if temp[0] >= 235 and temp[1] >= 235 and temp[2] >= 235:
        return rand_col()
    else:
        return temp
