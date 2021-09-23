import re


class Envelope:
    """ Class which compares envelopes """

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __lt__(self, other):
        list_1 = [self.side_a, self.side_b]
        list_2 = [other.side_a, other.side_b]
        list_1.sort()
        list_2.sort()

        return True if list_1[0] < list_2[0] and list_1[0] < list_2[0] else False

    def __eq__(self, other):
        list_1 = [self.side_a, self.side_b]
        list_2 = [other.side_a, other.side_b]
        list_1.sort()
        list_2.sort()

        return True if self.side_a == self.side_b and other.side_a == other.side_b else False


def main(s1, s2, s3, s4):
    """ Creates two objects of Envelope and compares if first can be put into second one"""
    con1 = Envelope(s1, s2)
    con2 = Envelope(s3, s4)
    if con1 < con2:
        print(f"\nYou can put envelope with sides {con1.side_a}, {con1.side_b}"
              f"into envelope with sides {con2.side_a}, {con2.side_b}\n")
    elif con1 == con2:
        print("Envelops are same")
    else:
        print(f"\nYou can put envelope with sides {con2.side_a}, {con2.side_b}"
              f"into envelope with sides {con1.side_a}, {con1.side_b}\n")


if __name__ == '__main__':
    while True:
        try:
            a_1 = float(input("\nEnter first side of the first envelope: "))
            b_1 = float(input("Enter second side of the first envelope: "))
            a_2 = float(input("Enter first side of the second envelope: "))
            b_2 = float(input("Enter second side of the second envelope: "))
            main(a_1, a_2, b_1, b_2)
        except ValueError as v:
            print("We can't convert " + re.findall("('.+')", v.__str__())[0] + " into a number.")
        except IndexError:
            print('''How to use:\n
            Enter two sides of the first envelope, then two sides of the second envelope step by step.\n''')

        guess = input("Do you want to continue? \n"
                      "(Enter 'YES' or 'Y' to continue)").lower()
        if guess not in ['yes', 'y']:
            break
