import sys

import PySide2
from PySide2.QtCore import QTime, QTimer, Qt, Signal, Slot
from PySide2.QtGui import QPainter, QColor, QPaintEvent, QKeyEvent, QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QAction

from blackclockwidget import Ui_BlackClock


class MainWidget(QWidget):
    close_widget = Signal()

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.ui = Ui_BlackClock()
        self.ui.setupUi(self)

        pal = self.ui.lcdNumber.palette()
        pal.setColor(pal.WindowText, Qt.gray)
        pal.setColor(pal.Background, Qt.red)
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

    def resizeEvent(self, event: PySide2.QtGui.QResizeEvent):
        super().resizeEvent(event)
        self.ui.lcdNumber.setMinimumWidth(self.width() / 4)
        self.ui.lcdNumber.setMinimumHeight(self.height() / 4)
        self.ui.lcdNumber.move(self.width() / 2 - self.ui.lcdNumber.width() / 2,
                               self.height() / 2 - self.ui.lcdNumber.height() / 2)

    def show_time(self):
        self.ui.lcdNumber.display(QTime.currentTime().toString("hh:mm"))


class Windows(object):
    def __init__(self):
        self.wins = []
        desktop = QApplication.desktop()
        for i in range(desktop.screenCount()):
            w = MainWidget()
            geometry = desktop.screenGeometry(i)
            w.setGeometry(geometry)
            w.setWindowFlags(Qt.FramelessWindowHint)
            # w.showFullScreen()
            w.close_widget.connect(self.close_all)
            self.wins.append(w)

    @Slot()
    def show_all(self):
        for w in self.wins:
            w.showFullScreen()

    @Slot()
    def close_all(self):
        for w in self.wins:
            w.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)

    wins = Windows()

    menu = QMenu()

    make_screen_black_action = QAction(QPixmap(':/start.png'), 'Make Screen Black')
    make_screen_black_action.triggered.connect(wins.show_all)

    def message():
        system_tray.showMessage('Test message', 'Foo is 42', QPixmap(':/main.png'))

    message_action = QAction('Message')
    message_action.triggered.connect(message)

    quit_action = QAction('Quit')
    quit_action.triggered.connect(app.quit)

    menu.addAction(make_screen_black_action)
    menu.addAction(message_action)
    menu.addSeparator()
    menu.addAction(quit_action)

    system_tray = QSystemTrayIcon()
    system_tray.setContextMenu(menu)
    system_tray.setIcon(QPixmap(':/main.png'))
    system_tray.show()

    sys.exit(app.exec_())
