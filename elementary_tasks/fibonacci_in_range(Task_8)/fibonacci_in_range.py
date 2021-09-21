class FibRange:
    """
    This class creates sequence of fibonacci numbers in rage from minimum (start_of_range) to maximum (end_of_range)
    numbers.
     Note: minimum and maximum numbers ar not included in returned range.
    __________

    Parameters:
        ~ start_of_range - number of start counting fibonacci sequence.
        ~ end_of_range   - number of start counting fibonacci sequence.
    """

    def __init__(self, start_of_range: int, end_of_range: int):
        param_lst = [abs(start_of_range), abs(end_of_range)]
        param_lst.sort()
        self.__start_of_range = param_lst[0]
        self.__end_of_range = param_lst[1]


    @property
    def fibonacci_sequence(self):
        """Returns sequence of fibonacci numbers """
        previous_num = 0
        start_count = 1
        fibbo_num = 0
        fibbo_list = []
        while True:
            fibbo_num = previous_num + fibbo_num

            if self.__start_of_range < fibbo_num < self.__end_of_range:
                fibbo_list.append(fibbo_num)

            previous_num = start_count
            start_count = fibbo_num

            if fibbo_num > self.__end_of_range:
                return ', '.join(str(number) for number in fibbo_list)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='This is the program that prints fibonacci numbers in definite range.')

    parser.add_argument('start', type=int, help='Argument that defines start of counting fibonacci')
    parser.add_argument('end', type=int, help='Argument that defines end of counting fibonacci')

    try:
        args = parser.parse_args()
        fib = FibRange(args.start, args.end)
        print(fib.fibonacci_sequence)
    except:
        parser.print_help()
