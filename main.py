import pygame, sys, os
from settings import Settings
from level import Level
from keyboard_events import Inputs
from debug import debug


class Game(object):
    def __init__(self) -> None:
        super().__init__()
        os.environ["SDL_VIDEO_WINDOW_CENTERED"] = "10,50"


        pygame.init()
        pygame.display.set_caption(Settings.title)

        self.screen = pygame.display.set_mode((Settings.width, Settings.heigth))
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.input_manager = Inputs(self)

    def run(self):
        self.running = True
        while self.running == True:

            self.clock.tick(Settings.fps)
            self.screen.fill("black")
            self.update()
            self.draw()
            

            debug(self.level.player.direction)


            pygame.display.update()
            

        pygame.quit()
        sys.exit()
   

    def update(self):
        self.level.update()
        self.input_manager.keyboard_input()

    def draw(self):
        self.level.draw()


if __name__ == "__main__":
    game = Game()
    game.run()