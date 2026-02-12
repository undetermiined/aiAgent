from functions.get_files_info import get_files_info

test_cases = [
    ["calculator", "."],
    ["calculator", "pkg"],
    ["calculator", "/bin"],
    ["calculator", "../"],
]


def main():
    for working, target in test_cases:
        result = get_files_info(working, target)
        if target == ".":
            target = "current"
        print(f"Result for {target} directory:")
        print(f"{result}\n")


main()
