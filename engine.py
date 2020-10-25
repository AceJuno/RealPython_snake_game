import copy
import pygame
import random
import sys


# Class responsible for running game
# inside you can find functions responsible for running every aspect of the game
class Engine:
    def __init__(self, screen):

        # init of basic variables
        self.snake_colour = 255, 0, 0
        self.background_color = 145, 121, 0
        self.line_colour = 255, 215, 9
        self.food_colour = 0, 255, 0

        self.screen = screen
        self.start = True

        # init of snake
        self.snake_list = []
        self.snake_list.append([50, 2, 22, 22])
        self.snake_list.append([26, 2, 22, 22])
        self.snake_list.append([2, 2, 22, 22])

        # init of food
        self.food_eaten = False
        self.x_food = random.randint(0, 49)
        self.y_food = random.randint(0, 32)
        self.food_pos = [2 + self.x_food * 24, 2 + self.y_food * 24]

        # init of move direction
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = True
        self.moves = [self.move_up, self.move_down, self.move_left, self.move_right]

    def backsetup(self):
        self.screen.fill(self.background_color)
        self.foodappear()

        for i in range(51):
            line = pygame.Rect(i * 24, 0, 2, self.screen.get_size()[1])
            pygame.draw.rect(self.screen, self.line_colour, line)
        for i in range(34):
            line = pygame.Rect(0, i * 24, self.screen.get_size()[0], 2)
            pygame.draw.rect(self.screen, self.line_colour, line)

        if self.start:
            for part in self.snake_list:
                sqr = pygame.Rect(part)
                pygame.draw.rect(self.screen, self.snake_colour, sqr)
            self.start = False
        return False

    def registermove(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.moves[0] = True
                    self.moves[1] = False
                    self.moves[2] = False
                    self.moves[3] = False

                elif event.key == pygame.K_DOWN:
                    self.moves[0] = False
                    self.moves[1] = True
                    self.moves[2] = False
                    self.moves[3] = False

                elif event.key == pygame.K_LEFT:
                    self.moves[0] = False
                    self.moves[1] = False
                    self.moves[2] = True
                    self.moves[3] = False

                elif event.key == pygame.K_RIGHT:
                    self.moves[0] = False
                    self.moves[1] = False
                    self.moves[2] = False
                    self.moves[3] = True
        return self.moves

    def snakemove(self):
        snake_head = self.snake_list[0]
        temp = copy.deepcopy(self.snake_list)
        i = len(self.snake_list) - 1

        while i > 0:
            self.snake_list[i][0] = self.snake_list[i - 1][0]
            self.snake_list[i][1] = self.snake_list[i - 1][1]
            i = i - 1

        if self.moves[0]:
            snake_head[1] = snake_head[1] - 24
        elif self.moves[1]:
            snake_head[1] = snake_head[1] + 24
        elif self.moves[2]:
            snake_head[0] = snake_head[0] - 24
        elif self.moves[3]:
            snake_head[0] = snake_head[0] + 24

        if snake_head[0] == self.food_pos[0] and snake_head[1] == self.food_pos[1]:
            self.food_eaten = True
            self.snake_list.append(temp[-1])

        for part in self.snake_list:
            sqr = pygame.Rect(part)
            pygame.draw.rect(self.screen, self.snake_colour, sqr)

    def foodappear(self):
        if self.food_eaten:
            self.x_food = random.randint(0, 49)
            self.y_food = random.randint(0, 32)
            self.food_pos = [2 + self.x_food * 24, 2 + self.y_food * 24]
            self.food_eaten = False

        sqr = pygame.Rect([2 + self.x_food * 24, 2 + self.y_food * 24, 22, 22])
        pygame.draw.rect(self.screen, self.food_colour, sqr)

    def collisiondetection(self):
        snakehead = self.snake_list[0]

        if snakehead[0] < 0 or snakehead[1] < 0:
            return True
        elif snakehead[0] > 1202 or snakehead[1] > 794:
            return True
        elif len(self.snake_list) == len(set(tuple(row) for row in self.snake_list)):
            return False
        else:
            return True
