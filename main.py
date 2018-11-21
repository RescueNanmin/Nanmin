from photo import File, CanonPhoto
from abc import ABC,abstractclassmethod


def run():
    file1 = File("/Users/song/Desktop/inventory.pdf")
    file2 = File("/Users/song/Desktop/inventory2.pdf")
    print("File1:" + file1.exists().__str__())
    print("File1:" + file1.get_name())
    print("File1:" + file1.path)
    print("File2:" + file2.exists().__str__())
    canon = CanonPhoto("/Users/song/Desktop/inventory.pdf")
    canon.test()


# noinspection PyDeprecation
class Test(ABC):
    @abstractclassmethod
    def ss(cls):
        pass


if __name__ == "__main__":
    run()
