from typing import AsyncGenerator, Callable, Iterable, Optional, Sequence

from prompt_toolkit.completion import Completer, CompleteEvent, DummyCompleter, Completion
from prompt_toolkit.document import Document


class PDynamicCompleter(Completer):
    """
    Completer class that can dynamically returns any Completer.
    :param get_completer: Callable that returns a :class:`.Completer` instance.
    """

    def __init__(self, get_completer: Callable[[], Optional[Completer]]) -> Completer:
        self.get_completer = get_completer

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        completer = self.get_completer(document, complete_event) or DummyCompleter()
        return completer.get_completions(document, complete_event)

    # async def get_completions_async(
    #     self, document: Document, complete_event: CompleteEvent
    # ) -> AsyncGenerator[Completion, None]:
    #     completer = self.get_completer(document, complete_event) or DummyCompleter()
    #
    #     async for completion in completer.get_completions_async(
    #         document, complete_event
    #     ):
    #         yield completion

    def __repr__(self) -> str:
        return "MultiCompleter(%r -> %r)" % (self.get_completer, self.get_completer())
