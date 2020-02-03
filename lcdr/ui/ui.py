from typing import Container

from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout import Window, BufferControl, Layout


def make_root_layout(buffer):
    bufferCtrl = BufferControl(buffer=buffer, preview_search=True)  # Editable buffer.
    root_container = Window(content=bufferCtrl)
    layout = Layout(root_container)
    return layout