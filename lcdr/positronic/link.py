#local ssh docker vagrant virtualbox vmware
from prompt_toolkit.shortcuts import radiolist_dialog


def setup_link():
    res = radiolist_dialog(
        title="System Link",
        text="Which Linux to connect to",
        values=[
            ("last", "Same as Last Configuration"),
            ("local", "Local"),
            ("ssh", "ssh"),
            ("docker", "docker"),
            ("vagrant", "vagrant"),
            ("vbox", "VirtualBox"),
            ("vmware", "VM Ware"),
            ("aws", "Amazon Web Services"),
            ("gcp", "Google Computing Platform"),
        ]
    ).run()


def link():
    pass


def local():
    pass

def ssh(host, port, user, passwd):
    pass

def vb(name):
    pass
