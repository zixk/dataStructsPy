from .Button import Button


class HtmlButton(Button):
    def render(self):
        print("Render HTML Button")

    def onClick(self, f):
        print("Performed action ", f, " on HTML Button")