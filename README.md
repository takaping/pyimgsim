# Image similarity evaluation using ImgSim"
## Evnvironment
* Windows 11
* Python 3.12.7
* Refer to requirements.txt

[License of OpenCV](https://opencv.org/license/)

[License of PySide](https://doc.qt.io/qtforpython-6/licenses.html)

[License of imgsim](https://pypi.org/project/imgsim/#description)

## Source files
| File name | Overview |
|----------|------|
| imagesetdialog.py | Implementing image set classes |
| imageview.py | Implement image view classes |
| mainwindow.py | Implement the main window class |
| pyimgsim.py | Main program<br>Configuring Signals and Slots between classes |
｜mainwindow.ui | Layout of main window<br>Use designer.exe <br>in the PySide6 package folder. |
| ui_mainwindow.py | Generate a Python file from mainwindow.ui <br>using pyside6-uic.exe in the Scripts folder, <br>then use it in mainwindow.py |
| imagesetdialog.ui | Dialog box for manipulating image sets<br>Use designer.exe <br>in the PySide6 package folder. |
 |ui_imagesetdialog.py | Generate a Python file from imagesetdialog.ui <br>using pyside6-uic.exe in the Scripts folder, <br>then use it in imagesetdialog.py |
