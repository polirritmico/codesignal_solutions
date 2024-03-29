#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
When you recently visited your little nephew, he told you a sad story: there's a
bully at school who steals his lunch every day, and locks it away in his locker.
He also leaves a note with a strange, coded message. Your nephew gave you one of
the notes in hope that you can decipher it for him. And you did: it looks like
all the digits in it are replaced with letters and vice versa. Digit 0 is
replaced with 'a', 1 is replaced with 'b' and so on, with digit 9 replaced by
'j'.

The note is different every day, so you decide to write a function that will
decipher it for your nephew on an ongoing basis.

Example

For note = "you'll n4v4r 6u4ss 8t: cdja", the output should be
solution(note) = "you'll never guess it: 2390".
"""


def solution(note: str) -> str:
    digits = "0123456789"
    letters = "abcdefghij"
    digits_to_letters = digits + letters
    letters_to_digits = letters + digits
    translation_table = str.maketrans(digits_to_letters, letters_to_digits)

    decoded_note = note.translate(translation_table)
    return decoded_note


def main():
    case = "you'll n4v4r 6u4ss 8t: cdja"
    # expected = "you'll never guess it: 2390"
    print(solution(case))


if __name__ == "__main__":
    main()
