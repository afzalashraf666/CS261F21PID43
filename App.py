import sys
import main
import FileSys
import SortingAlgorithms
import SearchFilters
import threading
from UICode import *
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

singleBool = False
sorting_instances = [ SortingAlgorithms.MergeSort(), SortingAlgorithms.InsertionSort(), SortingAlgorithms.SelectionSort(), SortingAlgorithms.MergeSort(),
                      SortingAlgorithms.BubbleSort(), SortingAlgorithms.QuickSort(), SortingAlgorithms.HeapSort(), SortingAlgorithms.CountingSort(),
                      SortingAlgorithms.RadixSort(), SortingAlgorithms.BucketSort(), SortingAlgorithms.GnomeSort(), SortingAlgorithms.ShellSort() ]
type_instances = [str, str, int, int, int, int, int, str]
class ScrappApp(Ui_ScrappApp):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)
        self.upDownSortWhole.clicked.connect(self.wholeSort)
        self.singleColSearchButton.clicked.connect(self.columnSearch)

    def showData(self, all_songs):
        
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
            self.songsTable.setItem(rows, 0, QTableWidgetItem(str(song.all_attributes[1])))
            self.songsTable.setItem(rows, 1, QTableWidgetItem(str(song.all_attributes[2])))
            self.songsTable.setItem(rows, 2, QTableWidgetItem(str(song.all_attributes[3])))
            self.songsTable.setItem(rows, 3, QTableWidgetItem(str(song.all_attributes[4])))
            self.songsTable.setItem(rows, 4, QTableWidgetItem(str(song.all_attributes[5])))
            self.songsTable.setItem(rows, 5, QTableWidgetItem(str(song.all_attributes[6])))
            self.songsTable.setItem(rows, 6, QTableWidgetItem(str(song.all_attributes[7])))
            self.songsTable.setItem(rows, 7, QTableWidgetItem(str(song.all_attributes[8])))
            
            rows += 1
    
    def wholeSort(self):
        global singleBool
        global sorting_instances
        if singleBool is False:
            singleBool = True
            all_data = FileSys.read_csv()
            print("Combox:" , (self.sortingDropdown.currentIndex()))
            instance = sorting_instances[int(self.sortingDropdown.currentIndex())]
            column = int(self.selectFilterPlusWholeSortColumn.currentIndex())
            print("Column:" , column)
            self.upDownSortWhole.setText("▼")
            sort_thread = threading.Thread(target=instance.perform_sorting, args=(all_data, column))
            sort_thread.start()
            self.showData(all_data)
            print("Combox:" , (self.searchingDropdown.currentIndex()))
        
        elif singleBool is True:
            singleBool = False
            all_data = FileSys.read_csv()
            print("ComboxRev:" , (self.sortingDropdown.currentIndex()))
            instance = sorting_instances[int(self.sortingDropdown.currentIndex())]
            column = int(self.selectFilterPlusWholeSortColumn.currentIndex())
            print("Column:" , column)
            self.upDownSortWhole.setText("▲")
            sort_thread = threading.Thread(target=instance.perform_sorting, args=(all_data, column))
            sort_thread.start()
            self.showData(all_data)
            print("ComboxRev0:" , (self.searchingDropdown.currentIndex()))
    
    def columnSeacrh(self):
        results = []
        instance = SearchFilters.startsWith()
        query = self.singleColSearchField.toPlainText()
        results = instance.perform_search(FileSys.read_csv(), query)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ScrappApp(Form)
    Form.show()
    sys.exit(app.exec_())
