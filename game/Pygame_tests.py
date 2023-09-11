import pygame
import os
from typing import Dict, Tuple, NamedTuple, Any
import sys
import Locations
from pygame.locals import *

# Pygame setup
# Initialize Pygame
pygame.init()
running = True

# Build game path
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

# Set frame rate
clock = pygame.time.Clock()
clock.tick(60)

# Constants
WHITE = [255, 255, 255]
GRAY = [80, 80, 80]

# Load images
BACKGROUND = pygame.image.load(os.path.join(IMAGE_FOLDER, "Background.png"))
TILE = pygame.image.load(os.path.join(IMAGE_FOLDER, "New_white_tile.png"))

# Initialize game screen
screen = pygame.display.set_mode(BACKGROUND.get_size())


class Tile(NamedTuple):
    size: Tuple[int, int]


st_tile = Tile((77, 67))


# Class for the locations (Tiles)
class Tile(pygame.sprite.Sprite):
    def __init__(self, adr: tuple[int, int], horiz: int = TILE.get_width() // 2, vert: int = TILE.get_height() // 2,
                 filename: str = "tile_new_white.png"):
        pygame.sprite.Sprite.__init__(self)
        # Open image file
        self.adr = adr
        self.image = pygame.image.load(os.path.join(IMAGE_FOLDER, filename))
        self.image_hover = pygame.image.load(os.path.join(IMAGE_FOLDER, "tile_new_gray2.png"))
        self.image_click = pygame.image.load(os.path.join(IMAGE_FOLDER, "tile_new_red.png"))
        self.image_unhover = self.image
        self.surf = pygame.Surface(self.image.get_size())

        self.horiz = horiz  # H position of the tile
        self.vert = vert  # V position of the tile
        # Create rectangular from image
        self.rect = self.surf.get_rect(center=(self.horiz, self.vert))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def isPressed(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # MOUSE... events have an event.pos attribute (the mouse position)
            # which you can pass to the collide point method of the rect.
            if self.rect.collidepoint(event.pos):
                self.image = self.image_click

    def hoveredOVer(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.image = self.image_hover
            else:
                self.image = self.image_unhover


def tileCreator(scr_width: int = BACKGROUND.get_width(), scr_height: int = BACKGROUND.get_height(),
                tile_size: NamedTuple = st_tile) -> list:
    def coordCalc():
        tile_holder = []
        vert_coordinates = [x * 39 for x in range(20)]
        horiz_coordinates = [x * 69 for x in range(17)]
        # vert_coordinates = [0, 39, 78, 117, 155, 194, 232, 272, 310, 349, 388, 427, 465, 504, 543, 582, 620, 659, 698,
        #                     737, 775, 814, 852]  # List of vertical coordinates
        # horiz_coordinates = [0, 69, 138, 203, 270, 338, 405, 472, 540, 607, 673, 741, 808, 875, 942, 1009, 1076, 1144,
        #                      1211, 1278]  # List of horizontal coordinates
        for col in range(0, len(horiz_coordinates), 2):
            for row in range(0, len(vert_coordinates), 2):
                tile_holder.append(Tile(adr=(col, row), horiz=horiz_coordinates[col], vert=vert_coordinates[row]))
        for col in range(1, len(horiz_coordinates), 2):
            for row in range(1, len(vert_coordinates), 2):
                tile_holder.append(Tile(adr=(col, row), horiz=horiz_coordinates[col], vert=vert_coordinates[row]))

        return tile_holder

    return coordCalc()


# Create dictionary with tiles
tile_h = tileCreator()

# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         mouseX, mouseY = pygame.mouse.get_pos()
#         if event.type == pygame.QUIT:
#             running = False
#             pygame.quit()
#             sys.exit()
#         for item in tile_h:
#             item.hoveredOVer(event)
#             item.isPressed(event)
#
#     # Place background
#     screen.blit(BACKGROUND, (0, 0))
#     for item in tile_h:
#         item.draw(screen)
#
#     # RENDER YOUR GAME HERE
#
#     # flip() the display to put your work on screen
#     pygame.display.flip()
