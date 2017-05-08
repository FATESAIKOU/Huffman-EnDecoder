"""
Implementation of HEnDecoder.

@auth: FATESAIKOU
"""


import Encode as ec

from bitarray import bitarray
#from pprint import pprint

class HEnDecoder:
    def __init__(self):
        print "Init"

    def GetStatus(self):
        return {
                'table': self.__code_table,
                'count': self.__code_count,
                'ori_data': self.__data,
                'compressed_data': self.__seq
                }


    def SetEncode(self, im_data, im_heigh, im_width, pmode):
        self.__data = im_data
        self.__heigh = im_heigh
        self.__width = im_width
        self.__pmode = pmode

    def Encode(self):
        (self.__diff_data, self.__diff_count) = ec.GetDiffCount(self.__data, self.__width, self.__pmode)
        (self.__code_table, self.__code_count) = ec.GenCodeTable(self.__diff_count)

        self.__seq = bitarray()
        self.__seq.encode(self.__code_table, self.__diff_data)

        self.__seq.decode(self.__code_table)

    def GetEncodeResult(self):
        return {
            'heigh': self.__heigh,
            'width': self.__width,
            'pmode': self.__pmode,
            'table': {k: v.to01() for (k, v) in self.__code_table.items()},
            'seq': self.__seq
        }

    def SetDecode(self):
        print "SetDecode"

    def Decode(self):
        print "Decode"

    def GetDecodeResult(self):
        print "GetDecodeResult"
    
    
