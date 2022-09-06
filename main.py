import pygame
import sys
from button import Button
from paddle import Paddle
from ball import Ball

pygame.init()

# -- soundtrack
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('sounds/soundtrack.wav')
pygame.mixer.music.play()

# -- sound effects
effect = pygame.mixer.Sound('sounds/ballsound.wav')
point = pygame.mixer.Sound('sounds/point.wav')

# -- settings for screen
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Just Another Game of Pong")

# -- colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAROON = (204, 0, 102)
BLUE = (0, 102, 204)

# -- paddles for player A
paddleA = Paddle(BLUE, 10, 100)
paddleA.rect.x = 10
paddleA.rect.y = 200

# -- paddles for player B
paddleB = Paddle(MAROON, 10, 100)
paddleB.rect.x = 680
paddleB.rect.y = 200

# -- ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# -- list of sprites
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# -- clock
clock = pygame.time.Clock()

# player starting scores
scoreA = 0
scoreB = 0


# -- font
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


# -- help-page, gives instructions how to play
def help_play():
    while True:
        help_mouse_pos = pygame.mouse.get_pos()

        screen.fill(WHITE)

        help_text = get_font(25).render("How to Play:", True, "Black")
        help_rect = help_text.get_rect(center=(350, 50))
        screen.blit(help_text, help_rect)

        inst_I = get_font(14).render("Use the arrow keys to control the right paddle.", True, "Black")
        inst_I_rect = inst_I.get_rect(center=(350, 160))
        screen.blit(inst_I, inst_I_rect)
        inst_II = get_font(14).render("Use W and S to control the left paddle.", True, "Black")
        inst_II_rect = inst_II.get_rect(center=(350, 190))
        screen.blit(inst_II, inst_II_rect)
        inst_III = get_font(14).render("Press SPACEBAR to pause and unpause.", True, "Black")
        inst_III_rect = inst_III.get_rect(center=(350, 250))
        screen.blit(inst_III, inst_III_rect)
        inst_IV = get_font(14).render("Press ESCAPE to return to Main Menu.", True, "Black")
        inst_IV_rect = inst_IV.get_rect(center=(350, 280))
        screen.blit(inst_IV, inst_IV_rect)

        help_back = Button(image=None, pos=(350, 460),
                           text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")

        help_back.changeColor(help_mouse_pos)
        help_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if help_back.checkForInput(help_mouse_pos):
                    main_menu()

        pygame.display.update()


# -- main menu with play, help and quit-buttons
def main_menu():
    while True:
        screen.fill(BLACK)

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(35).render("Just another", True, "#b68f40")
        menu_text_2 = get_font(35).render("Game of Pong", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(350, 50))
        menu_rect_2 = menu_text_2.get_rect(center=(350, 100))

        play_button = Button(image=pygame.image.load("assets/button rect.png"), pos=(350, 250),
                             text_input="PLAY", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        help_button = Button(image=pygame.image.load("assets/button rect.png"), pos=(350, 300),
                             text_input="HELP", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/button rect.png"), pos=(350, 350),
                             text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        screen.blit(menu_text, menu_rect)
        screen.blit(menu_text_2, menu_rect_2)

        for button in [play_button, help_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    playmode()
                if help_button.checkForInput(menu_mouse_pos):
                    help_play()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


# -- chose play mode
def playmode():
    while True:
        playmode_mouse_pos = pygame.mouse.get_pos()

        screen.fill(BLACK)

        mode_text = get_font(25).render("Choose play mode", True, "White")
        mode_rect = mode_text.get_rect(center=(350, 50))
        screen.blit(mode_text, mode_rect)

        play1_button = Button(image=pygame.image.load("assets/button rect.png"), pos=(350, 250),
                             text_input="1 PLAYER", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        play2_button = Button(image=pygame.image.load("assets/button rect.png"), pos=(350, 300),
                             text_input="2 PLAYERS", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        for button in [play1_button, play2_button]:
            button.changeColor(playmode_mouse_pos)
            button.update(screen)

        mode_back = Button(image=None, pos=(350, 460),
                           text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        mode_back.changeColor(playmode_mouse_pos)
        mode_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode_back.checkForInput(playmode_mouse_pos):
                    main_menu()
                if play1_button.checkForInput(playmode_mouse_pos):
                    play_cpu()
                if play2_button.checkForInput(playmode_mouse_pos):
                    play()

        pygame.display.update()


# -- GAME LOOPS
def play_cpu(scoreA=0, scoreB=0):
    while True:
        pygame.mixer.music.stop()
        screen.fill("black")
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        # pause text
        pause_text = get_font(50).render("PAUSED", True, "#FFFF00")
        pause_rect = pause_text.get_rect(center=(350, 150))
        continue_text = get_font(20).render("Press SPACEBAR to continue", True, "#FFFF00")
        continue_rect = continue_text.get_rect(center=(350, 230))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.play()
                main_menu()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                while True:
                    event = pygame.event.wait()
                    screen.fill("black")
                    screen.blit(pause_text, pause_rect)
                    screen.blit(continue_text, continue_rect)
                    pygame.display.flip()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        break
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.play()
                        main_menu()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


        # - human player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)

        # - cpu player
        if ball.rect.y > paddleA.rect.y:
            paddleA.moveDown(3)
        if ball.rect.y < paddleA.rect.y:
            paddleA.moveUp(3)

        all_sprites_list.update()

        if ball.rect.x >= 690:
            scoreA += 1
            ball.velocity[0] = -ball.velocity[0]
            point.play()
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
            point.play()
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()
            effect.play()

        all_sprites_list.draw(screen)

        # display scores
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), True, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), True, WHITE)
        screen.blit(text, (420, 10))

        clock.tick(60)

        pygame.display.update()


def play(scoreA=0, scoreB=0):
    while True:
        pygame.mixer.music.stop()
        screen.fill("black")
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        # pause text
        pause_text = get_font(50).render("PAUSED", True, "#FFFF00")
        pause_rect = pause_text.get_rect(center=(350, 150))
        continue_text = get_font(20).render("Press SPACEBAR to continue", True, "#FFFF00")
        continue_rect = continue_text.get_rect(center=(350, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.play()
                main_menu()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                while True:
                    event = pygame.event.wait()
                    screen.fill("black")
                    screen.blit(pause_text, pause_rect)
                    screen.blit(continue_text, continue_rect)
                    pygame.display.flip()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        break
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.play()
                        main_menu()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)

        all_sprites_list.update()

        if ball.rect.x >= 690:
            scoreA += 1
            ball.velocity[0] = -ball.velocity[0]
            point.play()
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
            point.play()
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()
            effect.play()

        all_sprites_list.draw(screen)

        # display scores
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), True, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), True, WHITE)
        screen.blit(text, (420, 10))

        clock.tick(60)

        pygame.display.update()


if __name__ == '__main__':
    main_menu()
