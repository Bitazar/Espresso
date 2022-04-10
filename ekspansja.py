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


from typing import List, Callable, Tuple
from itertools import chain, combinations
from copy import deepcopy

import numpy as np

from timing import benchmark

Matrix = List[List[bool]]


# fill f and r lists here
f = [0, 1, 3, 7, 8, 12]
r = [2, 4, 6, 9, 15]


class InvalidInputException(Exception):
    def __init__(self) -> None:
        super().__init__('Invalid input data')


class UndefinedBehaviourException(Exception):
    def __init__(self) -> None:
        super().__init__('Undefined behaviour has been obserbed')


def data_validation(first: List[int], second: List[int]) -> bool:
    """
    This function checks if intersection of given lists are empty and
    if the lowest value of both lists are greater than 0
    :param first: first list to be checked
    :type first: list of ints
    :param second: second list to be checked
    :type second: list of ints
    :returns: None
    :raises InvalidInputException: when given data is invalid
    """
    return list(set(first) & set(second)) or min(chain(first, second)) < 0


def bit_length(*sequences: List[int]) -> int:
    """
    This function returns binary lenght of the greatest int in given lists
    :param sequences: just a numbers
    :type sequences: lists of ints
    :returns: binary length of the greatest element
    :rtype: int
    """
    return len(bin(max(chain(*sequences)))) - 2


def one_and_zeros_to_True_and_False(line: str) -> List[bool]:
    """
    This function converts string of one and zerios into a list of
    True or False
    :param line: string containing only one and zeros
    :type line: str
    :returns: list of True or False
    :rtype: list of bools
    """
    return [True if char == '1' else False for char in line]


def parse_input(sequence: List[int], length: int) -> Matrix:
    """
    This function converts int inputs into it's "True False" form of given length
    :param sequence: List of given inputs from F or R
    :type sequence: list of ints
    :param length: Number of bits of max from F and R
    :type length: int
    :returns: List of strings containing binary form of inputs
    :rtype: list of strs
    """
    return [one_and_zeros_to_True_and_False(f'{bin(bits)[2:]:0>{length}}')
            for bits in sequence]


def bit_swaping(sequence: Matrix, swapper: str) -> Matrix:
    """
    This function swapping '1' and '0' in proper index of every element
    in sequence if under corresponding index in swapper is '1'
    :param sequence: list of strings, all the same length representing binary
        forms of numbers
    :type sequence: list of str
    :param swapper: string consisting of '0' and '1' of the same length as
        every element in sequence
    :type swapper: str
    :returns: list of strings of the same size as given but with swapped
        suitable indexes
    :rtype: list of str
    """
    for i, bit in enumerate(swapper):
        if bit:
            for j in range(len(sequence)):
                sequence[j][i] = not sequence[j][i]
    return sequence


def list_sorting(sequence: Matrix) -> Matrix:
    """
    This function sorts list of strings first by number of '1' in then
    second by value of them
    :param sequence: list of strings, all the same length representing
        binary forms of numbers
    :type sequence: list of str
    :returns: Sorted list of strings
    :rtype: list od str
    """
    return sorted(sequence, key=lambda x: (x.count(True), x))


def line_strength(left: str, right: str) -> bool:
    """
    This function check if rihgt has ones in the same spots as left
    left and right must have same length
    :param left: potentially 'stronger' line
    :type left: str
    :param right: potentially 'weaker' line
    :type right: str
    :returns: False if right don't have one in all corresponding places
    :rtype: bool
    """
    for lchar, rchar in zip(left, right):
        if lchar and not rchar:
            return False
    return True


def line_parsing(sequence: Matrix) -> Matrix:
    """
    This function removes unnecesary lines from matrix
    :param sequence: list of strings, all the same length representing binary
        forms of numbers
    :type sequence: list of str
    :returns: parsed sequence
    :rtype: list of str
    """
    for i, comp in enumerate(sequence):
        for j in range(len(sequence) - 1, i, -1):
            if line_strength(comp, sequence[j]):
                del sequence[j]
    return sequence


def get_column_count(columns: Matrix) -> Matrix:
    """
    This function return number of '1' in each column of given list of strings
    column mean collection of i index from every string in given list
    :param columns: list of strings, all the same length representing binary
        forms of numbers
    :type columns: list of str
    :returns: number of '1' in each column
    :rtype: list of int
    """
    return [list(column).count(True) for column in columns]


def column_sorting(columns: Matrix) -> Matrix:
    """
    This function sorts column form left to right by number of '1' in each
        column
    (columns containing the most '1' are in the left)
    :param columns: list of strings, all the same length representing
        binary forms of numbers
    :type columns: list of str
    :returns: sorted list of input
    :rtype: list of str
    """
    return np.array([x for x, _ in list(sorted(zip(columns,
                    get_column_count(columns)),
                    key=lambda x: x[1], reverse=True))])


def label_setting(swapper: str) -> List[str]:
    """
    This function is setting a label
    :param swapper: one element of F cube
    :type swapper: str
    :returns: label
    :rtype: list of str
    """
    return list(reversed([f'L{i}' if x else f'L{i}`'
                for i, x in enumerate(reversed(swapper))]))


def label_sorting(label: List[str], count: List[int]) -> List[str]:
    """
    This function forts labels in te same way as columns are sorted
    :param label: just a labels
    :type label: list of str
    :param count: count of ones in each column
    :type count: list of int
    :returns: sorted labels
    :rtype: list of str
    """
    return [x for x, _ in
            sorted(zip(label, count), key=lambda x: x[1], reverse=True)]


def remove_column(sequence: Matrix, index: int) -> None:
    """
    This function remove column of a given index from a cube
    :param sequence: b cube
    :type sequence: matrix
    :param index: index of comuln to be removed
    :type index: int
    """
    for column in sequence:
        del column[index]


def get_column(sequnece: Matrix, index: int) -> List[bool]:
    """
    This function retunrs comumn of a given index
    :param sequence: b cube
    :type sequence: matrix
    :param index: index o column to be returned
    :type index: int
    :returns: column of a given index
    :rtype: list of bools
    """
    return [row[index] for row in sequnece]


def print_matrix(sequence: Matrix) -> None:
    """
    This function was used to print matrixes in more
    familiar form in the console
    :param sequence: matrix to be printed
    :type sequence: matrix
    """
    result = ''
    for row in sequence:
        result += '"'
        for bit in row:
            result += '1' if bit else '0'
        result += '", '
    print('[' + result[:-2] + ']')


def pre_parsing_column(sequence: Matrix, label: List[str]) -> List[str]:
    """
    This function removes columns which contain only zeros
    removes rows which contain only one one and return label of it one
    :param sequence: b cube
    :type sequence: matrix
    :param label: sorted label
    :type label: list of str
    :returns: must be laleb in all impicants if such a one exists
    :rtype: list of str
    """
    minimal = []
    for i in reversed(range(len(sequence[0]))):
        if not any(get_column(sequence, i)):
            remove_column(sequence, i)
            del label[i]
    for i in reversed(range(len(sequence))):
        count = sequence[i].count(True)
        if not count:
            raise UndefinedBehaviourException()
        if count == 1:
            index = sequence[i].index(True)
            minimal.append(label.pop(index))
            del sequence[i]
            remove_column(sequence, index)
    return minimal


def is_ones(sequence: Matrix, label: List[str], combi: List[str]) -> List[str]:
    """
    This function chcecs if any of given combinations covers all row if yes
    returns all combinations which matche the requirements
    :param sequence: b matrix
    :type sequence: matrix
    :param label: labels
    :type label: list of str
    :param combi: combinations of labels of the same length
    :type combi: list of str
    :returns: list containing combinations which match the
        requirements or empty list
    :rtype: list of str or empty list
    """
    output = []
    for possible in list(combi):
        hold = sequence[:]
        for check in possible:
            if hold:
                for i in range(len(label)):
                    if label[i] == check:
                        for k in reversed(range(len(hold))):
                            if hold[k][i]:
                                del hold[k]
        if not hold:
            output.append(possible)
    return output


def output_parsing(output: List[List[str]]) -> List[str]:
    """
    This function parse implicants
    :param output: list of strings whcich have to be joined together
    :type output: list of list of str
    :returns: joined list
    :rtype: list of str
    """
    return list(dict.fromkeys(['x' + 'x'.join(line) for line in output]))


def implicants(outputparsed: List[str]) -> List[List[str]]:
    """
    This function split implicants by x
    :param outputparsed: list of implicants
    :type outputparsed: list of str
    :returns: separated implicants
    :rtype: list of list of str
    """
    return [item.split('x')[1:] for item in outputparsed]


def implicants_binary(implicants: List[str], length: int) -> List[List[str]]:
    """
    This function change implicants into "cube form"
    :param implicants: just implicants
    :type implicants: list of str
    :param length: bit length of the grates number
    :type length: int
    :returns: "cube form" of inputs
    :rtype: list of list of str
    """
    hold = []
    for implicant in implicants:
        hold.append(list())
        x = 0
        for j in reversed(range(0, length)):
            if x < len(implicant):
                if int(implicant[x][0]) == j:
                    hold[-1].append(True if len(implicant[x]) == 1 else False)
                    x += 1
                else:
                    hold[-1].append('*')
            else:
                hold[-1].append('*')
    return hold


def row_setting(sequence: Matrix, label: str) -> bool:
    """
    This function set a row of last matrix
    :param sequence: list of implicants formed to a matrix
    :type sequence: matrix
    :param label: list of implicants
    :type label: list of str
    :param i, j: look at last_matrix_setting() function
    :type label: list of str
    :returns: True or False
    :rtype: bool
    """
    for k in range(len(sequence)):
        if '*' != label[k] != sequence[k]:
            return False
    return True


def last_matrix_setting(sequences: Matrix, labels: List[str]) -> Matrix:
    """
    This function sets last matrix wchich must be to processed
    :param sequence: list of implicants formed to a matrix
    :type sequence: matrix
    :param label: list of implicants
    :type label: list of str
    :returns: last matrix
    :rtype: matrix
    """
    return [[row_setting(sequence, label) for label in labels]
            for sequence in sequences]


def label_combinations(labels: List[str], columns: Matrix) -> List[str]:
    """
    This function returns implicants for each line of f matrix
    :param labels: labels of matrix(stripped)
    :type labels: list of str
    :param columns: b matrix(strippend)
    :type columns: matrix
    :returns: list of implicants which needs to be merged if needed
    :rtype: list of str
    """
    for i in range(1, len(labels)):
        if (combination := is_ones(columns, labels, combinations(labels, i))):
            return combination
    raise Exception()


def labels_string(value: List[str], predone: List[str]) -> str:
    """
    This function creates output
    :param value: implicants have to be add
    :type value: list of str
    :param predone: list of must be implicants
    :type predone: list of str
    :returns: joined string
    :rtype: str
    """
    output = ''.join(value)
    output += ' + ' if value and predone else ''
    return output + ' + '.join(predone)


def predone_string(predone: List[str]) -> str:
    """
    This function also creates output
    :param predone: list of must be implicants
    :type predone: list of str
    :returns: joined string or nothing
    :rtype: str or None
    """
    return ' + '.join(predone)


def joining_implicants(
        sequence: Matrix,
        label: List[str],
        not_labels_join: Callable[[List[str]], str],
        lables_join: Callable[[List[str], List[str]], str]
        ) -> Tuple[List[str], bool]:
    """
    This function
    :param sequence:
    :type sequence:
    :param label:
    :type label:
    :param not_labels_join: function called when label list is empty
    :type not_labels_join: callable[[list[str]], str]
    :param lables_join: function called when label list is not empty
    :type lables_join: callable[[list[str], list[str]], str]
    :returns:
    :rtype:
    """
    columns = np.transpose(line_parsing(list_sorting(sequence)))
    labels = label_sorting(label, get_column_count(columns))
    columns = [list(x) for x in np.transpose(column_sorting(columns))]
    predone = pre_parsing_column(columns, labels)
    if not labels:
        return not_labels_join(predone), False
    return [lables_join(value, predone)
            for value in label_combinations(labels, columns)], True


def prepare_input(
        first: List[int],
        second: List[int]
        ) -> Tuple[Matrix, Matrix]:
    """
    This function converts F and R lists into a tuple of F and R matrixes
    :param first: list of int
    :type first: F indexes
    :param second: list of int
    :type second: R indexes
    :returns: F and R cubes
    :rtype: tuple of matrixes
    """
    if data_validation(first, second):
        raise InvalidInputException()
    nobits = bit_length(first, second)
    return parse_input(first, nobits), parse_input(second, nobits)


def first_part(
        fmatrix: List[int],
        rmatrix: List[int],
        inserter: Callable[[list[str], bool, str | list[str]], None]
        ) -> List[List[str]]:
    """
    This function return all implicants
    :param first: F indexes
    :type first: list of int
    :param second: R indexes
    :type second: list of int
    :returns: all implicants
    :rtype: list of list of str
    """
    output = []
    for line in fmatrix:
        bmatrix = bit_swaping(deepcopy(rmatrix), line)
        result, flag = joining_implicants(bmatrix, label_setting(line),
                                          ''.join,
                                          lambda x, y: ''.join(x) + ''.join(y))
        inserter(output, flag, result)
    return [sorted(line.split('L')[1:], reverse=True) for line in output]


def append_or_extend(
        output: list[str],
        flag: bool,
        result: str | list[str]
        ) -> None:
    if flag:
        output.extend(result)
    else:
        output.append(result)


@benchmark
def systematic(first: List[int], second: List[int]) -> List[str]:
    """
    This function return optimalized function
    :param first: F indexes
    :type first: list of int
    :param second: R indexes
    :type second: list of int
    :returns: optimalized function
    :rtype: list of str
    """
    n = bit_length(first, second)
    op = output_parsing(first_part(*prepare_input(first, second),
                        append_or_extend))
    return joining_implicants(last_matrix_setting(parse_input(first, n),
                              implicants_binary(implicants(op), n)),
                              op, predone_string, labels_string)[0]


def generate_first_output(
        first_output: list[list[str]],
        fmatrix: Matrix,
        length: int
        ) -> list[list[str]]:
    parsed, output = output_parsing(first_output), []
    for implicant in implicants_binary(implicants(parsed), length):
        for i, row in reversed(list(enumerate(fmatrix))):
            if row_setting(row, implicant):
                output.append(implicant)
                fmatrix.pop(i)
    return output


def for_first_output(
        line: str,
        length: int
        ) -> list[str]:
    result = []
    for i, char in enumerate(line):
        if char != '*':
            h = length - i - 1
            result.append(f'{h}' if char else f'{h}`')
    return result


@benchmark
def heuristic(first: List[int], second: List[int]) -> List[str]:
    fmatrix, rmatrix = prepare_input(first, second)
    temp = first_part(fmatrix, rmatrix,
                      lambda o, f, r: o.append(r[0] if f else r))
    n = bit_length(first, second)
    s_output = [for_first_output(line, n)
                for line in generate_first_output(temp, fmatrix, n)]
    return ' + '.join(output_parsing(s_output))


def main() -> None:
    print(systematic(f, r))
    print(heuristic(f, r))


if __name__ == '__main__':
    main()
