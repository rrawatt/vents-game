import pygame
from pygame.locals import *

skyblue = (140, 206, 235)
skyblue5 = (100, 125, 255)
lightgreen = (144, 238, 144)
lightcoral = (240, 128, 128)
lightpurple=(203, 195, 227)
lemonyellow=(241,235,156)
yellow=(255,150,0)
bluegreen = (8, 143, 143)
lightbrown=(196, 164, 132)
brown=(150,75,0)
darkbrown=(92, 64, 51)
cloud=(123,123,123)
slate=(192, 194, 201)

class Die:

    def __init__(self):
        self.rect = pygame.Rect(370, 700, 60, 60)
        self.value = 1

    def draw_button(self, WIN):
        color = lightbrown
        pygame.draw.rect(WIN, color, self.rect, border_radius=10)
        border_thickness = 5
        pygame.draw.rect(WIN, brown, self.rect, border_thickness, border_radius=10)

        if self.value == 1:
            dot_rect = pygame.Rect(self.rect.centerx - 5, self.rect.centery - 5, 10, 10)
            pygame.draw.rect(WIN, darkbrown, dot_rect, border_radius=1)
        elif self.value == 2:
            dot_rect1 = pygame.Rect(self.rect.left + 10, self.rect.centery - 5, 10, 10)
            dot_rect2 = pygame.Rect(self.rect.right - 20, self.rect.centery - 5, 10, 10)
            pygame.draw.rect(WIN, darkbrown, dot_rect1, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect2, border_radius=1)
        elif self.value == 3:
            dot_rect1 = pygame.Rect(self.rect.left + 10, self.rect.centery - 5, 10, 10)
            dot_rect2 = pygame.Rect(self.rect.centerx - 5, self.rect.centery - 5, 10, 10)
            dot_rect3 = pygame.Rect(self.rect.right - 20, self.rect.centery - 5, 10, 10)
            pygame.draw.rect(WIN, darkbrown, dot_rect1, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect2, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect3, border_radius=1)
        elif self.value == 4:
            dot_rect1 = pygame.Rect(self.rect.left + 15, self.rect.centery - 15, 10, 10)
            dot_rect2 = pygame.Rect(self.rect.right - 25, self.rect.centery - 15, 10, 10)
            dot_rect3 = pygame.Rect(self.rect.left + 15, self.rect.centery + 5, 10, 10)
            dot_rect4 = pygame.Rect(self.rect.right - 25, self.rect.centery + 5, 10, 10)
            pygame.draw.rect(WIN, darkbrown, dot_rect1, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect2, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect3, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect4, border_radius=1)
        elif self.value == 5:
            dot_rect1 = pygame.Rect(self.rect.left + 10, self.rect.centery - 20, 10, 10)
            dot_rect2 = pygame.Rect(self.rect.right - 20, self.rect.centery - 20, 10, 10)
            dot_rect3 = pygame.Rect(self.rect.centerx - 5, self.rect.centery -5, 10, 10)
            dot_rect4 = pygame.Rect(self.rect.left + 10, self.rect.centery + 10, 10, 10)
            dot_rect5 = pygame.Rect(self.rect.right - 20, self.rect.centery + 10, 10, 10)
            pygame.draw.rect(WIN, darkbrown, dot_rect1, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect2, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect3, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect4, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect5, border_radius=1)
        elif self.value == 6:
            dot_rect1 = pygame.Rect(self.rect.left + 10, self.rect.centery - 20, 10, 10)
            dot_rect2 = pygame.Rect(self.rect.right - 20, self.rect.centery - 20, 10, 10)
            dot_rect3 = pygame.Rect(self.rect.left + 10, self.rect.centery - 5, 10, 10)
            dot_rect4 = pygame.Rect(self.rect.right - 20, self.rect.centery - 5, 10, 10)
            dot_rect5 = pygame.Rect(self.rect.left + 10, self.rect.centery + 10, 10, 10)
            dot_rect6 = pygame.Rect(self.rect.right - 20, self.rect.centery + 10, 10, 10)
            pygame.draw.rect(WIN, darkbrown, dot_rect1, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect2, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect3, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect4, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect5, border_radius=1)
            pygame.draw.rect(WIN, darkbrown, dot_rect6, border_radius=1)

    def is_hover(self, pos):
        return self.rect.collidepoint(pos)

    def is_clicked(self, pos, click):
        return self.rect.collidepoint(pos) and click
