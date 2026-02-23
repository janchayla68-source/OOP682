import os
from PySide6.QtWidgets import QApplication
from log_viewer.services.mock_source import MockLogSource
from log_viewer.services.log_factory import LogFactory
from log_viewer.ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "logs", "voters.csv") 

    use_mock = False

    if use_mock:
        log = MockLogSource
    else:
        log = LogFactory.create_source(file_path)

    viewer = MainWindow
    viewer.show()

    app.exec()