import os

class File():

    def __init__(self, path):
        assert File.exists(path)
        self.path = path

    @classmethod
    def exists(cls, path):
        return os.path.exists(path)

    def get_name(self):
        return os.path.basename(self.path)