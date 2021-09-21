def text_manipulator(path: str, search_str: str, replace_str: str = None):
    """This func finds string in the text file and replaces it if needed.
    ________

    Params:
        ~ path - way to file you want to parse
        ~ search_str - string you want to find in the file
        ~ replace_str(optional) - string you want to replace in the file instead of search_str
    """
    try:
        with open(path, "r", encoding='utf-8') as text:
            data = text.read()

            if data.count(search_str) != 0:
                print(f"{data.count(search_str)} strings has been found in the text.")
                if replace_str is not None:
                    data = data.replace(search_str, replace_str)
                    print('String has been successfully replaced!')
            else:
                print(f"String '{search_str}' hasn't been found in the text")

        with open(path, "w", encoding='utf-8') as text:
            text.write(data)
    except FileNotFoundError as e:
        print("File hasn't changed.", e)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='This is the program that searches definite string in the text ')

    parser.add_argument('way_to_file', type=str, help='Argument that defines path of text file you want to parse.')
    parser.add_argument('searched_string', type=str, help='Argument that defines string you want to find in the text.')
    parser.add_argument('-r', '--replacing_string', type=str, default=None,
                        help='Argument that defines string you want to replace in the text.')

    try:
        args = parser.parse_args()
        text_manipulator(args.way_to_file, args.searched_string, args.replacing_string)
    except:
        parser.print_help()
