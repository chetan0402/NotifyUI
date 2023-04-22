from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
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


class NotifyWindow(QMainWindow):
    style_sheet: str = ""
    close_if_clicked: bool = False
    padding: int = 10

    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowType.ToolTip)
        self.setGeometry(0, 0, 356, 100)
        self.setFixedWidth(356)
        # self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed,QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        ava_space = (
            QtGui.QGuiApplication.primaryScreen().availableGeometry().bottomRight()
        )
        x = ava_space.x() - self.frameGeometry().width() - self.padding
        y = ava_space.y() - self.frameGeometry().height() - self.padding
        self.move(x, y)
        self.setBackgroundColor("#272727")

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

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.button() == Qt.MouseButton.LeftButton and self.close_if_clicked:
            self.animation = QPropertyAnimation(self, b"windowOpacity")
            self.animation.setDuration(500)
            self.animation.setStartValue(1.0)
            self.animation.setEndValue(0.0)
            self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
            self.animation.finished.connect(QApplication.exit)
            self.animation.start()


class NotifyText:
    style_sheet = ""
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


def sendWinStyleNotify(app_name: str, title: str, msg: str) -> None:
    """
    Sends a windows 10 inspired style notification.
    app_name: the name of the application.
    title: the title of the notification.
    msg: the message of the notification.
    e.g. "Notify Elements","Hello World","This is a test message."
    Note: This function is a thread. So it won't block the main thread.
    """
    thread = threading.Thread(target=__sendWinStyleNotify, args=(app_name, title, msg))
    thread.start()


def __sendWinStyleNotify(app_name: str, title: str, msg: str) -> None:
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
    app.send_notification()


if __name__ == "__main__":
    sendWinStyleNotify("Notify Elements", "Hello World", "This is a test message.")
