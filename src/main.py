#!/usr/bin/env python
"""
This file was wrote for test HEnDecoder

@author: FATESAIKOU
"""

from HEnDecoder.HEnDecoder import HEnDecoder
import Utils


# get option
opt = Utils.GetOption()

if opt.mode == 'encode':
    # Load Image Data
    (heigh, width, image_data) = Utils.LoadImage(opt.src)

    # Encode
    hcer = HEnDecoder()
    hcer.SetEncode(image_data, heigh, width, int(opt.pmode))
    hcer.Encode()

    # Show Symbol Table & Compress Rate & others
    Utils.ShowStatus(hcer.GetStatus())

    # Save Encoding Result to Provided Path
    Utils.SaveRaw(opt.dest, hcer.GetEncodeResult())

elif opt.mode == 'decode':
    # Load Compressed Image Data & Symbol Table & others
    (heigh, width, pmode, table, content) = Utils.LoadRaw(opt.src)

    # Decode
    hcer = HEnDecoder()
    hcer.SetDecode(heigh, width, pmode, table, content)
    hcer.Decode()

    # Save Decoding Result & Show the Image
    Utils.SaveImage(opt.dest, heigh, width, hcer.GetDecodeResult())
