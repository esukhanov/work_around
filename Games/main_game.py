import sys, pygame
pygame.init()

size = width, height = 840, 720
speed = [2, 2]
black = 0, 0, 0

background_image = pygame.image.load("images/72742_1.jpg")

screen = pygame.display.set_mode(size)

ball = pygame.image.load("images/small-47.jpg")
ballrect = ball.get_rect()
pygame.mixer.music.load("sounds/05. Sad Situation.mp3")
pygame.mixer.music.play(loops=1, start=0.0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(black)

    screen.blit(background_image,(0,0))
    screen.blit(ball, ballrect)
    pygame.display.flip()