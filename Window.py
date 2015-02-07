# Import ye libraries
import pygame
import Deck


# ...the window?
class Window():
    screen = 0     # The thing you're displaying stuff on
    screen_width = 0
    screen_height = 0
    deck = 0       # This will be the deck we're waiting for

    # Get things going, do initial display
    def __init__(self, x, y, title):
        # Get things going
        self.screen_width = x
        self.screen_height = y
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(title)

        # Set up the deck
        self.deck = Deck.Deck()

        # Do initial display
        self.display()

    # Do frame-by-frame variable updates, display udates, etc.
    def update(self):
        state = pygame.key.get_pressed()
        self.deck.update(state)

        self.display()
        return self.do_we_exit()     # Return whether or not the game loop is over, for the Engine's use

    # What's new in display land?
    def display(self):
        self.screen.fill((100, 100, 100))

        self.deck.display(self.screen, self.screen_width, self.screen_height)

        pygame.display.flip()

    # Is the game loop over yet?
    def do_we_exit(self):
        verdict = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                verdict = False
        return verdict

    # How we tidy up around here
    def close(self):
        self.screen = pygame.display.quit()