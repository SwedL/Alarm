<a href="https://imgbb.com/"><img src="https://i.ibb.co/58vsw4K/Alarm.png" width="200" text-align="center" alt="Alarm" border="0"></a>

![](https://img.shields.io/badge/Pyhton-3.11-orange)
![](https://img.shields.io/badge/Using-PyQt5-D1FF4F)


## About
A simple alarm clock for your desktop. Gives a signal when the specified time is reached. Also implemented is the function of turning off the computer at 20:00

## Installation
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

