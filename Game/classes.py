import pygame
import colors
from pygame.math import Vector2
from random import randint

cell_size = 40
cell_number = 20


class Food:
    def __init__(self, frontend = True):
        self.x = randint(0, cell_number - 1)
        self.y = randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        if frontend:
            self.pic = pygame.image.load("Graphics/apple.png").convert_alpha()

    # def __init__(self, _):
    #     self.x = randint(0, cell_number - 1)
    #     self.y = randint(0, cell_number - 1)
    #     self.pos = Vector2(self.x, self.y)

    def draw_food(self, gameWindow):
        food_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        gameWindow.blit(self.pic, food_rect)


class Snake:
    def __init__(self, frontend = True):
        self.body = [Vector2(10, 10), Vector2(10, 11), Vector2(10, 12)]
        self.direction = Vector2(0, -1)
        if frontend:
            self.head_up = pygame.image.load("Graphics/head_up.png").convert_alpha()
            self.head_down = pygame.image.load("Graphics/head_down.png").convert_alpha()
            self.head_left = pygame.image.load("Graphics/head_left.png").convert_alpha()
            self.head_right = pygame.image.load("Graphics/head_right.png").convert_alpha()

            self.bod_ver = pygame.image.load("Graphics/body_vertical.png").convert_alpha()
            self.bod_hor = pygame.image.load("Graphics/body_horizontal.png").convert_alpha()

            self.tail_up = pygame.image.load("Graphics/tail_down.png").convert_alpha()
            self.tail_down = pygame.image.load("Graphics/tail_up.png").convert_alpha()
            self.tail_left = pygame.image.load("Graphics/tail_right.png").convert_alpha()
            self.tail_right = pygame.image.load("Graphics/tail_left.png").convert_alpha()

            self.snake_corner1 = pygame.image.load("Graphics/body_bl.png").convert_alpha()
            self.snake_corner2 = pygame.image.load("Graphics/body_br.png").convert_alpha()
            self.snake_corner3 = pygame.image.load("Graphics/body_tr.png").convert_alpha()
            self.snake_corner4 = pygame.image.load("Graphics/body_tl.png").convert_alpha()

            self.head = pygame.image.load("Graphics/head_up.png").convert_alpha()
            self.tail = pygame.image.load("Graphics/tail_up.png").convert_alpha()

            self.crunch_sound = pygame.mixer.Sound("Sound/crunch.wav")

    # def __init__(self, _):
    #     self.body = [Vector2(10, 10), Vector2(10, 11), Vector2(10, 12)]
    #     self.direction = Vector2(0, 0)

    def draw_snake(self, gameWindow):
        self.update_head()
        self.update_tail()
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                gameWindow.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                gameWindow.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    gameWindow.blit(self.bod_ver, block_rect)
                elif previous_block.y == next_block.y:
                    gameWindow.blit(self.bod_hor, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        gameWindow.blit(self.snake_corner4, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        gameWindow.blit(self.snake_corner3, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        gameWindow.blit(self.snake_corner1, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        gameWindow.blit(self.snake_corner2, block_rect)


    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

    def move_snake_backend(self, action):
        if action == "front":
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            temp = Snake(False)
            temp.body = body_copy
            temp.direction = self.direction
            return temp
        elif action == "right":
            new_direction = self.direction.rotate(90)
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + new_direction)
            temp = Snake(False)
            temp.body = body_copy
            temp.direction = new_direction
            return temp
        elif action == "left":
            new_direction = self.direction.rotate(-90)
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + new_direction)
            temp = Snake(False)
            temp.body = body_copy
            temp.direction = new_direction
            return temp

    def change_snake_dir(self, action_index):
        if action_index == 0:
            self.direction = self.direction.rotate(-90)
        elif action_index == 2:
            self.direction = self.direction.rotate(90)
    

    def add_block(self):
        tail_direction = self.body[-2] - self.body[-1]
        new_block = self.body[-1] + tail_direction
        self.body.append(new_block)

    def check_death(self):
        if self.body[0].x > (cell_number - 1) or self.body[0].x < 0 or self.body[0].y > (cell_number - 1) or self.body[0].y < 0:
            return 1
        elif self.body[0] in self.body[1:]:
            return 1
        else:
            return 0

    def update_head(self):
        if self.direction == Vector2(1, 0):
            self.head = self.head_right
        elif self.direction == Vector2(-1, 0):
            self.head = self.head_left
        elif self.direction == Vector2(0, 1):
            self.head = self.head_down
        elif self.direction == Vector2(0, -1):
            self.head = self.head_up

    def update_tail(self):
        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down
