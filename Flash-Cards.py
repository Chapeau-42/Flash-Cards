# Import ye libraries
import pygame
import csv
import Window

# Start ye pygame
pygame.init()


# A Main function? Let's get started!
class Deck():
    running = True     # Control the game loop
    window = 0         # Where the Window goes
    frameRate = 0      # How many frames per second?
    clock = 0          # Makes the game go at the frame rate

    # Set things up, have a game loop
    def __init__(self):
        self.running = True
        self.window = Window.Window(700, 500, "Flash Cards")
        self.frameRate = 60
        self.clock = pygame.time.Clock()

        # But soft! What light from yonder game loop breaks?
        while self.running:
            self.running = self.window.update()
            self.clock.tick(self.frameRate)

        # Game loop's over, guys, time to go home
        self.window.close()
        pygame.quit()


# Let's get started!
deck = Deck()