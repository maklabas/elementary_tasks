class FibRange:
    def __init__(self, start_of_range, end_of_range):
        self.__start_of_range = start_of_range
        self.__end_of_range = end_of_range

    def fibonacci(self):
        previous_num = 0
        start_count = 1
        fibbo_num = 0
        while True:
            fibbo_num = previous_num + fibbo_num

            if self.__start_of_range < fibbo_num < self.__end_of_range:
                print(fibbo_num)

            previous_num = start_count
            start_count = fibbo_num

            if fibbo_num > self.__end_of_range:
                break


fib = FibRange(7, 35)
fib.fibonacci()
