# This file is part of memmer. Use of this source code is
# governed by a BSD-style license that can be found in the
# LICENSE file at the root of the source tree or at
# <https://github.com/Krzmbrzl/memmer/blob/main/LICENSE>.

from .compiled_ui_files.ui_MainWindow import Ui_MainWindow

from typing import Optional

import os
from pathlib import Path

from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QListWidgetItem

import pyexcel


def is_notes_sheet(sheet) -> bool:
    # A notes sheet ends in '_Notes' and only contains a single column
    return sheet.name.endswith("_Notes") and all((len(x) == 1 for x in sheet))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, base_path: Optional[str] = None, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.__connect_signals()

        self.__init_state(base_path)

    def __connect_signals(self):
        self.base_dir_edit.textChanged.connect(self.__base_dir_changed)

        self.mode_combo.currentIndexChanged.connect(self.__mode_changed)

        self.file_combo.currentIndexChanged.connect(self.__file_changed)

        self.sheet_combo.currentIndexChanged.connect(self.__sheet_changed)

    def __init_state(self, base_path: Optional[str]):
        self.setWindowTitle("TabFlash")

        self.note_list.setVisible(False)

        if base_path:
            self.base_dir_edit.setText(base_path)

    def __base_dir_changed(self, path: str):
        self.file_combo.clear()
        self.file_combo.setEnabled(False)
        self.sheet_combo.clear()
        self.sheet_combo.setEnabled(False)

        if not os.path.isdir(path):
            return

        base = Path(path)
        files = base.glob("**/*")
        files = [
            str(x.relative_to(base))
            for x in files
            if x.is_file() and not x.name.startswith(".")
        ]

        files.sort()

        if len(files) > 0:
            self.file_combo.setEnabled(True)
            self.file_combo.addItems(files)
            self.file_combo.setCurrentIndex(0)

    def __mode_changed(self, mode_idx: int):
        pass

    def __file_changed(self, file_idx: int):
        self.sheet_combo.setEnabled(False)
        self.sheet_combo.clear()

        try:
            self.spreadsheet = pyexcel.get_book(
                file_name=Path(self.base_dir_edit.text())
                / self.file_combo.itemText(file_idx)
            )

            sheet_names = self.spreadsheet.sheet_names()

            self.sheet_combo.setEnabled(True)

            for current in sheet_names:
                if is_notes_sheet(self.spreadsheet.sheet_by_name(current)):
                    # Special note sheet
                    continue

                self.sheet_combo.addItem(current)

            self.sheet_combo.setCurrentIndex(0)
        except:
            pass

    def __sheet_changed(self, sheet_idx: int):
        assert self.spreadsheet is not None

        # Note: The index is given as if no note sheets existed. Hence, the need
        # for this quirky looking sheet selection.
        sheet = None
        for current_sheet in self.spreadsheet:
            if is_notes_sheet(current_sheet):
                continue
            if sheet_idx == 0:
                sheet = current_sheet
                break

            sheet_idx -= 1

        assert sheet is not None

        if sheet is None:
            return

        self.table.setEnabled(True)

        rows = [x for x in sheet]

        nrows = len(rows)
        ncols = max((len(x) for x in rows))

        self.table.setRowCount(nrows - 1 if nrows > 1 else 0)
        self.table.setColumnCount(ncols)

        if nrows > 1:
            self.table.setHorizontalHeaderLabels(rows[0])

            nrows -= 1
            del rows[0]

            self.table.horizontalHeader().show()
        else:
            self.table.horizontalHeader().hide()

        for row in range(nrows):
            for col in range(ncols):
                self.table.setItem(row, col, QTableWidgetItem(str(rows[row][col])))

        # Note: the order is important!
        # We first make the columns wide enough to contain the text in its full width
        # Then we make the rows high enough to account for potential multiline content
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        notes_name = sheet.name + "_Notes"
        if notes_name in self.spreadsheet.sheet_names():
            note_sheet = self.spreadsheet.sheet_by_name(notes_name)

            if is_notes_sheet(note_sheet):
                self.note_list.clear()

                for current in note_sheet:
                    self.note_list.addItem(QListWidgetItem(str(current[0])))

                self.note_list.setVisible(True)
        else:
            self.note_list.setVisible(False)
