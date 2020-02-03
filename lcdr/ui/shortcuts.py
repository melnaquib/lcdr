from prompt_toolkit.key_binding import KeyBindings
from dialog import Dialog

def make_keybindings():
    kb = KeyBindings()

    @kb.add("q")
    @kb.add("c-c")
    def _e_quit(event):
        " Quit application. "
        event.app.exit()

    @kb.add("c-o")
    def _e_open_file():
        Dialog.dselect(filepath="~")

    return kb