from config import MAX_CHARS
from functions.get_files_content import get_file_content

test_cases = [
    ["calculator", "main.py"],
    ["calculator", "pkg/calculator.py"],
    ["calculator", "/bin/cat"],
    ["calculator", "pkg/does_not_exist.py"],
    ["calculator", "lorem.txt"],
]


def main():
    for working, target in test_cases:
        result = get_file_content(working, target)
        if len(result) > MAX_CHARS:
            print("Result for file:")
            print(f"{len(result)}")
            print(f"{result[-61:]}")
        else:
            print("Result for file:")
            print(f"{result}\n")


main()
