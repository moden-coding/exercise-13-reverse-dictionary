#!/usr/bin/env python3

def reverse_dictionary(d):
    return {}


def main():
    translations = {"move": ["liikuttaa"], "hide": ["piilottaa", "salata"]}
    result = reverse_dictionary(translations)
    print(result)


if __name__ == "__main__":
    main()
