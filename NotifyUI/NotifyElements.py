from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, QTime
from PyQt6 import QtGui
import sys
import threading


class NotifyApplication:
    """
    Create an application instance using this class.
    And then call send_notication to run the event loop and show the window
    """

    window = None
    app = None
    notification_sent = False

    def __init__(self, argv=sys.argv) -> None:
        self.app = QApplication(argv)
        self.window = NotifyWindow()

    def send_notification(self):
        """
        Sends the notification.
        """
        if not self.notification_sent:
            self.notification_sent = True
            self.window.show()
            self.app.exec()
        else:
            raise Exception(
                "Create a new application instance to send another notification."
            )


class NotifyCommon:
    style_sheet: str = ""
    fade_away_time: int = 500

    def setBackgroundColor(self, color: str) -> None:
        """
        Set the background color of the window.
        color: the color in string format.
        e.g. "red" or "#ff0000" or "rgb(255,0,0)" or "rgba(255,0,0,0.5)"
        """
        self.appendStyle("background-color", color)

    def appendStyle(self, property: str, value: str) -> None:
        """
        Append a style to the style sheet.
        property: the property of the style.
        e.g. "background-color" or "border-radius"
        value: the value of the property.
        e.g. "red" or "10px" or "rgba(255,0,0,0.5)"
        """
        self.style_sheet += property + ":" + value + ";"
        self.setStyleSheet(self.style_sheet)

    def fade(self, exec_at_end=None) -> None:
        """
        Fade away the element.
        """
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(self.fade_away_time)
        self.animation.setStartValue(self.windowOpacity())
        self.animation.setEndValue(0.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        if callable(exec_at_end):
            self.animation.finished.connect(exec_at_end)
        self.animation.start()

    def setFadeAwayTime(self, fadeTime: int) -> None:
        """
        Set the fade away time of the window.
        fadeTime: the fade away time in milliseconds.
        e.g. 1000 or 2000 or 3000.
        """
        self.fade_away_time = fadeTime


class NotifyTimer:
    """
    This class runs the function passed after the specified time.
    call_at_end: the function to be called after the specified time.
    end_qtime: the time after which the function is called. (Should be a QTime object)
    args: the arguments to be passed to the function.
    kargs: the keyword arguments to be passed to the function.

    Note:- Declare this as a variable to keep the timer alive.
    """

    time = QTime(0, 0, 0)
    end_time = QTime(0, 0, 0)

    def __init__(self, call_at_end: function, end_qtime: QTime, *args, **kargs) -> None:
        self.timer = QTimer()
        self.call_at_end = call_at_end
        self.end_time = end_qtime
        self.args = args[2:]
        self.kargs = kargs
        self.timer.timeout.connect(self.callbackFunc)
        self.timer.start(1000)

    def callbackFunc(self):
        self.time = self.time.addSecs(1)
        if self.end_time == self.time:
            self.timer.stop()
            if len(self.args) > 0 and len(self.kargs) > 0:
                self.call_at_end(*self.args, **self.kargs)
            elif len(self.args) > 0:
                self.call_at_end(*self.args)
            elif len(self.kargs) > 0:
                self.call_at_end(**self.kargs)
            else:
                self.call_at_end()


class NotifyWindow(QMainWindow, NotifyCommon):
    close_if_clicked: bool = False
    padding: int = 10
    fade_at_exit = True
    auto_fade_time = 0

    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowType.ToolTip)
        self.setGeometry(0, 0, 356, 100)
        self.setFixedWidth(356)
        # self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed,QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.setBackgroundColor("#272727")

    def addTextElement(
        self,
        x: int,
        y: int,
        text: str,
        font: QtGui.QFont = QtGui.QFont("Helvetica", 13, QtGui.QFont.Weight.Normal),
        color: str = "#ffffff",
    ):
        """
        Adds a text element to the window.
        x: the x position of the element.
        y: the y position of the element.
        h: the height of the element.
        w: the width of the element.
        text: the text of the element.
        font: the font of the text.
        e.g. QFont("Helvetica",10,QtGui.QFont.Weight.Normal)
        color: the color of the text.
        """
        return NotifyText(self, x, y, text, font, color)

    def setCloseClick(self, value: bool) -> None:
        """
        Toggle if the window should close when left clicked.
        value: True or False.
        """
        self.close_if_clicked = value

    def setPadding(self, value: int) -> None:
        """
        Set the padding of the window.
        value: the padding in pixels.
        e.g. 10 or 20 or 30.
        """
        self.padding = value

    def setFadeAtClick(self, value: bool) -> None:
        """
        Toggle if the window should fade away when left clicked.
        value: True or False.
        """
        self.fade_at_exit = value

    def setWindowTopLeft(self) -> None:
        """
        Set the window to the top left of the screen.
        """
        self.move(self.padding, self.padding)

    def setWindowTopRight(self) -> None:
        """
        Set the window to the top right of the screen.
        """
        ava_space = (
            QtGui.QGuiApplication.primaryScreen().availableGeometry().bottomRight()
        )
        x = ava_space.x() - self.frameGeometry().width() - self.padding
        y = self.padding
        self.move(x, y)

    def setWindowBottomLeft(self) -> None:
        """
        Set the window to the bottom left of the screen.
        """
        ava_space = (
            QtGui.QGuiApplication.primaryScreen().availableGeometry().bottomRight()
        )
        x = self.padding
        y = ava_space.y() - self.frameGeometry().height() - self.padding
        self.move(x, y)

    def setWindowBottomRight(self) -> None:
        """
        Set the window to the bottom right of the screen.
        """
        ava_space = (
            QtGui.QGuiApplication.primaryScreen().availableGeometry().bottomRight()
        )
        x = ava_space.x() - self.frameGeometry().width() - self.padding
        y = ava_space.y() - self.frameGeometry().height() - self.padding
        self.move(x, y)

    def autoFade(self, fade_time: QTime):
        """
        Automatically fade away after the specified time.
        fade_time: the fade time.
        """
        self.auto_fade_time = fade_time
        self.fade_timer_instance = NotifyTimer(
            self.fade, fade_time, exec_at_end=QApplication.exit
        )

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if (
            a0.button() == Qt.MouseButton.LeftButton
            and self.close_if_clicked
            and self.fade_at_exit
        ):
            self.fade(QApplication.exit)
        elif a0.button() == Qt.MouseButton.LeftButton and self.close_if_clicked:
            QApplication.exit()


class NotifyText(NotifyCommon):
    """
    Add a text element to the window.
    x: the x position of the element.
    y: the y position of the element.
    h: the height of the element.
    w: the width of the element.
    text: the text of the element.
    font: the font of the text.
    e.g. QFont("Helvetica",10,QtGui.QFont.Weight.Normal)
    color: the color of the text.
    """

    style_sheet = ""

    def __init__(
        self,
        parent: NotifyWindow,
        x: int,
        y: int,
        text: str,
        font: QtGui.QFont = QtGui.QFont("Helvetica", 13, QtGui.QFont.Weight.Normal),
        color: str = "#ffffff",
    ) -> None:
        element = QLabel(parent)
        element.setStyleSheet("color:" + color)
        element.setText(text)
        element.setFont(font)
        element.move(x, y)
        element.setFixedWidth(336)
        element.setWordWrap(True)
        # BUG - MainWindow doesn't expand vertically when QLabel has.
        parent.adjustSize()


def sendWinStyleNotify(
    app_name: str, title: str, msg: str, fadeTime: QTime = QTime(0, 1, 0)
) -> None:
    """
    Sends a windows 10 inspired style notification.
    `app_name`: the name of the application.
    `title`: the title of the notification.
    `msg`: the message of the notification.
    `fadeTime`: the fade time of the notificaion.

    e.g. "Notify Elements","Hello World","This is a test message."
    Note: This function is a thread. So it won't block the main thread.
    """
    thread = threading.Thread(
        target=__sendWinStyleNotify, args=(app_name, title, msg, fadeTime)
    )
    thread.start()


def __sendWinStyleNotify(
    app_name: str, title: str, msg: str, fadeTime: QTime = QTime(0, 1, 0)
) -> None:
    app = NotifyApplication()
    NotifyText(
        app.window,
        10,
        10,
        app_name,
        font=QtGui.QFont("Segoe UI", 10, QtGui.QFont.Weight.Normal),
    )
    NotifyText(
        app.window,
        10,
        40,
        title,
        font=QtGui.QFont("Segoe UI", 13, QtGui.QFont.Weight.Bold),
    )
    NotifyText(
        app.window,
        10,
        70,
        msg,
        font=QtGui.QFont("Segoe UI", 10, QtGui.QFont.Weight.Normal),
        color="#a5a5a5",
    )
    app.window.setCloseClick(True)
    app.window.setWindowBottomRight()
    app.window.autoFade(fadeTime)
    app.send_notification()


if __name__ == "__main__":
    sendWinStyleNotify(
        "Notify Elements",
        "Hello World",
        "This is a test message.",
        fadeTime=QTime(0, 0, 5),
    )
