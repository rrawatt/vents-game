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

class Cell:
    width = 60
    height = 60

    def __init__(self, i, j, state):
        self.i = i
        self.j = j
        self.state = state
        self.rect = pygame.Rect(100 + self.i * 60, 600 - self.j * 60, self.width, self.height)

    def draw_cell(self, WIN):#rendered column wise (not horizontally)
        color = skyblue if (self.i + self.j) % 2 == 0 else lemonyellow
        pygame.draw.rect(WIN, color, self.rect, border_radius=5)
        border_thickness = 2
        pygame.draw.rect(WIN, bluegreen, self.rect, border_thickness, border_radius=5)
        if self.j % 2 == 0:
            text = str(self.i + 10 * self.j + 1)
        else:
            text = str(9 - self.i + 10 * self.j + 1)

        font = pygame.font.SysFont('Times New Roman', 25)
        text_img = font.render(text, True, skyblue5) if (self.i + self.j) % 2 == 0 else font.render(text, True, yellow)
        text_width = text_img.get_width()
        text_height = text_img.get_height()
        x = 100 + self.i * 60 + 30 - text_width // 2
        y = 600 - self.j * 60 + 30 - text_height // 2

        WIN.blit(text_img, (x, y))


    def draw_vent(self, WIN):
        pygame.draw.rect(WIN, cloud, self.rect, border_radius=5)
        border_thickness = 2
        pygame.draw.rect(WIN, slate, self.rect, border_thickness, border_radius=5)

        # Calculate the y-coordinate for the three lines symmetrically around the square's center
        line_y_center = self.rect.centery
        line_spacing = 15  # Adjust the spacing between lines as needed
        line_length = 30  # Adjust the length of the lines as needed
        curve_radius = 2.5  # Adjust the radius of the curved ends as needed

        # Draw three parallel lines symmetrically around the square
        for i in range(-1, 2):  # -1, 0, 1 for three lines
            line_y = line_y_center + i * line_spacing
            line_start = (self.rect.centerx - line_length // 2, line_y)
            line_end = (self.rect.centerx + line_length // 2, line_y)

            # Draw lines with curved ends
            pygame.draw.line(WIN, slate, line_start, line_end, 5)

            # Add curved ends to the lines
            pygame.draw.circle(WIN, slate, (line_start[0], line_y), curve_radius)
            pygame.draw.circle(WIN, slate, (line_end[0], line_y), curve_radius)