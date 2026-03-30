from typing import get_origin, get_args

def is_optional(t):
    return get_origin(t) is not None and type(None) in get_args(t)
