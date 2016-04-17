import sys

from PySide.QtCore import (Qt, QTimer, QTime)
from PySide.QtGui import (QApplication, QWidget, QPainter, QColor)
from blackclockwidget import Ui_BlackClock


class MainWidget(QWidget, Ui_BlackClock):
    def __init__(self, application, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.app = application

        pal = self.lcdNumber.palette()

        pal.setColor(pal.WindowText, Qt.green)

        self.lcdNumber.setPalette(pal)

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.showTime)
        self.timer1.start()

        self.showTime()

    def paintEvent(self, *args, **kwargs):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 255))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.app.quit()

    def showTime(self):
        self.lcdNumber.display(QTime.currentTime().toString("hh:mm"))


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
