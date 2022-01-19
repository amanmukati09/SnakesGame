import random
import os
import pygame


pygame.mixer.init()

xx = pygame.init()

game_height = 1200
game_width = 600

gameWindow = pygame.display.set_mode((game_height, game_width))
# img = pygame.image.load("s.jpg")
# img = pygame.transform.scale(img, (game_height, game_width)).convert_alpha()

pygame.display.set_caption("Game01")
pygame.display.update()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

if not os.path.exists("highscore.txt"):
    with open("highscore.txt", "w") as f:
        f.write(str(0))

with open("highscore.txt", "r") as f:
    highScore = int(f.read())


def screen_score(text, color, x, y):
    font = pygame.font.SysFont(None, 75)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindows, color, snake_lists, snake_size_bs, snake_size_ls):
    for a, y in snake_lists:
        pygame.draw.rect(gameWindow, color, [a, y, snake_size_ls, snake_size_bs])


clock = pygame.time.Clock()


def welcome():
    exit_game = False
    gameWindow.fill(white)
    screen_score("WELCOME TO SNAKES ", blue, 300, 200)
    screen_score("Press Space to play ", blue, 330, 300)

    pygame.display.update()
    clock.tick(30)

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("m.mp3")
                    pygame.mixer.music.play()
                    game()


def game():
    # variables

    global head, highScore
    snake_list = []
    snake_length = 1

    fps = 60
    score = 0

    exit_game = False
    game_over = False
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, int(game_width / 2))
    food_y = random.randint(20, int(game_height / 2))

    snake_x = 0  # is from top left corner
    snake_y = 0

    snake_size_l = 10
    snake_size_b = 10

    initial_velocity = 3

    while not exit_game:
        if game_over:

            with open("highscore.txt", "w") as fx:
                fx.write(str(highScore))

            gameWindow.fill((25, 156, 67))
            screen_score("Game Over\nPress Enter", white, int(300), int(200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("m.mp3")
                        pygame.mixer.music.play()
                        game()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = + initial_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - initial_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - initial_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = + initial_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 20

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 7:
                score = score + 1
                snake_length += 5
                print("SCORE : ", score)
                food_x: int = random.randint(20, int(game_width / 2))
                food_y = random.randint(20, int(game_height / 2))

            if score > int(highScore):
                highScore = score

            gameWindow.fill((25, 155, 130))
            # gameWindow.blit(img, (0, 0))
            screen_score("SCORE " + str(score) + " High Score : " + str(highScore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size_b, snake_size_l])

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if snake_x < 0 or snake_x > game_width or snake_y < 0 or snake_y > game_height:
                game_over = True
                pygame.mixer.music.load("m.mp3")
                pygame.mixer.music.play()

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("m.mp3")
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snake_list, snake_size_b, snake_size_l)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


# game()
welcome()
