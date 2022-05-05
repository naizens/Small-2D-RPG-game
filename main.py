import pygame, sys, os
from settings import Settings
from level import Level
#from debug import debug


class Game(object):
    def __init__(self) -> None:
        super().__init__()
        os.environ["SDL_VIDEO_WINDOW_CENTERED"] = "10,50"


        pygame.init()
        pygame.display.set_caption(Settings.title)

        self.screen = pygame.display.set_mode((Settings.width, Settings.heigth))
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        self.running = True

        self.screen.fill("black")
        self.clock.tick(Settings.fps)

        self.update()
        self.draw()
        
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
            

        pygame.quit()
        sys.exit()
   

    def update(self):
        self.level.update()

    def draw(self):
        self.level.draw()


if __name__ == "__main__":
    game = Game()
    game.run()