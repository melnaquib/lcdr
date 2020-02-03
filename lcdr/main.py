from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout

from lcdr.ui.cdrBuffer import make_buffer
from lcdr.ui.ui import make_root_layout

def main():
    buffer = make_buffer()
    layout = make_root_layout(buffer=buffer)
    key_bindings = None
    clipboard = None

    app = Application(
        layout=layout, full_screen=True,
        key_bindings=key_bindings, clipboard=clipboard,
        mouse_support=True,
    )
    app.run()

if __name__ == '__main__':
    main()
