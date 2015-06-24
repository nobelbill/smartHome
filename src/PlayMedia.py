__author__ = '1002097'

import pygame

class PlayMedia :


    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def playMp3(self,fileName):
        pygame.mixer.music.load('workfile.mp3')
        sound= pygame.mixer.music.play()
        while sound.get_busy():
            pygame.time.delay(100)


py=PlayMedia()
py.playMp3('aa')