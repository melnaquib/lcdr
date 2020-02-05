import subprocess
import re
from collections import OrderedDict
from prompt_toolkit.completion import Completer, Completion

class HelpCompleter(Completer):

    def __init__(self, cmd: str, doc: str):
        self.cmd = cmd
        self.doc = doc
        self.switches = []
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
            c = Completion(text=m, display=l)
            c.orig = m
            self.switches.append(c)

    def get_completions(self, document, complete_event):
        line = document.current_line_before_cursor.lstrip()
        word = None if line.endswith(' ') else line.split(' ')[-1]
        if not word:
            return self.switches
        res = [i for i in self.switches if i.orig.startswith(word)]
        for i in res:
            i.text = i.orig.replace(word, '')
        return res