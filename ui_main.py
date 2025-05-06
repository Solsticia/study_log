from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QTimer, QDateTime, QLocale
from ui_log_entry import LogEntryWindow
from ui_history import HistoryWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Study Log App")
        self.setFixedSize(800, 550)  # 固定大小

        # 主部件和布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # 左边：日期时间
        self.datetime_label = QLabel()
        self.datetime_label.setAlignment(Qt.AlignCenter)
        self.datetime_label.setStyleSheet("font-size: 22px; color: #555555;")

        # 实时更新时间
        timer = QTimer(self)
        timer.timeout.connect(self.update_datetime)
        timer.start(1000)
        self.update_datetime()

        left_layout = QVBoxLayout()
        left_layout.addStretch()
        left_layout.addWidget(self.datetime_label)
        left_layout.addStretch()

        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        left_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 右边：两个按钮
        self.log_button = QPushButton("Start Today's Recording")
        self.history_button = QPushButton("Check History")

        self.log_button.setFixedHeight(60)
        self.history_button.setFixedHeight(60)

        self.log_button.clicked.connect(self.open_log_entry)
        self.history_button.clicked.connect(self.open_history)

        right_layout = QVBoxLayout()
        right_layout.addStretch()
        right_layout.addWidget(self.log_button)
        right_layout.addWidget(self.history_button)
        right_layout.addStretch()

        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        right_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 主布局组合
        main_layout.addWidget(left_widget, 2)
        main_layout.addWidget(right_widget, 3)

    def update_datetime(self):
        current = QDateTime.currentDateTime()
        # 英文格式，移除中英文混合
        date_str = current.toString("dddd, MMMM d yyyy | hh:mm:ss")
        self.datetime_label.setText(date_str)

    def open_log_entry(self):
        self.log_window = LogEntryWindow(self.show)
        self.log_window.setFixedSize(800, 550)  # 确保子窗口也是固定大小
        self.log_window.show()
        self.hide()

    def open_history(self):
        self.history_window = HistoryWindow(self.show)
        self.history_window.setFixedSize(800, 550)
        self.history_window.show()
        self.hide()
