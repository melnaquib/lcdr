# from dialog import Dialog
from prompt_toolkit import Application, prompt, PromptSession
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout

from lcdr.positronic.link import setup_link
from lcdr.suggest.MasterCompleter import make_masterCompleter
from lcdr.ui.cdrBuffer import make_buffer
from lcdr.ui.shortcuts import make_keybindings
from lcdr.ui.ui import make_root_layout

def main():
    # buffer = make_buffer()
    # layout = make_root_layout(buffer=buffer)
    key_bindings = make_keybindings()
    # clipboard = None
    completer = make_masterCompleter()

    # app = Application(
    #     layout=layout,
    #     # full_screen=True,
    #     # key_bindings=key_bindings,
    #     # clipboard=clipboard,
    #     mouse_support=True,
    # )

    # setup_link()

    # dlg = Dialog()
    # res = dlg.dselect(filepath="", width=10, height=10)
    # res

    prompt("Lt. Cmdr. Data >", mouse_support=True, completer=completer, key_bindings=key_bindings)
    # app.run()
    # ps = PromptSession()
    # ps.app

if __name__ == '__main__':
    main()
