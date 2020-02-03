ego = [
    'data',
    'lcdr',
    'mr data',
    'lcdr data'
]

def is_addressing_me(stmt: str):
    l = stmt.lower()
    res = any(lambda i: l.startswith(i), ego)
    return res