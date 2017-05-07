"""
Utils

@author: FATESAIKOU
"""

import sys
import numpy as np

import Image
import json
import struct

from optparse import OptionParser
from bitarray import bitarray

#from pprint import pprint

"""
Get Options

output: [ 'mode': str, 'src': str, 'dest': str, 'pmode': int(0-7)]
"""
def GetOption():
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

"""
Load Image

input: filename(path)
output: (int, int, np.array)
"""
def LoadImage(filename):
    image = Image.open(filename)

    (width, heigh) = image.size
    image_data = np.array(image.getdata())

    return (heigh, width, image_data)

"""
Save Image

input: filename(path), int, int, np.array 
"""
def SaveImage(filename, heigh, width, image_data):
    image = Image.new('L', (width, heigh))
    image.putdata(image_data)

    image.save(filename)

"""
Load Raw Data (compressed data)

input: filename(path)
output: (int, int, int, table, bitarray)
"""
def LoadRaw(filename):
    src = open(filename, 'rb')
    content = src.read()
    src.close()

    (heigh, width, pmode, table_size, seq_bit_len,) = struct.unpack('IIIII', content[0:20])
    (table_json,) = struct.unpack('%ds' % (table_size), content[20:20 + table_size])
    
    table = json.loads(table_json)
    seq = bitarray(content[20 + table_size:])[0:seq_bit_len]

    return (heigh, width, pmode, table, seq)

"""
Load Raw Data (compressed data)

input: filename(path),  res[
                            'heigh': int,
                            'width': int,
                            'pmode': int,
                            'table': list,
                            'seq'  : bitarray
                        ]
"""
def SaveRaw(filename, res):
    table_json = json.dumps(res.table).replace(" ", "")
    table_size = len(table_json)
    seq_bit_len = len(res.seq) # can be diff to byte

    dest = open(filename, 'wb')

    dest.write(struct.pack('IIIII', res.heigh, res.width, res.pmode, table_size, seq_bit_len))
    dest.write(struct.pack('%ds' % table_size, table_json))
    res.seq.tofile(dest)

    dest.close()
