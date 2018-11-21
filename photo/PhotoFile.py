from File import File
import rawpy


class PhotoFile(File):
    class metadata():
        def __init__(self, width, height):
            self.width = width
            self.height = height

    def __init__(self, path):
        super().__init__(path)
        self.meta = self.create_metadata_from_path()

    def create_metadata_from_path(self):
        with rawpy.imread(self.path) as raw:
            try:
                return self.metadata(raw.sizes.width, raw.sizes.height)
            except ImportError:
                print("Could not get metadata information from the file")
