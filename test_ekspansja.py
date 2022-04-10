"""
Ekspresso procedure
Copyright (C) 2022  Mateusz Jaracz 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


from ekspansja import _bit_length, parse_input

from typing import List

FIRST: List[int] = [1, 2, 59, 228]
SECOND: List[int] = [5, 6, 45, 56, 145]


def test_bit_length():
    assert _bit_length(FIRST, SECOND, FIRST) == 8


def test_parse_input():
    result_first = ['00000001', '00000010', '00111011', '11100100']
    result_second = ['00000101', '00000110', '00101101', '00111000', '10010001']
    assert parse_input(FIRST, 8) == result_first
    assert parse_input(SECOND, 8) == result_second
