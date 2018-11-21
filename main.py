from Orf import Orf
from File import File
from Converter import Converter

if __name__ == "__main__":
    File.exists('/Users/yeonbinkim/Downloads/P4010063.ORF')
    example = Orf('/Users/yeonbinkim/Downloads/P4010063.ORF')
    Converter.convert_photo_to_jpg(Orf,'/Users/yeonbinkim/Downloads/P4010063.jpg')
    # example.convert_olym('/Users/yeonbinkim/Downloads/P4010063.jpg')


