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


from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QListWidgetItem,
    QLabel,
    QFileDialog
)
from PySide6.QtCore import Slot

import sys

from ui_layout import Ui_Form
from parsing import parse, InputDTO
from ekspansja import InvalidInputException, systematic, heuristic
from text_formatting import TextFormatter, Formatting, remove_subsribt
from fileio import read_from_file, save_to_file
from logo import generate_icon


Labels: list[str] = ['s', 'ms', 'μs']


class MainWindow(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)
        self.__ui.stack.setCurrentIndex(1)
        self.__set_connections()
        self.__set_variables()
        self.setWindowIcon(generate_icon())

    def __set_connections(self) -> None:
        self.__ui.process.clicked.connect(self.__minimize)
        self.__ui.filebutton.clicked.connect(self.__read_from_file)
        self.__ui.savebutton.clicked.connect(self.__save_to_file)
        self.__ui.comboBox.currentIndexChanged.connect(self.__change_format)
        self.__ui.methodbox.currentIndexChanged.connect(self.__change_executor)

    def __set_variables(self) -> None:
        self.__last_value = None
        self.__format = TextFormatter()
        self.__executor = systematic

    def __read_from_file(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self,
            self.tr("Wczytaj plik"),
            self.tr("~/Desktop/"),
            self.tr("Pliki tekstowe (*.txt)"))
        if (file := read_from_file(path)):
            self.__ui.ledit.setText(file[0])
            self.__ui.redit.setText(file[1])
        else:
            self.__error_message('Nie udało się wczytać pliku')

    def __for_widget_in_list(self):
        for i in range(self.__ui.list.count()):
            yield self.__ui.list.itemWidget(self.__ui.list.item(i))

    @Slot(int)
    def __change_format(self, index: int) -> None:
        self.__format.mode = Formatting[index]
        self.__print_output()

    @Slot(int)
    def __change_executor(self, index: int) -> None:
        self.__executor = systematic if index == 0 else heuristic

    def __save_to_file(self) -> None:
        path, _ = QFileDialog.getSaveFileName(
            self,
            self.tr("Wczytaj plik"),
            self.tr("~/Desktop/"),
            self.tr("Pliki tekstowe (*.txt)"))
        if not save_to_file(path, [remove_subsribt(label.text())
                            for label in self.__for_widget_in_list()]):
            self.__error_message('Nie udało się zapisać do pliku')

    def __add_item_to_list(self, label: str) -> None:
        item = QListWidgetItem()
        self.__ui.list.addItem(item)
        self.__ui.list.setItemWidget(
            item, QLabel(self.__format(label)))

    def __print_output(self) -> None:
        self.__ui.stack.setCurrentIndex(0)
        self.__ui.list.clear()
        if isinstance(self.__last_value, list):
            for line in self.__last_value:
                self.__add_item_to_list(line)
        else:
            self.__add_item_to_list(self.__last_value)

    def __print_time(self, time: float) -> None:
        timestr = f'{int(time * 10 ** (3 * len(Labels))):,}'.replace(
            ',', '{} ') + '{}'
        self.__ui.timelabel.setText(timestr.format(
            *Labels[(len(Labels) - timestr.count('{')):]))

    def __error_message(self, message: str) -> None:
        self.__ui.stack.setCurrentIndex(1)
        self.__ui.err.setText(
            f'<p style="color:red">{message}</p>')

    def __call_logic(self, dto: InputDTO) -> None:
        try:
            self.__last_value, time = self.__executor(dto.first, dto.second)
            self.__print_time(time)
            self.__print_output()
        except InvalidInputException:
            self.__error_message('Nieprawidłowe dane wejściowe')

    def __minimize(self) -> None:
        first = self.__ui.ledit.text()
        second = self.__ui.redit.text()
        if (dto := parse(first, second)):
            self.__call_logic(dto)
        else:
            self.__error_message('Nieprawidłowe dane wejściowe')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
