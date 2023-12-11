from ui import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = AppUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())