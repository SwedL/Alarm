<p align="center"><img src="https://i.ibb.co/58vsw4K/Alarm.png" width="200"  alt="Logo Alarm" border="0"></p>

<p align="center">
<img src="https://img.shields.io/badge/Pyhton-3.11-orange" alt="Python shield" border="0">
<img src="https://img.shields.io/badge/PyQt5-5.15.10-D1FF4F" alt="PyQt5 shield" border="0">
</p>

## About
A simple alarm clock for your desktop. Gives a signal when the specified time is reached. Also implemented is the function of turning off the computer at 20:00

## Installation
Pre-create a directory for the application (some directory)<br>
Clone the repository code into the created directory (in some directory):
```sh
git clone https://github.com/SwedL/Alarm.git
```
Also in the project directory (some directory) create a virtual environment by running the command:

- Windows: `python -m venv venv`
- Linux: `python3 -m venv venv`

Activate it with the command:

- Windows: `.\venv\Scripts\activate`
- Linux: `source venv/bin/activate`

Go to the Alarm directory and install the dependencies in the virtual environment:
```sh
cd Alarm
```
```sh
pip install -r requirements.txt
```
Create Alarm.exe
```python
pyinstaller -w --onefile Alarm.py 
```
Other installation options can be obtained using:
```python
pyinstaller --help
```
The generated Alarm.exe application file will be located in the main directory
in the **"dist"** directory.

Also, for the application to work correctly, you need to copy the sound files **beep.wav** and **off.wav** to the Alarm.exe directory

+ \ some directory
  + Alarm.exe
  + beep.wav
  + off.wav

## Instructions
![](https://i.ibb.co/QMyfKn8/image-alarm.png "image alarm")

![](https://i.ibb.co/tQJztCb/2023-12-06-20-41-45-8.png "clock image") or ![](https://i.ibb.co/jLxLjr6/2023-12-06-20-41-45-5.png "button image") setting the time

![](https://i.ibb.co/HhnWnwJ/2023-12-06-20-41-45-7.png "set/stop image") activate/deactivate the alarm

![](https://i.ibb.co/ZN5Y3S8/2023-12-06-20-41-45-4.png "turn off image") automatic computer shutdown at 20:00

## Developers
* **Осминин Алексей** - [SwedL](https://github.com/SwedL)