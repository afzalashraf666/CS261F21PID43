import sys
import main
import time
import FileSys
import SortingAlgorithms
import SearchFilters
from threading import Thread
from UICode import *
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

sorting_instances = [
    SortingAlgorithms.MergeSort(),
    SortingAlgorithms.InsertionSort(),
    SortingAlgorithms.SelectionSort(),
    SortingAlgorithms.MergeSort(),
    SortingAlgorithms.BubbleSort(),
    SortingAlgorithms.QuickSort(),
    SortingAlgorithms.HeapSort(),
    SortingAlgorithms.CountingSort(),
    SortingAlgorithms.RadixSort(),
    SortingAlgorithms.BucketSort(),
    SortingAlgorithms.GnomeSort(),
    SortingAlgorithms.ShellSort(),
]

searching_instances = [
    SearchFilters.startsWith(),
    SearchFilters.startsWith(),
    SearchFilters.endsWith(),
    SearchFilters.contains(),
    SearchFilters.doesNotContain(),
]


class ScrappApp(Ui_ScrappApp):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)

        start = time.perf_counter()
        all_songs = FileSys.read_csv()
        end = time.perf_counter()
        time_taken = end - start

        self.showData(all_songs, time_taken)

        self.upDownSortWhole.clicked.connect(self.wholeSort)
        self.singleColSearchButton.clicked.connect(self.columnSeacrh)

    def showData(self, all_songs, time_taken):

        NumRows = len(all_songs)
        self.songsTable.setColumnCount(8)
        self.songsTable.setRowCount(NumRows)
        rows = 0
        header = self.songsTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)

        for song in all_songs:
            self.songsTable.setItem(
                rows, 0, QTableWidgetItem(str(song.all_attributes[1]))
            )
            self.songsTable.setItem(
                rows, 1, QTableWidgetItem(str(song.all_attributes[2]))
            )
            self.songsTable.setItem(
                rows, 2, QTableWidgetItem(str(song.all_attributes[3]))
            )
            self.songsTable.setItem(
                rows, 3, QTableWidgetItem(str(song.all_attributes[4]))
            )
            self.songsTable.setItem(
                rows, 4, QTableWidgetItem(str(song.all_attributes[5]))
            )
            self.songsTable.setItem(
                rows, 5, QTableWidgetItem(str(song.all_attributes[6]))
            )
            self.songsTable.setItem(
                rows, 6, QTableWidgetItem(str(song.all_attributes[7]))
            )
            self.songsTable.setItem(
                rows, 7, QTableWidgetItem(str(song.all_attributes[8]))
            )
            print("Row:", rows)
            rows += 1

        time_str = "Time Taken: " + str(time_taken) + " sec"
        print(time_str)
        self.time_lbl.setText(time_str)

        items_str = "Items Scrapped: " + str(len(all_songs))
        self.items_lbl.setText(items_str)

        print("Done")

    def wholeSort(self):

        global sorting_instances
        if self.reverseBox.isChecked() is False:
            all_data = FileSys.read_csv()
            instance = sorting_instances[int(self.sortingDropdown.currentIndex())]
            column = int(self.selectFilterPlusWholeSortColumn.currentIndex())
            print("Column:", column)

            start = time.perf_counter()
            instance.perform_sorting(all_data, column)
            end = time.perf_counter()
            time_taken = end - start

            sort_thread = Thread(target=self.showData, args=(all_data, time_taken))
            sort_thread.start()
            print("ComboxAscend:", (self.searchingDropdown.currentIndex()))

        elif self.reverseBox.isChecked() is True:
            all_data = FileSys.read_csv()
            instance = sorting_instances[int(self.sortingDropdown.currentIndex())]
            column = int(self.selectFilterPlusWholeSortColumn.currentIndex())
            print("Column:", column)

            start = time.perf_counter()
            instance.perform_sorting(all_data, column)
            all_data.reverse()
            end = time.perf_counter()
            time_taken = end - start

            sort_thread = Thread(target=self.showData, args=(all_data, time_taken))
            sort_thread.start()
            print("ComboxDescend:", (self.searchingDropdown.currentIndex()))

        print("----------------------")

    def columnSeacrh(self):
        results = []
        instance = searching_instances[int(self.selectFilter.currentIndex())]
        query = self.singleColSearchField.text()
        column = int(self.selectFilterPlusWholeSortColumn.currentIndex())
        results = instance.perform_search(FileSys.read_csv(), column, query)
        search_thread = Thread(target=self.showData, args=(results,))
        search_thread.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ScrappApp(Form)
    Form.show()
    app.exec_()
