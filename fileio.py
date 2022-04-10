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


def read_from_file(file_name: str) -> tuple[str] | None:
    try:
        with open(file_name, 'r') as handle:
            data = list(handle)
            return data if len(data) == 2 else None
    except Exception:
        return None


def save_to_file(file_name: str, data: list[str]) -> bool:
    try:
        with open(file_name, 'w', encoding='utf-8') as handle:
            for line in data:
                handle.write(line + '\n')
            return True
    except Exception:
        return False
