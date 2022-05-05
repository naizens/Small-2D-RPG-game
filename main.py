import pygame, sys
from settings import *
from debug import *

class Game(object):
    def __init__(self) -> None:
        super().__init__()
        os.environ["SDL_VIDEO_WINDOW_CENTERED"] = "10,50"


        pygame.init()
        pygame.display.set_caption(Settings.title)

        self.screen = pygame.display.set_mode((Settings.width, Settings.heigth))
        self.clock = pygame.time.Clock()

    def run(self):
        self.running = True

        self.screen.fill("black")
        self.clock.tick(Settings.fps)

        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
            

        pygame.quit()
        sys.exit()
   

if __name__ == "__main__":
    game = Game()
    game.run()