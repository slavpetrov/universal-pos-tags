# -*- coding: utf-8 -*-
# Creates an exhaustive fr-paris mapping to universal dependencies, since
# the fr-paris.map file provided as part of the universal dependencies 
# project appears to be incomplete, we are generating a more complete one
# using the rules described on this page:
# https://www.sketchengine.co.uk/french-freeling-part-of-speech-tagset/
#
from __future__ import division, print_function
import os

DATA_DIR = ".."
MAPFILE = os.path.join(DATA_DIR, "fr-paris.map")

fmap = open(MAPFILE, "wb")

utag = "ADJ"
for p0 in ["A"]:
    for p1 in ["O", "Q", "P", "0"]:
        for p2 in ["S", "V", "0"]:
            for p3 in ["F", "M", "C", "0"]:
                for p4 in ["S", "P", "N", "0"]:
                    for p5 in ["1", "2", "3", "0"]:
                        for p6 in ["S", "P", "N", "0"]:
                            btag = "".join([p0, p1, p2, p3, p4, p5, p6])
                            fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "CONJ"
for p0 in ["C"]:
    for p1 in ["C", "S", "0"]:
        btag = "".join([p0, p1])
        fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "DET"
for p0 in ["D"]:
    # F added to fit data, not in freeling list
    for p1 in ["A", "D", "E", "I", "T", "N", "P", "R", "F", "0"]:
        for p2 in ["1", "2", "3", "0"]:
            for p3 in ["F", "M", "C", "N", "0"]:
                for p4 in ["S", "P", "N", "0"]:
                    for p5 in ["S", "P", "0"]:
                        btag = "".join([p0, p1, p2, p3, p4, p5])
                        fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "NOUN"
for p0 in ["N"]:
    for p1 in ["C", "P", "0"]:
        for p2 in ["F", "M", "C", "N", "0"]:
            for p3 in ["S", "P", "N", "0"]:
                for p4 in ["S", "G", "O", "V", "0"]:
                    for p5 in ["0"]:
                        for p6 in ["A", "D", "0"]:
                            btag = "".join([p0, p1, p2, p3, p4, p5, p6])
                            fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "PRON"
for p0 in ["P"]:
    for p1 in ["D", "E", "I", "T", "N", "P", "X", "R", "0"]:
        # S added to fit data, not in freeling
        for p2 in ["1", "2", "3", "S", "0"]:
            for p3 in ["F", "M", "C", "N", "0"]:
                for p4 in ["S", "P", "N", "0"]:
                    for p5 in ["N", "A", "D", "O", "0"]:
                        for p6 in ["P", "0"]:
                            btag = "".join([p0, p1, p2, p3, p4, p5, p6])
                            fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "ADV"    
for p0 in ["R"]:
    for p1 in ["N", "G", "0"]:
        btag = "".join([p0, p1])
        fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "ADP"
for p0 in "S":
    for p1 in ["P", "0"]:
        btag = "".join([p0, p1])
        fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "VERB"
for p0 in ["V"]:
    for p1 in ["M", "A", "S", "0"]:
        for p2 in ["I", "S", "M", "P", "G", "N", "0"]:
            for p3 in ["P", "I", "F", "S", "C", "0"]:
                for p4 in ["1", "2", "3", "0"]:
                    # N added to fit data, not in freeling
                    for p5 in ["S", "P", "N", "0"]:
                        for p6 in ["F", "M", "C", "N", "0"]:
                            btag = "".join([p0, p1, p2, p3, p4, p5, p6])
                            fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "NUM"        
for p0 in ["Z"]:
    for p1 in ["d", "m", "p", "u", "0"]:
        btag = "".join([p0, p1])
        fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "X" # date
for p0 in ["W"]:
    btag = p0
    fmap.write("{:s}\t{:s}\n".format(btag, utag))

utag = "X" # interjection
for p0 in ["I"]:
    btag = p0
    fmap.write("{:s}\t{:s}\n".format(btag, utag))
    
utag = "."
for p0 in ["Fd", "Fc", "Flt", "Fla", "Fs", "Fat", "Faa", "Fg", "Fz", "Fpt",
           "Fpa", "Ft", "Fp", "Fit", "Fia", "Fe", "Frc", "Fra", "Fx", "Fh",
           "Fct", "Fca"]:
    btag = p0
    fmap.write("{:s}\t{:s}\n".format(btag, utag))

fmap.close()

    
