import re


class Triangle:
    """ Describes triangle which name and three sides.
    __________

    Params:

    ~ name - triangle name
    ~ side_a - first side of triangle;
    ~ side_b - second side of triangle;
    ~ side_c - third side of triangle.
    """
    def __init__(self, name: str, side_a: float, side_b: float, side_c: float):
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def square(self):
        """ Returns dict, which contains name and square of triangle if triangle can be created properly;
            Neither returns None."""
        if self.side_a + self.side_b > self.side_c and self.side_a + self.side_c > self.side_b and \
                self.side_b + self.side_c > self.side_a:

            p = (self.side_a + self.side_b + self.side_c) / 2
            Square = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
            return {self.name: Square}
        else:
            return None


def show_triangle(tr_dict: dict):
    """Outputs sorted triangles graphically"""
    print("\n============= Triangles list: ===============")
    index = 1
    # Dict sorting
    tr_dict = {key: value for key, value in sorted(tr_dict.items(), key=lambda item: item[1], reverse=True)}
    # Dict output
    for tr_name in tr_dict:
        print(f'{index}. [Triangle {tr_name}]: {round(tr_dict[tr_name], 2)} сm')
        index += 1


def main():
    """ Main logics of program.
    Parses data from string in definite sequence and checks if it valid.
    """
    # Dict which contains calculated data of triangles
    triangles_data = {}

    while True:
        incoming_data = input("\nEnter name and sides of triangle. Use coma to split data: ").split(',')
        try:
            name = incoming_data[0]
            side_a = float(incoming_data[1])
            side_b = float(incoming_data[2])
            side_c = float(incoming_data[3])

            triangle = Triangle(name, side_a, side_b, side_c)

            triangles_data.update(triangle.square)

        except IndexError:
            print("Data isn't enough to calculate triangles.\n"
                  "Enter name, length of first, second, third sides of triangle according to template:\n"
                  "<name>,<side length>,<side length>,<side length>:")
        except ValueError as v:
            exception_val = re.findall("('.+')", v.__str__())[0]
            print(f'We can\'t convert {exception_val} into number.')

        guess = input("Do you want to add another triangle? 'YES' or 'Y' to continue: ").strip().lower()

        if guess not in ['y', 'yes']:
            show_triangle(triangles_data)
            break


if __name__ == '__main__':
    main()
    # name, 13,13,13
    # namen, 15,15,15
