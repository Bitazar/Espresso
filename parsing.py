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


from dataclasses import dataclass


@dataclass(frozen=True)
class InputDTO:
    first: list[int]
    second: list[int]


def return_type(type: object):
    def handler(function):
        def wrapper(*args: ..., **kwargs: ...) -> any:
            if (value := function(*args, **kwargs)):
                for element in value:
                    if not isinstance(element, type):
                        return None
                return value
            return None
        return wrapper
    return handler


@return_type(int)
def evaluate(input: str) -> object | None:
    try:
        return eval('[' + input + ']')
    except Exception:
        return None


def parse(first: str, second: str) -> InputDTO | None:
    if (f := evaluate(first)) and (r := evaluate(second)):
        return InputDTO(f, r)
    return None
