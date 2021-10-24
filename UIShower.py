def loadCsv(self):
        fileName = 'C:/Users/newst/Documents/Data Strcuture and Algorithm Lab/UI 1/songsdata.csv'
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)