from WindowsDialog import WindowsDialog
from WebDialog import WebDialog


def client_code(dialog) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{dialog.createButton()}", end="")
    dialog.render()


if __name__ == "__main__":
    print("App: Launched with the WindowsDialog.")
    client_code(WindowsDialog())
    print("\n")

    print("App: Launched with the WebDialog.")
    client_code(WebDialog())
