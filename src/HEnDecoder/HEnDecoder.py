"""
Implementation of HEnDecoder.

@auth: FATESAIKOU
"""

#import numpy as np

import Decode as dc

from bitarray import bitarray
#from pprint import pprint

class HEnDecoder:
    def __init__(self):
        print "Init"

    def GetStatus(self):
        print "GetStatus"


    def SetEncode(self, im_data, im_heigh, im_width, pmode):
        self.__data = im_data
        self.__heigh = im_heigh
        self.__width = im_width
        self.__pmode = pmode

    def Encode(self):
        self.__diff_count = dc.GetDiffCount(self.__data, self.__width, self.__pmode)
        # table = Huffman-encode([(s, v) for (s, v) in appearance_dict.items() if v > 0]) (heap insert/pop)
        # seq = getSequence(self.__data, table)

        # update self status/data
        print "Encode"

    def GetEncodeResult(self):
        return {
            'heigh': 110,
            'width': 100,
            'pmode': 7,
            'table': [[1, 2], 3],
            'seq': bitarray('01')
        }

    def SetDecode(self):
        print "SetDecode"

    def Decode(self):
        print "Decode"

    def GetDecodeResult(self):
        print "GetDecodeResult"
    
    
