import pygame
from build_background import Background, Star_Background

class ShmupGUI():
    def __init__(self):

        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init() # for sound
        
        # set window caption
        pygame.display.set_caption("Shmup Game")
        
        # background music
        pygame.mixer.music.load('Music/background.mp3')
        pygame.mixer.music.set_volume(0.01)
        
        # create the display surface object of specific dimension.
        self.width = 600
        self.height = 800
        self.display  = pygame.display.set_mode((self.width, self.height))

        # initialize Clock
        self.FPS = 60
        self.clock= pygame.time.Clock() 


    def start(self):   

        # start music for infinite loop
        pygame.mixer.music.play(loops=-1)

        # background
        star_backgrounds = pygame.sprite.Group()
        star_background_level0 = Background(self.width, self.height)
        star_background_level1 = [Star_Background(self.width, self.height, 1, 40), Star_Background(self.width, self.height, 1, 40, is_alt=True)]
        star_background_level2 = [Star_Background(self.width, self.height, 2, 20), Star_Background(self.width, self.height, 2, 20, is_alt=True)]
        star_backgrounds.add(star_background_level0)
        star_backgrounds.add(star_background_level1)
        star_backgrounds.add(star_background_level2)

        # game loop
        score = 0
        running = True
        while running:
            
            # keep loop running at the right speed
            self.clock.tick(self.FPS)

            # Use the keyboard events for a single action or a step-by-step movement.
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:   
                    running = False

            # update and draw object
            star_backgrounds.update()
            star_backgrounds.draw(self.display)

            # after drawing everything, update the display
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = ShmupGUI()
    game.start()