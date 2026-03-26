import sys

import qtpy


def add_local_handler(main_window):
    from .handler import LocalCuteLogHandler
    from .config import ROOT_LOG,CONFIG
    handler = LocalCuteLogHandler()
    ROOT_LOG.addHandler(handler)
    CONFIG.set_logging_level(1)
    main_window.local_connection(handler.signals)

def main():
    import signal
    from .config import ROOT_LOG, CONFIG, parse_cmdline, init_qt_info
    from .main_window import MainWindow
    from .resources import cutelog_icon_path
    from qtpy.QtGui import QIcon
    from qtpy.QtWidgets import QApplication

    if sys.platform == 'win32':
        import ctypes
        appid = 'busimus.cutelog'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    init_qt_info()
    CONFIG.post_init()

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(cutelog_icon_path))
    overrides, load_logfiles = parse_cmdline(ROOT_LOG)
    CONFIG.set_overrides(overrides)
    mw = MainWindow(ROOT_LOG, app, load_logfiles)
    # add_local_handler(mw)
    signal.signal(signal.SIGINT, mw.signal_handler)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
