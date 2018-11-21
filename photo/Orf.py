from PhotoFile import PhotoFile
import rawpy
import imageio

class Orf(PhotoFile):

    def __init__(self, path):
        super().__init__(path)
        metadata=orf

    def convert_olym(self, output_path):
        with rawpy.imread(self.path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(output_path, rgb)