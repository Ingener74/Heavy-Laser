import sys

from PySide2.QtCore import QTime, QTimer, Qt, Signal
from PySide2.QtGui import QPainter, QColor, QPaintEvent, QKeyEvent
from PySide2.QtWidgets import QApplication, QWidget

from blackclockwidget import Ui_BlackClock


class MainWidget(QWidget):
    close_widget = Signal()

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.ui = Ui_BlackClock()
        self.ui.setupUi(self)

        pal = self.ui.lcdNumber.palette()

        pal.setColor(pal.WindowText, Qt.gray)

        self.ui.lcdNumber.setPalette(pal)

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.show_time)
        self.timer1.start()

        self.show_time()

    def paintEvent(self, event: QPaintEvent):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 255))

    def keyPressEvent(self, event: QKeyEvent):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Escape:
            self.close_widget.emit()

    def show_time(self):
        self.ui.lcdNumber.display(QTime.currentTime().toString("hh:mm"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wins = []
    desktop = QApplication.desktop()
    for i in range(desktop.screenCount()):
        w = MainWidget()
        geometry = desktop.screenGeometry(i)
        w.setGeometry(geometry)
        w.setWindowFlags(Qt.FramelessWindowHint)
        w.showFullScreen()
        w.close_widget.connect(app.quit)
        # w.show()
        wins.append(w)

    sys.exit(app.exec_())
