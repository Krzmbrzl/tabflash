# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFormLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QSpacerItem, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.base_dir_label = QLabel(self.centralwidget)
        self.base_dir_label.setObjectName(u"base_dir_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.base_dir_label)

        self.base_dir_edit = QLineEdit(self.centralwidget)
        self.base_dir_edit.setObjectName(u"base_dir_edit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.base_dir_edit)

        self.mode_combo = QComboBox(self.centralwidget)
        self.mode_combo.addItem("")
        self.mode_combo.addItem("")
        self.mode_combo.setObjectName(u"mode_combo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_combo.sizePolicy().hasHeightForWidth())
        self.mode_combo.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.mode_combo)

        self.mode_label = QLabel(self.centralwidget)
        self.mode_label.setObjectName(u"mode_label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.mode_label)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.file_label = QLabel(self.centralwidget)
        self.file_label.setObjectName(u"file_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.file_label)

        self.file_combo = QComboBox(self.centralwidget)
        self.file_combo.setObjectName(u"file_combo")
        self.file_combo.setEnabled(False)
        sizePolicy.setHeightForWidth(self.file_combo.sizePolicy().hasHeightForWidth())
        self.file_combo.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.file_combo)

        self.sheet_label = QLabel(self.centralwidget)
        self.sheet_label.setObjectName(u"sheet_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.sheet_label)

        self.sheet_combo = QComboBox(self.centralwidget)
        self.sheet_combo.setObjectName(u"sheet_combo")
        self.sheet_combo.setEnabled(False)
        sizePolicy.setHeightForWidth(self.sheet_combo.sizePolicy().hasHeightForWidth())
        self.sheet_combo.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sheet_combo)


        self.horizontalLayout.addLayout(self.formLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setEnabled(False)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TabFlash", None))
        self.base_dir_label.setText(QCoreApplication.translate("MainWindow", u"Base dir", None))
        self.mode_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"View", None))
        self.mode_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Fill", None))

        self.mode_label.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.file_label.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.sheet_label.setText(QCoreApplication.translate("MainWindow", u"Sheet", None))
    # retranslateUi

