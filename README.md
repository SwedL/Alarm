<p align="center"><img src="https://i.ibb.co/58vsw4K/Alarm.png" width="200"  alt="Logo Alarm" border="0"></p>

<p align="center">
<img src="https://img.shields.io/badge/Pyhton-3.11-orange" alt="Python shield" border="0">
<img src="https://img.shields.io/badge/PyQt5-5.15.10-D1FF4F" alt="PyQt5 shield" border="0">
</p>

## Описание приложения
Будильник для рабочего стола. Подает сигнал при достижении заданного времени. Также реализована функция выключения компьютера в 20:00.

## Установка
Предварительно создайте каталог для приложения (some directory)<br>
Клонируйте код репозитория в созданный каталог:
```sh
git clone https://github.com/SwedL/Alarm.git
```
Также в каталоге проекта (some directory) создайте виртуальное окружение, выполнив команду:

- Windows: `python -m venv venv`
- Linux: `python3 -m venv venv`

Активируйте окружение командой:

- Windows: `.\venv\Scripts\activate`
- Linux: `source venv/bin/activate`

Перейдите в каталог Alarm и установите зависимости в виртуальное окружение:
```sh
cd Alarm
```
```sh
pip install -r requirements.txt
```
Создайте Alarm.exe используя команду:
```python
pyinstaller -w --onefile Alarm.py 
```
С другими вариантами установки можно ознакомиться с помощью команды:
```python
pyinstaller --help
```
Сгенерированный файл приложения Alarm.exe будет расположен в основном каталоге.
в каталоге **"dist"**.

Также для корректной работы приложения необходимо скопировать звуковые файлы **beep.wav** и **off.wav** в директорию Alarm.exe.

+ \ some directory
  + Alarm.exe
  + beep.wav
  + off.wav

## Инструкция
![](https://i.ibb.co/QMyfKn8/image-alarm.png "image alarm")

![](https://i.ibb.co/tQJztCb/2023-12-06-20-41-45-8.png "clock image") или ![](https://i.ibb.co/jLxLjr6/2023-12-06-20-41-45-5.png "button image") setting the time

![](https://i.ibb.co/HhnWnwJ/2023-12-06-20-41-45-7.png "set/stop image") активация/деактивация будильника

![](https://i.ibb.co/ZN5Y3S8/2023-12-06-20-41-45-4.png "turn off image") автоматическое выключение компьютера при достижении 20:00 (08:00 p.m)

## Автор проекта
* **Осминин Алексей** - [SwedL](https://github.com/SwedL)
