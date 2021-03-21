from .Button import Button


class WindowsButton(Button):
    def render(self):
        print("Render Windows Button")

    def onClick(self, f):
        print("Performed action ", f , " on Windows Button")