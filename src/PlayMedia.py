__author__ = '1002097'

import pygame

class PlayMedia :


    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def playMp3(self,fileName):
        pygame.mixer.music.load('workfile.mp3')
        pygame.mixer.music.play()


py=PlayMedia()
py.playMp3('aa')