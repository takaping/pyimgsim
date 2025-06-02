import os
from pprint import pprint

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtGui import QImage, QPixmap, QStandardItemModel, QStandardItem
import cv2
import matplotlib.pyplot as plt

from ui_imgsetdialog import Ui_imgSetDialog
from imgset import ImageSet


class ImgsetDialog(QDialog, Ui_imgSetDialog):

    pixmap_updated = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.itemmodel = QStandardItemModel()
        self.similarityListView.setModel(self.itemmodel)
        self.realOpenButton.clicked.connect(self.on_real_images_open)
        self.realComboBox.activated.connect(self.on_real_img_changed)
        self.realViewComboBox.activated.connect(self.on_real_view_changed)
        self.synthOpenButton.clicked.connect(self.on_synth_images_open)
        self.synthComboBox.activated.connect(self.on_synth_img_changed)
        self.synthViewComboBox.activated.connect(self.on_synth_view_changed)
        self.similarityButton.clicked.connect(self.on_similarity_calc)

        self.__detector = cv2.SIFT.create()

        self.__real_imgset = None
        self.__synth_imgset = None


    def fpathlist_selected(self):
        fdlg = QFileDialog(self)
        fdlg.setFileMode(QFileDialog.ExistingFiles)
        fdlg.setNameFilter("Image files (*.bmp *.png *.jprg *.jpg *.jpe *.tiff *.tif);; all files (*.*)")
        fdlg.setViewMode(QFileDialog.Detail)
        if fdlg.exec():
                return fdlg.selectedFiles()
        return None


    def update_pixmap(self, img):
        h, w, ch = img.shape
        byte_per_line = w * ch
        qimg = QImage(img.data, w, h, byte_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        self.pixmap_updated.emit(pixmap)


    @Slot()
    def on_real_images_open(self):
        fpathlist =[r'D:\Users\takap\OneDrive\画像\datasets\Class3\1.png',
                    r'D:\Users\takap\OneDrive\画像\datasets\Class3\2.png',
                    r'D:\Users\takap\OneDrive\画像\datasets\Class3\3.png',
                    r'D:\Users\takap\OneDrive\画像\datasets\Class3\4.png',
                    r'D:\Users\takap\OneDrive\画像\datasets\Class3\5.png']
        #  fpathlist = self.fpathlist_selected()
        if fpathlist is None:
            return
        self.__real_imgset = ImageSet.create_imageset(fpathlist)
        self.__real_imgset.detect_and_compute(self.__detector)
        self.realComboBox.clear()
        self.realComboBox.addItems([os.path.basename(fpath) for fpath in fpathlist])
        self.realViewComboBox.setCurrentIndex(self.__real_imgset.index_of_view)
        self.realComboBox.setCurrentIndex(self.__real_imgset.index_of_image)
        self.update_pixmap(self.__real_imgset.current_image())


    @Slot()
    def on_real_img_changed(self, index):
        self.__real_imgset.index_of_image = index
        self.update_pixmap(self.__real_imgset.current_image())


    @Slot()
    def on_real_view_changed(self, index):
        self.__real_imgset.index_of_view = index
        self.update_pixmap(self.__real_imgset.current_image())


    @Slot()
    def on_synth_images_open(self):
        fpathlist =[r'D:\Users\takap\OneDrive\画像\datasets\Class6\1.png',
                    r'D:\Users\takap\OneDrive\画像\datasets\Class6\2.png',
                    r'D:\Users\takap\OneDrive\画像\datasets\Class6\3.png',
                    r'D:\Users\takap\OneDrive\画像\datasets\Class6\4.png',
                    r'D:\Users\takap\OneDrive\画像\datasets\Class6\5.png']
        # fpathlist = self.fpathlist_selected()
        if fpathlist is None:
            return
        self.__synth_imgset = ImageSet.create_imageset(fpathlist)
        self.__synth_imgset.detect_and_compute(self.__detector)
        self.synthComboBox.clear()
        self.synthComboBox.addItems([os.path.basename(fpath) for fpath in fpathlist])
        self.synthViewComboBox.setCurrentIndex(self.__synth_imgset.index_of_view)
        self.synthComboBox.setCurrentIndex(self.__synth_imgset.index_of_image)
        self.update_pixmap(self.__synth_imgset.current_image())


    @Slot()
    def on_synth_img_changed(self, index):
        self.__synth_imgset.index_of_image = index
        self.update_pixmap(self.__synth_imgset.current_image())


    @Slot()
    def on_synth_view_changed(self, index):
        self.__synth_imgset.index_of_view = index
        self.update_pixmap(self.__synth_imgset.current_image())


    @Slot()
    def on_similarity_calc(self):
        num_clusters = int(self.numCumlustersEdit.text())
        matcher = cv2.BFMatcher()
        extractor = cv2.BOWImgDescriptorExtractor(self.__detector, matcher)
        representative_descriptors, codebook = self.__real_imgset.compute_representative_descriptors(extractor, num_clusters=num_clusters)
        real_similaritylist = self.__real_imgset.similarity(extractor, representative_descriptors)
        synth_similaritylist = self.__synth_imgset.similarity(extractor, representative_descriptors)
        self.itemmodel.clear()
        for i, similarity in enumerate(real_similaritylist):
            item = QStandardItem(f'real: {self.realComboBox.itemText(i)} = {similarity:.03f}')
            self.itemmodel.appendRow(item)
        for i, similarity in enumerate(synth_similaritylist):
            item = QStandardItem(f'synth: {self.synthComboBox.itemText(i)} = {similarity:.03f}')
            self.itemmodel.appendRow(item)
        