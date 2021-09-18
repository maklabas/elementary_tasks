class FibRange:
    def __init__(self, start_of_range: int, end_of_range: int):
        self.__start_of_range = start_of_range
        self.__end_of_range = end_of_range

    @property
    def count_fibonacci(self):
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

    parser.add_argument('start', type=int, default=0, help='Argument that defines start of counting fibonacci')
    parser.add_argument('end', type=int, help='Argument that defines end of counting fibonacci')

    try:
        args = parser.parse_args()
        fib = FibRange(args.start, args.end)
        print(fib.count_fibonacci)
    except:
        parser.print_help()
