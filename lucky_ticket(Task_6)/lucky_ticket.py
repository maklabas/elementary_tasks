import csv


def summ(num: str) -> int:
    """Recursive func that returns sum of numbers in string."""
    return int(num[0]) + summ(num[1:]) if len(num) != 0 else 0


def check_Piter(number) -> bool:
    """Divides number on two parts and compares according to Piter system
    (sum of even equals sum of odd numbers)."""
    num_str = str(number)
    res_odd = ''
    res_even = ''
    for index, item in enumerate(num_str, start=0):
        if index % 2 == 0:
            res_odd = res_odd + item
        else:
            res_even = res_even + item
    return summ(res_odd) == summ(res_even)


def check_Moscow(number) -> bool:
    """Divides number on two parts and compares according to Moscow system
    (sum of left half numbers equals sum of right half numbers)."""
    num_str = str(number)
    left_part = num_str[0: int(len(num_str) / 2)]
    right_part = num_str[int(len(num_str) / 2):int(len(num_str))]

    return summ(left_part) == summ(right_part)


def main():
    path = input("Enter way to file: ")

    while True:
        try:
            with open(path, encoding='utf-8') as db:
                reader = csv.DictReader(db, delimiter=",")
                counter = 0
                if reader.fieldnames[0] == "Moscow":
                    for number in reader:
                        if check_Moscow(number["Moscow"]):
                            counter += 1
                    print('\nNumber of lucky tickets according to Moscow method is', counter)
                    break
                elif reader.fieldnames[0] == "Piter":
                    for number in reader:
                        if check_Piter(number["Piter"]):
                            counter += 1
                    print('\nNumber of lucky tickets according to Piter method is', counter)
                    break
                else:
                    print('\nUnknown marker. Check fieldname of the database file.\nIt must be "Piter" or "Moscow".')
                    break
        except FileNotFoundError:
            print(f'No such file or directory: "{path}". Enter way to file again')
            path = input("Enter way to file: ")


if __name__ == "__main__":
    main()
