# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIDesigner.py'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScrappApp(object):
    def setupUi(self, ScrappApp):
        ScrappApp.setObjectName("ScrappApp")
        ScrappApp.resize(900, 680)
        ScrappApp.setMinimumSize(QtCore.QSize(900, 680))
        ScrappApp.setMaximumSize(QtCore.QSize(900, 680))
        self.column1 = QtWidgets.QComboBox(ScrappApp)
        self.column1.setGeometry(QtCore.QRect(30, 110, 101, 22))
        self.column1.setObjectName("column1")
        self.column1.addItem("")
        self.column1.addItem("")
        self.column1.addItem("")
        self.column1.addItem("")
        self.column1.addItem("")
        self.column1.addItem("")
        self.column1.addItem("")
        self.column1.addItem("")
        self.column1.addItem("")
        self.radioAND = QtWidgets.QRadioButton(ScrappApp)
        self.radioAND.setGeometry(QtCore.QRect(150, 90, 50, 17))
        self.radioAND.setObjectName("radioAND")
        self.radioOR = QtWidgets.QRadioButton(ScrappApp)
        self.radioOR.setGeometry(QtCore.QRect(150, 100, 50, 40))
        self.radioOR.setObjectName("radioOR")
        self.radioNOT = QtWidgets.QRadioButton(ScrappApp)
        self.radioNOT.setGeometry(QtCore.QRect(150, 130, 51, 17))
        self.radioNOT.setObjectName("radioNOT")
        self.sortingDropdown = QtWidgets.QComboBox(ScrappApp)
        self.sortingDropdown.setGeometry(QtCore.QRect(670, 150, 201, 31))
        self.sortingDropdown.setEditable(False)
        self.sortingDropdown.setCurrentText("")
        self.sortingDropdown.setDuplicatesEnabled(False)
        self.sortingDropdown.setObjectName("sortingDropdown")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.sortingDropdown.addItem("")
        self.searchingDropdown = QtWidgets.QComboBox(ScrappApp)
        self.searchingDropdown.setGeometry(QtCore.QRect(670, 110, 201, 31))
        self.searchingDropdown.setEditable(False)
        self.searchingDropdown.setCurrentText("")
        self.searchingDropdown.setDuplicatesEnabled(False)
        self.searchingDropdown.setObjectName("searchingDropdown")
        self.searchingDropdown.addItem("")
        self.searchingDropdown.addItem("")
        self.searchingDropdown.addItem("")
        self.searchingDropdown.addItem("")
        self.songsTable = QtWidgets.QTableWidget(ScrappApp)
        self.songsTable.setGeometry(QtCore.QRect(20, 250, 851, 341))
        self.songsTable.setMinimumSize(QtCore.QSize(0, 192))
        self.songsTable.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.songsTable.setAcceptDrops(False)
        self.songsTable.setAutoFillBackground(True)
        self.songsTable.setFrameShape(QtWidgets.QFrame.Box)
        self.songsTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.songsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.songsTable.setShowGrid(True)
        self.songsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.songsTable.setWordWrap(True)
        self.songsTable.setCornerButtonEnabled(True)
        self.songsTable.setRowCount(300000)
        self.songsTable.setColumnCount(8)
        self.songsTable.setObjectName("songsTable")
        item = QtWidgets.QTableWidgetItem()
        self.songsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.songsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.songsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.songsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.songsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.songsTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.songsTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.songsTable.setHorizontalHeaderItem(7, item)
        self.songsTable.horizontalHeader().setVisible(True)
        self.songsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.songsTable.horizontalHeader().setHighlightSections(True)
        self.songsTable.horizontalHeader().setStretchLastSection(True)
        self.songsTable.verticalHeader().setVisible(True)
        self.songsTable.verticalHeader().setCascadingSectionResizes(True)
        self.songsTable.verticalHeader().setHighlightSections(True)
        self.songsTable.verticalHeader().setMinimumSectionSize(20)
        self.songsTable.verticalHeader().setSortIndicatorShown(False)
        self.songsTable.verticalHeader().setStretchLastSection(True)
        self.progressBar = QtWidgets.QProgressBar(ScrappApp)
        self.progressBar.setGeometry(QtCore.QRect(120, 610, 351, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(ScrappApp)
        self.label.setGeometry(QtCore.QRect(50, 610, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.time_lbl = QtWidgets.QLabel(ScrappApp)
        self.time_lbl.setGeometry(QtCore.QRect(50, 650, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.time_lbl.setFont(font)
        self.time_lbl.setObjectName("time_lbl")
        self.startButton = QtWidgets.QPushButton(ScrappApp)
        self.startButton.setGeometry(QtCore.QRect(650, 610, 91, 31))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(ScrappApp)
        self.stopButton.setGeometry(QtCore.QRect(750, 610, 91, 31))
        self.stopButton.setObjectName("stopButton")
        self.logo = QtWidgets.QLabel(ScrappApp)
        self.logo.setGeometry(QtCore.QRect(280, 10, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setFrameShape(QtWidgets.QFrame.Panel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.column2 = QtWidgets.QComboBox(ScrappApp)
        self.column2.setGeometry(QtCore.QRect(210, 110, 101, 22))
        self.column2.setObjectName("column2")
        self.column2.addItem("")
        self.column2.addItem("")
        self.column2.addItem("")
        self.column2.addItem("")
        self.column2.addItem("")
        self.column2.addItem("")
        self.column2.addItem("")
        self.column2.addItem("")
        self.column2.addItem("")
        self.selectFilterPlusWholeSortColumn = QtWidgets.QComboBox(ScrappApp)
        self.selectFilterPlusWholeSortColumn.setGeometry(QtCore.QRect(60, 200, 191, 31))
        self.selectFilterPlusWholeSortColumn.setObjectName("selectFilterPlusWholeSortColumn")
        self.selectFilterPlusWholeSortColumn.addItem("")
        self.selectFilterPlusWholeSortColumn.addItem("")
        self.selectFilterPlusWholeSortColumn.addItem("")
        self.selectFilterPlusWholeSortColumn.addItem("")
        self.selectFilterPlusWholeSortColumn.addItem("")
        self.selectFilterPlusWholeSortColumn.addItem("")
        self.selectFilterPlusWholeSortColumn.addItem("")
        self.selectFilterPlusWholeSortColumn.addItem("")
        self.selectFilterPlusWholeSortColumn.addItem("")
        self.selectFilter = QtWidgets.QComboBox(ScrappApp)
        self.selectFilter.setGeometry(QtCore.QRect(270, 200, 201, 31))
        self.selectFilter.setObjectName("selectFilter")
        self.selectFilter.addItem("")
        self.selectFilter.addItem("")
        self.selectFilter.addItem("")
        self.selectFilter.addItem("")
        self.selectFilter.addItem("")
        self.singleColSearchField = QtWidgets.QLineEdit(ScrappApp)
        self.singleColSearchField.setGeometry(QtCore.QRect(480, 200, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(12)
        self.singleColSearchField.setFont(font)
        self.singleColSearchField.setObjectName("singleColSearchField")
        self.singleColSearchButton = QtWidgets.QPushButton(ScrappApp)
        self.singleColSearchButton.setGeometry(QtCore.QRect(690, 200, 96, 31))
        self.singleColSearchButton.setMinimumSize(QtCore.QSize(96, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.singleColSearchButton.setFont(font)
        self.singleColSearchButton.setAutoRepeatInterval(100)
        self.singleColSearchButton.setAutoDefault(False)
        self.singleColSearchButton.setDefault(False)
        self.singleColSearchButton.setFlat(False)
        self.singleColSearchButton.setObjectName("singleColSearchButton")
        self.line = QtWidgets.QFrame(ScrappApp)
        self.line.setGeometry(QtCore.QRect(20, 180, 851, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(ScrappApp)
        self.line_2.setGeometry(QtCore.QRect(20, 230, 851, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(ScrappApp)
        self.line_3.setGeometry(QtCore.QRect(20, 590, 851, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.items_lbl = QtWidgets.QLabel(ScrappApp)
        self.items_lbl.setGeometry(QtCore.QRect(250, 650, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.items_lbl.setFont(font)
        self.items_lbl.setObjectName("items_lbl")
        self.colSearchField = QtWidgets.QLineEdit(ScrappApp)
        self.colSearchField.setGeometry(QtCore.QRect(340, 110, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(12)
        self.colSearchField.setFont(font)
        self.colSearchField.setObjectName("colSearchField")
        self.colSearchButton = QtWidgets.QPushButton(ScrappApp)
        self.colSearchButton.setGeometry(QtCore.QRect(450, 150, 96, 31))
        self.colSearchButton.setMinimumSize(QtCore.QSize(96, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.colSearchButton.setFont(font)
        self.colSearchButton.setAutoRepeatInterval(100)
        self.colSearchButton.setAutoDefault(False)
        self.colSearchButton.setDefault(False)
        self.colSearchButton.setFlat(False)
        self.colSearchButton.setObjectName("colSearchButton")
        self.upDownSortSingle = QtWidgets.QPushButton(ScrappApp)
        self.upDownSortSingle.setGeometry(QtCore.QRect(790, 200, 41, 31))
        self.upDownSortSingle.setObjectName("upDownSortSingle")
        self.upDownSortWhole = QtWidgets.QPushButton(ScrappApp)
        self.upDownSortWhole.setGeometry(QtCore.QRect(620, 150, 41, 31))
        self.upDownSortWhole.setObjectName("upDownSortWhole")

        self.retranslateUi(ScrappApp)
        QtCore.QMetaObject.connectSlotsByName(ScrappApp)

    def retranslateUi(self, ScrappApp):
        _translate = QtCore.QCoreApplication.translate
        ScrappApp.setWindowTitle(_translate("ScrappApp", "Music Data Scraping"))
        self.column1.setItemText(0, _translate("ScrappApp", "Column 1"))
        self.column1.setItemText(1, _translate("ScrappApp", "Song name"))
        self.column1.setItemText(2, _translate("ScrappApp", "Artist name"))
        self.column1.setItemText(3, _translate("ScrappApp", "Views"))
        self.column1.setItemText(4, _translate("ScrappApp", "Likes"))
        self.column1.setItemText(5, _translate("ScrappApp", "Comments"))
        self.column1.setItemText(6, _translate("ScrappApp", "Reposts"))
        self.column1.setItemText(7, _translate("ScrappApp", "Rel. Date"))
        self.column1.setItemText(8, _translate("ScrappApp", "Genre"))
        self.radioAND.setText(_translate("ScrappApp", "AND"))
        self.radioOR.setText(_translate("ScrappApp", "OR"))
        self.radioNOT.setText(_translate("ScrappApp", "NOT"))
        self.sortingDropdown.setPlaceholderText(_translate("ScrappApp", "Select Sorting Algorithm"))
        self.sortingDropdown.setItemText(0, _translate("ScrappApp", "Select Sorting Algorithm"))
        self.sortingDropdown.setItemText(1, _translate("ScrappApp", "Insertion Sort"))
        self.sortingDropdown.setItemText(2, _translate("ScrappApp", "Selection Sort"))
        self.sortingDropdown.setItemText(3, _translate("ScrappApp", "Merge Sort"))
        self.sortingDropdown.setItemText(4, _translate("ScrappApp", "Bubble Sort"))
        self.sortingDropdown.setItemText(5, _translate("ScrappApp", "Quick Sort"))
        self.sortingDropdown.setItemText(6, _translate("ScrappApp", "Heap Sort"))
        self.sortingDropdown.setItemText(7, _translate("ScrappApp", "Counting Sort"))
        self.sortingDropdown.setItemText(8, _translate("ScrappApp", "Radix Sort"))
        self.sortingDropdown.setItemText(9, _translate("ScrappApp", "Bucket Sort"))
        self.sortingDropdown.setItemText(10, _translate("ScrappApp", "Gnome Sort"))
        self.sortingDropdown.setItemText(11, _translate("ScrappApp", "Shell Sort"))
        self.searchingDropdown.setPlaceholderText(_translate("ScrappApp", "Select Sorting Algorithm"))
        self.searchingDropdown.setItemText(0, _translate("ScrappApp", "Select Searching Algorithm"))
        self.searchingDropdown.setItemText(1, _translate("ScrappApp", "Linear Search"))
        self.searchingDropdown.setItemText(2, _translate("ScrappApp", "Binary Search"))
        self.searchingDropdown.setItemText(3, _translate("ScrappApp", "Jump Search"))
        self.songsTable.setSortingEnabled(False)
        item = self.songsTable.horizontalHeaderItem(0)
        item.setText(_translate("ScrappApp", "Song name"))
        item = self.songsTable.horizontalHeaderItem(1)
        item.setText(_translate("ScrappApp", "Artist name"))
        item = self.songsTable.horizontalHeaderItem(2)
        item.setText(_translate("ScrappApp", "Views"))
        item = self.songsTable.horizontalHeaderItem(3)
        item.setText(_translate("ScrappApp", "Likes"))
        item = self.songsTable.horizontalHeaderItem(4)
        item.setText(_translate("ScrappApp", "Comments"))
        item = self.songsTable.horizontalHeaderItem(5)
        item.setText(_translate("ScrappApp", "Reposts"))
        item = self.songsTable.horizontalHeaderItem(6)
        item.setText(_translate("ScrappApp", "Rel. Date"))
        item = self.songsTable.horizontalHeaderItem(7)
        item.setText(_translate("ScrappApp", "Genre"))
        self.label.setText(_translate("ScrappApp", "Progress:"))
        self.time_lbl.setText(_translate("ScrappApp", "Time Taken: 62ms"))
        self.startButton.setText(_translate("ScrappApp", "START"))
        self.stopButton.setText(_translate("ScrappApp", "STOP"))
        self.logo.setText(_translate("ScrappApp", "Music Data Scraping"))
        self.column2.setItemText(0, _translate("ScrappApp", "Column 2"))
        self.column2.setItemText(1, _translate("ScrappApp", "Song name"))
        self.column2.setItemText(2, _translate("ScrappApp", "Artist name"))
        self.column2.setItemText(3, _translate("ScrappApp", "Views"))
        self.column2.setItemText(4, _translate("ScrappApp", "Likes"))
        self.column2.setItemText(5, _translate("ScrappApp", "Comments"))
        self.column2.setItemText(6, _translate("ScrappApp", "Reposts"))
        self.column2.setItemText(7, _translate("ScrappApp", "Rel. Date"))
        self.column2.setItemText(8, _translate("ScrappApp", "Genre"))
        self.selectFilterPlusWholeSortColumn.setItemText(0, _translate("ScrappApp", "Select Column to filter"))
        self.selectFilterPlusWholeSortColumn.setItemText(1, _translate("ScrappApp", "Song name"))
        self.selectFilterPlusWholeSortColumn.setItemText(2, _translate("ScrappApp", "Artist name"))
        self.selectFilterPlusWholeSortColumn.setItemText(3, _translate("ScrappApp", "Views"))
        self.selectFilterPlusWholeSortColumn.setItemText(4, _translate("ScrappApp", "Likes"))
        self.selectFilterPlusWholeSortColumn.setItemText(5, _translate("ScrappApp", "Comments"))
        self.selectFilterPlusWholeSortColumn.setItemText(6, _translate("ScrappApp", "Reposts"))
        self.selectFilterPlusWholeSortColumn.setItemText(7, _translate("ScrappApp", "Rel. Date"))
        self.selectFilterPlusWholeSortColumn.setItemText(8, _translate("ScrappApp", "Genre"))
        self.selectFilter.setItemText(0, _translate("ScrappApp", "Select Filter"))
        self.selectFilter.setItemText(1, _translate("ScrappApp", "Starts with"))
        self.selectFilter.setItemText(2, _translate("ScrappApp", "Ends with"))
        self.selectFilter.setItemText(3, _translate("ScrappApp", "Contains"))
        self.selectFilter.setItemText(4, _translate("ScrappApp", "Does not contain"))
        self.singleColSearchField.setPlaceholderText(_translate("ScrappApp", "Enter query"))
        self.singleColSearchButton.setText(_translate("ScrappApp", "Search"))
        self.items_lbl.setText(_translate("ScrappApp", "Items Scrapped: 300"))
        self.colSearchField.setPlaceholderText(_translate("ScrappApp", "Search in multiple columns"))
        self.colSearchButton.setText(_translate("ScrappApp", "Search"))
        self.upDownSortSingle.setText(_translate("ScrappApp", "▲"))
        self.upDownSortWhole.setText(_translate("ScrappApp", "▲"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScrappApp = QtWidgets.QWidget()
    ui = Ui_ScrappApp()
    ui.setupUi(ScrappApp)
    ScrappApp.show()
    sys.exit(app.exec_())
