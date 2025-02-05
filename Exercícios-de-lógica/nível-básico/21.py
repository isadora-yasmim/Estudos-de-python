import pygame
pygame.init()
pygame.mixer.init(frequency=44100)
pygame.mixer.music.load('NFR.mp3')#carrega a musica
pygame.mixer.music.play()#da play na musica
while pygame.mixer.music.get_busy():#mantem o programa rodando ate a musica terminar
    pygame.time.Clock().tick(10)#pausa para evitar uso excessivo da cpu