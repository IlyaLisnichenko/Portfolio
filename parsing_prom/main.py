from utils import get_page, file_write


def main():
    product = get_page(min_discount=3)
    file_write(data=product, type_file="json")
    file_write(data=product, type_file="csv")


if __name__ == '__main__':
    main()
