import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from imgsetdialog import ImgsetDialog
from imageview import ImageView

app = QApplication(sys.argv)
img_view = ImageView()
main_window = MainWindow()
main_window.setCentralWidget(img_view)
imgset_dlg = ImgsetDialog(main_window)

imgset_dlg.pixmap_updated.connect(img_view.update_view)

main_window.show()
imgset_dlg.show()
sys.exit(app.exec())
