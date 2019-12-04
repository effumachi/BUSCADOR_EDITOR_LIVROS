import os
import pygame
surface = pygame.display.set_mode((500, 500), 0, 32)
#surface.fill((255, 255, 255))
#pygame.draw.circle(surface, (0, 0, 0), (10, 10), 15, 0)
pygame.display.update()
pygame.image.save(os.path.expanduser("pic.png"))