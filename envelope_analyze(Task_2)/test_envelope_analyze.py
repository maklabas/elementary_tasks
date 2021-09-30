import unittest

from envelope_analyze import Envelope, main


class TestEnvelope(unittest.TestCase):
    def test_is_equals(self):
        test_cases = [
            {
                "in_1": {"side_a": 5, "side_b": 5},
                "in_2": {"side_a": 5, "side_b": 5},
                "out": True,
                "statement": "=="
            },
            {
                "in_1": {"side_a": 12, "side_b": 1},
                "in_2": {"side_a": 2, "side_b": 11},
                "out": False,
                "statement": "<"  # Incorrect sizes
            },
            {
                "in_1": {"side_a": 12, "side_b": 1},
                "in_2": {"side_a": 2, "side_b": 11},
                "out": False,
                "statement": ">"  # Incorrect sizes
            },
            {
                "in_1": {"side_a": 12, "side_b": 1},
                "in_2": {"side_a": 2, "side_b": 11},
                "out": False,
                "statement": "=="  # Incorrect sizes
            },
            {
                "in_1": {"side_a": 15, "side_b": 5},
                "in_2": {"side_a": 4, "side_b": 11},
                "out": True,
                "statement": ">"
            },
            {
                "in_1": {"side_a": 15, "side_b": 5},
                "in_2": {"side_a": 4, "side_b": 11},
                "out": False,
                "statement": "<"
            },

        ]
        for case in test_cases:
            c1 = Envelope(**case['in_1'])
            c2 = Envelope(**case['in_2'])
            if case['statement'] == '<':
                self.assertEqual(case['out'], c1 < c2)
            elif case['statement'] == '>':
                self.assertEqual(case['out'], c1 > c2)
            elif case['statement'] == '==':
                self.assertEqual(case['out'], c1 == c2)

    def test_main(self):
        test_cases = [
            {
                "in": {"s1": 5, "s2": 5, "s3": 5, "s4": 5},
                "out": "\nEnvelops are same\n"

            },
            {
                "in": {"s1": 12, "s2": 1, "s3": 2, "s4": 11},
                "out": "\nYou can't put envelope into another one\n"

            },
            {
                "in": {"s1": 15, "s2": 5, "s3": 4, "s4": 11},
                "out": "\nYou can put envelope with sides 4.0, 11.0 into envelope with sides 15.0, 5.0\n"

            },
            {
                "in": {"s1": '11.1', "s2": '4.4', "s3": '5', "s4": '15'},   # Converting to float
                "out": "\nYou can put envelope with sides 11.1, 4.4 into envelope with sides 5.0, 15.0\n"

            },
            {
                "in": {"s1": 'abracadabra', "s2": 4, "s3": 5, "s4": 15},
                "out": "\nWe can't convert 'abracadabra' into a number.\n"
                       "How to use:\n"
                       "Enter two sides of the first envelope, then two sides of the second envelope step by step.\n"

            },
            {
                "in": {"s1": 0, "s2": 1, "s3": 2, "s4": 11},
                "out": "\nEnvelope has incorrect sides\n"

            },

        ]
        for case in test_cases:
            self.assertEqual(main(**case["in"]), case["out"])