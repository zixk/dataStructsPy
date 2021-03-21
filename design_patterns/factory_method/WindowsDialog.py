from Dialog import Dialog
from products.WindowsButton import WindowsButton


class WindowsDialog(Dialog):
    def createButton(self):
        return WindowsButton()