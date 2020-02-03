import subprocess
import re
from collections import OrderedDict
from prompt_toolkit.completion import Completer, Completion

class HelpCompleter(Completer):

    def __init__(self, cmd: str, doc: str):
        self.cmd = cmd
        self.doc = doc
        self.switches = OrderedDict()
        self.build()

    def build(self):
        for l in self.doc.split('\n'):
            self.parse_line(l)


    def parse_line(self, line:str):
        if line.strip().startswith('-'):
            self.parse_switch(line)

    def parse_switch(self, line):
        l = line.strip()
        sw = re.compile(r'(-+\w+\b)')
        for m in re.findall(sw, line):
            if m not in self.switches:
                self.switches[m] = []
            self.switches[m].append(line)

    def get_completions(self, document, complete_event):
        line = document.current_line_before_cursor
        idx = document.find_previous_word_beginning()
        if -1 == idx:
            idx = document.find_previous_word_beginning(2)
        word = line[idx:]
        res = []
        for sw, ls in self.switches.items():
            if sw.startswith(word):
                text = sw.replace(word, '')
                res.append(Completion(text=text, display=''.join(ls)))
