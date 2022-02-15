def main():
    try:
        configuration = open('/path/to/mars.jpg')
    except FileNotFoundError:
        print("Couldn't find the file!")


if __name__ == '__main__':
    main()