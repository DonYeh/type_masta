import requests
import sys
import pygame
import copy
import time
from word_bank import word_bank
from compare import compare
from pygame.locals import *


def main():
    width = 500
    height = 500

    # define colors
    blue = (97, 159, 182)
    green = (152, 251, 152)
    red = (204, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    light_grey = (192, 192, 192)

    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()  # for sounds
    font = pygame.font.SysFont('Monaco', 80)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    # clock = pygame.time.Clock()
    # all_sprites = pygame.sprite.Group()
    letters_to_color = ""

    # def start_timer():
    #     start_timer_count = 0
    #     if start_timer_count == 0:
    #         start_time = pygame.time.get_ticks()
    #         start_timer_count += 1
    #     else:
    #         pass

    character_count = 1  # to calculate WPM
    error_count = 0  # to calculate accuracy
    # time = 0
    # wpm = ((character_count/5)/time)
    clock = pygame.time.Clock()
    # pygame.time.set_timer(pygame.USEREVENT, 1000)
    # start_timer = 2  # random initialization number that's != 3
    # Game initialization
    did_win = False
    typed_wrong = False
    delay_count = 30
    stop_game = False
    typed_letter = ""
    letters_to_color = ""
    incorrect_letter_to_color = ""
    # color_typed_letter = ""
    index = 0
    word_to_spell = word_bank()  # call word_bank to generate a random word
    # music = pygame.mixer.music.load("<filename>")
    correct_sound = pygame.mixer.Sound("./wink-sound-effect.wav")
    incorrect_sound = pygame.mixer.Sound("./quick_fart_x.wav")
    start_time = pygame.time.get_ticks()
    # print(type(start_time))
    # start_timer = False

    while not stop_game:
        # Process input (events)B
        # start_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            # Event handlings
            if event.type == pygame.KEYDOWN:
                print(sorted(pygame.font.get_fonts()))
                # start_timer()
                if event.unicode.isalpha() or "'":
                    typed_letter = event.unicode
                    print(word_to_spell)
                    # print(type(word_to_spell))
                    print(typed_letter)
                    # take the letter from user input (event.unicode) and compare it to the
                    # corresponding letter in the word_to_spell
                    # start_time = pygame.time.get_ticks()

                    if (compare(typed_letter, word_to_spell[index]) and index < (len(word_to_spell))):
                        print("YEAAAAAASSSS")
                        character_count += 1
                        correct_sound.play()
                        print("index: %d " % index)
                        # print(type(word_to_spell[index])) #string
                        # print("word length: %d" % len(word_to_spell))
                        # input_box += typed_letter
                        print("character count: %d" % character_count)
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
                        incorrect_sound.play()
                        error_count += 1
                        # can't get the string to align the letter correctly...
                        incorrect_letter_to_color = word_to_spell[:(index+1)]
                        # print("Index of the incorrect letter typed: %d" % index)
                        print("error count: %d" % error_count)
                        typed_wrong = True
                        delay_count = 200

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
        screen.fill(light_grey)

        # Render text
        block = font.render(word_to_spell, True, (blue))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)

        # Render text red
        block3 = font.render(incorrect_letter_to_color, True, (red))
        rect3 = rect.copy()
        screen.blit(block3, rect3)

        # Render text green
        block2 = font.render(letters_to_color, True, (green))
        rect2 = rect.copy()
        screen.blit(block2, rect2)

        # render box to display accuracy

        displayfont = pygame.font.SysFont(None, 30)
        acc = float(1 - (error_count/character_count))
        text = displayfont.render('accuracy: %.2f' %
                                  acc, True, (white))
        textrect2 = text.get_rect()
        textrect2.midtop = screen.get_rect().midtop
        textrect2.move_ip(0, 30)
        screen.blit(text, textrect2)

        # render box to display timer

        displayfont = pygame.font.SysFont(None, 30)
        seconds = float((pygame.time.get_ticks() - start_time)/1000)
        text = displayfont.render(
            'timer: %.1f' % seconds, True, (white))
        textrect3 = text.get_rect()
        textrect3.topleft = screen.get_rect().topleft
        textrect3.move_ip(50, 30)
        screen.blit(text, textrect3)

        # render box to display WPM

        displayfont = pygame.font.SysFont(None, 30)
        wpm = float(((character_count/5)*60/seconds))
        text = displayfont.render('WPM: %.1f' %
                                  wpm, True, (white))
        textrect = text.get_rect()
        textrect.topright = screen.get_rect().topright
        textrect.move_ip(-50, 30)
        screen.blit(text, textrect)

        # Game logic

        pygame.display.update()
        if did_win:
            delay_count -= 15

            if delay_count == 0:
                did_win = False
                index = 0
                word_to_spell = word_bank()
                letters_to_color = ""

        if typed_wrong:
            delay_count -= 10
            if delay_count == 0:
                incorrect_letter_to_color = ""
                typed_wrong = False

        # if start_time:
        #     seconds = (pygame.time.get_ticks() - start_time)/1000
        #     message = 'Seconds:' + str(seconds)
        #     screen.blit(displayfont.render(message, True, (white)), (20, 20))

        pygame.display.flip()  # after drawing everything, flip the display *do this last*

        # Game display

        clock.tick(60)  # FPS

    pygame.quit()


if __name__ == '__main__':
    main()
