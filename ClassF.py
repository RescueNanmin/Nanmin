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
    Device_Nam
e
    def __init__(self, path):
        self.path = path


class OlymPhoto (Photo):

    def convertOlym
            for File.Photo.path in glob.glob(File.Photo.path):
                with rawpy.imread(File.Photo.path) as raw:
                rgb = raw.postprocess()
                imageio.imwrite('Simplified.jpg', rgb)
