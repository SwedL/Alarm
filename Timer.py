import os
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, QTime, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication


import timer_design  # Это наш конвертированный файл дизайна


class Budil(QThread):
    current_time = QTime.currentTime()

    def __init__(self, value=None):
        QThread.__init__(self)

        self.alarm_time = value
        self.player = QMediaPlayer()
        self.off2000 = False

    def play_audio(self, sound):
        full_file_path = os.path.join(os.getcwd(), sound)
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()

    @staticmethod
    def turn_off():
        os.system('C:/Windows/System32/shutdown.exe -p')

    def run(self):
        while True:
            self.current_time = QTime.currentTime()
            QtCore.QThread.msleep(750)
            # если время сигнала установлено то идёт сверка
            if self.alarm_time and self.current_time >= self.alarm_time:
                self.play_audio('beep.wav')
            if self.off2000 and self.current_time > QTime(20, 0, 0):
                self.play_audio('off.mp3')
                QtCore.QThread.msleep(2000)
                self.turn_off()


class ExampleApp(QtWidgets.QMainWindow, timer_design.Ui_mainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowTitle('Timer')
        self.setWindowIcon(QIcon('ENT2.png'))
        self.budil = Budil()        # создаём объект поток QThread
        self.budil.start()          # запускаем поток QThread

        self.pushButton.clicked.connect(self.set_clock)    # при нажатии включаем или отключаем будильник
        self.radioButton.setChecked(False)    # установка состояния кнопки of2000 (не нажата)
        self.budil.off2000 = self.radioButton.isChecked()    # вкл/выкл проверки на 20:00 согласно состоянию of2000
        self.radioButton.clicked.connect(self.of2000)    # вызов функции вкл. of2000
        self.alarm = False
        self.alarmEdit.setTime(QTime.currentTime())
        self.alarmEdit.timeChanged.connect(self.disarmed)    # при изменении времени будильника кнопка SET отключается

    def disarmed(self):                             # ф-я отключающая будильник при изменении времени
        self.pushButton.setChecked(False)
        self.alarm = False
        self.budil.alarm_time = None

    def set_clock(self):
        if not self.alarm and self.alarmEdit.time() > QTime.currentTime(): # будильник не включен if setTime < текущего
            self.budil.alarm_time = self.alarmEdit.time()      # установка времени сигнала в будильник
            self.alarm = True                                  # будильник изменён на вкл.

        else:                                                  # будильник включен
            self.alarm = False                                 # будильник изменён на выключен
            self.budil.alarm_time = None                       # время сигнала стёрто и отслеживание не происходит

    def of2000(self):                                          # вкл/выкл проверки на выключение после 20:00
        self.budil.off2000 = self.radioButton.isChecked()


def move2RightBottomCorner(win):
    screen_geometry = QApplication.desktop().availableGeometry()    # получение размеров экрана
    screen_size = (screen_geometry.width(), screen_geometry.height())    # ширина/длина экрана
    win_size = (win.frameSize().width(), win.frameSize().height())    # ширина/длина окна App
    x = screen_size[0] - win_size[0] - win_size[1]
    y = screen_size[1] - win_size[1]
    win.move(x, y)


def main():
    app = QtWidgets.QApplication(sys.argv)    # Новый экземпляр QApplication
    window = ExampleApp()    # Создаём объект класса ExampleApp
    window.move(window.width() * -3, 0)
    window.show()    # Показываем окно
    move2RightBottomCorner(window)    # функция перемещения окна в нижнюю часть экрана
    sys.exit(app.exec_())


if __name__ == '__main__':    # Если мы запускаем файл напрямую, а не импортируем
    main()    # то запускаем функцию main()

