import sys,os,cv2
from PyQt5 import QtWidgets,QtGui

sys.path.insert(0, os.path.abspath('ui'))
from MainUi import Ui_MainWindow

sys.path.insert(0, os.path.abspath('OpenCV'))
import Legend

class SEMReader(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(window)
        self.window = window
        self.BtnInputImage.clicked.connect(self.image_directory_input)

    def image_directory_input(self):
        path = QtWidgets.QFileDialog.getOpenFileName\
            (None, "Input Image", "", "Image files(*.png *.jpeg *.jpg *.bmp);;All files(*)")
        self.pixmap=QtGui.QPixmap(path[0])
        self.lblImage.setPixmap(self.pixmap)
        self.lblImage.setScaledContents(True)

        self.image=cv2.imread(path[0])
        if self.image is not None:
            print("ok")
        else:
            print("not ok")

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QMainWindow()
    ui=SEMReader()
    window.show()
    sys.exit(app.exec_())