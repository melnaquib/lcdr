from prompt_toolkit.buffer import Buffer
from prompt_toolkit.history import FileHistory

from lcdr.suggest.MasterCompleter import make_masterCompleter


def make_buffer():
    completer = make_masterCompleter()
    history = FileHistory('~/.lcdr_history')
    on_text_changed = None,
    on_completions_changed = None,
    on_suggestion_set = None
    buffer = Buffer(
        completer=completer,
        auto_suggest=True,
        history=history,

        # on_text_changed=on_text_changed,
        # on_completions_changed=on_completions_changed,
        # on_suggestion_set=on_suggestion_set
    )
    return buffer