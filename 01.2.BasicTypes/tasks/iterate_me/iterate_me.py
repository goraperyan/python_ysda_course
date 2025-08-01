def get_squares(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with squared values
    """
    return [x ** 2 for x in elements]


# ====================================================================================================


def get_indices_from_one(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with indices started from 1
    """
    return list(range(1, len(elements) + 1)) if len(elements) > 0 else []


# ====================================================================================================


def get_max_element_index(elements: list[int]) -> int | None:
    """
    :param elements: list with integer values
    :return: index of maximum element if exists, None otherwise
    """
    if len(elements) == 0:
        return None

    max_value = elements[0]
    max_id = 0
    for i, v in enumerate(elements):
        if max_value < v:
            max_value = v
            max_id = i
    return max_id


# ====================================================================================================


def get_every_second_element(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with each second element of list
    """
    return [elements[i] for i in range(1, len(elements), 2)]


# ====================================================================================================


def get_first_three_index(elements: list[int]) -> int | None:
    """
    :param elements: list with integer values
    :return: index of first "3" in the list if exists, None otherwise
    """
    for i, v in enumerate(elements):
        if v == 3:
            return i
    return None

# ====================================================================================================


def get_last_three_index(elements: list[int]) -> int | None:
    """
    :param elements: list with integer values
    :return: index of last "3" in the list if exists, None otherwise
    """
    for i, v in enumerate(reversed(elements)):
        if v == 3:
            return len(elements) - i - 1
    return None


# ====================================================================================================


def get_sum(elements: list[int]) -> int:
    """
    :param elements: list with integer values
    :return: sum of elements
    """
    return sum(elements)


# ====================================================================================================


def get_min_max(elements: list[int], default: int | None) -> tuple[int | None, int | None]:
    """
    :param elements: list with integer values
    :param default: default value to return if elements are empty
    :return: (min, max) of list elements or (default, default) if elements are empty
    """
    return (min(elements), max(elements)) if len(elements) != 0 else (default, default)


# ====================================================================================================

def get_by_index(elements: list[int], i: int, boundary: int) -> int | None:
    """
    :param elements: list with integer values
    :param i: index of elements to check with boundary
    :param boundary: boundary for check element value
    :return: element at index `i` from `elements` if element greater then boundary and None otherwise
    """
    return value if (value := elements[i]) > boundary else None
