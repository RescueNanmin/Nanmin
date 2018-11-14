from photo import File


def run():
    file1 = File("/Users/song/Desktop/inventory.pdf")
    file2 = File("/Users/song/Desktop/inventory2.pdf")
    print("File1:" + file1.exists().__str__())
    print("File1:" + file1.get_name())
    print("File1:" + file1.path)
    print("File2:" + file2.exists().__str__())
    print(File.ss())


if __name__ == "__main__":
    run()
