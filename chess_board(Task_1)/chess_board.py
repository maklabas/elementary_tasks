class ChessBoard:
    """
    This class makes chessboard by defining two parameters:
    _____________

    - width (number of chessboard cells in row)
    - height (number of chessboard cells in height)

    """

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def print_chessboard(self):
        """ This function prints chessboard"""

        res = ''

        # creating output row
        # default chessboard has even number of cells
        for i in range(0, self.__width):
            if i % 2:  # number of cell pairs equal quantity of even numbers, counting by width index
                res = res + '█░'  # '█░' - one cell pair

        # if number of cells is odd - we must add '█'
        if self.__width % 2 != 0:
            res = res + '█'
        # в пизду. аппендь ёбаную функцию!!!!!!!!!!!!!!!!!!!!!!
        # cycle of creating chessboard
        for i in range(0, self.__height):
            # if number of cells is even, cycle adds '░' in the beginning and removes last cell
            if i % 2 and self.__width != 0:
                print('░' + res[:self.__width - 1])
            else:
                # if number of cells is odd - cycle prints original row
                print(res)


if __name__ == "__main__":  # pragma: no cover
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('width', type=int, help='Defines width of chessboard.')
    parser.add_argument('height', type=int, help='Defines height of chessboard.')
    try:
        args = parser.parse_args()
        t = ChessBoard(args.width, args.height)
        t.print_chessboard()
    except:
        parser.print_help()
