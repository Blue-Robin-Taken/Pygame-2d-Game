import pygame
import sys
import tile
from player import Player

# maps
from PygameGame.Maps import map1

pygame.init()

windowResize = pygame.surface.Surface((96 * 2, 54 * 2))
screen = pygame.display.set_mode((96 * 2, 54 * 2), pygame.RESIZABLE)
vec = pygame.math.Vector2


def loadMap(group):
    mapList = map1.list
    for i in range(len(mapList)):
        newTile = tile.Tile(mapList[i][1], mapList[i][0])
        newTile.add(group)


def main():
    alivePygame = True
    mapGroup = pygame.sprite.Group()
    loadMap(mapGroup)
    player = Player([0.0, 0.0])
    clock = pygame.time.Clock()
    while alivePygame:
        dt = clock.tick(60) / 1000

        # Player presses space
        playerKeyDown = False
        playerRight = False
        playerLeft = False

        # Collisions
        collideRects = []
        for i in mapGroup:
            collideRects.append(i)

        # If the player closes the window
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playerKeyDown = True
        # Player movement
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_LEFT]:
            playerLeft = True
        if keysPressed[pygame.K_RIGHT]:
            playerRight = True

        # Background color
        windowResize.fill((75, 177, 211))

        # The map/tilemap group drawn to the resize

        mapGroup.draw(windowResize)
        mapGroup.update(surf=windowResize, debug=False)

        # Player shown to the screen
        windowResize.blit(player.image, (player.rect.x, player.rect.y))

        # updating player
        player.update(dt, collideRects, playerKeyDown, {'left': playerLeft, 'right': playerRight}, True, windowResize)

        # Scale windowResize to the screen
        screen.blit(pygame.transform.scale(windowResize, (screen.get_width(), screen.get_height())), (0, 0))

        pygame.display.update()


if __name__ == '__main__':
    main()
