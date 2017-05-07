"""
Utils

@author: FATESAIKOU
"""

import sys

from optparse import OptionParser

#from pprint import pprint

def GetOption():
    # Define Options
    parser = OptionParser()
    parser.add_option("-m", "--mode", dest="mode",
                    help="use this program in encode/decode mode",
                    metavar="MODE")
    parser.add_option("-i", "--input-file", dest="src",
                    help="read from FILE", metavar="FILE")
    parser.add_option("-o", "--output-file", dest="dest",
                    help="write result to FILE", metavar="FILE")
    parser.add_option("-p", "--prediction-mode", dest="pmode",
                    help="predict each pixel with PMODE(an integar within 0 to 7)",
                    metavar="PMODE")

    # Get Options
    (opt, args) = parser.parse_args()

    # Check Options
    if opt.mode not in ['decode', 'encode']:
        print "The MODE should be either 'decode' or 'encode'!"
        sys.exit(0)

    if opt.pmode not in ['0', '1', '2', '3', '4', '5', '6', '7']:
        print "The PMODE should be a integar within 0 to 7!"
        sys.exit(0)

    return opt

def ShowStatus():
    print "ShowStatus"

def LoadImage():
    print "LoadImage"

def SaveImage():
    print "SaveImage"

def LoadRaw():
    print "LoadRaw"

def SaveRaw():
    print "SaveRaw"

