from gendiff import generate_diff, parsing


def main():
    files = parsing()
    print (generate_diff(files.first_file, files.second_file))
    

if __name__ == "__main__":
    main()