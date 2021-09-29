import io
import unittest
from unittest import mock
from unittest.mock import Mock, patch, call

# from coverage import report

# from envelope_analyze import Envelope, main
from chess_board import ChessBoard
import io


class TestChessBoard(unittest.TestCase):
    # @patch('chess_board.ChessBoard.print_chessboard')
    # @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.print')
    def test_print_chessboard(self, mocked_print):
        test_cases = [

            {
                "in": {"width": 5, "height": 5},
                "out": "█░█░█\n"
                       "░█░█░\n"
                       "█░█░█\n"
                       "░█░█░\n"
                       "█░█░█\n"
            },
            {
                "in": {"width": 3, "height": 3},
                "out": "█░█\n"
                       "░█░\n"
                       "█░█\n"
            },
        ]

        for case in test_cases:
            ChessBoard(**case['in']).print_chessboard()
            mocked_print.assert_called_with(case['out'])

        ''' полурабочий выводит только одну строку
        for case in test_cases:
             ChessBoard(**case['in']).print_chessboard()
             mocked_print.assert_called_with(case['out'])'''
        # ChessBoard(2, 1).print_chessboard()
        # mocked_print.assert_called_with('█')

        # for case in test_cases:
        #     ChessBoard(**case['in']).print_chessboard()
        #     assert mocked_print.mock_called_once(case['out'])
        #       self.assertEqual(print(case['out']), ChessBoard(**case['in']).print_chessboard())


'''class TestChessBoard(unittest.TestCase):
    @patch('builtins.print')
    def test_print(self, mocked_print):
        v = ChessBoard(4, 4).print_chessboard()
        ([call(v), call()], mocked_print.mock_calls)
        # assert mocked_print.mock_calls == [call('foo'), call()]
'''

'''
class TestChessBoard(unittest.TestCase):
    test_cases = [

        {
            "in": {"width": 4, "height": 4},
            "out": "█░█░█\n"
                   "░█░█░\n"
                   "█░█░█\n"
                   "░█░█░\n"
                   "█░█░█\n"
        },
        {
            "in": {"width": 3, "height": 3},
            "out": "█░█\n"
                   "░█░\n"
                   "█░█\n"
        },
        {
            "in": {"width": 40, "height": 45},
            "out": "█░█\n"
                   "░█░\n"
                   "█░█\n"
        },
        {
            "in": {"width": 1, "height": 1},
            "out": "█\n"
        },
        {
            "in": {"width": 1, "height": 0},
            "out": ""
        },
        {
            "in": {"width": 0, "height": 1},
            "out": "\n"
        },
        {
            "in": {"width": 0, "height": 0},
            "out": ""
        },
    ]

    for cases in test_cases:
        @patch('sys.stdout', new_callable=io.StringIO)
        def test_print_chessboard_mock(self, mock_stdout, case=cases):
            ChessBoard(**case['in']).print_chessboard()
            self.assertEqual(case['out'], mock_stdout.getvalue())
'''

"""
class TestChessBoard(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_chessboard(self, mock_stdout):
        test_cases = [
            {
                "in": {"width": 2, "height": 2},
                "out": "█░\n"
                       "░█\n"
            },
            {
                "in": {"width": 3, "height": 3},
                "out": "█░█\n"
                       "░█░\n"
                       "█░█\n"
            },
            # {
            #     "in": {"width": 1, "height": 1},
            #     "out": "█\n"
            # },
            # {
            #     "in": {"width": 1, "height": 0},
            #     "out": ""
            # },
            # {
            #     "in": {"width": 0, "height": 1},
            #     "out": ""
            # },
        ]
        for case in test_cases:
            ChessBoard(**case['in']).print_chessboard()
            self.assertEqual(case['out'], mock_stdout.getvalue())
"""
'''

    def test_(self):
        test_cases = [
            {
                "input": {
                    "width": 4, "height": 4
                },
                "output": [
                    "█░█░",
                    "░█░█",
                    "█░█░",
                    "░█░█"
                ]
            },

        ]

        for case in test_cases:
            self.assertEqual(ChessBoard(**case['input']).print_chessboard(), case['output'])
'''

'''
class TestEnvelope(unittest.TestCase):
    def test_main(self):
        test_cases = [
            {
                'arguments': {'s1': 11, 's2': 15, 's3': 22, 's4': 30},
                'expected_result': "You can put envelope with sides 11, 15 into envelope with sides 22, 30"
            },
            {
                'arguments': {'s1': 22, 's2': 30, 's3': 11, 's4': 15},
                'expected_result': "You can put envelope with sides 22, 30 into envelope with sides 11, 15"
            },
            {
                'arguments': {'s1': 10, 's2': 10, 's3': 10, 's4': 10},
                'expected_result': "You can put envelope with sides 22, 30 into envelope with sides 11, 15"
            },
            {
                'arguments': {'s1': 10, 's2': 10, 's3': 10, 's4': 10},
                'expected_result': "You can put envelope with sides 22, 30 into envelope with sides 11, 15"
            },
            {
                'arguments': {'s1': 'ab', 's2': 'ra', 's3': 'ca', 's4': 'dabra'},
                'expected_result': "\nWe can't convert 'ab' into a number.\n"
                                   "How to use:\n"
                                   "Enter two sides of the first envelope,"
                                   " then two sides of the second envelope step by step.\n"
            },
        ]
        for test_case in test_cases:
            result = main()
            self.assertEqual(test_case['expected_result'], result)'''
