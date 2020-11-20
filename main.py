import pygame
from Planes import Plane
from random import randint
from grid import Grid

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
CHECKER_SIZE = 50
STARTING_POSITION = (0, 0)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

NUMBER_OF_CHECKERS = 10
NUMBER_OF_PLANES = 4
REFRESH_RATE = 1

pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

grid = Grid(WINDOW_HEIGHT, CHECKER_SIZE)
clock = pygame.time.Clock()


def fill_screen_grid():
    screen.fill(WHITE)
    for index in range(0, NUMBER_OF_CHECKERS):
        current_coordinate = CHECKER_SIZE * index
        pygame.draw.line(screen, BLACK, (current_coordinate, 0), (current_coordinate, WINDOW_HEIGHT))
        pygame.draw.line(screen, BLACK, (0, current_coordinate), (WINDOW_WIDTH, current_coordinate))


locations = []
collided = False
turns = 0
points = 0


def get_random_checkers():
    return randint(1, NUMBER_OF_CHECKERS - 1) * CHECKER_SIZE, randint(1, NUMBER_OF_CHECKERS - 1) * CHECKER_SIZE


planes_list = pygame.sprite.Group()

for i in range(NUMBER_OF_PLANES):
    x, y = get_random_checkers()
    while (x, y) in locations:
        x, y = get_random_checkers()
    locations.append((x, y))
    planes_list.add(Plane(x, y))

finish = False
game_over = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    fill_screen_grid()
    planes_list.draw(screen)

    if not game_over:
        plane: Plane
        for plane in planes_list:
            if not grid.is_dangerous(plane, planes_list):
                plane.move_plane_randomly(CHECKER_SIZE, grid)
                points += 1
            else:
                index_s1, index_s2 = grid.find_good_checker(plane, planes_list)
                plane.move_plane(index_s1 * CHECKER_SIZE, index_s2 * CHECKER_SIZE)
                points -= 1
        turns += 1
        for plane in planes_list:
            if len(pygame.sprite.spritecollide(plane, planes_list, False)) != 1:
                collided = True

    if collided or turns == 1000:
        game_over = True

        screen.fill(BLACK)
        text = pygame.font.Font(None, 36).render(f'Game Over. POINTS: {points}', True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    pygame.display.flip()
    clock.tick(2)

pygame.quit()
