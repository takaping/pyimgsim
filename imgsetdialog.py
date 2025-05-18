import os

from PySide6 .QtCore import Qt, Signal, Slot, QStringListModel
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtGui import QImage, QPixmap
from ui_imgsetdialog import Ui_imgSetDialog
import cv2
import numpy as np
import imgsim


class ImgsetDialog(QDialog, Ui_imgSetDialog):
    pixmap_updated = Signal(object)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

        self.realOpenButton.clicked.connect(self.on_real_images_open)
        self.realComboBox.currentIndexChanged.connect(self.on_real_img_changed)
        self.synthOpenButton.clicked.connect(self.on_synth_images_open)
        self.synthComboBox.currentIndexChanged.connect(self.on_synth_img_changed)
        self.similarityButton.clicked.connect(self.on_similarity_calc)

        self.real_imgs = []
        self.synth_imgs = []


    def select_files(self):
        fdlg = QFileDialog(self)
        fdlg.setFileMode(QFileDialog.ExistingFiles)
        fdlg.setNameFilter("Image files (*.bmp *.png *.jprg *.jpg *.jpe *.tiff *.tif);; all files (*.*)")
        fdlg.setViewMode(QFileDialog.Detail)
        if fdlg.exec_():
                return fdlg.selectedFiles()
        return None


    def open_images(self, fpaths):
        try:
            imgs = []
            for fpath in fpaths:
                n = np.fromfile(fpath, np.uint8)
                img = cv2.imdecode(n, cv2.IMREAD_GRAYSCALE)
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                imgs.append(img)
        except Exception as e:
            print(e)
            return None
        else:
            return imgs


    def update_pixmap(self, img):
        h, w, ch = img.shape
        byte_per_line = w * ch
        qimg = QImage(img.data, w, h, byte_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        self.pixmap_updated.emit(pixmap)


    @Slot()
    def on_real_images_open(self):
        fpaths = self.select_files()
        if fpaths:
            self.real_imgs.clear()
            self.real_imgs = self.open_images(fpaths)
            self.realComboBox.clear()
            self.realComboBox.addItems([os.path.basename(fpath) for fpath in fpaths])
            self.update_pixmap(self.real_imgs[0])


    @Slot(int)
    def on_real_img_changed(self, index):     
        self.update_pixmap(self.real_imgs[index])


    @Slot()
    def on_synth_images_open(self):
        fpaths = self.select_files()
        if fpaths:
            self.synth_imgs.clear()
            self.synth_imgs = self.open_images(fpaths)
            self.synthComboBox.clear()
            self.synthComboBox.addItems([os.path.basename(fpath) for fpath in fpaths])
            self.update_pixmap(self.synth_imgs[0])


    @Slot(int)
    def on_synth_img_changed(self, index):     
        self.update_pixmap(self.synth_imgs[index])
    

    @Slot()
    def on_similarity_calc(self):
        vctr = imgsim.Vectorizer(device='cpu')
        real_vecs = []
        for img in self.real_imgs:
            real_vecs.append(vctr.vectorize(img))
        real_cent = np.mean(real_vecs, axis=0)
        real_dists = []
        outer_dist = 0.0
        outer_index = 0
        for i, vec in enumerate(real_vecs):
            dist = float(imgsim.distance(real_cent, vec))
            if outer_dist < dist:
                outer_dist = dist
                outer_index = i
            real_dists.append(dist)

        synth_dists = []
        for img in self.synth_imgs:
            vec = vctr.vectorize(img)
            synth_dists.append(float(imgsim.distance(real_cent, vec)))
        
        str_dist = [f'outer[{outer_index}]={outer_dist:.03f}']
        for dist in synth_dists:
            str_dist.append(f'{dist:.03f}')
        model = QStringListModel(str_dist)
        self.similarityListView.setModel(model)
