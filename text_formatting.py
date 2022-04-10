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


@dataclass(frozen=True, slots=True)
class FormattingStyle:
    normalChar: str
    negationChar: str
    disjunction: str
    conjunction: str
    openingChar: str = ''
    closingChar: str = ''


class FormattingMeta(type):
    def __getitem__(cls, key: int) -> FormattingStyle:
        key_list = [value for value in dir(cls) if value[0] != '_']
        if len(key_list) - 1 < key or key < -len(key_list):
            raise IndexError('Formatting index out of index')
        return cls.__dict__[
            list(cls.__dict__['__annotations__'].keys())[key]]


class Formatting(metaclass=FormattingMeta):
    Mathematical: FormattingStyle = FormattingStyle('x', 'x̄', '', '+')
    Logical: FormattingStyle = FormattingStyle('x', '¬x', '∧', '∨', '(', ')')
    AltLogical: FormattingStyle = FormattingStyle(
        'x', '~x', '∧', '∨', '(', ')')
    Programmingbool: FormattingStyle = FormattingStyle('x', '!x', '&&', '||')
    Programmingwb: FormattingStyle = FormattingStyle('x', '!x', '&', '|')


@dataclass(eq=False)
class TextFormatter:
    mode: Formatting = Formatting.Mathematical

    def __subscribt(self, string: str) -> str:
        if string[-1] == '`':
            return f'{self.mode.negationChar}<sub>{string[:-1]}</sub>'
        return f'{self.mode.normalChar}<sub>{string}</sub>'

    def __modify_sentence(self, piece: str) -> str:
        return self.mode.openingChar + self.mode.disjunction.join(
            [self.__subscribt(x) for x in piece.split('x')[1:]]
        ) + self.mode.closingChar

    def __modify_text(self, line: str) -> list[str]:
        return [self.__modify_sentence(piece)
                for piece in line.split(' ') if piece != '+']

    def __call__(self, line: str) -> str:
        return f' {self.mode.conjunction} '.join(
            self.__modify_text(line))


def remove_subsribt(line: str) -> str:
    return (line.replace('<sub>', '').replace('</sub>', ''))
