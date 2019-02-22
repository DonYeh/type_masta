from word_bank import word_bank
from compare import compare
from pygame.locals import *
import requests
import sys
import pygame


def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    font = pygame.font.Font(None, 50)

    # input_box = pygame.Rect(250, 250, 140, 32)

    screen = pygame.display.set_mode((width, height))
    typed_letter = ""
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    color_correct = (128, 255, 0)  # green
    color_incorrect = (204, 0, 0)  # red

    # Game initialization

    word_to_spell = word_bank()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handlings
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    typed_letter = event.unicode
                    print(word_to_spell)
                    print(typed_letter)
                    # take the letter from user input (event.unicode) and compare it to the
                    # corresponding letter in the word_to_spell
                    if compare(typed_letter, word_to_spell[0]):
                        print("YEAAAAAASSSS")
                    else:
                        print("you suck again!")
                elif event.key == pygame.K_BACKSPACE:
                    typed_letter = typed_letter[:-1]
                elif event.key == pygame.K_RETURN:
                    print(typed_letter)
                    typed_letter = ""
                    word_to_spell = word_bank()

                elif event.type == pygame.QUIT:
                    stop_game = True

        screen.fill((0, 0, 0))

        # Render text
        # block = font.render(typed_letter, True, (0, 0, 255))

        # call word_bank to generate a random word
        block = font.render(word_to_spell, True, (0, 0, 255))

        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        # pygame.draw.rect(screen, (255, 255, 255), input_box)

        # Blit the input_box rect.
        # pygame.draw.rect(screen, (255, 255, 255), input_box, 2)
        pygame.display.flip()

        # Game logic

        # Draw background
        # screen.fill(blue_color)
        pygame.display.update()

        # Game display

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
