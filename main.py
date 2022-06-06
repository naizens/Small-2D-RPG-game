import pygame, sys, os
from settings import Settings
from level import Level
from keyboard_events import Inputs
from menus import StartScreen, PauseScreen, GameOverScreen, WonScreen
from debug import debug


class Game(object):
    def __init__(self) -> None:
        super().__init__()
        os.environ["SDL_VIDEO_WINDOW_CENTERED"] = "10,50"


        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(Settings.title)

        self.screen = pygame.display.set_mode((Settings.width, Settings.heigth))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial Bold", 40)

        self.main_sound = pygame.mixer.Sound(os.path.join(Settings.sound_path, "main_music.wav"))
        self.main_sound.set_volume(0.1)
        self.main_sound.play(loops = -1)
        
        
        self.level = Level(self)
        self.input_manager = Inputs(self)
        
        self.game_starting = True
        self.game_paused = False
        self.gameover = False
        self.won = False
        
        self.start_screen = StartScreen()
        self.pause_screen = PauseScreen()
        self.gameover_screen = GameOverScreen()
        self.won_screen = WonScreen()
        
    def run(self):
        self.running = True
        while self.running == True:
            self.clock.tick(Settings.fps)
            self.input_manager.keyboard_input()
            
            
            if self.game_starting:
                self.start_screen.draw(self.screen)
  
            elif self.game_paused:
                self.pause_screen.draw(self.screen)

            elif self.gameover:
                self.gameover_screen.draw(self.screen)
                
            elif self.won:
                print("Won")
                self.won_screen.draw(self.screen)
            
            else:
                self.screen.fill(Settings.water_color)
                self.draw()
                self.update()
                

            #debug(self.level.player.status)
            
            

            pygame.display.update()
            

        pygame.quit()
        sys.exit()
    
    def update_fps(self):
        self.fps = round(self.clock.get_fps())
        self.fps_text = self.font.render(str(self.fps), True, "white")
        return self.fps_text 

    def update(self):
        self.level.update()
        self.update_fps()

    def draw(self):
        self.level.draw()
        self.level.player.draw()
        self.screen.blit(self.update_fps(), (Settings.width - 50, 10))

if __name__ == "__main__":
    game = Game()
    game.run()