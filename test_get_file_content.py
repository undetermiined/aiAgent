from functions.get_files_content import get_file_content

test_cases = [
    ["calculator", "lorem.txt"],
    ["calculator", "main.py"],
    ["calculator", "pkg/calculator.py"],
    ["calculator", "/bin/cat"],
    ["calculator", "pkg/does_not_exist.py"],
]


def main():
    for working, target in test_cases:
        result = get_file_content(working, target)
        print("Result for file:")
        print(f"{result}\n")


main()
