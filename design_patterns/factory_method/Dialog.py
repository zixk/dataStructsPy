from abc import abstractmethod
from products import Button


class Dialog():
    @abstractmethod
    def createButton(self) -> Button:
        pass

    def render(self):
        okButton = self.createButton()
        okButton.onClick("close Dialog")
        okButton.render()