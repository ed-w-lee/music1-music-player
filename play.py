import argparse

parser = argparse.ArgumentParser(description='play some sounds')
parser.add_argument('--dir', help='where to find sfx')
args = parser.parse_args()

import pygame as pg
import time
import os
import keyboard

pg.mixer.init()
pg.init()

alphabet = ('abcdefghijklmnopqrstuvwxyz', '.,:')
dvorak_mapping = ('anihdyujgcvpmlsrxo;kf.,bt/', 'ewZ')
keys, punctuation = dvorak_mapping

sfx = {}
sfx_dir = args.dir
c = 0
for filename in os.listdir(sfx_dir):
    if filename.split('.')[-1] == 'ogg':
        print (alphabet[0][c], filename)
        sfx[keys[c]] = [False, pg.mixer.Sound(os.path.join(sfx_dir, filename))]
        c += 1

pg.mixer.set_num_channels(50)

def play_music(event):
    name = event.name
    if name in list(keys):
        if sfx[name][0]:
            sfx[name][1].stop()
        else:
            sfx[name][1].play(-1)
        sfx[name][0] = not sfx[name][0]
    elif name in punctuation:
        for name in sfx:
            sfx[name][0] = False
        pg.mixer.stop()
keyboard.on_press(play_music)

while True:
    pass
