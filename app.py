from pyforge.code_parser import CodeParser


def main():

    file_path = input("Enter Python file path: ")

    parser = CodeParser(file_path)

    result = parser.analyze()

    print("\n========== IMPORTS ==========")

    for item in result["imports"]:
        print(item)

    print("\n========== CLASSES ==========")

    for item in result["classes"]:
        print(item)

    print("\n========== FUNCTIONS ==========")

    for item in result["functions"]:
        print(item)


if __name__ == "__main__":
    main()