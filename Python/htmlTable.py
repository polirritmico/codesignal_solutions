#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HTML tables allow web developers to arrange data into rows and columns of cells.
They are created using the <table> tag. Its content consists of one or more rows
denoted by the <tr> tag. Further, the content of each row comprises one or more
cells denoted by the <td> tag, and content within the <td> tags is what site
visitors see in the table. For this task assume that tags have no attributes in
contrast to real world HTML.

Some tables contain the <th> tag. This tag defines header cells, which shouldn't
be counted as regular cells.

You are given a rectangular HTML table. Extract the content of the cell with
coordinates (row, column).

If you are not familiar with HTML, check out this note.

Example

    For table = "
        <table>
            <tr>
                <td>1</td>
                <td>TWO</td>
            </tr><tr>
                <td>three</td>
                <td>FoUr4</td>
            </tr>
        </table>
    ", row = 0, and column = 1, the output should be
    solution(table, row, column) = "TWO".

    <table>
     <tr>
      <td>1</td>
      <td>TWO</td>
     </tr>
     <tr>
      <td>three</td>
      <td>FoUr4</td>
     </tr>
    </table>

    corresponds to:
    1	TWO
    three	FoUr4

    For table = "<table><tr><td>1</td><td>TWO</td></tr></table>",
        row = 1, and column = 0, the output should be
    solution(table, row, column) = "No such cell".

    <table>
     <tr>
      <td>1</td>
      <td>TWO</td>
     </tr>
    </table>

    corresponds to:
    1	TWO


Input/Output

string

The content of the cell with coordinates (row, column) or the string "No such
cell" if there is no cell with those coordinates in the table.

"""
from bs4 import BeautifulSoup


def solution(table: str, row: int, column: int) -> str:
    soup = BeautifulSoup(table, "html.parser")
    for th in soup.find_all("th"):
        th.extract()
    all_rows = soup.find_all("tr")
    if len(all_rows) <= row or len(all_rows[row]) <= column:
        return "No such cell"
    target_cell = all_rows[row].find_all("td")[column]
    return target_cell.tex


def main():
    table = "<table><tr><th>CIRCUMFERENCE</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr><tr><td>BITS</td><td>3</td><td>4</td><td>8</td><td>10</td><td>12</td><td>15</td></tr></table>"
    row = 0
    column = 6
    # expected = "No such cell"
    print(solution(table, row, column))


if __name__ == "__main__":
    main()
