import pygame

print('setup start')

pygame.init()

window = pygame.display.set_mode(size=(1280, 720))

print('setup end')

print('setup loop')

while True:
    #event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()