class NaturalNumbers:
    """
    Use it for counting sequence of natural numbers.
    Counting starts from "0" according to ISO 80000-2 math standard.
    _________
    Parameters:
        ~ max_num   - Square root of the number defines the last natural number of the sequence
    """

    def __init__(self, max_num: int):
        self.max_num = max_num
        self.result = []

    def list_numbers(self):
        """Makes list of numbers"""
        for i in range(0, self.max_num):
            if i ** 2 < self.max_num:
                self.result.append(i)

    @property
    def numbers(self):
        """Returns string sequence of numbers if they exists"""
        self.list_numbers()
        if self.result:
            return ', '.join(str(number) for number in self.result)
        else:
            return "Number can't be less than zero. Try again with number above zero"


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='This is the program that prints the sequence of natural numbers.',
                                     conflict_handler='resolve')

    parser.add_argument('maximum', type=int,
                        help='Square root of this number defines the last natural number of the printed sequence')

    try:
        args = parser.parse_args()
        natural_seq = NaturalNumbers(args.maximum)
        print(natural_seq.numbers)
    except:

        parser.print_help()
