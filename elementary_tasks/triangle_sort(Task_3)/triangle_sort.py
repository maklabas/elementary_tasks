import re

triangles_data = {}
while True:
    incoming_data = input("\nEnter name, length of first, second, third sides of triangle according to template:\n"
                          "<name>,<side length>,<side length>,<side length>: ").split(',')
    incoming_data = [val.strip() for val in incoming_data]
    try:
        name = incoming_data[0]
        side_a = float(incoming_data[1])
        side_b = float(incoming_data[2])
        side_c = float(incoming_data[3])

        if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            p = (side_a + side_b + side_c) / 2
            Square = (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5
            triangles_data.update({name: Square})
        else:
            print('no')
    except IndexError:
        if len(incoming_data) == 0:
            print('Help mes')
        else:
            print('we dont have enough data to make calculations')
    except ValueError as v:
        exception_val = re.findall("('.+')", v.__str__())[0]
        print(f'We can\'t convert {exception_val} into number.')

    guess = input("want continue?").strip().lower()
    if guess != 'y':
        print("\n============= Triangles list: ===============")
        index = 1
        for triangle_name in triangles_data:
            print(f'{index}. [Triangle {triangle_name}]: {round(triangles_data[triangle_name],2)} сm')
            index += 1
        break
