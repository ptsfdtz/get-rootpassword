import sys
from PyQt5.QtWidgets import QApplication
import compute
from setUI import MD5GeneratorApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MD5GeneratorApp(compute)
    ex.show()
    sys.exit(app.exec_())
