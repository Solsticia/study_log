from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import log_manager
from datetime import date, datetime

class LogEntryWindow(QWidget):
    def __init__(self, return_callback):
        super().__init__()

        self.return_callback = return_callback

        self.setWindowTitle("Today's Study Log")
        self.setFixedSize(800, 550)  # 固定窗口大小

        layout = QVBoxLayout()

        title = QLabel("Today's Study Log - Enter your activities below")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; color: #333333;")
        layout.addWidget(title)

        # 表格：Start Time | End Time | Task Description
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Start Time (HH:MM)", "End Time (HH:MM)", "Task Description"])
        self.table.horizontalHeader().setStretchLastSection(True)  # 让 Task Description 自适应宽度
        self.table.horizontalHeader().setSectionsMovable(False)
        layout.addWidget(self.table)

        # >>> 添加：修正列宽
        self.table.setColumnWidth(0, 165)  # Start Time
        self.table.setColumnWidth(1, 165)  # End Time
        # Task Description 留自动扩展

        layout.addWidget(self.table)
        self.table.setFixedHeight(381)   # 可以根据需要调整高度

        # 加载今天已有数据
        existing_data = log_manager.load_today_data()
        if existing_data:
            for row in existing_data:
                self.add_row(row[0], row[1], row[2])

        # 总时间标签
        self.total_time_label = QLabel("Total time worked today: 0 hours 0 minutes")
        self.total_time_label.setAlignment(Qt.AlignCenter)
        self.total_time_label.setStyleSheet("font-size: 16px; color: #555555;")
        layout.addWidget(self.total_time_label)

        # 按钮布局
        button_layout = QHBoxLayout()

        add_row_btn = QPushButton("Add Row")
        add_row_btn.clicked.connect(self.add_empty_row)
        button_layout.addWidget(add_row_btn)

        save_btn = QPushButton("Save Log")
        save_btn.clicked.connect(self.save_log)
        button_layout.addWidget(save_btn)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.go_back)
        button_layout.addWidget(back_btn)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        # 更新总时间
        self.update_total_time()

        # 允许用户修改表格，不用删除整个格子
        self.table.itemChanged.connect(self.update_total_time)

    def add_empty_row(self):
        self.add_row("", "", "")

    def add_row(self, start_time, end_time, description):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(start_time))
        self.table.setItem(row_position, 1, QTableWidgetItem(end_time))
        self.table.setItem(row_position, 2, QTableWidgetItem(description))

    def save_log(self):
        data = []
        for row in range(self.table.rowCount()):
            start_item = self.table.item(row, 0)
            end_item = self.table.item(row, 1)
            desc_item = self.table.item(row, 2)

            start = start_item.text() if start_item else ""
            end = end_item.text() if end_item else ""
            desc = desc_item.text() if desc_item else ""

            if start or end or desc:
                data.append([start, end, desc])

        log_manager.save_today_data(data)
        QMessageBox.information(self, "Saved", "Today's log has been saved.")
        self.update_total_time()

    def go_back(self):
        self.close()
        self.return_callback()

    def update_total_time(self):
        total_minutes = 0

        for row in range(self.table.rowCount()):
            start_item = self.table.item(row, 0)
            end_item = self.table.item(row, 1)

            start = start_item.text().strip() if start_item else ""
            end = end_item.text().strip() if end_item else ""

            if start and end:
                try:
                    start_time = datetime.strptime(start, "%H:%M")
                    end_time = datetime.strptime(end, "%H:%M")
                    minutes = (end_time - start_time).total_seconds() / 60
                    if minutes > 0:
                        total_minutes += minutes
                except ValueError:
                    pass  # 如果时间格式错误，忽略该行

        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)
        self.total_time_label.setText(f"Total time worked today: {hours} hours {minutes} minutes")
