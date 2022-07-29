import pygame
import os

assetList = list()
for asset in os.listdir(os.path.relpath("MapAssets")):
    assetList.append(pygame.image.load(os.path.relpath("MapAssets") + "/" + asset))


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, image):
        super().__init__()
        self.x = position[0]
        self.y = position[1]
        self.image = assetList[image]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.otherRect = pygame.rect.Rect((self.x, self.y + self.image.get_height() / 2),
                                          (self.image.get_width(), self.image.get_height() / 2))
        # otherRect is used to calculate collisions from the bottom of the tile
        # self.leftRect = pygame.rect.Rect((self.x, self.y + 2),(self.image.get_width() / 3, self.image.get_height() / 1.5))
        # leftRect is used to calculate collisions from the left of the tile
        # self.rightRect = pygame.rect.Rect((self.x + self.image.get_width() / 3, self.y + 2),(self.image.get_width() / 2, self.image.get_height() / 1.5))
        # rightRect is used to calculate collisions from the right of the tile
        self.topRect = pygame.rect.Rect((self.x, self.y),
                                        (self.image.get_width(), self.image.get_height() / 2))

    def update(self, surf, debug):
        if debug:
            pass
            pygame.draw.rect(surf, (181, 177, 178), self.topRect)
            pygame.draw.rect(surf, (173, 169, 183), self.otherRect)
