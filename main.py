from Pyside6.QtWidgets import QApplication
from sevices.file_log_viewer import FileLogViewer
from sevices.mock_source import MockLogSource
from ui.main_window import Mainwindow

if __name__ == "__main__":
    app = QApplication([])
    log = MockLogSource()
    log = FileLogViewer("log/voters.log")
    viewer = FileLogViewer()
    viewer.show()
    app.exec_()
