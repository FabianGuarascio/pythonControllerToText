import pygame
import os
clear = lambda: os.system('cls')
pygame.init()
pygame.joystick.init()
joystick1 = pygame.joystick.Joystick(0)
# Create a dictionary to map controller buttons to letters
letter_map = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z"
}
hat_map = {
    'up':False,
    'right':False,
    'down':False,
    'none':True
}
direction_map = {
    (0, 0):  'none',
    (0, 1):  'up',
    (1, 0):  'right',
    (0, -1): 'down',
    (-1, 0): 'left',
    (1, 1) : 'up_right',
    (1, -1): 'down_right',
    (-1, 1): 'up_left',
    (-1, -1):'down_left'
}
sentence = ' '

def setHatDirection(direction):
    for key in hat_map:
        hat_map[key] = key == direction
    
while True:
    for event in pygame.event.get():
        StartValue = 0
        
        if event.type == pygame.JOYHATMOTION:
            direction_value = event.dict['value']
            setHatDirection(direction_map[direction_value])
        
        if hat_map['up']: StartValue = 6
        elif hat_map['right']: StartValue = 12
        elif hat_map['down']: StartValue = 18

        if event.type == pygame.JOYBUTTONDOWN:
            if event.dict['button'] == 9:
                with open("file.txt", "a") as f:
                    f.write(' ')
                sentence += ' '
                continue
            if event.dict['button'] == 8:
                sentence = sentence[:-1]
                with open("file.txt", "r") as f:
                    contents = f.read()
                contents = contents[:-1]
                with open("file.txt", "w") as f:
                    f.write(contents)
                continue
            sentence += letter_map[event.dict['button'] + StartValue]
            with open("file.txt", "a") as f:
                f.write(letter_map[event.dict['button'] + StartValue])
        clear()
        print(sentence)
