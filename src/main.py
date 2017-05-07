#!/usr/bin/env python
"""
This file was wrote for test HEnDecoder

@author: FATESAIKOU
"""

#from HEnDecoder.HEnDecoder import HEnDecoder
import Utils

from pprint import pprint

# get option
opt = Utils.GetOption()
pprint(opt)

if opt.mode == 'encode':
    (heigh, width, image_data) = Utils.LoadImage(opt.src)
#
#   hcer = HEnDecoder()
#   hcer.SetEncode(image_data, heigh, width, predict_mode)
#   hcer.Encode()
#
#   Utils.ShowStatus(hcer.GetStatus())
#
#   Utils.SaveRaw(filename, hcer.GetEncodeResult())
#
elif opt.mode == 'decode':
    (heigh, width, pmode, table, content) = Utils.LoadRaw(opt.src)
#
#   hcer = HEnDecoder()
#   hcer.SetDecode(heigh, width, pmode, table, content)
#   hcer.Decode()
#
#   Utils.SaveImage(opt.dest, heigh, width, hcer.GetDecodeResult())

print "Test Start!"
