import pygame

class Inputs():
    def __init__(self, game) -> None:

        self.game = game

    def keyboard_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                    self.game.running = False

            if keys[pygame.K_w]:
                self.game.level.player.direction.y = -1
            elif keys[pygame.K_s]:
                self.game.level.player.direction.y = 1
            else:
                self.game.level.player.direction.y = 0

            if keys[pygame.K_d]:
                self.game.level.player.direction.x = 1
            elif keys[pygame.K_a]:
                self.game.level.player.direction.x = -1
            else:
                self.game.level.player.direction.x = 0

"""     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            # Checks for events if a key is pressed

                if event.key == pygame.K_UP:
                    self.game.level.player.direction.y = -1
                elif event.key == pygame.K_DOWN:
                    self.game.level.player.direction.y = 1
                elif event.key == pygame.K_LEFT:
                    self.game.level.player.direction.x = -1
                elif event.key == pygame.K_RIGHT:
                    self.game.level.player.direction.x = 1
                
                
            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    self.game.level.player.direction.y = 0
                elif event.key == pygame.K_DOWN:
                    self.game.level.player.direction.y = 0
                elif event.key == pygame.K_LEFT:
                    self.game.level.player.direction.x = 0
                elif event.key == pygame.K_RIGHT:
                    self.game.level.player.direction.x = 0
"""