import requests
import sys
import pygame
from word_bank import word_bank
from compare import compare
# from color_letters import colored_letters
from pygame.locals import *


def main():
    width = 500
    height = 500

    # define colors
    blue = (97, 159, 182)
    green = (128, 255, 0)
    red = (204, 0, 0)
    black = (0, 0, 0)

    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()  # for sounds
    font = pygame.font.Font(None, 50)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    letters_to_color = ""

    # input_box = pygame.Rect(250, 250, 140, 32)

    # Game initialization
    did_win = False
    delay_count = 30
    stop_game = False
    typed_letter = ""
    letters_to_color = ""
    # color_typed_letter = ""
    index = 0
    word_to_spell = word_bank()  # call word_bank to generate a random word

    while not stop_game:
        # Process input (events)
        for event in pygame.event.get():
            # Event handlings
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    typed_letter = event.unicode
                    print(word_to_spell)
                    # print(type(word_to_spell))
                    print(typed_letter)
                    # take the letter from user input (event.unicode) and compare it to the
                    # corresponding letter in the word_to_spell

                    if (compare(typed_letter, word_to_spell[index]) and index < (len(word_to_spell))):
                        print("YEAAAAAASSSS")
                        print("index: %d " % index)
                        # print(type(word_to_spell[index])) #string
                        print("word length: %d" % len(word_to_spell))
                        # input_box += typed_letter

                        letters_to_color += typed_letter

                        index += 1

                        if index == len(word_to_spell):
                            print("end of the word")
                            # letters_to_color += typed_letter
                            did_win = True
                            delay_count = 300
                            # index = 0
                            # word_to_spell = word_bank()
                            # letters_to_color = ""

                    else:
                        print("noooope!")

                        # change the color of the incorrect letter to red

                        print(index)
                elif event.key == pygame.K_BACKSPACE:
                    typed_letter = typed_letter[:-1]
                elif event.key == pygame.K_RETURN:
                    print(typed_letter)
                    typed_letter = ""
                    word_to_spell = word_bank()

                elif event.type == pygame.QUIT:
                    stop_game = True
        # Update

        def colored_letters(letter_to_color, word_length):
            letters_to_color = letters_to_color + letter_to_color

            print(letters_to_color)  # string
            return (letters_to_color)

        # Draw background
        screen.fill(black)

        # Render text
        block = font.render(word_to_spell, True, (blue))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)

        # re-Render correct/incorrect text
        block2 = font.render(letters_to_color, True, (green))
        rect2 = block2.get_rect()
        rect2.midbottom = screen.get_rect().midbottom
        screen.blit(block2, rect2)

        pygame.display.flip()  # after drawing everything, flip the display *do this last*

        # Game logic

        pygame.display.update()
        if did_win:
            delay_count -= 1

            if delay_count == 0:
                did_win = False
                index = 0
                word_to_spell = word_bank()
                letters_to_color = ""

        # Game display

        clock.tick(60)  # FPS

    pygame.quit()


if __name__ == '__main__':
    main()
