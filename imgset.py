from pprint import pprint

import cv2
import numpy as np


class ImageSet:
    def __init__(self) -> None:
        self.__imglist = []
        self.__kplist = []
        self.__desclist = []
        self.__index_of_view = 0
        self.__index_of_image = 0
        self.__bowdesclist = []


    @classmethod
    def create_imageset(self, fpathlist: list) -> object:
        imgset = ImageSet()
        imgset.open_images(fpathlist)
        return imgset


    @property
    def index_of_image(self) -> int:
        return self.__index_of_image


    @index_of_image.setter
    def index_of_image(self, index: int) -> None:
        self.__index_of_image = index


    @property
    def index_of_view(self) -> int:
        return self.__index_of_view


    @index_of_view.setter
    def index_of_view(self, index: int) -> None:
        self.__index_of_view = index


    def clear_all(self) -> None:
        self.__imglist.clear()
        self.__kplist.clear()
        self.__desclist.clear()
        self.__index_of_view = 0
        self.__index_of_image = 0
        self.__bowdesclist.clear()

    def open_images(self, fpathlist: list) -> None:
        self.clear_all()
        for fpath in fpathlist:
            n = np.fromfile(fpath, np.uint8)
            self.__imglist.append(cv2.imdecode(n, cv2.IMREAD_GRAYSCALE))


    def detect_and_compute(self, detector: object) -> None:
        for img in self.__imglist:
            kp, desc = detector.detectAndCompute(img, None)
            self.__kplist.append(kp)
            self.__desclist.append(desc)
    

    def current_image(self) -> object:
        if self.__index_of_view == 0:
            return cv2.cvtColor(self.__imglist[self.__index_of_image], cv2.COLOR_GRAY2RGB)
        else:
            img = cv2.drawKeypoints(self.__imglist[self.__index_of_image], self.__kplist[self.__index_of_image], None, flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
            return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        

    def compute_bowdesclist(self, extractor):
        self.__bowdesclist.clear()
        for img, kp in zip(self.__imglist, self.__kplist):
            desc = extractor.compute(img, kp)[0]
            self.__bowdesclist.append(desc)

    def compute_representative_descriptors(self, extractor, num_clusters=100):
        bovw_trainer = cv2.BOWKMeansTrainer(clusterCount=num_clusters)
        for desc in self.__desclist:
            bovw_trainer.add(desc.astype(np.float32))
        codebook = bovw_trainer.cluster()
        extractor.setVocabulary(codebook)
        self.compute_bowdesclist(extractor)
        representative_descriptors = np.mean(self.__bowdesclist, axis=0)
        return representative_descriptors, codebook


    def similarity(self, extractor, representative_descriptors):
        similarities = []
        self.compute_bowdesclist(extractor)
        for desc in self.__bowdesclist:
            s = sum(map(lambda x: min(x[0], x[1]), zip(representative_descriptors, desc)))
            similarities.append(s)
        return similarities