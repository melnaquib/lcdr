from prompt_toolkit.completion import NestedCompleter


def make_dataCompleter():
    d = {
        "data": {
            "link": {
                "local"
            }
        }
    }
    c = NestedCompleter.from_nested_dict(d)
