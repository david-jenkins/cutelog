from qtpy.QtWidgets import QMainWindow, QStatusBar, QWidget, QVBoxLayout

from .config import CONFIG
from .logger_widget import WidgetMenuBar, LoggerTabWidget, MainMenuBar

class MainWindow(QMainWindow):

    def __init__(self, log, app, load_logfiles=[]):
        self.log = log.getChild('Main')
        self.app = app
        super().__init__()

        self.shutting_down = False

        self.setupUi()
        for filename in load_logfiles:
            self.loggerTabWidget.load_records(filename)
        self.menubar.start_server()

    def setupUi(self):
        self.resize(800, 600)
        self.setWindowTitle('cutelog')

        self.loggerTabWidget = LoggerTabWidget(self.log, self)
        self.loggerTabWidget.status_update.connect(self.set_status)
        self.setCentralWidget(self.loggerTabWidget)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.setup_menubar()

        self.restore_geometry()

        self.show()

    def setup_menubar(self):
        self.menubar = MainMenuBar(self.loggerTabWidget, self.log, self)
        self.loggerTabWidget.currentChanged.connect(self.menubar.change_actions_state)

        self.setMenuBar(self.menubar)

    def local_connection(self, local_signals):
        self.loggerTabWidget.local_connection(local_signals)

    def save_geometry(self):
        CONFIG.save_geometry(self.geometry())

    def restore_geometry(self):
        geometry = CONFIG.load_geometry()
        if geometry:
            self.resize(geometry.width(), geometry.height())

    def set_status(self, string, timeout=3000):
        self.statusBar().showMessage(string, timeout)

    def closeEvent(self, event):
        self.log.info('Close event on main window')
        self.shutdown()
        event.ignore()  # prevents errors due to closing the program before server has stopped

    def shutdown(self):
        self.log.info('Shutting down')
        if self.shutting_down:
            self.log.error('Exiting forcefully')
            raise SystemExit
        self.shutting_down = True
        self.save_geometry()
        self.loggerTabWidget.shutdown()
        self.app.quit()

    def signal_handler(self, *args):
        self.shutdown()


class WidgetWithMenu(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        
        layout = QVBoxLayout()
        
        self.loggerTabWidget = LoggerTabWidget(parent=self)
        self.loggerTabWidget.status_update.connect(self.set_status)
        self.statusbar = QStatusBar(self)
        self.statusbar.setSizeGripEnabled(False)
        self.menubar = WidgetMenuBar(self.loggerTabWidget, parent=self)
        
        layout.addWidget(self.menubar) 
        layout.addWidget(self.loggerTabWidget)
        layout.addWidget(self.statusbar) 
        
        self.setLayout(layout)

    def local_connection(self, local_signals):
        self.loggerTabWidget.local_connection(local_signals)

    def set_status(self, string, timeout=3000):
        self.statusbar.showMessage(string, timeout)

    def shutdown(self):
        self.loggerTabWidget.shutdown()
        
    def signal_handler(self, *args):
        self.shutdown()

class WidgetWithMainMenu(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        
        layout = QVBoxLayout()
        
        self.loggerTabWidget = LoggerTabWidget(parent=self)
        self.loggerTabWidget.status_update.connect(self.set_status)
        self.statusbar = QStatusBar(self)
        self.statusbar.setSizeGripEnabled(False)
        self.menubar = MainMenuBar(self.loggerTabWidget, parent=self)
        self.loggerTabWidget.currentChanged.connect(self.menubar.change_actions_state)
        
        layout.addWidget(self.menubar) 
        layout.addWidget(self.loggerTabWidget)
        layout.addWidget(self.statusbar) 
        
        self.setLayout(layout)

    def local_connection(self, local_signals):
        self.loggerTabWidget.local_connection(local_signals)

    def set_status(self, string, timeout=3000):
        self.statusbar.showMessage(string, timeout)

    def shutdown(self):
        self.loggerTabWidget.shutdown()
        
    def signal_handler(self, *args):
        self.shutdown()
