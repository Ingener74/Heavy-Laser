import sys

from PySide.QtCore import Qt
from PySide.QtGui import (QApplication, QWidget, QPainter, QColor, QLCDNumber, QVBoxLayout, QDesktopWidget)


class MainWidget(QWidget):
    def __init__(self, application, parent=None):
        QWidget.__init__(self, parent)

        self.app = application

        self.clock = QLCDNumber()
        self.clock.display("00")

        l1 = QVBoxLayout()
        l1.addChildWidget(self.clock)

        self.setLayout(l1)

    def paintEvent(self, *args, **kwargs):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 255))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.app.quit()
            # self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wins = []
    desktop = QApplication.desktop()
    for i in xrange(0, desktop.screenCount()):
        w = MainWidget(app)
        geometry = desktop.screenGeometry(i)
        w.setGeometry(geometry)
        w.setWindowFlags(Qt.FramelessWindowHint)
        w.showFullScreen()
        wins.append(w)

    sys.exit(app.exec_())
