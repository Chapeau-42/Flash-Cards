# Imports
import pygame
import csv
import random


# Here are your flash cards
class Deck():
    cards = []      # This is where the cards go
    order = []      # This is the order you show your cards in
    index = 0       # Which card are we showing?
    card_time = 0   # When did we last
    time_gap = 0    # How long do we wait between card flips?
    font = 0        # What font do we write in?
    font_colour = 0 # What colour do we write in?

    def __init__(self):
        self.cards = []
        self.order = []
        self.index = 0
        self.card_time = pygame.time.get_ticks()
        self.time_gap = 500
        self.font = pygame.font.SysFont("Century Gothic", 40)
        self.font_colour = (50, 50, 100)

        self.load()

    # Get data to put on cards and randomize order
    def load(self):
        # Reset your deck
        self.cards = []
        self.order = []
        self.index = 0

        # Open file
        path = input('Please enter the path to the deck file: ')
        f = open(path, newline='')
        f_reader = csv.reader(f)

        # The deck! Get the deck!
        for row in f_reader:
            for j in range(len(row)):
                self.cards.append(row[j])
                self.order.append(0)

        # Randomize the card order
        for i in range(len(self.cards)):
            j = random.randint(0, len(self.cards)-1)
            while self.order[j] != 0:
                j = random.randint(0, len(self.cards)-1)
            self.order[j] = i

    # Update the card being shown
    def update(self, state):
        time = pygame.time.get_ticks()
        if state[pygame.K_SPACE] != 0 and time > self.card_time + self.time_gap:
            self.index += 1
            self.card_time = time

    # Flashing the Cards
    def display(self, screen, screen_width, screen_height):
        if self.index < len(self.cards):
            screen.fill(self.get_bg())
            text = self.font.render(self.cards[self.order[self.index]], 0, self.font_colour)
        else:
            screen.fill((97, 64, 81))
            text = self.font.render("done!", 0, (150, 200, 150))
        screen.blit(text, (50, 50))

    # What colour do we paint the background?
    def get_bg(self):
        offset = (self.order[self.index] / len(self.cards)) * 20

        return (150 + offset, 150 + offset, 150 + offset)