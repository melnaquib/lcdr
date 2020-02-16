import subprocess
import re
from collections import OrderedDict

from bs4 import BeautifulSoup
from prompt_toolkit.completion import Completer, Completion

class ManCompleter(Completer):

    def __init__(self, cmd: str, doc: bytes):
        self.cmd = cmd
        self.doc = doc
        self.switches = []
        self.build()

    def build(self):
        self.htmldoc = subprocess.check_output(["groff", "-mandoc", "-Thtml"], input=self.doc).decode()
        soup = BeautifulSoup(self.htmldoc, 'html.parser')
        # for p in soup.find("p", {"style": "margin-top: 1em", "valign": "top"}, recursive=True):
        for p in soup.find_all("p", recursive=True):
            self.parse_line(p.text)


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