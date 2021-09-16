class ChessBoard:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def check_int(x):
        if isinstance(x, int):
            return True
        return False

    # @property
    # def board_size_height(self):
    #     return self.__height
    #
    # @property
    # def board_size_width(self):
    #     return self.__height
    #
    # @board_size_height.setter
    # def board_size_height(self, height):
    #     if ChessBoard.check_int(height):
    #         pass
    #     else:
    #         print('Coords must be integer numbers')
    #
    # @board_size_width.setter
    # def board_size_width(self, width):
    #     if ChessBoard.check_int(width):
    #         pass
    #     else:
    #         print('Coords must be integer numbers')

    def chess_board(self):
        # height = 4
        # width = 5
        res = ''
        if ChessBoard.check_int(self.__width) and ChessBoard.check_int(self.__height):
            # создаем строку вывода
            # выводим парами.
            for i in range(0, self.__width):
                if i % 2:  # пар столько сколько четных чисел в ширине доски
                    res = res + '█░'

            # проверка на четность
            if self.__width % 2 is True:
                res = res + '█'

            # делаем шахматную доску шахматкой а не полосами
            for i in range(0, self.__height):
                # добавляем первый э-т другого цвета и убираем последний ж-т для реверса если четно
                if i % 2:
                    print('░' + res[:self.__width - 1])
                else:
                    # если нечетно - оставляем исходную строку
                    print(res)
        else:
            print('Size must be integer numbers')


width = input("Enter width: ")
height = input("Enter height: ")
t = ChessBoard(width, height)
print(t.chess_board())
