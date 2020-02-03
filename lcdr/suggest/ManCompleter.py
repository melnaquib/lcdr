from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion

class ManCompleter(Completer):
    def get_completions(self, document, complete_event):
        yield Completion('completion', start_position=0)
