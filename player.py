import pygame

pygame.init()
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        # --- init variables ---
        self.gravity = 5
        self.position = position
        self.image = pygame.image.load("Assets/Player.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.gravity = 9.807
        self.dx = 0
        self.dy = 0
        self.max_velocity = 500
        self.maxJumps = 1
        self.jumpAmount = 0
        self.friction = 1
        self.maxAcceleration = 30

    def update(self, dt, collideRect, isJump, movement: dict, debug: bool, surface):
        collisions = 0
        self.velocity = [0, 0]
        for rect in reversed(collideRect):  # rect is really the tile
            checkRect = (self.rect.x, self.rect.y + 1, self.image.get_width(), self.image.get_height())
            if rect.rect.colliderect(checkRect):
                collisions += 1
                self.jumpAmount = 0
        if collisions <= 0:
            self.acceleration[1] += self.gravity

        if movement['right']:
            self.velocity[0] += 100
            self.acceleration[0] += 1
        elif movement['left']:
            self.velocity[0] -= 100
            self.acceleration[0] -= 1
        else:
            if self.acceleration[0] > 0:
                self.acceleration[0] -= self.friction
            elif self.acceleration[0] < 0:
                self.acceleration[0] += self.friction
        for rect in collideRect:  # rect is really the tile
            dy = self.velocity[1] * dt + 0.5 * self.acceleration[1] * dt ** 2
            dx = self.velocity[0] * dt + ((0.5 * self.acceleration[0]) * (
                    dt ** 2))
            fakeRect = (self.position[0], self.position[1] + dy, self.image.get_width(), self.image.get_height())
            if rect.rect.colliderect(fakeRect):
                if self.acceleration[1] < 0:
                    self.velocity[1] = 100
                    self.acceleration[1] = 100
                    self.position[1] = rect.rect.bottom
                elif self.velocity[1] >= 0:
                    self.velocity[1] = 0
                    self.acceleration[1] = 0
                    self.position[1] = rect.rect.top - self.image.get_width()
            fakeRect = (self.position[0] + dx, self.position[1], self.image.get_width(), self.image.get_height())
            if rect.rect.colliderect(fakeRect):
                if self.velocity[0] > 0:
                    self.position[0] = rect.rect.left - self.image.get_width()
                    self.velocity[0] = 0
                    self.acceleration[0] = 0
                elif self.velocity[0] < 0:
                    self.position[0] = rect.rect.right
                    self.velocity[0] = 0
                    self.acceleration[0] = 0

                print(self.acceleration[1])

        if isJump and self.jumpAmount <= self.maxJumps:
            self.jumpAmount += 1
            self.velocity[1] = 0
            self.acceleration[1] = -200
            # self.gravity = 9.807
        self.velocity[1] += self.acceleration[1]
        self.velocity[0] += self.acceleration[0]

        if self.velocity[1] > self.max_velocity:
            self.velocity[1] = self.max_velocity
        if self.acceleration[0] > self.maxAcceleration:
            self.acceleration[0] = self.maxAcceleration
        self.dx = self.velocity[0] * dt + ((0.5 * self.acceleration[0]) * (
                dt ** 2))  # https://www.khanacademy.org/science/physics/one-dimensional-motion/kinematic-formulas/a/what-are-the-kinematic-formulas?modal=1&referrer=upsell

        self.dy = self.velocity[1] * dt + 0.5 * self.acceleration[1] * dt ** 2
        self.position[0] += self.dx
        self.position[1] += self.dy

        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
