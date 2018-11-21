import os
import glob
import rawpy
import imageio


with rawpy.imread("P4010063.ORF") as raw:
    rgb = raw.postprocess()
    imageio.imwrite('Simplified.jpg', rgb)
