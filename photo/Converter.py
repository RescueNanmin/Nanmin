import File
import imageio
import rawpy

class Converter:

    @staticmethod
    def convert_photo_to_jpg(input_file, output_path):
        assert input_file.issubclass(File)
        with rawpy.imread(input_file.path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(output_path, rgb)
