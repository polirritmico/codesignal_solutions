#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You've intercepted an encrypted message, and you are really curious about its
contents. You were able to find out that the message initially contained only
lowercase English letters, and was encrypted with the following cipher:

- Let all letters from 'a' to 'z' correspond to the numbers from 0 to 25,
respectively.
- The number corresponding to the ith letter of the encrypted message is then
equal to the sum of numbers corresponding to the first i letters of the initial
unencrypted message modulo 26.

Now that you know how the message was encrypted, implement the algorithm to
decipher it.

Example

For message = "taiaiaertkixquxjnfxxdh", the output should be
solution(message) = "thisisencryptedmessage".

The initial message "thisisencryptedmessage" was encrypted as follows:

    letter 0: t -> 19 -> t;
    letter 1: th -> (19 + 7) % 26 -> 0 -> a;
    letter 2: thi -> (19 + 7 + 8) % 26 -> 8 -> i;
    etc.

"""


def solution(message: str) -> str:
    decoded_message = ""
    left_character_value = 0
    for letter in message:
        letter_value = ord(letter) - 97  # 97 = 'a'
        decoded_letter_value = (letter_value - left_character_value) % 26
        decoded_message += chr(decoded_letter_value + 97)
        left_character_value = letter_value
    return decoded_message


def main():
    case = "taiaiaertkixquxjnfxxdh"
    # expected = "thisisencryptedmessage"
    print(solution(case))


if __name__ == "__main__":
    main()
