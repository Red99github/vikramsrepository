import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warboat")
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BORDER = pygame.Rect(0, HEIGHT//2 - 10, WIDTH, 10)
HEALTH_FONT = pygame.font.SysFont('timesnewroman', 20)
WINNER_FONT = pygame.font.SysFont('timesnewroman', 25)
FPS = 60
VEL = 5
BULLET_VEL = 5
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 33, 84
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('warboatgame', 'Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('warboatgame', 'Assets', 'explosion.mp3'))
FANFARE_SOUND = pygame.mixer.Sound(os.path.join('warboatgame', 'Assets', 'fanfare.mp3'))

tutorial_text = HEALTH_FONT.render("NORTH: WASD, SPACE                            SOUTH: ↑↓←→, 0", 1, WHITE)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('warboatgame','Assets', 'rboat.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('warboatgame', 'Assets', 'rboat.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
WATER = pygame.transform.scale(
    pygame.image.load(os.path.join('warboatgame', 'Assets', 'oceanbg.jpg')), (WIDTH, HEIGHT))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(WATER, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(tutorial_text, (0, 250))

    red_health_text = HEALTH_FONT.render("HULL CONDITION: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("HULL CONDITION: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 475))
    WIN.blit(yellow_health_text, (10, 10))


    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, GREY, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, GREY, bullet)

    pygame.display.update()



def yellow_handle_movement(keys_pressed, yellow):
    
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if keys_pressed[pygame.K_a] and yellow.x - VEL > -2: #left
        yellow.x -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.width < 242: #down
        yellow.y += VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.height < WIDTH: #right
        yellow.x += VEL



def red_handle_movement(keys_pressed, red):
    
    if keys_pressed[pygame.K_UP] and red.y - VEL - 8 > 240: #up
        red.y -= VEL
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > -2: #left
        red.x -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.width < HEIGHT: #down
        red.y += VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.height < WIDTH: #right
        red.x += VEL



def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.y += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.y > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.y -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.y < 0:
            red_bullets.remove(bullet)



def main(): 
    red = pygame.Rect(WIDTH//2, 465, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(WIDTH//2, 0, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    red_health = 5
    yellow_health = 5
    

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    
                if event.key == pygame.K_KP_0 and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "SOUTHERN WARBOAT DESTROYED!"

        if yellow_health <= 0:
            winner_text = "NORTHERN WARBOAT DESTROYED!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2 - 23))
    pygame.display.update()
    pygame.time.delay(1750)
    FANFARE_SOUND.play()
    pygame.time.delay(3000)


if __name__ == "__main__":
     main()