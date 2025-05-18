from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem


class ImageView(QGraphicsView):
    def __init__(self):
        self.scene = QGraphicsScene()
        super().__init__(self.scene)
        self.item = QGraphicsPixmapItem()
        self.scene.addItem(self.item)


    @Slot(object)
    def update_view(self, pixmap):
        self.item.setPixmap(pixmap)
        self.scene.setSceneRect(self.item.boundingRect())
        