#!/usr/bin/python3

import os
import sys
import shutil

DIR = os.environ['HOME']

try:
    shutil.rmtree(DIR + "/test/a")
except ValueError:
    pass

os.mkdir(DIR + "/test/a")

if len(sys.argv) > 1:
    NUM = int(sys.argv[1])
    NUM_BIN = ("%04d" % int(bin(NUM)[2:]))
    BIT1 = NUM_BIN[:1]
    BIT2 = NUM_BIN[1:2]
    BIT3 = NUM_BIN[2:3]
    BIT4 = NUM_BIN[3:4]
    if not os.path.isdir(DIR + "/test/a/" + BIT1 + "/"):
        os.mkdir(DIR + "/test/a/" + BIT1 + "/")
        if not os.path.isdir(DIR + "/test/a/" + BIT1 + "/" + BIT2 + "/"):
            os.mkdir(DIR + "/test/a/" + BIT1 + "/" + BIT2 + "/")
            if not os.path.isdir(DIR + "/test/a/" + BIT1 + "/" + BIT2 + "/" + BIT3 + "/"):
                os.mkdir(DIR + "/test/a/" + BIT1 + "/" + BIT2 + "/" + BIT3 + "/")
                if not os.path.isdir(DIR + "/test/a/" + BIT1 + "/" + BIT2 + "/" + BIT3 + "/" + BIT4 + "/"):
                    os.mkdir(DIR + "/test/a/" + BIT1 + "/" + BIT2 + "/" + BIT3 + "/" + BIT4 + "/")
else:
    print('Please enter arg!')

try:
    shutil.rmtree(DIR + "/test/b")
except ValueError:
    pass

os.mkdir(DIR + "/test/b")

if len(sys.argv) > 1:
    NUM = int(sys.argv[2])
    NUM_BIN = ("%04d" % int(bin(NUM)[2:]))
    BIT1 = NUM_BIN[:1]
    BIT2 = NUM_BIN[1:2]
    BIT3 = NUM_BIN[2:3]
    BIT4 = NUM_BIN[3:4]
    if not os.path.isdir(DIR + "/test/b/" + BIT1 + "/"):
        os.mkdir(DIR + "/test/b/" + BIT1 + "/")
        if not os.path.isdir(DIR + "/test/b/" + BIT1 + "/" + BIT2 + "/"):
            os.mkdir(DIR + "/test/b/" + BIT1 + "/" + BIT2 + "/")
            if not os.path.isdir(DIR + "/test/b/" + BIT1 + "/" + BIT2 + "/" + BIT3 + "/"):
                os.mkdir(DIR + "/test/b/" + BIT1 + "/" + BIT2 + "/" + BIT3 + "/")
                if not os.path.isdir(DIR + "/test/b/" + BIT1 + "/" + BIT2 + "/" + BIT3 + "/" + BIT4 + "/"):
                    os.mkdir(DIR + "/test/b/" + BIT1 + "/" + BIT2 + "/" + BIT3 + "/" + BIT4 + "/")
else:
    print('Please enter arg!')