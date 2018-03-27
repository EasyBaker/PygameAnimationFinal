#Nathan Blouse
#Best Game


# Imports
import pygame
import random
import intersects

repeat = False
#Initialize game engine
pygame.init()

#Sound
pygame.mixer.music.load("Storm_exclamation.wav")
pygame.mixer.Sound('creepy.wav').play()

#Image
knuckles = pygame.image.load('knuckles.png')
rock = pygame.image.load('meteor.png')
heart = pygame.image.load('heart.png')
background = pygame.image.load('background.png')
barnstar = pygame.image.load('barnstar.png')
goldstar = pygame.image.load('goldstar.png')

# Window
SIZE = (800, 600)
TITLE = "Falling Sky"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (75, 200, 255)
DARK_BLUE = (0, 0, 100)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
NOT_QUITE_DARK_GRAY = (100, 100, 100)
YELLOW = (200, 200, 100)
BLACK = (0, 0, 0)

meteor = []
def draw_meteor():
    if repeat == False:
        num_meteors = 8
    elif repeat == True:
        num_meteors = random.randrange(2, 6)
    for i in range(num_meteors):
            x = random.randrange(0, 800)
            y = random.randrange(-50, 100)
            point = [x, y, 30, 30]
            meteor.append(point)

def draw_meteors(meteor):
    x = meteor[0]
    y = meteor[1]

    screen.blit(rock, (x, y))

star = []
num_stars = 50
def draw_star():
    for i in range(num_stars):
            u = random.randint(1,2)
            x = random.randrange(0, 800)
            y = random.randrange(1, 520)
            end = [x, y, 30, 30, u]
            star.append(end)

def draw_stars(stars):
    x = star[0]
    y = star[1]
    l = star[4]

    if star[4] == 1:
        screen.blit(barnstar, (x, y))
    elif star[4] == 2:
        screen.blit(goldstar, (x, y))

# Block
player = [375, 525, 25, 25]
knuck = [340, 510, 25, 25]
p_vel = [0, 0]
p_speed = 10

def draw_hearts():
    global hearts

    heart1 = [25, 25, 50, 50]
    heart2 = [100, 25, 50, 50]
    heart3 = [175, 25, 50, 50]

    hearts = [heart1, heart2, heart3]

stormy = True
draw_hearts()
draw_meteor()
count = 0
deaths = 0
lightning_timer = 0
# Game loop
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    state = pygame.key.get_pressed()
        
    left = state[pygame.K_a]
    right = state[pygame.K_d]

    if left:
        p_vel[0] = -p_speed
    elif right:
        p_vel[0] = p_speed
    else:
        p_vel[0] = 0


    #Game Logic
    ''' move the block in horizontal direction '''
    player[0] += p_vel[0]
    knuck[0] += p_vel[0]

    for p in player:
        if player[0] > 800:
            player[0] = 1
        elif knuck[0] > 800:
            knuck[0] = 1
        elif player[0] < 0:
            player[0] = 799
        elif knuck[0] < 0:
            knuck[0] = 799

    for m in meteor:
        if intersects.rect_rect(player, m):
            meteor.remove(m)
            deaths += 1
            if deaths == 1:
                del hearts[2]
            elif deaths == 2:
                del hearts[1]
            elif deaths == 3:
                del hearts[0]

        
    ''' move the meteors in vertical direction '''
    for m in meteor:
        m[1] += 2
        if m[1] >= 610:
                m[0] = random.randrange(0, 800)
                m[1] = random.randrange(-50, 100)
                count += 1

    for m in meteor:
        if intersects.rect_rect(player, m):                    
            meteor.remove(m)
            deaths += 1
            if deaths == 1:
                del hearts[2]
            elif deaths == 2:
                del hearts[1]
            elif deaths == 3:
                del hearts[0]

    
    if count == 6:
        repeat = True
        draw_meteor()
        count = 0

    if deaths == 3:
        pygame.quit()

    #Flash picture
    if stormy:
        if random.randrange(0, 150) == 0:
            lightning_timer = 5
        else:
            lightning_timer -= 1
    
    # Drawing code
    if lightning_timer <= 0:
        screen.fill(BLACK)
    elif lightning_timer > 0:
        pygame.mixer.music.play()
        screen.blit(background, (0,0))

    '''pygame.draw.rect(screen, WHITE, player)'''
    screen.blit(knuckles, knuck)

    #Draw Meteor
    for m in meteor:
        draw_meteors(m)

    #Hearts
    for h in hearts:
        screen.blit(heart, h)

    #Stars
    for s in star:
        pygame.draw.rect(Surface, BLUE, s)
        draw_stars(s)
        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
