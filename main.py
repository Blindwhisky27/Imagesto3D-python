import convert


def main():
    path = "car images/"
    image = input("Enter the image name: ")
    print("Input taken: " + path + image)
    print("Conversion started...")
    convert.convert(path + image)


if __name__ == '__main__':
    main()
