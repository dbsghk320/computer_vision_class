import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout,  QHBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from Pyside6.QtWidgets import Qt




class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('My first Application')

        mainwindow = QHBoxLayout(self)  # UI를 수평적으로 해달라

        left_menu = QLabel()
        left_menu_layout = QVBoxLayout(left_menu)
        left_menu_layout.addWidget(QPushButton('이미지 회전'))
        left_menu_layout.addWidget(QPushButton('오츠 알고리즘'))
        left_menu_layout.addWidget(QPushButton('평균 필터링'))
        left_menu_layout.addWidget(QPushButton('가우시안 필터링'))
        left_menu_layout.addWidget(QPushButton('색공간'))
        left_menu_layout.addWidget(QPushButton('임계처리'))
        left_menu_layout.addWidget(QPushButton('산술 연산'))
        left_menu_layout.addWidget(QPushButton('기하하적 변환'))
        left_menu_layout.addWidget(QPushButton('영상 필터'))
        left_menu_layout.addWidget(QPushButton('경계 검출'))
        left_menu_layout.addWidget(QPushButton('영상 분할'))
        left_menu_layout.setAlignment(Qt.alignTop)

        right_content = QLabel()
        image = QPixmap('./cat-01.jpg')
        right_content.setPixmap(image)
        mainwindow.addWidget(left_menu)
        mainwindow.addWidget(right_content)

        self.setLayout(mainwindow)
        self.setGeometry(50, 50, 1280, 720)
        self.show()


if __name__ == '__main__':
    app = QApplication()
    ex = MyApp()
    sys.exit(app.exec())
