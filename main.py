import sys
from PyQt5.QtWidgets import QApplication
from ui_main import MainWindow

def main():
    app = QApplication(sys.argv)

    # 全局样式（现代简洁风，浅色调 + 高端绿色）
    app.setStyleSheet("""
        QWidget {
            font-family: "Segoe UI", Arial;
            font-size: 15px;
            background-color: #f8f9fa;
        }
        QPushButton {
            font-size: 16px;
            background-color: #2e8b57;  /* 深绿色 */
            color: white;
            border-radius: 6px;
            padding: 8px 16px;
        }
        QPushButton:hover {
            background-color: #276749;  /* 深一点的绿色 */
        }
        QLabel {
            color: #333333;
        }
        QHeaderView::section {
            background-color: #e9ecef;
            padding: 6px;
            border: 1px solid #dee2e6;
            font-weight: bold;
        }
        QTableWidget {
            gridline-color: #ced4da;
        }
        QTableWidget QTableCornerButton::section {
            background-color: #e9ecef;
            border: 1px solid #dee2e6;
        }
    """)

    window = MainWindow()
    window.setFixedSize(800, 550)  # 所有窗口固定大小，保证布局美观
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
