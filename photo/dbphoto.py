class Photo:

    def __init__(self, height, width, path, iso, device):
        self.height = height
        self.width = width
        self.path = path
        self.iso = iso
        self.device = device

class Device:

    def __init__ (self,name,maker):
        self.name=name
        self.maker=maker
