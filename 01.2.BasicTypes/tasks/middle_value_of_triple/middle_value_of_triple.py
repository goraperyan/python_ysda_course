def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    if (a - b) * (c - a) >= 0:
        return a
    elif (b - c) * (a - b) >= 0:
        return b
    else:
        return c
