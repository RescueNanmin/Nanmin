class Light:
    contrast = None
    exposure = None

    def change_exposure(self, value):
        pass

    def change_contrast(self, value):
        pass


class Pixel:
    red = 1
    blue = 1
    green = 1


class Photo:
    picture = None  # Pixel array
    date = None
    location = None
    height = None
    width = None
    ISO = None
    light = Light()

    def get_resolution(self):
        return self.width, self.height
