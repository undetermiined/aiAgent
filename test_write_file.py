from config import MAX_CHARS
from functions.write_files import write_file

test_cases = [
    ["calculator", "lorem.txt", "wait, this isn't lorem ipsum"],
    ["calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"],
    ["calculator", "/tmp/temp.txt", "this should not be allowed"],
]


def main():
    for working, target, content in test_cases:
        result = write_file(working, target, content)
        print(f"Writing result for {target} file:")
        print(f"{result}\n")


main()
