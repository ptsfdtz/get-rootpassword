from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QDesktopWidget

class MD5GeneratorApp(QWidget):
    def __init__(self, compute):
        super().__init__()
        self.compute = compute
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MD5 Generator')
        self.resize(400, 200)  # 设置窗口大小
        self.center()  # 将窗口移动到屏幕中央

        layout = QGridLayout()

        self.label = QLabel('请输入SN码:')
        layout.addWidget(self.label, 0, 0, 1, 1)

        self.sn_input = QLineEdit(self)
        layout.addWidget(self.sn_input, 0, 1, 1, 3)

        self.result_label = QLabel('结果:')
        layout.addWidget(self.result_label, 1, 0, 1, 1)

        self.result_display = QLineEdit(self)
        self.result_display.setReadOnly(True)  # 设置为只读
        layout.addWidget(self.result_display, 1, 1, 1, 3)

        self.generate_button = QPushButton('生成MD5', self)
        self.generate_button.clicked.connect(self.on_generate_clicked)
        layout.addWidget(self.generate_button, 2, 1, 1, 3)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.setLayout(layout)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def on_generate_clicked(self):
        sn = self.sn_input.text()
        if sn:
            result = self.compute.generate_md5(sn)
            self.result_display.setText(result)
        else:
            self.result_display.setText('请输入SN码')
