import sys
import login, Chart, translate
from PyQt5.QtWidgets import QApplication
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = login.main()
    sys.exit(app.exec_())
