import subprocess
from functools import lru_cache
from typing import AsyncGenerator, Callable, Iterable, Optional, Sequence

from prompt_toolkit.completion import Completer, CompleteEvent, DummyCompleter, Completion, PathCompleter, \
    ExecutableCompleter, NestedCompleter
from prompt_toolkit.document import Document

from lcdr.suggest.PDynamicCompleter import PDynamicCompleter
from lcdr.suggest.HelpCompleter import HelpCompleter
from lcdr.suggest.ManCompleter import ManCompleter

pathCompleter = PathCompleter()

@lru_cache()
def get_completer_from_prefix(prefix):
    # try:
    #     doc = subprocess.check_output(["man", prefix]).decode()
    #     completer = ManCompleter(prefix, doc)
    #     return completer
    # except Exception as ex::
    #     pass
    try:
        doc = subprocess.check_output([prefix, "--help"]).decode()
        completer = HelpCompleter(prefix, doc)
        return completer
    except Exception as ex:
        pass
    try:
        doc = subprocess.check_output([prefix, "-h"]).decode()
        completer = HelpCompleter(prefix, doc)
        return completer
    except Exception as ex:
        pass
    completer = DummyCompleter()
    return completer

@lru_cache()
def make_avail_cmd_completer():
    completer = ExecutableCompleter()
    return completer

avail_cmd_completer = make_avail_cmd_completer()

def get_completer(document: Document, complete_event: CompleteEvent):
    #data cmds man help conda_install
    line = document.current_line_before_cursor.lstrip()
    if ' ' not in line:
        return avail_cmd_completer
    cmd = line.split(" ")[0]
    return get_completer_from_prefix(cmd)

def make_masterCompleter():
    master_completer = PDynamicCompleter(get_completer=get_completer)
    return master_completer
