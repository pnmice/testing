#!/usr/bin/python3

import os
import glob

DIR = os.environ['HOME']

DIR_A = glob.glob(DIR+'/test/a/*/*/*/*/')
DIR_B = glob.glob(DIR+'/test/b/*/*/*/*/')


NUM = ('\n'.join(DIR_A)).split('/')[5:9]
NUM_BIN_A = int(''.join(NUM), 2)

NUM = ('\n'.join(DIR_B)).split('/')[5:9]
NUM_BIN_B = int(''.join(NUM), 2)

print(NUM_BIN_A+NUM_BIN_B)
