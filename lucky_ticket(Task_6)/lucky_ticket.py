import csv
import re


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
        if re.findall("(.+\.csv)", path):
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
                        print('\nUnknown marker. Check your database file.\n'
                              'First line must be "Piter" or "Moscow" and tickets then.')
                        break

            except (FileNotFoundError, IndexError) as exc:
                if exc is FileNotFoundError:
                    print(f'No such file or directory: "{path}". Enter way to file again')
                    path = input("Enter way to file: ")
                elif exc is IndexError:
                    print("Your file doesn't matches to right format."
                          "First line has be with city marker.")
            except TypeError:
                print("Your file is probably empty.")
                break

        else:
            print("Your has to be '.csv' format and first line has to be with city marker. "
                  "Program counts quantity of lucky tickets in rhe file according to city marker.")
            path = input("Enter way to file: ")


if __name__ == "__main__":
    main()
