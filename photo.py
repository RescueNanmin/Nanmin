import os


class File:
    path = ""

    def __init__(self, path):
        self.path = path

    def exists(self):
        return os.path.exists(self.path)

    def get_name(self):
        return os.path.basename(self.path)

