from Dialog import Dialog
from products.HtmlButton import HtmlButton


class WebDialog(Dialog):
    def createButton(self):
        return HtmlButton()