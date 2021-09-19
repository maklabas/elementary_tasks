class NaturalNumbers:
    def __init__(self, max_num: int):
        self.max_num = max_num
        self.result = []

    def __list_numbers(self):
        for i in range(0, self.max_num):
            if i ** 2 < self.max_num:
                self.result.append(i)

    @property
    def show_numbers(self):
        self.__list_numbers()
        if self.result is True:
            return ', '.join(str(number) for number in self.result)
        else:
            return 'This number is too small. Try again with bigger number'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='This is the program that prints the sequence of natural numbers.')

    parser.add_argument('maximum', type=int,
                        help='Square root of this number defines the last natural number of the sequence')

    try:
        args = parser.parse_args()
        nat_seq = NaturalNumbers(args.maximum)
        print(nat_seq.show_numbers)
    except:
        parser.print_help()
