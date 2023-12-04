#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
the function should exit after 105 commands.
the function should return the program output once it contains 100 symbols.

Befunge-93 consists of the following commands:

    # >: start moving right
    # <: start moving left
    # v: start moving down
    # ^: start moving up
    # #: bridge; skip next cell
    # _: pop a value; move right if value = 0, left otherwise
    # |: pop a value; move down if value = 0, up otherwise
    # +: addition; pop a, pop b, then push a + b
    # -: subtraction; pop a, pop b, then push b - a
    # *: multiplication; pop a, pop b, then push a * b
    # /: integer division; pop a, pop b, then push b / a
    # %: modulo operation; pop a, pop b, then push b % a
    # !: logical NOT; pop a value, if the value = 0, push 1, otherwise push 0
    # `: greater than; pop a and b, then push 1 if b > a, otherwise 0
    # :: duplicate value on top of the stack
    # \\: swap the top stack value with the second to the top
    # $: pop value from the stack and discard it
    # .: pop value and output it as an integer followed by a space
    # ,: pop value and output it as ASCII character
    # digits 0-9: push the encountered number on the stack
    # ": start string mode; push each character's ASCII value all the way up to the next "
    # (whitespace character): empty instruction; does nothing
    # @: end program; the program output should be returned then

If the stack is empty and it is necessary to pop a value, no exception is
raised; instead, 0 is produced.

The output of the program after
    the program hits the @ command;
    the program executes 105 commands;
        commands: >, <, v, ^, #, _, |, :, \\, $, ., ,
    the program output contains 100 symbols;

"""


class BefungeInterpreter:
    exit_char = "@"
    max_instructions = 105
    max_output = 100
    string_mode_char = '"'
    directions = {
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
        "^": (-1, 0),
    }
    commands = {
        ">": lambda self: setattr(self, "direction", self.directions[">"]),
        "<": lambda self: setattr(self, "direction", self.directions["<"]),
        "v": lambda self: setattr(self, "direction", self.directions["v"]),
        "^": lambda self: setattr(self, "direction", self.directions["^"]),
        "_": lambda self: setattr(self, "direction", self.directions[">"] if self.pop() == 0 else self.directions["<"]),
        "|": lambda self: setattr(self, "direction", self.directions["v"] if self.pop() == 0 else self.directions["^"]),
        "#": lambda self: self.update_pointer(self.direction),
        "$": lambda self: self.pop(),
        ".": lambda self: setattr(self, "output", f"{self.output}{self.pop()} "),
        ",": lambda self: setattr(self, "output", f"{self.output}{chr(self.pop())}"),
        ":": lambda self: self.stack.append(self.stack[-1]) if len(self.stack) != 0 else None,
        "\\": lambda self: self.stack.append(self.pop(-2)),
    }
    operators = {
        "+": lambda self, a, b: self.stack.append(a + b),
        "-": lambda self, a, b: self.stack.append(b - a),
        "*": lambda self, a, b: self.stack.append(a * b),
        "/": lambda self, a, b: self.stack.append(b // a),
        "%": lambda self, a, b: self.stack.append(b % a),
        "`": lambda self, a, b: self.stack.append(1 if b > a else 0),
    }
    single_operators = {
        "!": lambda self, a: self.stack.append(1 if a == 0 else 0),
    }

    def __init__(self):
        self.direction: list[int] = self.directions[">"]
        self.output: str = ""
        self.pointer: list[int] = [0, 0]
        self.size: set[int] = (0, 0)
        self.stack: list[int] = []
        self.string_mode: bool = False

    def execute(self, program: list[str]) -> None:
        self.size = (len(program), len(program[0]))
        instructions_counter = 0
        while instructions_counter < 100000:
            current = program[self.pointer[0]][self.pointer[1]]

            if self.string_mode:
                if current == self.string_mode_char:
                    self.string_mode = False
                else:
                    self.stack.append(ord(current))
            elif current == self.string_mode_char:
                self.string_mode = True
            elif current in self.commands:
                self.commands[current](self)
            elif current in self.operators:
                self.operators[current](self, self.pop(), self.pop())
            elif current in self.single_operators:
                self.single_operators[current](self, self.pop())
            elif current in "1234567890":
                self.stack.append(int(current))
            elif current == self.exit_char:
                return

            self.update_pointer(self.direction)
            instructions_counter += 1

    def pop(self, index: int = -1) -> int:
        stack_size = len(self.stack)
        if stack_size == 0 or abs(index) > stack_size:
            return 0
        return self.stack.pop(index)

    def update_pointer(self, direction: list[int]) -> None:
        self.pointer[0] = (self.pointer[0] + direction[0]) % self.size[0]
        self.pointer[1] = (self.pointer[1] + direction[1]) % self.size[1]

    def program_output(self) -> str:
        if len(self.output) > self.max_output:
            return self.output[: self.max_output]
        return self.output


def solution(input: list[str]) -> str:
    interpreter = BefungeInterpreter()
    interpreter.execute(input)
    return interpreter.program_output()


def main():
    case = [
        "               v",
        'v  ,,,,,"Hello"<',
        ">48*,          v",
        '"!dlroW",,,,,,v>',
        "25*,@         > ",
    ]
    # expected = "Hello World!\n"
    print(solution(case))


if __name__ == "__main__":
    main()
