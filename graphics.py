import pygame
from tg import *



FPS=50
quitGame=False

pygame.init()
vidInfo = pygame.display.Info()

WIDTH = vidInfo.current_w
HEIGHT = vidInfo.current_h
RESOLUTION = (WIDTH, HEIGHT)
RECT_SIZE = WIDTH * 0.1

SCREEN = pygame.display.set_mode(RESOLUTION)#, pygame.FULLSCREEN)

pygame.event.set_blocked([pygame.USEREVENT, pygame.VIDEOEXPOSE, pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.KEYDOWN, pygame.KEYUP, pygame.VIDEORESIZE, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN, pygame.MOUSEBUTTONUP])

clock = pygame.time.Clock()



clique=0
disclique=0
while not quitGame:

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			quitGame=True
			break
		elif event.type == pygame.MOUSEBUTTONDOWN :
			clique+=1
			clock.tick_busy_loop(FPS*0.1)
			if pygame.event.get(pygame.MOUSEBUTTONDOWN):
				Rect = pygame.Rect(event.pos, (RECT_SIZE, RECT_SIZE))
				Grafo.newV(Rect)
				pygame.Surface.fill(SCREEN,(0,255,0))
				Grafo.mostrarV()
			else:
				pygame.Surface.fill(SCREEN,(255,0,0))
		elif event.type == pygame.MOUSEBUTTONUP:
			disclique-=1

	pygame.display.update()
	
	clique=0
	disclique=0
	clock.tick(FPS)

pygame.quit()



