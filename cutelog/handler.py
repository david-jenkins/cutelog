

from logging import Handler
from qtpy.QtCore import QObject, Signal
from .logger_tab import LogRecord

class LocalCuteLogSignals(QObject):
    new_record = Signal(LogRecord)
    connection_finished = Signal(object)
    internal_prefix = b"!!cutelog!!"

class LocalCuteLogHandler(Handler):
    def __init__(self, level = 0):
        super().__init__(level)
        self.signals =  LocalCuteLogSignals()

    def emit(self, record) :
        self.signals.new_record.emit(LogRecord(record.__dict__))