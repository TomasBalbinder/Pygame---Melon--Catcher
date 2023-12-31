import pygame
import random

pygame.init()

#screen
widht = 1280
height = 800
screen = pygame.display.set_mode((widht, height))
pygame.display.set_caption('Melons Catcher')
snow_img = pygame.image.load('snowman.png')
pygame.display.set_icon(snow_img)

#title_text
load_font= pygame.font.SysFont('stencil',40)
title = load_font.render('Melons Catcher', True, 'gold')
title_rect = title.get_rect()
title_rect.center = (widht //2, 40)

#quit game text
quitgame_font= pygame.font.SysFont('stencil',80)

#character_img
char_img = pygame.image.load('warrior.PNG').convert_alpha()
char_size = char_img.get_size()
char_rect = char_img.get_rect()
char_rect.center = (char_size[0], height // 2)

#moving
char_moving = 20
fruit_moving = 7

#fruit_img
fruit_img = pygame.image.load('fruit.PNG').convert_alpha()
fruit_size = fruit_img.get_size()
fruit_rect = fruit_img.get_rect()
fruit_rect.center = (widht, random.randint(100 + (fruit_size[1]//2), height - (fruit_size[1]//2)))

#heart_img
heart_img = pygame.image.load('heart.png').convert_alpha()
heart_rect = heart_img.get_rect()
heart_rect.center = (widht - 100 ,40)

heart_img1 = pygame.image.load('heart.png').convert_alpha()
heart_rect1 = heart_img1.get_rect()
heart_rect1.center = (widht - 140 ,40)

heart_img2 = pygame.image.load('heart.png').convert_alpha()
heart_rect2 = heart_img2.get_rect()
heart_rect2.center = (widht - 180 ,40)

#sounds
pygame.mixer.music.load('hero.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.04)
punch_sound = pygame.mixer.Sound("punch.mp3")
lost_melone_sound = pygame.mixer.Sound('lost_melone.wav')

#quit_game text
quitgame_text = quitgame_font.render(f"QUIT GAME",True, 'gold')
quitgame_rect = quitgame_text.get_rect()
quitgame_rect.center = (widht//2, height//2)

playagin_text = load_font.render(f"Do you want to play again? press SPACE",True, 'gold')
playagin_rect = playagin_text.get_rect()
playagin_rect.center = (widht//2, height//2 + 100)

#win_game text
wngame_text = quitgame_font.render(f"You WON",True, 'gold')
wngame_rect = quitgame_text.get_rect()
wngame_rect.center = (widht//2 + 30, height//2)

#score
score = 0
life = 3
win_bar = 15

#FPS
fps = 60
clock = pygame.time.Clock()

#shows text when won or lose
def end_game(life):   
    screen.fill('black')
    score_rect.center = (widht//2, height//2 - 100)
    screen.blit(score_text, score_rect)
    screen.blit(playagin_text, playagin_rect)
    if life == 0:
        screen.blit(quitgame_text, quitgame_rect)
    else:
        screen.blit(wngame_text, wngame_rect)
    pygame.mixer.music.stop()
    pygame.display.update()


# infinit loop for end win or loose game
def infinit_loop(life, score, loop, win_bar, fruit_moving):
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                loop = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            life = 3
            score = 0
            win_bar = 15
            fruit_moving = 7
            heart_img.set_alpha(255)
            heart_img1.set_alpha(255)
            heart_img2.set_alpha(255)
            pygame.mixer.music.play()        
            pause = False 
    return life, score, loop, win_bar, fruit_moving

loop = True
while loop:
    loop1 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    screen.fill('black')
    screen.blit(heart_img,heart_rect)
    screen.blit(heart_img1,heart_rect1)
    screen.blit(heart_img2,heart_rect2)
    screen.blit(char_img,char_rect)
    screen.blit(fruit_img, fruit_rect)
    screen.blit(title, title_rect)

    pygame.draw.line(screen,'gold',(0,70),(widht,70),3)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and char_rect.top >100:
        char_rect.y -= char_moving

    if keys[pygame.K_s] and char_rect.bottom < height:
        char_rect.y += char_moving

    if keys[pygame.K_a] and char_rect.left > 0:
        char_rect.x -= char_moving

    if keys[pygame.K_d] and char_rect.right < widht//2:
        char_rect.x += char_moving

    score_text = load_font.render(f"Score: {score}",True, 'gold')
    score_rect = score_text.get_rect()
    score_rect.center = (150, 40)
    screen.blit(score_text, score_rect)

    pygame.draw.rect(screen,'green',(widht - (win_bar),75,win_bar,10))

    fruit_rect.x = fruit_rect.x - fruit_moving
    if char_rect.colliderect(fruit_rect):
        win_bar = win_bar + 15
        punch_sound.play() 
        fruit_moving = fruit_moving + 0.3                                                                
        score = score + 1
        fruit_rect.center = (widht, random.randint(100 + (fruit_size[1]//2), height - (fruit_size[1]//2)))
        if win_bar >= widht:
            end_game(life)
            life, score, loop, win_bar, fruit_moving = infinit_loop(life, score, loop, win_bar, fruit_moving)
       
    elif fruit_rect.x < 0:
        lost_melone_sound.play()
        life = life - 1
        if life == 2:
            heart_img.set_alpha(0)       
        elif life == 1:
            heart_img1.set_alpha(0)           
        elif life == 0:
            heart_img2.set_alpha(0)
            end_game(life)
            life, score, loop, win_bar, fruit_moving = infinit_loop(life, score, loop, win_bar, fruit_moving)
        fruit_rect.center = (widht, random.randint(100 + (fruit_size[1]//2), height - (fruit_size[1]//2)))  
    pygame.display.update()
    clock.tick(fps)
pygame.quit()

    