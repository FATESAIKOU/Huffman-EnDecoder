"""
Implementation of HEnDecoder.

@auth: FATESAIKOU
"""


import Encode as ec
import Decode as dc

from bitarray import bitarray

class HEnDecoder:
    def GetStatus(self):
        return {
                'table': self.__code_table,
                'count': self.__code_count,
                'pmode': self.__pmode,
                'ori_len': len(self.__data) * 8,
                'compressed_len': len(self.__seq)
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

    def SetDecode(self, im_heigh, im_width, pmode, table, content):
        self.__heigh = im_heigh
        self.__width = im_width
        self.__pmode = pmode
        self.__code_table = table
        self.__seq = content

    def Decode(self):
        self.__diff_data = self.__seq.decode(self.__code_table)
        
        self.__data = dc.BuildFromDiff(self.__diff_data, self.__width, self.__pmode)

    def GetDecodeResult(self):
        return self.__data
