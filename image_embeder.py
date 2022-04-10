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
PRE: str = "from PySide6.QtGui import QPixmap, QIcon\n\n"
POST: str = """

def generate_icon() -> QIcon:
    pixmap = QPixmap()
    pixmap.loadFromData(SOURCE)
    return QIcon(pixmap)

"""


def read_as_hex(file_name: str) -> bin:
    with open(file_name, 'rb') as handle:
        return handle.read().hex()


def spliter(hex_data: bin) -> str:
    return map(''.join, zip(hex_data[::2], hex_data[1::2]))


def add_prefix(string_data: list[str]) -> list[str]:
    return ['\\' + 'x' + datum for datum in string_data]


def make_module_string(string_data: list[str]) -> str:
    return PRE + "SOURCE: bin = b'" + ''.join(string_data) + "'\n" + POST


def save_to_file(file_name: str, data: str) -> None:
    with open(file_name, 'w') as handle:
        handle.write(data + '\n')


def main() -> None:
    source = input("Input image: ")
    destiny = input("Result module: ")
    prefixed = add_prefix(spliter(read_as_hex(source)))
    save_to_file(destiny, make_module_string(prefixed))


if __name__ == '__main__':
    main()
