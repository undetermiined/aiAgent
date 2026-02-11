from functions.get_files_info import get_files_info

test_cases = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
]


def main():
    for current_test in test_cases:
        result = get_files_info(current_test)
        print(f"Result for {current_test} directory:")
        print(f"    -{result}")


main()
