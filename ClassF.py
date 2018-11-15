import os
import glob
import rawpy
import imageio

class File:
    path = ""

    def __init__(self, path):
        self.path = path

    def exists(self):
        return os.path.exists(self.path)

    def get_name(self):
        return os.path.basename(self.path)

class Photo (File):
    Height
    Width
    Date_Taken
    Device_Name

class OlymPhoto (Photo):

    def convertOlym
            for infile in glob.glob(File.Photo.path):
                with rawpy.imread(infile) as raw:
                rgb = raw.postprocess()
                imageio.imwrite('test.jpg', rgb)
