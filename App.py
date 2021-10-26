from UICode import *
import sys

class ScrappApp(Ui_ScrappApp):
    def __init__(self,window):
        super().__init__()
        self.setupUi(window)
        self.upDownSortWhole.clicked.connect(self.shown)





    def shown(self):
        self.items_lbl.setText("555554554")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ScrappApp(Form)
    Form.show()
    sys.exit(app.exec_())